#!/usr/bin/env python3
"""Correctness harness: production rows + canonical regression grid + probes.

Oracle: the upstream fp32 reference semantics from the vendored canonical test
(baseline/upstream_jit_kernel/jit_kernel/tests/diffusion/test_fused_norm_scale_shift.py):
all operands floated to fp32, layer/rms norm + ``y = norm * (1 + scale) + shift``
computed in fp32, one final round to the activation dtype
(``res_out`` = fp32 pre-norm value rounded once).

Checks per case:
  - candidate vs baseline within the static contract tolerance;
  - candidate vs fp32 oracle within the static contract tolerance
    (the bar upstream applies to its own kernel);
  - dynamic bound: max-abs error of the candidate vs the unrounded fp32
    reference must be <= 2x the baseline's error + 1e-6;
  - NaN/Inf rejection and output shape/dtype checks (outputs poisoned where the
    allocation-return ABI allows it to matter).

Negative probes run last (riskiest CUDA behavior at the end); the remote driver
runs ``--mode probes`` as its own process.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import traceback
from pathlib import Path

import torch

BENCH_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BENCH_DIR))

import adapter  # noqa: E402

NSS = adapter.NSS
SRNSS = adapter.SRNSS

GRID_SHAPES = [(1, 1024, 8, 3072), (4, 512, 16, 3072)]  # (B, S, F, D)
GRID_DTYPES = ["float16", "bfloat16", "float32"]
GRID_NORM_TYPES = ["layer", "rms"]
GRID_AFFINE_MODES = ["D", "NAT"]
GRID_INDEX_MODES = ["BSD", "1", "1SD", "BD", "B1D", "D", "1D", "11D", "BF1D"]
GRID_EPS = 1e-5


def _tol(*dtype_names: str | None) -> float:
    present = [d for d in dtype_names if d]
    return 5e-2 if any(d != "float32" for d in present) else 1e-5


def _expand_bsfd(t: torch.Tensor | None, B: int, S: int, D: int) -> torch.Tensor | None:
    """Broadcast an operand of any contract layout to a (B, S, D) fp32 view."""
    if t is None:
        return None
    f = t.float()
    if f.ndim == 1:
        f = f.view(1, 1, -1) if f.numel() != 1 else f.view(1, 1, 1)
    elif f.ndim == 2:
        f = f.unsqueeze(1)  # [B?, D] -> [B?, 1, D]
    elif f.ndim == 4:
        F = f.shape[1]
        f = f.expand(f.shape[0], F, S // F, D).reshape(f.shape[0], S, D)
    return f.expand(B, S, D)


def _norm_fp32(v: torch.Tensor, weight, bias, norm_type: str, eps: float) -> torch.Tensor:
    wf = weight.float() if weight is not None else None
    bf = bias.float() if bias is not None else None
    if norm_type == "layer":
        return torch.layer_norm(v, v.shape[-1:], weight=wf, bias=bf, eps=eps)
    return torch.rms_norm(v, v.shape[-1:], weight=wf, eps=eps)


def reference_nss(inputs: dict) -> dict:
    x = inputs["x"]
    B, S, D = x.shape
    normed = _norm_fp32(x.float(), inputs["weight"], inputs["bias"],
                        inputs["norm_type"], inputs["eps"])
    scale = _expand_bsfd(inputs["scale"], B, S, D)
    shift = _expand_bsfd(inputs["shift"], B, S, D)
    y_f32 = normed * (1 + scale) + shift
    return {"y_f32": y_f32, "y": y_f32.to(x.dtype)}


def reference_srnss(inputs: dict) -> dict:
    x = inputs["x"]
    B, S, D = x.shape
    v = x.float()
    gate = inputs.get("gate")
    if gate is not None:
        v = _expand_bsfd(gate, B, S, D) * v
    v = inputs["residual"].float() + v
    normed = _norm_fp32(v, inputs["weight"], inputs["bias"],
                        inputs["norm_type"], inputs["eps"])
    scale = _expand_bsfd(inputs["scale"], B, S, D)
    shift = _expand_bsfd(inputs["shift"], B, S, D)
    y_f32 = normed * (1 + scale) + shift
    return {"y_f32": y_f32, "y": y_f32.to(x.dtype),
            "res_out_f32": v, "res_out": v.to(x.dtype)}


def reference(function: str, inputs: dict) -> dict:
    return reference_nss(inputs) if function == NSS else reference_srnss(inputs)


def _max_abs(a: torch.Tensor, b: torch.Tensor) -> float:
    if a.numel() == 0:
        return 0.0
    return float((a.float() - b.float()).abs().max().item())


def _assert_close(name: str, got: torch.Tensor, want: torch.Tensor, tol: float) -> list[str]:
    errors = []
    if got.shape != want.shape:
        return [f"{name}: shape {tuple(got.shape)} != {tuple(want.shape)}"]
    if got.dtype != want.dtype:
        errors.append(f"{name}: dtype {got.dtype} != {want.dtype}")
    gf, wf = got.float(), want.float()
    if torch.isnan(gf).any() or torch.isinf(gf).any():
        return errors + [f"{name}: contains NaN/Inf"]
    diff = (gf - wf).abs()
    bound = tol + tol * wf.abs()
    if diff.numel() and not bool(torch.all(diff <= bound).item()):
        errors.append(
            f"{name}: max_abs={float(diff.max()):.3e} exceeds atol=rtol={tol}"
        )
    return errors


def run_case(function: str, inputs: dict, tol: float, *, sides=("baseline", "candidate")) -> list[str]:
    errors: list[str] = []
    ref = reference(function, inputs)
    outs: dict[str, dict] = {}
    for side in sides:
        module = adapter.baseline_binding() if side == "baseline" else adapter.candidate_binding()
        out: dict = {}
        adapter._call(module, {"function": function}, inputs, out)
        torch.cuda.synchronize()
        outs[side] = out
        for key in ("y",) + (("res_out",) if function == SRNSS else ()):
            errors += _assert_close(f"{side}.{key} vs oracle", out[key], ref[key], tol)

    if "baseline" in outs and "candidate" in outs:
        for key in ("y",) + (("res_out",) if function == SRNSS else ()):
            errors += _assert_close(
                f"candidate.{key} vs baseline", outs["candidate"][key], outs["baseline"][key], tol
            )
            err_b = _max_abs(outs["baseline"][key], ref[f"{key}_f32"])
            err_c = _max_abs(outs["candidate"][key], ref[f"{key}_f32"])
            if err_c > 2.0 * err_b + 1e-6:
                errors.append(
                    f"dynamic bound on {key}: candidate err {err_c:.3e} > 2x baseline err {err_b:.3e} + 1e-6"
                )
    return errors


def _seed_for(case_id: str, seed: int) -> None:
    component = int.from_bytes(hashlib.sha256(case_id.encode()).digest()[:2], "little")
    torch.manual_seed(seed + component)
    torch.cuda.manual_seed_all(seed + component)


def production_cases(workloads_path: Path):
    rows = json.loads(workloads_path.read_text())
    for row in rows:
        if not row.get("production"):
            continue
        yield row["id"], row


def run_production(args, device) -> list[dict]:
    results = []
    cand = None
    if "candidate" in args.sides and hasattr(adapter.candidate_binding(), "dispatch_stats"):
        cand = adapter.candidate_binding()
        before = dict(cand.dispatch_stats())
    for case_id, row in production_cases(args.workloads):
        _seed_for(case_id, args.seed)
        inputs = adapter.build_inputs(row, device)
        tol = float(row["atol"])
        try:
            errors = run_case(row["function"], inputs, tol, sides=args.sides)
        except Exception:
            errors = [f"exception: {traceback.format_exc()}"]
        results.append({"case": case_id, "kind": "production", "errors": errors})
        del inputs
        torch.cuda.empty_cache() if row["shapes"]["S"] >= 100000 else None
    if cand is not None:
        after = dict(cand.dispatch_stats())
        fallback_delta = after.get("fallback", 0) - before.get("fallback", 0)
        routed_delta = after.get("routed", 0) - before.get("routed", 0)
        # Production rows expected on the routed path: nss with row-class
        # (D/1D/11D) fp32 scale/shift, mirroring _ROUTED_TO_BASELINE.
        expected_routed = sum(
            1
            for _, row in production_cases(args.workloads)
            if row["function"] == NSS
            and row["shapes"]["scale"]["layout"] in ("D", "1D", "11D")
            and row["shapes"]["scale"]["dtype"] == "float32"
        )
        errors = []
        if fallback_delta != 0:
            errors.append(
                f"{fallback_delta} production calls fell back unexpectedly "
                f"(routed buckets are counted separately)"
            )
        if routed_delta != expected_routed:
            errors.append(
                f"routed-call count {routed_delta} != expected {expected_routed} "
                f"(declared routed bucket: nss row-class fp32 scale/shift)"
            )
        results.append({
            "case": "production-grid-native-routing",
            "kind": "production",
            "errors": errors,
            "routed_calls": routed_delta,
            "routed_calls_expected": expected_routed,
        })
    return results


def grid_cases():
    """Mirror the upstream canonical test's per-dimension parametrization on the contract shapes."""
    base_shape = GRID_SHAPES[0]
    for function in (NSS, SRNSS):
        for norm in GRID_NORM_TYPES:
            for shape in GRID_SHAPES:
                for dt in GRID_DTYPES:
                    yield function, f"shape{shape[1]}x{shape[3]}-{dt}-{norm}", dict(
                        shape=shape, dtype=dt, norm=norm)
            for dt in GRID_DTYPES:
                yield function, f"affine-{dt}-{norm}", dict(
                    shape=base_shape, dtype="float16", affine_dtype=dt, norm=norm)
            for dt in GRID_DTYPES:
                yield function, f"scaleshift-{dt}-{norm}", dict(
                    shape=base_shape, dtype="float16", ss_dtype=dt, norm=norm)
            for affine in GRID_AFFINE_MODES:
                yield function, f"affinemode-{affine}-{norm}", dict(
                    shape=base_shape, dtype="float16", affine_mode=affine, norm=norm)
            for mode in GRID_INDEX_MODES:
                yield function, f"ssmode-{mode}-{norm}", dict(
                    shape=base_shape, dtype="float16", ss_mode=mode, norm=norm)
            if function == SRNSS:
                for mode in GRID_INDEX_MODES:
                    yield function, f"gatemode-{mode}-{norm}", dict(
                        shape=base_shape, dtype="float16", gate_mode=mode, norm=norm)


