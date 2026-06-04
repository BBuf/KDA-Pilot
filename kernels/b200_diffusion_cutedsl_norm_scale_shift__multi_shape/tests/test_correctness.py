"""Correctness tests for ``b200_diffusion_cutedsl_norm_scale_shift__multi_shape``.

Pytest entry point wired to ``bench/correctness.py`` (case construction,
fp32 references, tolerance policy). Requires a CUDA device plus the vendored
baseline's dependencies (torch, cuda-python, nvidia-cutlass-dsl, einops) —
i.e. the ``sglang_bbuf`` container on ion-b200. Gated behind
``KDA_RUN_CORRECTNESS=1`` so collection stays cheap elsewhere.

Implementation under test: ``KDA_IMPL=candidate`` (default; the public wrapper
in ``src/register.py`` routing native-or-fallback) or ``KDA_IMPL=baseline``
(harness self-validation against the vendored baseline only).
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "b200_diffusion_cutedsl_norm_scale_shift__multi_shape"
OP_TYPE = "cutedsl_norm_scale_shift"
KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = [
    pytest.mark.skipif(
        os.environ.get("KDA_RUN_CORRECTNESS") != "1",
        reason="Set KDA_RUN_CORRECTNESS=1 inside the remote GPU container.",
    ),
    pytest.mark.skipif(
        torch is None or not (torch and torch.cuda.is_available()),
        reason="CUDA required",
    ),
]

IMPL = os.environ.get("KDA_IMPL", "candidate")


def _correctness():
    name = "kda_correctness_lib"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(
        name, KERNEL_DIR / "bench" / "correctness.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def test_register_metadata() -> None:
    lib = _correctness()
    spec = lib.candidate_register().register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])
    assert set(spec["exports"]) == {
        "fused_norm_scale_shift",
        "fused_scale_residual_norm_scale_shift",
    }


def test_registered_callable_routes_both_entry_points() -> None:
    """register()["callable"] must accept BOTH wrapped signatures (arity-routed)."""
    lib = _correctness()
    spec = lib.candidate_register().register()
    wrapper = spec["callable"]
    exports = spec["exports"]
    gen = torch.Generator(device="cuda")
    gen.manual_seed(123)
    mk = lambda *s: torch.randn(*s, generator=gen, device="cuda", dtype=torch.float32)
    x = mk(1, 64, 3072).to(torch.bfloat16)
    residual = mk(1, 64, 3072).to(torch.bfloat16)
    gate = (mk(1, 1, 3072) * 0.5).to(torch.bfloat16)
    sc = (mk(1, 1, 3072) * 0.5).to(torch.bfloat16)
    sh = (mk(1, 1, 3072) * 0.5).to(torch.bfloat16)

    # NSS arity (7 positional args)
    y_w = wrapper(x, None, None, sc, sh, "layer", 1e-6)
    y_e = exports["fused_norm_scale_shift"](x, None, None, sc, sh, "layer", 1e-6)
    assert torch.equal(y_w, y_e) or torch.allclose(y_w.float(), y_e.float())

    # SRNSS arity (9 positional args) -> must NOT raise TypeError
    out_w = wrapper(residual, x, gate, None, None, sc, sh, "layer", 1e-6)
    out_e = exports["fused_scale_residual_norm_scale_shift"](
        residual, x, gate, None, None, sc, sh, "layer", 1e-6
    )
    for a, b in zip(out_w, out_e):
        assert torch.equal(a, b) or torch.allclose(a.float(), b.float())

    # SRNSS with 8 positional args (eps defaulted) and keyword forms
    out8 = wrapper(residual, x, gate, None, None, sc, sh, "layer")
    assert isinstance(out8, tuple) and len(out8) == 2
    out_kw = wrapper(
        residual=residual, x=x, gate=gate, weight=None, bias=None,
        scale=sc, shift=sh, norm_type="layer", eps=1e-6,
    )
    assert isinstance(out_kw, tuple) and len(out_kw) == 2
    y_kw = wrapper(x=x, weight=None, bias=None, scale=sc, shift=sh,
                   norm_type="layer", eps=1e-6)
    assert isinstance(y_kw, torch.Tensor)


def _production_cases():
    lib = _correctness()
    return [(c.case_id, c) for c in lib.production_cases()]


@pytest.mark.parametrize(
    "case_id,case", _production_cases() if os.environ.get("KDA_RUN_CORRECTNESS") == "1" else []
)
def test_production_signature(case_id, case) -> None:
    lib = _correctness()
    lib.run_production_case(case, IMPL)


def test_production_dispatch_all_native() -> None:
    """Every unique captured signature must take the native path (no fallback)."""
    if IMPL != "candidate":
        pytest.skip("dispatch-log assertion applies to the candidate wrapper")
    lib = _correctness()
    reg = lib.candidate_register()
    stats = reg.dispatch_stats()
    stats.clear()
    for case in lib.production_cases():
        lib.run_production_case(case, "candidate")
    assert stats.get("fallback", 0) == 0, f"production fallbacks: {dict(stats)}"
    assert stats.get("native", 0) > 0


@pytest.mark.parametrize(
    "kw",
    [
        pytest.param(kw, id=f"A{i}")
        for i, kw in enumerate(_correctness().grid_cases_shape_dtype())
    ]
    if os.environ.get("KDA_RUN_CORRECTNESS") == "1"
    else [],
)
def test_grid_shape_dtype(kw) -> None:
    _correctness().run_grid_case(IMPL, **kw)


@pytest.mark.parametrize(
    "kw",
    [
        pytest.param(kw, id=f"B{i}")
        for i, kw in enumerate(_correctness().grid_cases_affine())
    ]
    if os.environ.get("KDA_RUN_CORRECTNESS") == "1"
    else [],
)
def test_grid_affine(kw) -> None:
    _correctness().run_grid_case(IMPL, **kw)


@pytest.mark.parametrize(
    "kw",
    [
        pytest.param(kw, id=f"C{i}-{kw['index_mode']}")
        for i, kw in enumerate(_correctness().grid_cases_index_modes())
    ]
    if os.environ.get("KDA_RUN_CORRECTNESS") == "1"
    else [],
)
def test_grid_index_modes(kw) -> None:
    _correctness().run_grid_case(IMPL, **kw)


@pytest.mark.parametrize(
    "kw",
    [
        pytest.param(kw, id=f"D{i}-g{kw['gate_mode']}")
        for i, kw in enumerate(_correctness().grid_cases_gate_modes())
    ]
    if os.environ.get("KDA_RUN_CORRECTNESS") == "1"
    else [],
)
def test_grid_gate_modes(kw) -> None:
    _correctness().run_grid_case(IMPL, **kw)


@pytest.mark.parametrize(
    "kw",
    [
        pytest.param(kw, id=f"E{i}")
        for i, kw in enumerate(_correctness().grid_cases_srnss_shape_dtype())
    ]
    if os.environ.get("KDA_RUN_CORRECTNESS") == "1"
    else [],
)
def test_grid_srnss_shape_dtype(kw) -> None:
    _correctness().run_grid_case(IMPL, **kw)


def test_validate_rejects_non_divisible_frames() -> None:
    """BF1D scale with S % F != 0 must raise (mirrors the SGLang test)."""
    lib = _correctness()
    nss, _ = lib.implementations(IMPL)
    B, S, F, D = 1, 1000, 7, 3072  # 1000 % 7 != 0
    x = torch.randn(B, S, D, device="cuda", dtype=torch.bfloat16)
    bad = torch.randn(B, F, 1, D, device="cuda", dtype=torch.bfloat16)
    with pytest.raises(ValueError, match="divisible"):
        nss(x, None, None, bad, bad, "layer", 1e-5)


def test_argument_order_probe() -> None:
    """Swapping residual/x with a non-trivial gate must mismatch the oracle."""
    lib = _correctness()
    _, srnss = lib.implementations(IMPL)
    gen = torch.Generator(device="cuda")
    gen.manual_seed(99)
    B, S, D = 1, 64, 3072
    mk = lambda *s: torch.randn(*s, generator=gen, device="cuda", dtype=torch.float32)
    residual = mk(B, S, D).to(torch.bfloat16)
    x = mk(B, S, D).to(torch.bfloat16)
    gate = (mk(1, 1, D) * 0.5).to(torch.bfloat16)
    scale = (mk(1, 1, D) * 0.5).to(torch.bfloat16)
    shift = (mk(1, 1, D) * 0.5).to(torch.bfloat16)
    ref_y, _ = lib.reference_scale_residual_norm_scale_shift(
        residual, x, gate, None, None, scale, shift, "layer", 1e-5
    )
    y_swapped, _ = srnss(x, residual, gate, None, None, scale, shift, "layer", 1e-5)
    err = (y_swapped.float() - ref_y).abs().max().item()
    assert err > 0.1, f"swapped args unexpectedly matched oracle (err={err:.3e})"


def test_nan_detection() -> None:
    """NaN in any input must be caught by the harness finiteness check."""
    lib = _correctness()
    nss, _ = lib.implementations(IMPL)
    x = torch.randn(1, 64, 3072, device="cuda", dtype=torch.bfloat16)
    x[0, 3, 5] = float("nan")
    sc = torch.zeros(1, 1, 3072, device="cuda", dtype=torch.bfloat16)
    out = nss(x, None, None, sc, sc, "layer", 1e-5)
    base = lib.implementations("baseline")[0](x, None, None, sc, sc, "layer", 1e-5)
    ref = lib.reference_norm_scale_shift(x, None, None, sc, sc, "layer", 1e-5)
    with pytest.raises(AssertionError, match="NaN/Inf"):
        lib.assert_outputs_close("nan-probe", out, base, ref)


def test_checker_rejects_wrong_formula() -> None:
    """The tolerance machinery must reject a wrong-formula candidate."""
    lib = _correctness()
    gen = torch.Generator(device="cuda")
    gen.manual_seed(7)
    x = torch.randn(1, 128, 3072, generator=gen, device="cuda", dtype=torch.float32).to(
        torch.bfloat16
    )
    sc = (
        torch.randn(1, 1, 3072, generator=gen, device="cuda", dtype=torch.float32) * 0.5
    ).to(torch.bfloat16)
    base = lib.implementations("baseline")[0](x, None, None, sc, sc, "layer", 1e-5)
    ref = lib.reference_norm_scale_shift(x, None, None, sc, sc, "layer", 1e-5)
    # wrong formula: norm(x) * scale + shift (missing the "1 +")
    normf = lib._norm_f32(x.float(), None, None, "layer", 1e-5)
    wrong = (normf * sc.float() + sc.float()).to(torch.bfloat16)
    with pytest.raises(AssertionError):
        lib.assert_outputs_close("wrong-formula", wrong, base, ref)


def test_snapshot_only_guard() -> None:
    """No real SGLang modules may be imported during harness runs."""
    lib = _correctness()
    lib.snapshot_guard()


def test_high_mean_low_variance_rows() -> None:
    """Adversarial layer-norm statistics: large mean, small variance.

    bf16 inputs cap the representable mean/std ratio (ulp(16)=0.125), but this
    still exercises the variance path where a fused E[x^2]-mean^2 form loses
    precision; the shipped two-pass form must track the fp32 reference within
    the dynamic bound.
    """
    lib = _correctness()
    nss, _ = lib.implementations(IMPL)
    gen = torch.Generator(device="cuda")
    gen.manual_seed(11)
    x = (
        16.0
        + 0.5 * torch.randn(1, 256, 3072, generator=gen, device="cuda", dtype=torch.float32)
    ).to(torch.bfloat16)
    sc = (
        torch.randn(1, 1, 3072, generator=gen, device="cuda", dtype=torch.float32) * 0.5
    ).to(torch.bfloat16)
    out = nss(x, None, None, sc, sc, "layer", 1e-6)
    base = lib.implementations("baseline")[0](x, None, None, sc, sc, "layer", 1e-6)
    ref = lib.reference_norm_scale_shift(x, None, None, sc, sc, "layer", 1e-6)
    lib.assert_outputs_close("high-mean-low-var", out, base, ref)


def test_cpu_operand_falls_back() -> None:
    """A CPU scale/shift must never reach the native path (fail-closed)."""
    if IMPL != "candidate":
        pytest.skip("dispatch assertion applies to the candidate wrapper")
    lib = _correctness()
    reg = lib.candidate_register()
    nss, _ = lib.implementations("candidate")
    stats = reg.dispatch_stats()
    before_native = stats.get("native", 0)
    x = torch.randn(1, 64, 3072, device="cuda", dtype=torch.bfloat16)
    sc_cpu = torch.zeros(1, 1, 3072, dtype=torch.bfloat16)  # cpu tensor
    try:
        nss(x, None, None, sc_cpu, sc_cpu, "layer", 1e-5)
    except Exception:
        pass  # whatever the baseline does with cpu operands is its contract
    assert stats.get("native", 0) == before_native, "cpu operand took native path"


def test_empty_rows_falls_back() -> None:
    """S=0 activations must never reach the native path."""
    if IMPL != "candidate":
        pytest.skip("dispatch assertion applies to the candidate wrapper")
    lib = _correctness()
    reg = lib.candidate_register()
    nss, _ = lib.implementations("candidate")
    stats = reg.dispatch_stats()
    before_native = stats.get("native", 0)
    x = torch.empty(1, 0, 3072, device="cuda", dtype=torch.bfloat16)
    sc = torch.zeros(1, 1, 3072, device="cuda", dtype=torch.bfloat16)
    try:
        nss(x, None, None, sc, sc, "layer", 1e-5)
    except Exception:
        pass  # baseline behavior for empty rows is its own contract
    assert stats.get("native", 0) == before_native, "empty rows took native path"


def test_non_tensor_scale_falls_back() -> None:
    """scale=None must route to the baseline's own validation, not crash the wrapper."""
    if IMPL != "candidate":
        pytest.skip("dispatch assertion applies to the candidate wrapper")
    lib = _correctness()
    reg = lib.candidate_register()
    _, srnss = lib.implementations("candidate")
    stats = reg.dispatch_stats()
    before_native = stats.get("native", 0)
    x = torch.randn(1, 64, 3072, device="cuda", dtype=torch.bfloat16)
    with pytest.raises(Exception):
        srnss(x.clone(), x, None, None, None, None, None, "layer", 1e-5)
    assert stats.get("native", 0) == before_native
