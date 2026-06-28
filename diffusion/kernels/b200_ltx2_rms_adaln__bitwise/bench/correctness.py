#!/usr/bin/env python3
"""Correctness gate for b200_ltx2_rms_adaln__bitwise.

This task forbids tolerance: the candidate must be BIT-WISE EQUAL to the PyTorch
eager baseline, verified with torch.equal AND raw uint16 storage equality.

Covers, before any benchmark number counts:
  - the production rows from bench/workloads.json (full-shape [B,S,D] bf16);
  - an in-gate regression grid adapted from the canonical "CuTe DSL Norm Scale
    Shift" contract to this rank-3 RMS-AdaLN ABI: B x S x D, bf16, every
    supported broadcast layout ([D],[B,D],[B,1,D],[B,S,D]) AND mixed scale/shift
    layouts, D % 256 == 0, D <= 8192, eps in {1e-6, 1e-5};
  - adversarial bf16 rounding-boundary rows (values that stress 1+scale,
    multiply, add);
  - out-of-gate rows (fp16/fp32, scalar `1`, `1SD`, `11D`, 4D, non-contiguous,
    CPU, invalid D): adapter.call_candidate must eager-fallback bit-exact, AND
    the raw kernel (adapter._CANDIDATE_FNS) must fail closed (throw);
  - a poison-detection self-test (a skipped launch must be caught).

Independent oracle = plain PyTorch eager (rms_norm(x,(D,),eps)*(1+scale)+shift),
in bf16. Baseline, candidate, and oracle are compared bit-for-bit; output buffers
are poisoned before every run; NaN/Inf in any output is a failure.

No sglang import anywhere (asserted via bench.adapter).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import torch

_BENCH_DIR = Path(__file__).resolve().parent
_TASK_ROOT = _BENCH_DIR.parent
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import bench.adapter as adapter  # noqa: E402 (asserts the no-sglang contract)

_EP = adapter._EP


def oracle(inputs: dict) -> list[torch.Tensor]:
    # Independent eager reference. The candidate on in-gate rows is the CUDA
    # kernel (independent of this), so kernel-vs-oracle is a real check; the
    # eager semantics (incl. [B,D] -> [B,1,D]) live in one place.
    return [adapter.eager_rms_adaln(
        inputs["x"], inputs["scale"], inputs["shift"], inputs["eps"])]


def _poison(outputs: list) -> None:
    for t in outputs:
        if t.is_floating_point():
            t.fill_(float("nan"))
        else:
            t.fill_(-17)


def _bw(tag: str, ref: list, got: list) -> list[str]:
    """Bitwise compare (raw storage equality) with NaN/Inf detection."""
    errors = []
    if len(ref) != len(got):
        return [f"{tag}: output count mismatch {len(ref)} vs {len(got)}"]
    for i, (r, g) in enumerate(zip(ref, got)):
        if r.shape != g.shape or r.dtype != g.dtype:
            errors.append(f"{tag}[{i}]: shape/dtype mismatch")
            continue
        gf = g.float()
        if torch.isnan(gf).any() or torch.isinf(gf).any():
            errors.append(f"{tag}[{i}]: NaN/Inf in output")
            continue
        if not adapter.bitwise_equal(r, g):
            n = int((gf != r.float()).sum().item())
            md = (gf - r.float()).abs().max().item()
            errors.append(f"{tag}[{i}]: NOT bitwise equal ({n} elems differ, max_abs={md:.3e})")
    return errors


# ---------------------------------------------------------------------------
# in-gate grid (all supported layouts, incl. mixed), bf16, D % 256 == 0
# ---------------------------------------------------------------------------

# Canonical "CuTe DSL Norm Scale Shift" grid for this task, adapted to the
# rank-3 RMS-AdaLN ABI: the contract's 4D (B,S,F,D) shapes are flattened to
# x=[B, S*F, D]. (1,1024,8,3072)->[1,8192,3072]; (4,512,16,3072)->[4,8192,3072].
# D=3072 (% 256 == 0, <= 8192).
_CANONICAL = ((1, 8192, 3072), (4, 8192, 3072))
# Smaller smoke shapes for fast iteration (only behind --quick; NOT the grid).
_SMOKE = (
    (1, 6, 256), (2, 33, 2048), (1, 128, 4096), (4, 64, 3072),
    (2, 257, 2048), (1, 1536, 4096), (2, 126, 2048),
)
# layout name -> shape factory over (B, S, D)
_LAYOUT_SHAPE = {
    "full": lambda B, S, D: [B, S, D],
    "perbatch": lambda B, S, D: [B, D],
    "perbatch1": lambda B, S, D: [B, 1, D],
    "perchan": lambda B, S, D: [D],
}


def _spec(rid, B, S, D, scale_layout, shift_layout, eps=1e-6) -> dict:
    return {
        "id": rid, "production": False, "function": _EP,
        "shapes": {
            "x": {"shape": [B, S, D], "dtype": "bfloat16"},
            "scale": {"shape": _LAYOUT_SHAPE[scale_layout](B, S, D), "dtype": "bfloat16"},
            "shift": {"shape": _LAYOUT_SHAPE[shift_layout](B, S, D), "dtype": "bfloat16"},
        },
        "eps": eps, "atol": 0.0, "rtol": 0.0,
    }


def build_ingate_rows(quick: bool) -> list[dict]:
    rows = []
    pure = ("full", "perbatch", "perbatch1", "perchan")
    mixed = (("full", "perchan"), ("perbatch", "full"), ("perchan", "perbatch1"))
    # Canonical adapted grid (the contract grid): every supported layout + mixed.
    canon = _CANONICAL[:1] if quick else _CANONICAL
    for (B, S, D) in canon:
        for lay in pure:
            rows.append(_spec(f"canon_{lay}_b{B}_s{S}_d{D}", B, S, D, lay, lay, 1e-6))
        for sl, hl in mixed:
            rows.append(_spec(f"canon_mix_{sl}-{hl}_b{B}_s{S}_d{D}", B, S, D, sl, hl, 1e-6))
    # Smoke rows: extra breadth (small shapes, eps sweep). Subset under --quick.
    smoke = _SMOKE[::4] if quick else _SMOKE
    for n, (B, S, D) in enumerate(smoke):
        eps = 1e-6 if n % 2 == 0 else 1e-5
        for lay in pure:
            rows.append(_spec(f"smoke_{lay}_b{B}_s{S}_d{D}_eps{eps}", B, S, D, lay, lay, eps))
        for sl, hl in mixed:
            rows.append(_spec(f"smoke_mix_{sl}-{hl}_b{B}_s{S}_d{D}", B, S, D, sl, hl, eps))
    return rows


# ---------------------------------------------------------------------------
# adversarial bf16 rounding-boundary rows (inputs crafted in _build_case)
# ---------------------------------------------------------------------------

def build_adversarial_rows() -> list[dict]:
    rows = []
    for n, (B, S, D) in enumerate(((2, 64, 2048), (1, 128, 4096))):
        spec = _spec(f"adv_full_b{B}_s{S}_d{D}", B, S, D, "full", "full", 1e-6)
        spec["adversarial"] = True
        rows.append(spec)
    return rows


def _craft_adversarial(case: dict, device: torch.device, seed: int) -> None:
    """Overwrite inputs with values that stress the three rounding stages:
    scale near -1 (1+scale -> ~0 / subnormal), wide-magnitude x and shift, and a
    uniform sweep over [-2, 2] so many bf16 ties are exercised."""
    g = torch.Generator(device=device).manual_seed(seed)
    x = case["inputs"]["x"]
    scale = case["inputs"]["scale"]
    shift = case["inputs"]["shift"]
    # wide-magnitude x (after RMSNorm normalizes to ~unit RMS, products still vary)
    x.copy_((torch.rand(x.shape, generator=g, device=device) * 8 - 4).to(x.dtype))
    # scale: uniform sweep in [-2, 2] (includes the 1+scale ~ 0 boundary near -1)
    scale.copy_((torch.rand(scale.shape, generator=g, device=device) * 4 - 2).to(scale.dtype))
    # shift: wide magnitude
    shift.copy_((torch.rand(shift.shape, generator=g, device=device) * 8 - 4).to(shift.dtype))


# ---------------------------------------------------------------------------
# runners
# ---------------------------------------------------------------------------


def _build_case(spec: dict, device: torch.device, seed: int) -> dict:
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    case = adapter.make_case(spec, device=device, seed=seed)
    if spec.get("adversarial"):
        _craft_adversarial(case, device, seed)
    return case


def run_row(spec: dict, device: torch.device, impl: str, row_index: int) -> list[str]:
    seed = 90000 + row_index
    case = _build_case(spec, device, seed)
    inputs = case["inputs"]
    ref = oracle(inputs)

    errors = []
    sides = []
    if impl in ("both", "baseline"):
        sides.append(("baseline", adapter.call_baseline, case["baseline_outputs"]))
    if impl in ("both", "candidate"):
        sides.append(("candidate", adapter.call_candidate, case["candidate_outputs"]))
    for name, fn, outputs in sides:
        _poison(outputs)
        fn(spec, inputs, outputs)
        torch.cuda.synchronize()
        errors += _bw(f"{spec['id']}:{name}-vs-oracle", ref, outputs)
    if impl == "both" and not errors:
        errors += _bw(f"{spec['id']}:candidate-vs-baseline",
                      case["baseline_outputs"], case["candidate_outputs"])
    return errors


def run_self_test(device: torch.device) -> list[str]:
    spec = _spec("selftest_skipped_launch", 1, 33, 2048, "full", "full")
    case = _build_case(spec, device, 4242)
    ref = oracle(case["inputs"])
    _poison(case["candidate_outputs"])  # deliberately no kernel call
    if not _bw("selftest", ref, case["candidate_outputs"]):
        return ["poison self-test FAILED: skipped launch was not detected"]
    return []


def run_out_of_gate_tests(device: torch.device) -> list[str]:
    """Out-of-gate inputs. Two kinds:
      - 'fallback': eager can compute the row, so the public candidate must
        eager-fallback bit-exact vs the oracle.
      - 'reject': eager cannot compute the row (rank-incompatible / mixed-device),
        so the public candidate must raise a controlled error.
    In BOTH kinds the raw kernel must fail closed (throw before any launch)."""
    failures = []
    eps = 1e-6
    bf16 = torch.bfloat16

    def t(shape, dtype=bf16, dev=device):
        return torch.randn(shape, device=dev, dtype=dtype)

    def mis(shape, dev=device):
        # contiguous bf16 view with a nonzero storage offset -> base pointer is
        # bf16-aligned but NOT 16-byte aligned (exercises the alignment gate).
        n = 1
        for s in shape:
            n *= s
        v = torch.randn(n + 8, device=dev, dtype=bf16).narrow(0, 1, n).view(*shape)
        assert v.is_contiguous() and v.data_ptr() % 16 != 0
        return v

    B, S, D = 2, 64, 2048
    # tag -> (kind, x, scale, shift)
    cases = {
        "fp16": ("fallback", t([B, S, D], torch.float16), t([B, S, D], torch.float16), t([B, S, D], torch.float16)),
        "fp32": ("fallback", t([B, S, D], torch.float32), t([B, S, D], torch.float32), t([B, S, D], torch.float32)),
        "D_not_mult256": ("fallback", t([B, S, 2050]), t([B, S, 2050]), t([B, S, 2050])),
        "D_too_big": ("fallback", t([1, 8, 8448]), t([1, 8, 8448]), t([1, 8, 8448])),
        "rank4_x": ("fallback", t([1, 8, 2, D]), t([1, 8, 2, D]), t([1, 8, 2, D])),
        "scalar1": ("fallback", t([B, S, D]), t([1]), t([1])),
        "layout_1SD": ("fallback", t([B, S, D]), t([1, S, D]), t([1, S, D])),   # B>1, not supported
        "layout_11D": ("fallback", t([B, S, D]), t([1, 1, D]), t([1, 1, D])),   # B>1, not supported
        "noncontig_x": ("fallback", t([B, S, 2 * D])[:, :, ::2], t([B, S, D]), t([B, S, D])),
        "noncontig_scale": ("fallback", t([B, S, D]), t([B, S, 2 * D])[:, :, ::2], t([B, S, D])),
        "cpu_all": ("fallback", t([B, S, D], dev="cpu"), t([B, S, D], dev="cpu"), t([B, S, D], dev="cpu")),
        # device fail-closed: CUDA x + CPU scale/shift -> reject (eager device mismatch)
        "cuda_x_cpu_scale": ("reject", t([B, S, D]), t([B, S, D], dev="cpu"), t([B, S, D], dev="cpu")),
        # BF1D non-divisible frames (sibling convention BF1D=(B,F,1,D)): x=[1,1000,3072],
        # scale/shift=[1,7,1,3072], S % F = 1000 % 7 != 0 -> reject.
        "bf1d_nondiv": ("reject", t([1, 1000, 3072]), t([1, 7, 1, 3072]), t([1, 7, 1, 3072])),
        # contiguous but 16B-misaligned scale -> fallback (eager handles any alignment)
        "misaligned_scale": ("fallback", t([B, S, D]), mis([B, S, D]), t([B, S, D])),
    }

    def _raw_fails_closed(tag, x, scale, shift):
        raw_out = torch.empty(tuple(x.shape), device=x.device, dtype=x.dtype)
        try:
            adapter._CANDIDATE_FNS[_EP](x, scale, shift, eps, raw_out)
            if x.is_cuda:
                torch.cuda.synchronize()
            return [f"out_of_gate[{tag}]: raw kernel accepted out-of-gate input (must fail closed)"]
        except Exception:
            return []  # expected

    for tag, (kind, x, scale, shift) in cases.items():
        inputs = {"x": x, "scale": scale, "shift": shift, "eps": eps}
        out = [torch.empty_like(x)]
        _poison(out)
        raised = False
        try:
            adapter.call_candidate({"function": _EP}, inputs, out)
            if x.is_cuda:
                torch.cuda.synchronize()
        except Exception:  # noqa: BLE001
            raised = True
        if kind == "fallback":
            if raised:
                failures.append(f"out_of_gate[{tag}]: public candidate raised instead of bit-exact fallback")
            else:
                failures += _bw(f"out_of_gate[{tag}]:fallback-vs-oracle", oracle(inputs), out)
        else:  # reject
            if not raised:
                failures.append(f"out_of_gate[{tag}]: public candidate accepted a reject-row (must raise a controlled error)")
        failures += _raw_fails_closed(tag, x, scale, shift)

    # misaligned (contiguous, nonzero-offset) OUTPUT -> public path must fall back
    # bit-exact; raw kernel must fail closed.
    xx, ss, hh = t([B, S, D]), t([B, S, D]), t([B, S, D])
    inp = {"x": xx, "scale": ss, "shift": hh, "eps": eps}
    mis_out = [mis([B, S, D])]
    try:
        adapter.call_candidate({"function": _EP}, inp, mis_out)
        torch.cuda.synchronize()
        failures += _bw("misaligned_output:fallback-vs-oracle", oracle(inp), mis_out)
    except Exception as exc:  # noqa: BLE001
        failures.append(f"out_of_gate[misaligned_output]: public candidate raised instead of fallback: {exc}")
    try:
        adapter._CANDIDATE_FNS[_EP](xx, ss, hh, eps, mis([B, S, D]))
        torch.cuda.synchronize()
        failures.append("out_of_gate[misaligned_output]: raw kernel accepted misaligned output (must fail closed)")
    except Exception:
        pass

    # cross-device (only when more than one GPU is visible)
    if torch.cuda.device_count() > 1:
        x = t([B, S, D]); sc = t([B, S, D], dev="cuda:1"); sh = t([B, S, D], dev="cuda:1")
        inputs = {"x": x, "scale": sc, "shift": sh, "eps": eps}
        out = [torch.empty_like(x)]; _poison(out)
        raised = False
        try:
            adapter.call_candidate({"function": _EP}, inputs, out); torch.cuda.synchronize()
        except Exception:  # noqa: BLE001
            raised = True
        if not raised:
            failures.append("out_of_gate[cross_device]: public candidate accepted cross-device (must raise)")
        failures += _raw_fails_closed("cross_device", x, sc, sh)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--impl", choices=("both", "baseline", "candidate"), default="both")
    parser.add_argument("--rows", choices=("all", "grid", "production"), default="all")
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--max-failures", type=int, default=25)
    parser.add_argument("--report", default=None)
    args = parser.parse_args()

    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)

    rows: list[dict] = []
    if args.rows in ("all", "grid"):
        rows += build_ingate_rows(args.quick)
        rows += build_adversarial_rows()
    if args.rows in ("all", "production"):
        rows += json.loads((_BENCH_DIR / "workloads.json").read_text())

    failures: list[str] = []
    failures += run_self_test(device)
    failures += run_out_of_gate_tests(device)

    ran = 0
    for i, spec in enumerate(rows):
        if len(failures) >= args.max_failures:
            failures.append(f"... stopping early after {args.max_failures} failures")
            break
        try:
            failures += run_row(spec, device, args.impl, i)
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{spec.get('id', '?')}: EXCEPTION {type(exc).__name__}: {exc}")
        ran += 1

    summary = {
        "impl": args.impl, "rows_requested": len(rows), "rows_ran": ran,
        "failures": failures, "ok": not failures, "device": str(device),
        "gpu": torch.cuda.get_device_name(device), "torch": torch.__version__,
    }
    if args.report:
        Path(args.report).write_text(json.dumps(summary, indent=2) + "\n")

    print(f"[correctness] impl={args.impl} rows={ran}/{len(rows)} "
          f"failures={len(failures)} gpu={summary['gpu']}")
    for f in failures:
        print(f"  FAIL {f}")
    if not failures:
        print("[correctness] PASS (bitwise)")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