def build_grid_inputs(function: str, cfg: dict, device) -> dict:
    B, S, F, D = cfg["shape"]
    x_dt = adapter.DTYPES[cfg["dtype"]]
    affine_dt = adapter.DTYPES[cfg.get("affine_dtype", cfg["dtype"])]
    ss_dt = adapter.DTYPES[cfg.get("ss_dtype", cfg["dtype"])]
    affine_mode = cfg.get("affine_mode", "D")
    ss_mode = cfg.get("ss_mode", "BSD")
    gate_mode = cfg.get("gate_mode", "B1D")

    def make(mode, dt):
        if mode == "NAT":
            return None
        shape = adapter.operand_shape(mode, B, S, D, F)
        return torch.randn(shape, dtype=dt, device=device)

    x = torch.randn((B, S, D), dtype=x_dt, device=device)
    inputs = {
        "x": x,
        "weight": make(affine_mode if affine_mode == "NAT" else "D", affine_dt),
        "bias": make(affine_mode if affine_mode == "NAT" else "D", affine_dt),
        "scale": make(ss_mode, ss_dt),
        "shift": make(ss_mode, ss_dt),
        "norm_type": cfg["norm"],
        "eps": GRID_EPS,
    }
    if function == SRNSS:
        inputs["residual"] = torch.randn_like(x)
        inputs["gate"] = make(gate_mode, x_dt)
    return inputs


