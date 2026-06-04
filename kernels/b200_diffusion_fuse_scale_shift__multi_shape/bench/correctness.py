#!/usr/bin/env python3
"""Correctness gate for b200_diffusion_fuse_scale_shift__multi_shape.

Covers, before any benchmark number counts:
  - the canonical Scale Shift regression grid from
    docs/diffusion_correctness_contract.md (B x L x C x dtype, 2D/3D/4D and
    scalar scale/shift layouts, gated + residual rows with mixed index
    patterns, with- and without-affine forms);
  - the production rows from bench/workloads.json (including C=5120, bf16 x
    with fp32 scale/shift, the chunk2 non-contiguous fp32 layout, and the
    full-shape qwen-edit row);
  - a poison-detection self-test (skipped launch must be caught);
  - host-validation rejection tests (bad ranks/layouts must raise on both
    sides).

Both implementations are checked against an independent fp32 torch oracle
that replicates the upstream wrapper semantics (including the scalar-scalar
all-zero copy fast path), and against each other. Output buffers are poisoned
before every run; NaN/Inf in any checked output is a failure.

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

_EP1, _EP2, _EP3 = adapter._EP1, adapter._EP2, adapter._EP3

_GRID_B = (1, 2, 4)
_GRID_L = (6, 33, 128, 257)
_GRID_C = (512, 1024, 1536, 3072)
_GRID_DT = ("float16", "bfloat16", "float32")
_FRAMES = {6: 3, 33: 3, 128: 4, 257: 1}
_EPS = 1e-6


def _tol(dtype: str) -> dict:
    if dtype == "float32":
        return {"atol": 1e-5, "rtol": 1e-5}
    return {"atol": 5e-2, "rtol": 5e-2}


# ---------------------------------------------------------------------------
# independent oracle (upstream wrapper semantics in fp32 torch)
# ---------------------------------------------------------------------------


def _is_scalar(t: torch.Tensor) -> bool:
    return t.dim() == 0 or (t.dim() == 1 and t.numel() == 1)


def _expand_blc_f32(t: torch.Tensor, B: int, L: int, C: int) -> torch.Tensor:
    if _is_scalar(t):
        return t.float().reshape(1, 1, 1).expand(B, L, C)
    if t.dim() == 2:
        t = t[:, None, :]
    return t.float().expand(B, L, C)


def oracle_ep1(inputs: dict) -> list[torch.Tensor]:
    x, scale, shift = inputs["x"], inputs["scale"], inputs["shift"]
    sc = inputs["scale_constant"]
    B, L, C = x.shape
    if scale.dim() == 4:
        F = scale.shape[1]
        frame_seqlen = L // F
        s_f = scale.float().squeeze(2).repeat_interleave(frame_seqlen, dim=1)
        h_f = shift.float().reshape(B, L, C)
    else:
        if _is_scalar(scale) and _is_scalar(shift):
            if not (scale.float().any() or shift.float().any()):
                return [x.clone()]  # upstream copy fast path (ignores scale_constant)
        s_f = _expand_blc_f32(scale, B, L, C)
        h_f = _expand_blc_f32(shift, B, L, C)
    out = (x.float() * (sc + s_f) + h_f).to(x.dtype)
    return [out]


def _oracle_ln_core(r32: torch.Tensor, inputs: dict) -> tuple[torch.Tensor, torch.Tensor]:
    """LayerNorm + select01 modulation over fp32 rows r32 [B, L, C]."""
    B, L, C = r32.shape
    x_dtype = inputs["x"].dtype
    mean = r32.mean(dim=-1, keepdim=True)
    var = ((r32 - mean) ** 2).mean(dim=-1, keepdim=True)
    xh = (r32 - mean) * torch.rsqrt(var + inputs["eps"])
    if inputs["weight"] is not None:
        xh = xh * inputs["weight"].float()
    if inputs["bias"] is not None:
        xh = xh + inputs["bias"].float()
    sel = (inputs["index"] != 0)[:, :, None]  # [B, L, 1]
    s = torch.where(sel, inputs["scale1"].float()[:, None, :], inputs["scale0"].float()[:, None, :])
    h = torch.where(sel, inputs["shift1"].float()[:, None, :], inputs["shift0"].float()[:, None, :])
    y = (xh * (1.0 + s) + h).to(x_dtype)
    gate = torch.where(
        sel.expand(B, L, C),
        inputs["gate1"][:, None, :].expand(B, L, C),
        inputs["gate0"][:, None, :].expand(B, L, C),
    )  # raw dtype pass-through, no fp32 round trip
    return y, gate


def oracle_ep2(inputs: dict) -> list[torch.Tensor]:
    y, gate = _oracle_ln_core(inputs["x"].float(), inputs)
    return [y, gate]


def oracle_ep3(inputs: dict) -> list[torch.Tensor]:
    x = inputs["x"]
    r32 = inputs["residual"].float() + inputs["residual_gate"].float() * x.float()
    residual_out = r32.to(x.dtype)
    y, gate = _oracle_ln_core(r32, inputs)
    return [y, residual_out, gate]


_ORACLES = {_EP1: oracle_ep1, _EP2: oracle_ep2, _EP3: oracle_ep3}


# ---------------------------------------------------------------------------
# comparison
# ---------------------------------------------------------------------------


def _compare(tag: str, ref: list, got: list, tol: dict) -> list[str]:
    errors = []
    if len(ref) != len(got):
        return [f"{tag}: output count mismatch {len(ref)} vs {len(got)}"]
    for i, (r, g) in enumerate(zip(ref, got)):
        if r.shape != g.shape or r.dtype != g.dtype:
            errors.append(f"{tag}[{i}]: shape/dtype mismatch")
            continue
        gf, rf = g.float(), r.float()
        if torch.isnan(gf).any() or torch.isinf(gf).any():
            errors.append(f"{tag}[{i}]: NaN/Inf in output")
            continue
        diff = (gf - rf).abs()
        ok = bool(torch.all(diff <= (tol["atol"] + tol["rtol"] * rf.abs())).item())
        if not ok:
            errors.append(
                f"{tag}[{i}]: max_abs={diff.max().item():.3e} exceeds atol={tol['atol']} rtol={tol['rtol']}"
            )
    return errors


def _poison(outputs: list) -> None:
    for t in outputs:
        if t.is_floating_point():
            t.fill_(float("nan"))
        else:
            t.fill_(-17)


# ---------------------------------------------------------------------------
# row construction (workload-schema dicts; tensors built by adapter.make_case)
# ---------------------------------------------------------------------------


def _ep1_spec(rid, B, L, C, dtype, layout, sc, *, scale_dtype=None, prod=False):
    scale_dtype = scale_dtype or dtype
    if layout == "full3d":
        s_shape = [B, L, C]
    elif layout == "bcast11":
        s_shape = [1, 1, C]
    elif layout == "bcast2d":
        s_shape = [B, C]
    elif layout == "frame4d":
        s_shape = [B, _FRAMES[L], 1, C]
    elif layout == "chunk2":
        s_shape = [B, L, C]
    else:
        raise ValueError(layout)
    spec = {
        "id": rid, "production": prod, "function": _EP1,
        "shapes": {
            "x": {"shape": [B, L, C], "dtype": dtype},
            "scale": {"shape": s_shape, "dtype": scale_dtype,
                      "layout": "chunk2" if layout == "chunk2" else "contiguous"},
            "shift": {"shape": [B, L, C] if layout == "frame4d" else s_shape,
                      "dtype": scale_dtype,
                      "layout": "chunk2" if layout == "chunk2" else "contiguous"},
        },
        "scale_constant": sc, **_tol(dtype),
    }
    return spec


def _gated_spec(rid, fn, B, L, C, dtype, *, affine, index_dtype="int32"):
    spec = {
        "id": rid, "production": False, "function": fn,
        "shapes": {
            "x": {"shape": [B, L, C], "dtype": dtype},
            "weight": {"shape": [C], "dtype": dtype} if affine else None,
            "bias": {"shape": [C], "dtype": dtype} if affine else None,
            "mod": {"shape": [B, C], "dtype": dtype},
            "index": {"shape": [B, L], "dtype": index_dtype},
        },
        "eps": _EPS, **_tol(dtype),
    }
    if fn == _EP3:
        spec["shapes"]["residual"] = {"shape": [B, L, C], "dtype": dtype}
        spec["shapes"]["residual_gate"] = {"shape": [B, L, C], "dtype": dtype}
    return spec


def build_grid_rows(quick: bool) -> list[dict]:
    rows = []
    combos = [
        (B, L, C, dt)
        for B in _GRID_B for L in _GRID_L for C in _GRID_C for dt in _GRID_DT
    ]
    if quick:
        combos = combos[::5]
    for n, (B, L, C, dt) in enumerate(combos):
        sc = float(n % 2)  # rotate scale_constant 0/1 across the grid
        for layout in ("full3d", "bcast11", "bcast2d", "frame4d"):
            rows.append(_ep1_spec(f"grid_ep1_{layout}_b{B}_l{L}_c{C}_{dt}_sc{int(sc)}",
                                  B, L, C, dt, layout, sc))
        for fn, tag in ((_EP2, "ep2"), (_EP3, "ep3")):
            affine = (n % 2 == 0)
            idx_dt = "int64" if n % 3 == 0 else "int32"
            rows.append(_gated_spec(
                f"grid_{tag}_b{B}_l{L}_c{C}_{dt}_{'aff' if affine else 'noaff'}_{idx_dt}",
                fn, B, L, C, dt, affine=affine, index_dtype=idx_dt))
    # offset-stress rows: a large common offset on the normalized values
    # targets the catastrophic-cancellation failure mode of a raw
    # E[x^2]-mean^2 variance (which blows the output up by O(1)..O(1e3) at
    # offset 16384). Tolerance note: at that offset the fp32 input ulp is
    # ~1e-3, so even the reference's centered two-pass form differs from the
    # oracle by ~1e-2 (measured: baseline 1.6e-2) — input-magnitude error,
    # common to every fp32 implementation. The rows therefore use the 5e-2
    # tolerance, which still rejects the cancellation failure mode decisively
    # while accepting the unavoidable magnitude-scaled rounding.
    for fn, tag in ((_EP2, "ep2"), (_EP3, "ep3")):
        for dt, off in (("float32", 16384.0), ("bfloat16", 64.0)):
            spec = _gated_spec(f"grid_{tag}_offset_{dt}", fn, 1, 128, 3072, dt, affine=False)
            spec["offset"] = off
            spec["atol"] = spec["rtol"] = 5e-2
            rows.append(spec)
    # scalar scale/shift rows (upstream fast-path semantics, incl. the
    # scale_constant=0 copy quirk) per dtype
    for dt in _GRID_DT:
        for rid, sc, zero in (
            (f"grid_ep1_scalar_zero_sc1_{dt}", 1.0, True),
            (f"grid_ep1_scalar_zero_sc0_{dt}", 0.0, True),
            (f"grid_ep1_scalar_nonzero_sc1_{dt}", 1.0, False),
        ):
            spec = _ep1_spec(rid, 2, 33, 1024, dt, "bcast11", sc)
            spec["scalar"] = {"zero": zero}
            spec["shapes"]["scale"]["shape"] = [1]
            spec["shapes"]["shift"]["shape"] = [1]
            rows.append(spec)
    return rows


def _mixed_index_patterns(case_inputs: dict, row_index: int) -> None:
    """Rotate index edge patterns: random (as built), all-zero, all-one."""
    mode = row_index % 3
    if mode == 1:
        case_inputs["index"].fill_(0)
    elif mode == 2:
        case_inputs["index"].fill_(1)


# ---------------------------------------------------------------------------
# runners
# ---------------------------------------------------------------------------


def _build_case(spec: dict, device: torch.device, seed: int) -> dict:
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    case = adapter.make_case(spec, device=device, seed=seed)
    if spec.get("scalar") is not None:
        # Replace the placeholder 1-element tensors with the requested scalars.
        dt = case["inputs"]["scale"].dtype
        val = 0.0 if spec["scalar"]["zero"] else 0.75
        case["inputs"]["scale"] = torch.full((1,), val, device=device, dtype=dt)
        case["inputs"]["shift"] = torch.full((1,), val, device=device, dtype=dt)
    offset = spec.get("offset")
    if offset is not None:
        # Common offset on the values the LayerNorm normalizes: x for the
        # plain gated entry point, the residual stream for the residual one
        # (r = residual + residual_gate * x inherits the offset additively).
        target = "residual" if spec["function"] == _EP3 else "x"
        case["inputs"][target] += offset
    return case


def run_row(spec: dict, device: torch.device, impl: str, row_index: int) -> list[str]:
    seed = 90000 + row_index
    case = _build_case(spec, device, seed)
    inputs = case["inputs"]
    if spec["function"] in (_EP2, _EP3):
        _mixed_index_patterns(inputs, row_index)
    tol = case["tolerance"]
    oracle = _ORACLES[spec["function"]](inputs)

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
        errors += _compare(f"{spec['id']}:{name}-vs-oracle", oracle, outputs, tol)

    if impl == "both" and not errors:
        errors += _compare(
            f"{spec['id']}:candidate-vs-baseline",
            case["baseline_outputs"], case["candidate_outputs"], tol,
        )
    return errors


def run_self_test(device: torch.device) -> list[str]:
    """Poisoned outputs with a skipped launch MUST be flagged."""
    spec = _ep1_spec("selftest_skipped_launch", 1, 33, 512, "bfloat16", "bcast11", 1.0)
    case = _build_case(spec, device, 4242)
    oracle = _ORACLES[_EP1](case["inputs"])
    _poison(case["candidate_outputs"])
    # deliberately no kernel call
    errs = _compare("selftest", oracle, case["candidate_outputs"], case["tolerance"])
    if not errs:
        return ["poison self-test FAILED: skipped launch was not detected"]
    return []


def run_rejection_tests(device: torch.device, impl: str) -> list[str]:
    """Invalid layouts must raise on the checked side(s)."""
    failures = []

    def expect_raise(tag, side, fn):
        try:
            fn()
            torch.cuda.synchronize()
        except Exception:
            return
        failures.append(f"rejection {tag}: {side} accepted invalid input")

    x = torch.randn(2, 33, 1024, device=device, dtype=torch.bfloat16)
    out = torch.empty_like(x)
    gate_out = torch.empty_like(x)
    mods3d = [torch.randn(2, 1, 1024, device=device, dtype=torch.bfloat16) for _ in range(6)]
    index = torch.randint(0, 2, (2, 33), device=device, dtype=torch.int32)
    bad_scale5d = torch.randn(1, 1, 1, 1, 1024, device=device, dtype=torch.bfloat16)
    x_nc = torch.randn(2, 33, 2048, device=device, dtype=torch.bfloat16)[:, :, ::2]

    sides = []
    if impl in ("both", "baseline"):
        sides.append(("baseline", adapter._BASELINE_FNS))
    if impl in ("both", "candidate"):
        sides.append(("candidate", adapter._CANDIDATE_FNS))

    for side, fns in sides:
        expect_raise("ep2-3d-modulation", side, lambda f=fns: f[_EP2](
            x, None, None, *mods3d, index, _EPS, out, gate_out))
        expect_raise("ep1-5d-scale", side, lambda f=fns: f[_EP1](
            x, bad_scale5d, bad_scale5d, 1.0, out))
        expect_raise("ep1-noncontig-x", side, lambda f=fns: f[_EP1](
            x_nc, torch.randn(1, 1, 1024, device=device, dtype=torch.bfloat16),
            torch.randn(1, 1, 1024, device=device, dtype=torch.bfloat16), 1.0,
            torch.empty_like(x_nc)))
    return failures


def run_strided_affine_tests(device: torch.device, impl: str) -> list[str]:
    """Strided 1-D weight/bias views must be accepted and correct on both
    sides (the reference normalizes them with .contiguous(); the candidate
    reads them strided through its generic path)."""
    failures = []
    B, L, C = 2, 33, 3072
    torch.manual_seed(7321)
    for fn, tag in ((_EP2, "ep2"), (_EP3, "ep3")):
        spec = _gated_spec(f"strided_affine_{tag}", fn, B, L, C, "bfloat16", affine=False)
        case = _build_case(spec, device, 7321)
        inputs = case["inputs"]
        # length-C views with stride 2 over a 2C-length base
        inputs["weight"] = torch.randn(2 * C, device=device, dtype=torch.bfloat16)[::2]
        inputs["bias"] = torch.randn(2 * C, device=device, dtype=torch.bfloat16)[1::2]
        assert inputs["weight"].stride(0) == 2 and inputs["bias"].stride(0) == 2
        oracle = _ORACLES[fn](inputs)
        tol = case["tolerance"]
        sides = []
        if impl in ("both", "baseline"):
            sides.append(("baseline", adapter.call_baseline, case["baseline_outputs"]))
        if impl in ("both", "candidate"):
            sides.append(("candidate", adapter.call_candidate, case["candidate_outputs"]))
        for name, call, outputs in sides:
            _poison(outputs)
            try:
                call(spec, inputs, outputs)
                torch.cuda.synchronize()
            except Exception as exc:  # noqa: BLE001
                failures.append(f"strided_affine_{tag}: {name} rejected strided weight/bias: {exc}")
                continue
            failures += _compare(f"strided_affine_{tag}:{name}-vs-oracle", oracle, outputs, tol)
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--impl", choices=("both", "baseline", "candidate"), default="both")
    parser.add_argument("--rows", choices=("all", "grid", "production"), default="all")
    parser.add_argument("--quick", action="store_true", help="subsample the canonical grid")
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
    failures += run_strided_affine_tests(device, args.impl)

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
        "impl": args.impl,
        "rows_requested": len(rows),
        "rows_ran": ran,
        "failures": failures,
        "ok": not failures,
        "device": str(device),
        "gpu": torch.cuda.get_device_name(device),
        "torch": torch.__version__,
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
