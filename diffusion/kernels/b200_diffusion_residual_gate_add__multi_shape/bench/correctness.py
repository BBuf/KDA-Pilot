#!/usr/bin/env python3
"""Correctness gate for b200_diffusion_residual_gate_add__multi_shape.

Covers, before any benchmark number counts:
  - the 8 production rows from bench/workloads.json;
  - a regression grid: gate modes (full [B,L,D] and broadcast [B,1,D]), dtypes
    (bf16/fp16/fp32), tail/alignment rows (odd D, D not a multiple of the 16B
    vector width, small L), sign/zero coverage, repeated seeds, and the 4D
    broadcast over several frame counts;
  - a poison-detection self-test (a skipped launch must be caught);
  - rejection tests (malformed gate shape, dtype mismatch, output aliasing, and
    non-contiguous inputs must raise on the checked side).

Both implementations are checked against an independent fp32 torch oracle
(one-round: residual + update*gate, and a + b) and against each other. Output
buffers are poisoned before every run; NaN/Inf in any checked output fails.

No sglang import anywhere in this process (asserted via bench.adapter).
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

import bench.adapter as adapter  # noqa: E402  (asserts the no-sglang contract)

_EP_RGA, _EP_BCAST = adapter._EP_RGA, adapter._EP_BCAST
_DTYPES = adapter._DTYPES


def _tol(dtype: str) -> dict:
    if dtype == "float32":
        return {"atol": 1e-5, "rtol": 1e-5}
    return {"atol": 5e-2, "rtol": 5e-2}


# ---------------------------------------------------------------------------
# independent fp32 oracles (one-round, matching docs/baseline_source.md)
# ---------------------------------------------------------------------------


def oracle_rga(inputs: dict) -> list[torch.Tensor]:
    residual, update, gate = inputs["residual"], inputs["update"], inputs["gate"]
    out = (residual.float() + update.float() * gate.float()).to(residual.dtype)
    return [out]


def oracle_bcast(inputs: dict) -> list[torch.Tensor]:
    a, b = inputs["a"], inputs["b"]
    out = (a.float() + b.float()).to(b.dtype)  # a broadcasts over b's seq dim
    return [out]


_ORACLES = {_EP_RGA: oracle_rga, _EP_BCAST: oracle_bcast}


# ---------------------------------------------------------------------------
# comparison / poison
# ---------------------------------------------------------------------------


def _compare(tag: str, ref: list, got: list, tol: dict) -> list[str]:
    errors = []
    if len(ref) != len(got):
        return [f"{tag}: output count mismatch {len(ref)} vs {len(got)}"]
    for i, (r, g) in enumerate(zip(ref, got)):
        if r.shape != g.shape or r.dtype != g.dtype:
            errors.append(f"{tag}[{i}]: shape/dtype mismatch {tuple(g.shape)}/{g.dtype}")
            continue
        gf, rf = g.float(), r.float()
        if torch.isnan(gf).any() or torch.isinf(gf).any():
            errors.append(f"{tag}[{i}]: NaN/Inf in output")
            continue
        diff = (gf - rf).abs()
        ok = bool(torch.all(diff <= (tol["atol"] + tol["rtol"] * rf.abs())).item())
        if not ok:
            errors.append(
                f"{tag}[{i}]: max_abs={diff.max().item():.3e} exceeds "
                f"atol={tol['atol']} rtol={tol['rtol']}"
            )
    return errors


def _poison(outputs: list) -> None:
    for t in outputs:
        t.fill_(float("nan"))


# ---------------------------------------------------------------------------
# regression-row construction (workload-schema dicts; tensors via make_case)
# ---------------------------------------------------------------------------


def _rga_spec(rid, B, L, D, dtype, gate_mode, *, prod=False) -> dict:
    g_shape = [B, L, D] if gate_mode == "full" else [B, 1, D]
    return {
        "id": rid, "production": prod, "function": _EP_RGA, "gate_mode": gate_mode,
        "shapes": {
            "residual": {"shape": [B, L, D], "dtype": dtype},
            "update": {"shape": [B, L, D], "dtype": dtype},
            "gate": {"shape": g_shape, "dtype": dtype},
            "out": {"shape": [B, L, D], "dtype": dtype},
        },
        **_tol(dtype),
    }


def _bcast_spec(rid, B, S, P, D, dtype) -> dict:
    return {
        "id": rid, "production": False, "function": _EP_BCAST,
        "shapes": {
            "a": {"shape": [B, 1, P, D], "dtype": dtype},
            "b": {"shape": [B, S, P, D], "dtype": dtype},
            "out": {"shape": [B, S, P, D], "dtype": dtype},
        },
        **_tol(dtype),
    }


def build_grid_rows(quick: bool) -> list[dict]:
    rows: list[dict] = []
    dts = ("bfloat16", "float16", "float32")
    # Gate modes x dtypes x a few (L, D) including aligned + tail D and small L.
    LD = [(1, 4096, 4096), (1, 256, 3072), (1, 7, 2048), (1, 128, 2047), (1, 33, 130), (1, 1, 4608)]
    if quick:
        LD = LD[::2]
    n = 0
    for dt in dts:
        for (B, L, D) in LD:
            for gm in ("full", "bcast"):
                rows.append(_rga_spec(f"grid_rga_{gm}_b{B}_l{L}_d{D}_{dt}", B, L, D, dt, gm))
                n += 1
    # 4D broadcast over several frame counts and a tail D.
    for dt in dts:
        for (S, P, D) in [(126, 3, 2048), (1, 3, 2048), (40, 4, 1024), (17, 3, 130)]:
            rows.append(_bcast_spec(f"grid_bcast_s{S}_p{P}_d{D}_{dt}", 1, S, P, D, dt))
    # Deterministic zero/sign coverage: zeros + positive + negative values.
    for gm in ("full", "bcast"):
        rows.append({**_rga_spec(f"grid_rga_{gm}_zerosign", 1, 64, 2048, "bfloat16", gm),
                     "fill": "zerosign"})
    rows.append({**_bcast_spec("grid_bcast4d_zerosign", 1, 40, 3, 2048, "bfloat16"),
                 "fill": "zerosign"})
    # Repeated randomized seeds for representative rows (distinct id -> distinct
    # seed = 90000 + row_index), covering full, broadcast, tail-D, and 4D.
    for k in (2, 3):
        rows.append(_rga_spec(f"grid_rga_full_repeat{k}", 1, 4096, 4096, "bfloat16", "full"))
        rows.append(_rga_spec(f"grid_rga_bcast_repeat{k}", 1, 4096, 4096, "bfloat16", "bcast"))
        rows.append(_rga_spec(f"grid_rga_tailD_repeat{k}", 1, 128, 2047, "bfloat16", "full"))
        rows.append(_bcast_spec(f"grid_bcast4d_repeat{k}", 1, 126, 3, 2048, "bfloat16"))
    return rows


# Deterministic pattern with zeros, positive, and negative values (sign/zero
# coverage). gate==0 -> out==residual; negative gate flips the update sign.
_ZEROSIGN_PATTERN = (0.0, 1.5, -2.0, 0.0, 0.75, -1.0, 3.0, -0.25)


def _apply_zerosign(case: dict) -> None:
    pat = torch.tensor(_ZEROSIGN_PATTERN)
    for t in case["inputs"].values():
        if torch.is_tensor(t) and t.is_floating_point():
            n = t.numel()
            reps = (n + len(_ZEROSIGN_PATTERN) - 1) // len(_ZEROSIGN_PATTERN)
            vals = pat.to(device=t.device, dtype=t.dtype).repeat(reps)[:n]
            t.view(-1).copy_(vals)


def _build_case(spec: dict, device: torch.device, seed: int) -> dict:
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    case = adapter.make_case(spec, device=device, seed=seed)
    if spec.get("fill") == "zerosign":
        _apply_zerosign(case)
    return case


def run_row(spec: dict, device: torch.device, impl: str, row_index: int) -> list[str]:
    case = _build_case(spec, device, 90000 + row_index)
    inputs = case["inputs"]
    tol = case["tolerance"]
    oracle = _ORACLES[spec["function"]](inputs)

    errors: list[str] = []
    sides = []
    if impl in ("both", "baseline"):
        sides.append(("baseline", adapter.call_baseline, case["baseline_outputs"]))
    if impl in ("both", "candidate"):
        sides.append(("candidate", adapter.call_candidate, case["candidate_outputs"]))
    for name, fn, outputs in sides:
        _poison(outputs)
        fn(spec, inputs, outputs)
        torch.cuda.synchronize()
        errors += _compare(f"{spec['id']}:{name}-vs-oracle", oracle, outputs, tol)
    if impl == "both" and not errors:
        errors += _compare(
            f"{spec['id']}:candidate-vs-baseline",
            case["baseline_outputs"], case["candidate_outputs"], tol,
        )
    return errors


def run_self_test(device: torch.device) -> list[str]:
    """A poisoned output with a skipped launch MUST be flagged."""
    spec = _rga_spec("selftest_skipped_launch", 1, 33, 512, "bfloat16", "bcast")
    case = _build_case(spec, device, 4242)
    oracle = _ORACLES[_EP_RGA](case["inputs"])
    _poison(case["candidate_outputs"])
    # deliberately no kernel call
    errs = _compare("selftest", oracle, case["candidate_outputs"], case["tolerance"])
    return [] if errs else ["poison self-test FAILED: skipped launch not detected"]


def run_rejection_tests(device: torch.device, impl: str) -> list[str]:
    """Invalid inputs must raise on BOTH sides (shared adapter validation runs
    before either implementation)."""
    failures: list[str] = []
    bf16 = torch.bfloat16

    def expect_raise(tag, call):
        try:
            call()
            torch.cuda.synchronize()
        except Exception:
            return
        failures.append(f"rejection {tag}: accepted invalid input")

    sides = []
    if impl in ("both", "baseline"):
        sides.append(("baseline", adapter.call_baseline))
    if impl in ("both", "candidate"):
        sides.append(("candidate", adapter.call_candidate))

    res = torch.randn(1, 64, 2048, device=device, dtype=bf16)
    upd = torch.randn(1, 64, 2048, device=device, dtype=bf16)
    out = torch.empty_like(res)
    nc = torch.randn(1, 64, 4096, device=device, dtype=bf16)[:, :, ::2]  # non-contiguous
    rga, bca = {"function": _EP_RGA}, {"function": _EP_BCAST}

    cases = [
        # tag, workload, inputs, outputs
        ("rga-bad-gate-2d", rga,
         {"residual": res, "update": upd, "gate": torch.randn(1, 2048, device=device, dtype=bf16)}, [out]),
        ("rga-gate-wrong-D", rga,
         {"residual": res, "update": upd, "gate": torch.randn(1, 1, 1024, device=device, dtype=bf16)}, [out]),
        ("rga-dtype-mismatch", rga,
         {"residual": res, "update": upd, "gate": torch.randn(1, 1, 2048, device=device, dtype=torch.float32)}, [out]),
        ("rga-gate-leaddim-not1", rga,
         {"residual": res, "update": upd, "gate": torch.randn(2, 1, 2048, device=device, dtype=bf16)}, [out]),
        ("rga-alias-out", rga,
         {"residual": res, "update": upd, "gate": torch.randn(1, 1, 2048, device=device, dtype=bf16)}, [res]),
        ("rga-noncontig", rga,
         {"residual": nc, "update": torch.empty(1, 64, 2048, device=device, dtype=bf16),
          "gate": torch.randn(1, 1, 2048, device=device, dtype=bf16)},
         [torch.empty(1, 64, 2048, device=device, dtype=bf16)]),
        ("rga-full-gate-noncontig", rga,
         {"residual": res, "update": upd,
          "gate": torch.randn(1, 64, 4096, device=device, dtype=bf16)[:, :, ::2]}, [out]),
        ("bcast-batch-gt1", bca,
         {"a": torch.randn(2, 1, 3, 8, device=device, dtype=bf16),
          "b": torch.randn(2, 5, 3, 8, device=device, dtype=bf16)},
         [torch.empty(2, 5, 3, 8, device=device, dtype=bf16)]),
    ]
    for side, call in sides:
        for tag, wl, inp, outs in cases:
            expect_raise(f"{tag}:{side}", lambda c=call, w=wl, i=inp, o=outs: c(w, i, o))
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--impl", choices=("both", "baseline", "candidate"), default="both")
    parser.add_argument("--rows", choices=("all", "grid", "production"), default="all")
    parser.add_argument("--quick", action="store_true", help="subsample the regression grid")
    parser.add_argument("--max-failures", type=int, default=25)
    parser.add_argument("--report", default=None, help="optional JSON report path")
    args = parser.parse_args()

    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)

    rows: list[dict] = []
    if args.rows in ("all", "grid"):
        rows += build_grid_rows(args.quick)
    if args.rows in ("all", "production"):
        rows += json.loads((_BENCH_DIR / "workloads.json").read_text())

    failures: list[str] = []
    failures += run_self_test(device)
    failures += run_rejection_tests(device, args.impl)

    ran = 0
    for i, spec in enumerate(rows):
        if len(failures) >= args.max_failures:
            failures.append(f"... stopping early after {args.max_failures} failures")
            break
        try:
            failures += run_row(spec, device, args.impl, i)
        except Exception as exc:  # noqa: BLE001 - any crash is a row failure
            failures.append(f"{spec['id']}: EXCEPTION {type(exc).__name__}: {exc}")
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
        print("[correctness] PASS")
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