def run_grid(args, device) -> list[dict]:
    results = []
    for function, tag, cfg in grid_cases():
        case_id = f"grid-{'nss' if function == NSS else 'srnss'}-{tag}"
        _seed_for(case_id, args.seed)
        inputs = build_grid_inputs(function, cfg, device)
        tol = _tol(cfg["dtype"], cfg.get("ss_dtype"), cfg.get("affine_dtype"))
        try:
            errors = run_case(function, inputs, tol, sides=args.sides)
        except Exception:
            errors = [f"exception: {traceback.format_exc()}"]
        results.append({"case": case_id, "kind": "grid", "errors": errors})
    return results


# ---------------------------------------------------------------------------
# Negative probes
# ---------------------------------------------------------------------------

def _behavior(fn):
    """Capture (exception type name) or ('ok', output) for behavior-parity probes."""
    try:
        out = fn()
        torch.cuda.synchronize()
        return ("ok", out)
    except Exception as exc:  # noqa: BLE001
        return ("raise:" + type(exc).__name__, None)


def _parity_probe(name: str, function: str, inputs: dict) -> dict:
    base = adapter.baseline_binding()
    cand = adapter.candidate_binding()

    def call(module):
        out: dict = {}
        adapter._call(module, {"function": function}, inputs, out)
        return out

    b_kind, b_out = _behavior(lambda: call(base))
    c_kind, c_out = _behavior(lambda: call(cand))
    errors = []
    if b_kind.startswith("raise") or c_kind.startswith("raise"):
        if b_kind != c_kind:
            errors.append(f"behavior mismatch: baseline={b_kind} candidate={c_kind}")
    else:
        for key in b_out:
            if b_out[key].shape != c_out[key].shape:
                errors.append(f"{key}: shape mismatch on accepted edge input")
            elif b_out[key].numel() and not torch.equal(
                torch.nan_to_num(b_out[key].float(), nan=0.0),
                torch.nan_to_num(c_out[key].float(), nan=0.0),
            ):
                diff = _max_abs(b_out[key], c_out[key])
                if diff > 5e-2:
                    errors.append(f"{key}: outputs differ on accepted edge input (max_abs={diff:.3e})")
    return {"case": f"probe-{name}", "kind": "probe", "errors": errors,
            "behavior": {"baseline": b_kind, "candidate": c_kind}}


