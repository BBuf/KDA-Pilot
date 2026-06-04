"""Correctness library for the norm-scale-shift kernel family.

Provides fp32 references, the tolerance policy, the production case set (39
unique captured signatures), the adapted SGLang regression grid, and negative
probes. ``tests/test_correctness.py`` is the pytest entry point wired to this
module; ``bench/benchmark.py`` reuses the same case construction.

Tolerance policy (per criterion AC-2.3 of the task plan):
  1. static outer bound: candidate vs baseline-copy agree within the SGLang
     reference-test tolerance (atol=rtol=5e-2 non-fp32, 1e-5 fp32);
  2. dynamic bound: candidate's max-abs error vs the fp32 reference must not
     exceed ``DYN_MULT`` x the baseline-copy's own error vs the same reference
     (plus a tiny floor for exact-zero baseline error).
Every check asserts finiteness (NaN/Inf rejection) first.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import torch

BENCH_DIR = Path(__file__).resolve().parent
KERNEL_DIR = BENCH_DIR.parent

DYN_MULT = 2.0
DYN_FLOOR = 1e-6


def _load_module(name: str, path: Path):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, path
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod  # required: dataclasses resolves cls.__module__
    spec.loader.exec_module(mod)
    return mod


def shapes_mod():
    return _load_module("kda_shapes", BENCH_DIR / "shapes.py")


def baseline_entry():
    return _load_module("kda_baseline_entry", KERNEL_DIR / "baseline" / "entry.py")


def candidate_register():
    return _load_module("kda_candidate_register", KERNEL_DIR / "src" / "register.py")


def implementations(impl: str):
    """Return (fused_norm_scale_shift, fused_scale_residual_norm_scale_shift)."""
    if impl == "baseline":
        mod = baseline_entry()
        return mod.fused_norm_scale_shift, mod.fused_scale_residual_norm_scale_shift
    if impl == "candidate":
        exports = candidate_register().register()["exports"]
        return (
            exports["fused_norm_scale_shift"],
            exports["fused_scale_residual_norm_scale_shift"],
        )
    raise ValueError(impl)


# ---------------------------------------------------------------------------
# FP32 references (mirroring the pinned SGLang test oracle)
# ---------------------------------------------------------------------------


def _apply_scale_shift_f32(y: torch.Tensor, scale, shift) -> torch.Tensor:
    """y * (1 + scale) + shift with 2-D/3-D broadcast or 4-D frame layout."""
    B, S, D = y.shape
    sf = scale.float()
    hf = shift.float()
    if sf.ndim == 4:
        F = sf.shape[1]
        y4 = y.reshape(B, F, S // F, D)
        out = y4 * (1 + sf) + hf
        return out.reshape(B, S, D)
    if sf.ndim == 1 and sf.numel() != 1:
        sf = sf.view(1, 1, D)
    if hf.ndim == 1 and hf.numel() != 1:
        hf = hf.view(1, 1, D)
    if sf.ndim == 2:
        sf = sf.unsqueeze(1)
    if hf.ndim == 2:
        hf = hf.unsqueeze(1)
    return y * (1 + sf) + hf


def _norm_f32(x_f32: torch.Tensor, weight, bias, norm_type: str, eps: float):
    D = x_f32.shape[-1]
    wf = weight.float() if weight is not None else None
    bf = bias.float() if bias is not None else None
    if norm_type == "layer":
        return torch.nn.functional.layer_norm(x_f32, (D,), wf, bf, eps)
    if norm_type == "rms":
        return torch.nn.functional.rms_norm(x_f32, (D,), wf, eps)
    raise ValueError(norm_type)


def reference_norm_scale_shift(x, weight, bias, scale, shift, norm_type, eps):
    y = _norm_f32(x.float(), weight, bias, norm_type, eps)
    return _apply_scale_shift_f32(y, scale, shift)


def reference_scale_residual_norm_scale_shift(
    residual, x, gate, weight, bias, scale, shift, norm_type, eps
):
    xf = x.float()
    if gate is not None:
        gf = gate.float()
        if gf.ndim == 1 and gf.numel() != 1:
            gf = gf.view(1, 1, -1)
        if gf.ndim == 2:
            gf = gf.unsqueeze(1)
        if gf.ndim == 4:
            B, S, D = x.shape
            F = gf.shape[1]
            xf = (xf.reshape(B, F, S // F, D) * gf).reshape(B, S, D)
        else:
            xf = gf * xf
    res_out = residual.float() + xf
    # Contract-exact: the baseline rounds the pre-norm value to x.dtype before
    # normalization (res_out stores the rounded value; the norm consumes it).
    norm_input = res_out.to(x.dtype).float()
    y = _norm_f32(norm_input, weight, bias, norm_type, eps)
    return _apply_scale_shift_f32(y, scale, shift), norm_input


# ---------------------------------------------------------------------------
# Tolerance checking
# ---------------------------------------------------------------------------


def static_tol(dtype: torch.dtype) -> float:
    return 1e-5 if dtype == torch.float32 else 5e-2


def assert_outputs_close(
    name: str,
    candidate_out: torch.Tensor,
    baseline_out: torch.Tensor,
    reference_f32: torch.Tensor,
    *,
    dyn_mult: float = DYN_MULT,
):
    if not torch.isfinite(candidate_out).all():
        raise AssertionError(f"{name}: candidate output contains NaN/Inf")
    if not torch.isfinite(baseline_out).all():
        raise AssertionError(f"{name}: baseline output contains NaN/Inf")
    tol = static_tol(candidate_out.dtype)
    torch.testing.assert_close(
        candidate_out, baseline_out, atol=tol, rtol=tol,
        msg=lambda m: f"{name}: static bound vs baseline failed\n{m}",
    )
    # Oracle invariant: the vendored baseline itself must sit within the
    # SGLang reference-test tolerance of the fp32 reference.
    torch.testing.assert_close(
        baseline_out.float(), reference_f32, atol=tol, rtol=tol,
        msg=lambda m: f"{name}: baseline vs fp32 reference exceeded tolerance\n{m}",
    )
    err_c = (candidate_out.float() - reference_f32).abs().max().item()
    err_b = (baseline_out.float() - reference_f32).abs().max().item()
    bound = dyn_mult * err_b + DYN_FLOOR
    if err_c > bound:
        raise AssertionError(
            f"{name}: dynamic bound failed: candidate_err={err_c:.3e} > "
            f"{dyn_mult}*baseline_err({err_b:.3e})+{DYN_FLOOR:g}={bound:.3e}"
        )


# ---------------------------------------------------------------------------
# Case execution
# ---------------------------------------------------------------------------


def run_production_case(case, impl: str, device="cuda", seed=20260604):
    """Run one unique captured signature; returns (outputs, baseline_outputs, refs)."""
    sm = shapes_mod()
    nss, srnss = implementations(impl)
    b_nss, b_srnss = implementations("baseline")
    tensors, norm_type, eps = sm.build_inputs(case, device=device, seed=seed)
    if case.sig.kernel == sm.NSS:
        x, weight, bias, scale, shift = tensors
        out = nss(x, weight, bias, scale, shift, norm_type, eps)
        base = (
            out
            if impl == "baseline"
            else b_nss(x, weight, bias, scale, shift, norm_type, eps)
        )
        ref = reference_norm_scale_shift(x, weight, bias, scale, shift, norm_type, eps)
        assert_outputs_close(case.case_id, out, base, ref)
    else:
        residual, x, gate, weight, bias, scale, shift = tensors
        y, res_out = srnss(residual, x, gate, weight, bias, scale, shift, norm_type, eps)
        if impl == "baseline":
            by, bres = y, res_out
        else:
            by, bres = b_srnss(
                residual, x, gate, weight, bias, scale, shift, norm_type, eps
            )
        ref_y, ref_res = reference_scale_residual_norm_scale_shift(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )
        assert_outputs_close(f"{case.case_id}.y", y, by, ref_y)
        assert_outputs_close(f"{case.case_id}.res_out", res_out, bres, ref_res)


def production_cases():
    cases, _ = shapes_mod().load_unique_cases()
    return cases


# ---------------------------------------------------------------------------
# Adapted regression grid (pinned-commit SGLang test, bounded subsets)
# ---------------------------------------------------------------------------

GRID_SHAPES = [  # (B, S, F, D) from the pinned test
    (1, 115200, 1, 3072),
    (1, 32760, 1, 1536),
    (1, 6, 1, 3072),
    (1, 1024, 8, 3072),
    (4, 512, 16, 3072),
]
GRID_DTYPES = [torch.float16, torch.bfloat16, torch.float32]
GRID_NORMS = ["layer", "rms"]
GRID_INDEX_MODES = ["BSD", "1", "1SD", "BD", "B1D", "D", "1D", "11D", "BF1D"]
GRID_EPS = 1e-5

_SHAPE_MAP = {
    "1": lambda B, S, F, D: (1,),
    "D": lambda B, S, F, D: (D,),
    "1D": lambda B, S, F, D: (1, D),
    "BD": lambda B, S, F, D: (B, D),
    "11D": lambda B, S, F, D: (1, 1, D),
    "B1D": lambda B, S, F, D: (B, 1, D),
    "1SD": lambda B, S, F, D: (1, S, D),
    "BSD": lambda B, S, F, D: (B, S, D),
    "BF1D": lambda B, S, F, D: (B, F, 1, D),
}


def _grid_tensor(shape, dtype, device, gen, kind):
    base = torch.randn(shape, generator=gen, device=device, dtype=torch.float32)
    if kind in ("scale", "shift", "gate"):
        base = base * 0.5
    elif kind == "weight":
        base = base * 0.25 + 1.0
    elif kind == "bias":
        base = base * 0.25
    return base.to(dtype)


def run_grid_case(
    impl: str,
    *,
    kernel: str,
    BSFD,
    dtype,
    norm_type: str,
    affine: str,
    index_mode: str,
    gate_mode=None,  # None / "none" / index-mode string (srnss only)
    device="cuda",
    seed=777,
):
    B, S, F, D = BSFD
    gen = torch.Generator(device=device)
    gen.manual_seed(seed)
    nss, srnss = implementations(impl)
    b_nss, b_srnss = implementations("baseline")

    x = _grid_tensor((B, S, D), dtype, device, gen, "x")
    weight = bias = None
    if affine == "D":
        weight = _grid_tensor((D,), dtype, device, gen, "weight")
        bias = _grid_tensor((D,), dtype, device, gen, "bias")
    op_shape = _SHAPE_MAP[index_mode](B, S, F, D)
    scale = _grid_tensor(op_shape, dtype, device, gen, "scale")
    shift = _grid_tensor(op_shape, dtype, device, gen, "shift")
    name = f"grid-{kernel}-B{B}S{S}F{F}D{D}-{str(dtype).split('.')[-1]}-{norm_type}-{affine}-{index_mode}"

    if kernel == "nss":
        out = nss(x, weight, bias, scale, shift, norm_type, GRID_EPS)
        base = (
            out
            if impl == "baseline"
            else b_nss(x, weight, bias, scale, shift, norm_type, GRID_EPS)
        )
        ref = reference_norm_scale_shift(
            x, weight, bias, scale, shift, norm_type, GRID_EPS
        )
        assert_outputs_close(name, out, base, ref)
        return name

    residual = _grid_tensor((B, S, D), dtype, device, gen, "x")
    gate = None
    if gate_mode not in (None, "none"):
        gate = _grid_tensor(_SHAPE_MAP[gate_mode](B, S, F, D), dtype, device, gen, "gate")
    name += f"-g{gate_mode or 'none'}"
    y, res_out = srnss(
        residual, x, gate, weight, bias, scale, shift, norm_type, GRID_EPS
    )
    if impl == "baseline":
        by, bres = y, res_out
    else:
        by, bres = b_srnss(
            residual, x, gate, weight, bias, scale, shift, norm_type, GRID_EPS
        )
    ref_y, ref_res = reference_scale_residual_norm_scale_shift(
        residual, x, gate, weight, bias, scale, shift, norm_type, GRID_EPS
    )
    assert_outputs_close(f"{name}.y", y, by, ref_y)
    assert_outputs_close(f"{name}.res_out", res_out, bres, ref_res)
    return name


def grid_cases_shape_dtype():
    for BSFD in GRID_SHAPES:
        for dtype in GRID_DTYPES:
            for norm in GRID_NORMS:
                yield dict(
                    kernel="nss", BSFD=BSFD, dtype=dtype, norm_type=norm,
                    affine="NAT", index_mode="11D",
                )


def grid_cases_affine():
    for affine in ("D", "NAT"):
        for norm in GRID_NORMS:
            yield dict(
                kernel="nss", BSFD=(1, 1024, 8, 3072), dtype=torch.bfloat16,
                norm_type=norm, affine=affine, index_mode="11D",
            )


def grid_cases_index_modes():
    for mode in GRID_INDEX_MODES:
        yield dict(
            kernel="nss", BSFD=(1, 1024, 8, 3072), dtype=torch.bfloat16,
            norm_type="layer", affine="NAT", index_mode=mode,
        )


def grid_cases_gate_modes():
    for gmode in ["none"] + GRID_INDEX_MODES:
        yield dict(
            kernel="srnss", BSFD=(1, 1024, 8, 3072), dtype=torch.bfloat16,
            norm_type="layer", affine="NAT", index_mode="11D", gate_mode=gmode,
        )


def grid_cases_srnss_shape_dtype():
    for BSFD in GRID_SHAPES[2:]:  # bounded: small + frame shapes
        for dtype in GRID_DTYPES:
            for norm in GRID_NORMS:
                yield dict(
                    kernel="srnss", BSFD=BSFD, dtype=dtype, norm_type=norm,
                    affine="D", index_mode="11D", gate_mode="B1D",
                )


def all_grid_cases():
    yield from grid_cases_shape_dtype()
    yield from grid_cases_affine()
    yield from grid_cases_index_modes()
    yield from grid_cases_gate_modes()
    yield from grid_cases_srnss_shape_dtype()


def snapshot_guard():
    baseline_entry()  # ensures loader is active
    sys.modules["kda_baseline_loader"].assert_snapshot_only()
