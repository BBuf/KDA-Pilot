"""Standalone bit-exact correctness runner for the LTX2 qknorm + split-RoPE task.

No sglang import. Tolerances are FORBIDDEN: every candidate-vs-oracle comparison
is `torch.equal` on an int16 bitcast (adapter.compare_outputs).

Sections:
  1. production rows (bench/workloads.json)
  2. regression grid
  3. adversarial rounding-boundary (stage-level): boundary bf16 x/cos/sin fed
     DIRECTLY to apply_split_rotary_emb_eager and the CUDA kernel (bypassing
     RMSNorm), with a sensitivity guard proving the data exercises the
     round-first-then-addcmul distinction.
  4. candidate reject tests: adapter.call_candidate on mutated REAL cases must
     raise ValueError before any kernel launch.
  5. support-helper tests (pure Python, no GPU): split_rope_support_status.

Fail-closed: in normal mode any FAIL or SKIP in the CUDA sections (1-4), or CUDA
being unavailable, makes the process exit non-zero. `--rejects-only` is the only
CPU-only pass mode (runs section 5).

Usage:
    python bench/correctness.py            # full run (requires CUDA)
    python bench/correctness.py --rejects-only   # CPU: support-helper tests only
"""

import argparse
import json
import sys
from pathlib import Path

import torch

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import bench.adapter as adapter  # noqa: E402
from baseline.ltx2_split_rope import (  # noqa: E402
    apply_split_rotary_emb_eager,
    split_rope_support_status,
)

WORKLOADS = _TASK_ROOT / "bench" / "workloads.json"


# --------------------------------------------------------------------------- #
# Section 1-2: production rows + regression grid (full pipeline, bit-exact)
# --------------------------------------------------------------------------- #
def _run_case(workload, device):
    """Returns ('PASS'|'FAIL'|'SKIPPED', message)."""
    case = adapter.make_case(workload, device=device, seed=int(workload.get("seed", 0)))
    inputs = case["inputs"]
    adapter.call_baseline(workload, inputs, case["baseline_outputs"])
    try:
        adapter.call_candidate(workload, inputs, case["candidate_outputs"])
    except ValueError as exc:
        return "FAIL", f"candidate rejected a supported row: {exc}"
    except RuntimeError as exc:
        return "SKIPPED", f"candidate unavailable (build/import): {exc}"
    verdict = adapter.compare_outputs(
        workload, case["baseline_outputs"], case["candidate_outputs"], case["tolerance"]
    )
    return ("PASS" if verdict.get("ok") else "FAIL"), verdict.get("message", "")


def _regression_workloads():
    rows = []
    for b in (1, 2):
        for head_dim in (64, 128):
            for s_q, s_k in ((129, 129), (126, 1536), (257, 257)):
                hidden = 32 * head_dim
                rows.append({
                    "id": f"reg_b{b}_d{head_dim}_q{s_q}_k{s_k}",
                    "num_heads": 32, "head_dim": head_dim, "eps": 1e-6,
                    "seed": 7000 + len(rows),
                    "shapes": {
                        "q": {"shape": [b, s_q, hidden], "dtype": "bfloat16"},
                        "k": {"shape": [b, s_k, hidden], "dtype": "bfloat16"},
                    },
                })
    return rows


# --------------------------------------------------------------------------- #
# Section 3: adversarial rounding-boundary (stage-level, bypasses RMSNorm)
# --------------------------------------------------------------------------- #
# Boundary bf16 values: signs, zero/-zero, small/near-subnormal, halves, and
# encodings adjacent to 1.0 (bf16 step near 1.0 is 2**-7) so that
# round_bf16(first*cos) differs from first*cos and the sine term can nudge the
# rounded intermediate across a bf16 boundary.
_BF16_POOL = [
    0.0, -0.0, 0.5, -0.5, 1.0, -1.0, 2.0, -2.0, 3.0, -3.0,
    1.0 + 2 ** -7, 1.0 - 2 ** -8, 0.5 + 2 ** -8, 2 ** -6, -2 ** -6,
    2 ** -8, -2 ** -8, 0.75, -0.75, 1.5, -1.5, 1.25, 0.125, 7.0,
]