def run_probes(args, device) -> list[dict]:
    results = []
    bf16 = torch.bfloat16
    B, S, D = 1, 1024, 3072

    def base_inputs(function=NSS, dtype=bf16, S_=S):
        x = torch.randn((B, S_, D), dtype=dtype, device=device)
        inputs = {
            "x": x, "weight": None, "bias": None,
            "scale": torch.randn((1, 1, D), dtype=dtype, device=device),
            "shift": torch.randn((1, 1, D), dtype=dtype, device=device),
            "norm_type": "layer", "eps": 1e-5,
        }
        if function == SRNSS:
            inputs["residual"] = torch.randn_like(x)
            inputs["gate"] = torch.randn((1, 1, D), dtype=dtype, device=device)
        return inputs

    # 1. Wrong-formula detector: a missing "1 +" must be caught by the oracle check.
    torch.manual_seed(args.seed)
    inputs = base_inputs()
    ref = reference_nss(inputs)
    wrong = _norm_fp32(inputs["x"].float(), None, None, "layer", 1e-5) \
        * _expand_bsfd(inputs["scale"], B, S, D) + _expand_bsfd(inputs["shift"], B, S, D)
    detector_works = bool((ref["y_f32"] - wrong).abs().max().item() > 5e-2)
    results.append({"case": "probe-wrong-formula-detectable", "kind": "probe",
                    "errors": [] if detector_works else
                    ["oracle cannot distinguish norm*(1+scale) from norm*scale on this input"]})

    # 2. Argument-order probe: swapping residual and x must change the result.
    inputs = base_inputs(SRNSS)
    inputs["gate"] = torch.randn((1, 1, D), dtype=bf16, device=device)  # non-trivial gate
    ref_ok = reference_srnss(inputs)
    swapped = dict(inputs)
    swapped["x"], swapped["residual"] = inputs["residual"], inputs["x"]
    ref_swapped = reference_srnss(swapped)
    distinct = bool((ref_ok["y_f32"] - ref_swapped["y_f32"]).abs().max().item() > 5e-2)
    out: dict = {}
    adapter._call(adapter.baseline_binding(), {"function": SRNSS}, inputs, out)
    torch.cuda.synchronize()
    order_held = _assert_close("argorder", out["res_out"], ref_ok["res_out"], 5e-2) == []
    results.append({"case": "probe-argument-order", "kind": "probe",
                    "errors": ([] if (distinct and order_held) else
                               ["argument-order probe failed: " +
                                ("oracle not order-sensitive; " if not distinct else "") +
                                ("baseline does not match correct order" if not order_held else "")])})

    # 3. NaN and Inf injection must be REJECTED BY THE CHECKER (not merely
    # propagate): run_case on a poisoned input must report NaN/Inf errors.
    for probe_name, bad_value in (
        ("probe-nan-detection", float("nan")),
        ("probe-inf-detection", float("inf")),
    ):
        _seed_for(probe_name, args.seed)
        inputs = base_inputs()
        inputs["x"][0, 0, 0] = bad_value
        try:
            checker_errors = run_case(NSS, inputs, 5e-2, sides=args.sides)
            flagged = any("NaN/Inf" in e for e in checker_errors)
            probe_errors = [] if flagged else [
                "checker did not flag NaN/Inf on a poisoned input "
                f"(checker errors: {checker_errors[:2] if checker_errors else 'none'})"
            ]
        except Exception:
            probe_errors = [f"exception: {traceback.format_exc()}"]
        results.append({"case": probe_name, "kind": "probe", "errors": probe_errors})

    if "candidate" in args.sides:
        # 4-9: behavior parity on edge inputs (candidate must fail closed like the baseline).
        results.append(_parity_probe("empty-rows", NSS, base_inputs(S_=0)))

        cpu_case = base_inputs()
        cpu_case["scale"] = cpu_case["scale"].cpu()
        results.append(_parity_probe("cpu-operand", NSS, cpu_case))

        none_case = base_inputs()
        none_case["scale"] = None
        results.append(_parity_probe("non-tensor-scale", NSS, none_case))

        noncontig = base_inputs()
        noncontig["scale"] = torch.randn((D, 1, 1), dtype=bf16, device=device).permute(2, 1, 0)
        results.append(_parity_probe("non-contiguous-scale", NSS, noncontig))

        misaligned = base_inputs()
        buf = torch.randn(B * S * D + 1, dtype=bf16, device=device)
        misaligned["x"] = buf[1:].view(B, S, D)
        results.append(_parity_probe("misaligned-x", NSS, misaligned))

        bf1d = base_inputs()
        bf1d["x"] = torch.randn((1, 1000, D), dtype=bf16, device=device)
        bf1d["scale"] = torch.randn((1, 7, 1, D), dtype=bf16, device=device)
        bf1d["shift"] = torch.randn((1, 7, 1, D), dtype=bf16, device=device)
        results.append(_parity_probe("bf1d-non-divisible", NSS, bf1d))

        if torch.cuda.device_count() > 1:
            xdev = base_inputs()
            xdev["scale"] = xdev["scale"].to("cuda:1" if str(device) != "cuda:1" else "cuda:0")
            results.append(_parity_probe("cross-device-operand", NSS, xdev))

        # 10. Dispatcher fallback counters must move on fallback-class inputs.
        cand = adapter.candidate_binding()
        if hasattr(cand, "dispatch_stats"):
            before = dict(cand.dispatch_stats())
            probe_in = base_inputs()
            probe_in["scale"] = probe_in["scale"].cpu()
            try:
                out = {}
                adapter._call(cand, {"function": NSS}, probe_in, out)
                torch.cuda.synchronize()
            except Exception:
                pass
            after = dict(cand.dispatch_stats())
            moved = after.get("fallback", 0) > before.get("fallback", 0)
            results.append({"case": "probe-fallback-counter", "kind": "probe",
                            "errors": [] if moved else
                            ["fallback counter did not increment on a CPU-operand input"]})

    # 11. High-mean / low-variance layer norm stress (two-pass variance accuracy).
    inputs = base_inputs()
    inputs["x"] = (16.0 + 0.5 * torch.randn((B, S, D), device=device)).to(bf16)
    tol = 5e-2
    try:
        errors = run_case(NSS, inputs, tol, sides=args.sides)
    except Exception:
        errors = [f"exception: {traceback.format_exc()}"]
    results.append({"case": "probe-high-mean-low-variance", "kind": "probe", "errors": errors})

    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--mode", choices=["all", "production", "grid", "probes"], default="all")
    parser.add_argument("--workloads", type=Path, default=BENCH_DIR / "workloads.json")
    parser.add_argument("--seed", type=int, default=20260604)
    parser.add_argument("--report", type=Path, default=BENCH_DIR / "correctness_report.json")
    parser.add_argument("--sides", default="baseline,candidate",
                        help="comma list: baseline,candidate (baseline-only sanity: 'baseline')")
    args = parser.parse_args()
    args.sides = tuple(s.strip() for s in args.sides.split(",") if s.strip())

    if not torch.cuda.is_available():
        raise SystemExit("CUDA is required")
    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)

    results: list[dict] = []
    if args.mode in ("all", "production"):
        results += run_production(args, device)
    if args.mode in ("all", "grid"):
        results += run_grid(args, device)
    if args.mode in ("all", "probes"):
        results += run_probes(args, device)

    failed = [r for r in results if r["errors"]]
    summary = {
        "device": str(device),
        "gpu": torch.cuda.get_device_name(device),
        "mode": args.mode,
        "sides": list(args.sides),
        "seed": args.seed,
        "total": len(results),
        "failed": len(failed),
        "results": results,
    }
    args.report.write_text(json.dumps(summary, indent=2) + "\n")
    for r in failed:
        print(f"FAIL {r['case']}")
        for e in r["errors"]:
            print(f"  - {e}")
    print(f"correctness: {len(results) - len(failed)}/{len(results)} passed "
          f"(mode={args.mode}, sides={','.join(args.sides)}) -> {args.report}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
