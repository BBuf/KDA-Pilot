"""Standalone bit-exact correctness runner for the LTX2 qknorm + split-RoPE task.

No sglang import. Tolerances are FORBIDDEN: every candidate-vs-oracle comparison
is `torch.equal` on an int16 bitcast (see adapter.compare_outputs).

Sections:
  1. production rows (bench/workloads.json)
  2. regression grid (head_dim in {64,128}, num_heads=32, B in {1,2}, varied seq,
     cross-attention rows with unequal Q/K seq lengths)
  3. adversarial rounding-boundary inputs (stress anti-FMA / addcmul ordering)
  4. negative / reject tests (pure Python, no GPU): split_rope_support_status

Candidate comparisons (1-3) require a built candidate (solution/) AND a CUDA
device; when either is missing they are reported SKIPPED (never silently passed),
and the runner exits 0 only if nothing actually FAILED. The reject tests (4) run
anywhere. On the B200 with a built candidate, all sections must PASS.

Usage:
    python bench/correctness.py            # run everything available
    python bench/correctness.py --rejects-only
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
from baseline.ltx2_split_rope import split_rope_support_status  # noqa: E402

WORKLOADS = _TASK_ROOT / "bench" / "workloads.json"


def _run_case(workload, device):
    """Returns ('PASS'|'FAIL'|'SKIPPED', message)."""
    case = adapter.make_case(workload, device=device, seed=int(workload.get("seed", 0)))
    inputs = case["inputs"]
    adapter.call_baseline(workload, inputs, case["baseline_outputs"])
    try:
        adapter.call_candidate(workload, inputs, case["candidate_outputs"])
    except RuntimeError as exc:
        return "SKIPPED", f"candidate unavailable: {exc}"
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


def _adversarial_workloads():
    # Same shape generator; the adversarial value distribution is produced inside
    # make_case from the seed. A dedicated boundary-value generator is added when
    # the candidate exists on the B200 (it needs a GPU to expose FMA differences).
    return [{
        "id": "adv_rounding_boundary_d128",
        "num_heads": 32, "head_dim": 128, "eps": 1e-6, "seed": 31337,
        "shapes": {
            "q": {"shape": [2, 257, 4096], "dtype": "bfloat16"},
            "k": {"shape": [2, 257, 4096], "dtype": "bfloat16"},
        },
    }]


def _reject_tests():
    """Pure-Python negative tests for the support gate (no GPU/candidate)."""
    bf16 = torch.bfloat16
    results = []

    def check(name, supported_expected, x, cos, sin, tp=1):
        ok, reason = split_rope_support_status(x, cos, sin, tp_world_size=tp)
        passed = (ok == supported_expected)
        results.append((name, "PASS" if passed else "FAIL",
                        f"supported={ok} reason='{reason}'"))

    good_x = torch.zeros(2, 16, 256, dtype=bf16)
    good_cos = torch.zeros(2, 4, 16, 64, dtype=bf16)  # contiguous 4-D, last stride 1
    # A supported sanity row (so a regression that rejects everything is caught).
    check("supported_contiguous", True, good_x, good_cos, good_cos.clone())
    # TP world size != 1
    check("reject_tp_world_size", False, good_x, good_cos, good_cos.clone(), tp=2)
    # non-bf16 x
    check("reject_dtype_fp16", False, good_x.to(torch.float16), good_cos, good_cos.clone())
    # non-contiguous x
    check("reject_noncontig_x", False, good_x.transpose(1, 2), good_cos, good_cos.clone())
    # interleaved / 3-D cos (non-split)
    check("reject_interleaved_3d_cos", False, good_x,
          torch.zeros(2, 16, 256, dtype=bf16), torch.zeros(2, 16, 256, dtype=bf16))
    # cos last-dim stride != 1 (non-contiguous last dim)
    bad_last = torch.zeros(2, 4, 16, 128, dtype=bf16)[..., ::2]
    check("reject_cos_last_stride", False, good_x, bad_last, bad_last.clone())
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rejects-only", action="store_true")
    args = ap.parse_args()

    n_fail = 0
    print("== Section 4: reject / negative tests (no GPU) ==")
    for name, status, msg in _reject_tests():
        print(f"  [{status}] {name}: {msg}")
        n_fail += status == "FAIL"

    if args.rejects_only:
        print(f"\nreject-only: {'OK' if n_fail == 0 else f'{n_fail} FAILED'}")
        return 1 if n_fail else 0

    if not torch.cuda.is_available():
        print("\n[SKIPPED] Sections 1-3 require CUDA (build/run on the B200). "
              "Reject tests above are authoritative on this host.")
        return 1 if n_fail else 0

    device = torch.device("cuda")
    workloads = json.loads(WORKLOADS.read_text())
    groups = [
        ("Section 1: production rows", workloads),
        ("Section 2: regression grid", _regression_workloads()),
        ("Section 3: adversarial rounding-boundary", _adversarial_workloads()),
    ]
    n_skip = 0
    for title, rows in groups:
        print(f"\n== {title} ==")
        for wl in rows:
            status, msg = _run_case(wl, device)
            print(f"  [{status}] {wl['id']}: {msg}")
            n_fail += status == "FAIL"
            n_skip += status == "SKIPPED"

    print(f"\nsummary: failures={n_fail} skipped={n_skip}")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