def _adversarial_inputs(device):
    pool = torch.tensor(_BF16_POOL, dtype=torch.float32, device=device).to(torch.bfloat16)
    n = pool.numel()
    b, s, num_heads, head_dim = 1, 2048, 1, 64
    r = head_dim // 2
    t = torch.arange(s, device=device).view(s, 1)
    j = torch.arange(r, device=device).view(1, r)
    x = torch.empty(b, s, head_dim, dtype=torch.bfloat16, device=device)
    x[0, :, :r] = pool[(t + j) % n]
    x[0, :, r:] = pool[(t * 3 + j * 5) % n]
    cos_phys = pool[(t * 2 + j) % n].view(b, s, num_heads, r)
    sin_phys = pool[(t + j * 7) % n].view(b, s, num_heads, r)
    # Production layout: physical [B,S,H,r] viewed [B,H,S,r] (non-contiguous, last stride 1).
    return x, cos_phys.transpose(1, 2), sin_phys.transpose(1, 2)


def _adversarial_stage_test(device):
    try:
        from solution.build import load_candidate_module
        mod = load_candidate_module()
    except Exception as exc:  # noqa: BLE001
        return "SKIPPED", f"candidate unavailable (build/import): {exc}"

    x, cos, sin = _adversarial_inputs(device)
    out_eager = apply_split_rotary_emb_eager(x, (cos, sin))
    out_cand = torch.empty_like(x)
    mod.ltx2_split_rope_candidate(x, cos, sin, out_cand)

    # Sensitivity guard: a single-fp32-expression reference (NO intermediate bf16
    # round of first*cos) must differ from the eager fallback on >=1 element,
    # proving the data actually exercises the round-first distinction.
    r = x.shape[-1] // 2
    first = x[..., :r].float()
    second = x[..., r:].float()
    cosf = cos.squeeze(1).float()
    sinf = sin.squeeze(1).float()
    of = (first * cosf - sinf * second).to(torch.bfloat16)
    os = (second * cosf + sinf * first).to(torch.bfloat16)
    out_wrong = torch.cat([of, os], dim=-1)
    differs = int((out_wrong.view(torch.int16) != out_eager.view(torch.int16)).sum().item())
    if differs == 0:
        return "FAIL", "sensitivity guard: adversarial data does not exercise the rounding distinction"
    if not torch.equal(out_cand.contiguous().view(torch.int16), out_eager.contiguous().view(torch.int16)):
        mism = int((out_cand.view(torch.int16) != out_eager.view(torch.int16)).sum().item())
        return "FAIL", f"candidate != eager on {mism} adversarial elements"
    return "PASS", f"bit-equal on boundary values; guard tripped on {differs} elems vs single-expr ref"


# --------------------------------------------------------------------------- #
# Section 4: candidate reject tests (call_candidate must raise ValueError)
# --------------------------------------------------------------------------- #
def _candidate_reject_tests(device):
    from baseline.reference import build_rms_norm

    results = []
    wl = {
        "id": "reject_base", "num_heads": 4, "head_dim": 64, "eps": 1e-6, "seed": 4242,
        "shapes": {
            "q": {"shape": [2, 16, 256], "dtype": "bfloat16"},
            "k": {"shape": [2, 16, 256], "dtype": "bfloat16"},
        },
    }
    case = adapter.make_case(wl, device=device, seed=4242)
    base_in = case["inputs"]
    base_out = case["candidate_outputs"]
    hidden = 256

    def expect_reject(name, inputs, outputs):
        try:
            adapter.call_candidate(wl, inputs, outputs)
            results.append((name, "FAIL", "no ValueError raised"))
        except ValueError as exc:
            results.append((name, "PASS", str(exc)[:90]))
        except Exception as exc:  # noqa: BLE001
            results.append((name, "FAIL", f"wrong exception {type(exc).__name__}: {exc}"))

    def mut(**overrides):
        d = dict(base_in)
        d.update(overrides)
        return d

    cpu = torch.device("cpu")

    class _RMSNormSubclass(torch.nn.RMSNorm):
        pass

    # First confirm the unmutated base case is ACCEPTED (so we are not trivially
    # rejecting everything).
    try:
        adapter.call_candidate(wl, base_in, base_out)
        results.append(("base_accepted", "PASS", "valid case accepted"))
    except Exception as exc:  # noqa: BLE001
        results.append(("base_accepted", "FAIL", f"valid case rejected: {exc}"))

    # config / norm
    expect_reject("reject_tp_ne_1", mut(tp_world_size=2), base_out)
    expect_reject("reject_non_rmsnorm",
                  mut(q_norm=torch.nn.LayerNorm(hidden, dtype=torch.bfloat16, device=device)), base_out)
    expect_reject("reject_rmsnorm_subclass",
                  mut(q_norm=_RMSNormSubclass(hidden, eps=1e-6, dtype=torch.bfloat16, device=device)), base_out)
    expect_reject("reject_eps_mismatch",
                  mut(q_norm=build_rms_norm(base_in["q_norm_weight"], 1e-5)), base_out)
    expect_reject("reject_fp32_weights",
                  mut(q_norm=torch.nn.RMSNorm(hidden, eps=1e-6, dtype=torch.float32, device=device)), base_out)
    # q/k tensors (both sides)
    expect_reject("reject_non_bf16_q", mut(q=base_in["q"].float()), base_out)
    expect_reject("reject_non_bf16_k", mut(k=base_in["k"].float()), base_out)
    expect_reject("reject_noncontig_q", mut(q=base_in["q"].transpose(1, 2)), base_out)
    expect_reject("reject_noncontig_k", mut(k=base_in["k"].transpose(1, 2)), base_out)
    expect_reject("reject_head_dim_mismatch", mut(head_dim=128), base_out)  # 4*128=512 != H 256
    # cos/sin (dtype, rank, stride, shape, both sides)
    expect_reject("reject_qcos_3d", mut(q_cos=base_in["q_cos"].reshape(2, 4 * 16, 32)), base_out)
    expect_reject("reject_qcos_dtype", mut(q_cos=base_in["q_cos"].float()), base_out)
    expect_reject("reject_ksin_dtype", mut(k_sin=base_in["k_sin"].float()), base_out)
    wide = torch.zeros(2, 4, 16, 64, dtype=torch.bfloat16, device=device)[..., ::2]  # last stride 2
    expect_reject("reject_qcos_last_stride", mut(q_cos=wide), base_out)
    expect_reject("reject_qsin_shape",
                  mut(q_sin=torch.zeros(2, 4, 16, 16, dtype=torch.bfloat16, device=device)), base_out)
    # device: CPU tensors with valid dtype/shape must still reject
    expect_reject("reject_qcos_cpu", mut(q_cos=base_in["q_cos"].to(cpu)), base_out)
    expect_reject("reject_out_cpu", base_in, [base_out[0].to(cpu), base_out[1]])
    if torch.cuda.device_count() > 1:
        expect_reject("reject_out_wrong_gpu",
                      base_in, [base_out[0].to(torch.device("cuda:1")), base_out[1]])
    # outputs (shape, dtype, contiguity)
    expect_reject("reject_out_shape",
                  base_in, [torch.empty(2, 16, hidden + 8, dtype=torch.bfloat16, device=device), base_out[1]])
    expect_reject("reject_out_dtype", base_in, [base_out[0].float(), base_out[1]])
    noncontig_out = torch.empty(2, 16, hidden * 2, dtype=torch.bfloat16, device=device)[..., ::2]
    expect_reject("reject_out_noncontig", base_in, [noncontig_out, base_out[1]])

    # mutate-after-accept: the SAME inputs/outputs objects, mutated in place into an
    # unsupported config, must still reject (proves validation is not bypassed by a
    # per-call-skipping cache; validation must run on every call).
    mca = adapter.make_case(wl, device=device, seed=909)
    mca_in, mca_out = mca["inputs"], mca["candidate_outputs"]
    try:
        adapter.call_candidate(wl, mca_in, mca_out)   # accepted
        mca_in["head_dim"] = 128                       # in-place mutation -> H mismatch
        adapter.call_candidate(wl, mca_in, mca_out)
        results.append(("reject_mutate_after_accept", "FAIL", "no ValueError after in-place mutation"))
    except ValueError as exc:
        results.append(("reject_mutate_after_accept", "PASS", str(exc)[:90]))
    except Exception as exc:  # noqa: BLE001
        results.append(("reject_mutate_after_accept", "FAIL", f"wrong exception {type(exc).__name__}: {exc}"))
    return results


# --------------------------------------------------------------------------- #
# Section 5: support-helper tests (pure Python, no GPU/candidate)
# --------------------------------------------------------------------------- #
def _support_helper_tests():
    bf16 = torch.bfloat16
    results = []

    def check(name, supported_expected, x, cos, sin, tp=1):
        ok, reason = split_rope_support_status(x, cos, sin, tp_world_size=tp)
        results.append((name, "PASS" if ok == supported_expected else "FAIL",
                        f"supported={ok} reason='{reason}'"))

    # Internally consistent supported row: H=256 = num_heads(4) * head_dim(64); r=32.
    good_x = torch.zeros(2, 16, 256, dtype=bf16)
    good_cos = torch.zeros(2, 4, 16, 32, dtype=bf16)
    check("supported_consistent", True, good_x, good_cos, good_cos.clone())
    # H inconsistent with num_heads*head_dim (4*128=512 != 256) must now reject.
    check("reject_h_inconsistent", False, good_x, torch.zeros(2, 4, 16, 64, dtype=bf16),
          torch.zeros(2, 4, 16, 64, dtype=bf16))
    check("reject_tp_world_size", False, good_x, good_cos, good_cos.clone(), tp=2)
    check("reject_dtype_fp16", False, good_x.to(torch.float16), good_cos, good_cos.clone())
    check("reject_noncontig_x", False, good_x.transpose(1, 2), good_cos, good_cos.clone())
    check("reject_interleaved_3d_cos", False, good_x,
          torch.zeros(2, 16, 256, dtype=bf16), torch.zeros(2, 16, 256, dtype=bf16))
    bad_last = torch.zeros(2, 4, 16, 64, dtype=bf16)[..., ::2]
    check("reject_cos_last_stride", False, good_x, bad_last, bad_last.clone())
    # cos/sin batch or sequence-length not matching x must reject
    check("reject_cos_batch_mismatch", False, good_x,
          torch.zeros(1, 4, 16, 32, dtype=bf16), torch.zeros(1, 4, 16, 32, dtype=bf16))
    check("reject_cos_seq_mismatch", False, good_x,
          torch.zeros(2, 4, 15, 32, dtype=bf16), torch.zeros(2, 4, 15, 32, dtype=bf16))
    return results


def _emit(title, results, counters):
    print(f"\n== {title} ==")
    for name, status, msg in results:
        print(f"  [{status}] {name}: {msg}")
        counters[0] += status == "FAIL"
        counters[1] += status == "SKIPPED"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rejects-only", action="store_true")
    args = ap.parse_args()

    counters = [0, 0]  # [failures, skips]
    _emit("Section 5: support-helper tests (no GPU)", _support_helper_tests(), counters)

    if args.rejects_only:
        n_fail = counters[0]
        print(f"\nreject-only: {'OK' if n_fail == 0 else f'{n_fail} FAILED'}")
        return 1 if n_fail else 0

    if not torch.cuda.is_available():
        print("\n[FAIL] normal mode requires CUDA (build/run on the B200). "
              "Use --rejects-only for the CPU-only support-helper subset.")
        return 1  # fail-closed: a full correctness run must not pass without CUDA

    device = torch.device("cuda")
    workloads = json.loads(WORKLOADS.read_text())
    _emit("Section 1: production rows",
          [(wl["id"], *_run_case(wl, device)) for wl in workloads], counters)
    _emit("Section 2: regression grid",
          [(wl["id"], *_run_case(wl, device)) for wl in _regression_workloads()], counters)
    _emit("Section 4: candidate reject tests (call_candidate -> ValueError)",
          _candidate_reject_tests(device), counters)
    status, msg = _adversarial_stage_test(device)
    _emit("Section 3: adversarial rounding-boundary (stage-level)",
          [("adv_boundary_stage", status, msg)], counters)

    n_fail, n_skip = counters
    print(f"\nsummary: failures={n_fail} skipped={n_skip}")
    # Fail-closed: skips in a CUDA run are treated as failures (the gate must not
    # pass while candidate comparisons are skipped).
    return 1 if (n_fail or n_skip) else 0


if __name__ == "__main__":
    raise SystemExit(main())
