"""Correctness harness for ``h200_diffusion_norm_infer__multi_shape``.

Runs only when ``KDA_RUN_CORRECTNESS=1`` (a CUDA + SGLang environment is
required: the SGLang baselines and the optional candidate dispatcher are
imported lazily). Designed to run inside the ``sglang_bbuf`` container on the
remote H200 box.

Coverage:
- the six captured production shapes (helios LayerNorm fp32; five RMSNorm bf16
  ``D=128`` shapes);
- the canonical regression grid from the SGLang oracle test
  (``test_qwen_image_modulation.py``): LayerNorm over batch/seq/hidden/dtype;
- ``triton_one_pass_rms_norm`` cross-validation on the same ``M = B*S`` row
  counts and the per-head tiles ``(4096,128)`` / ``(16384,128)``;
- the select01 modulation oracle path that consumes ``norm_infer``.

Each case is checked against the SGLang baseline AND a PyTorch FP32 reference,
with explicit NaN/Inf assertions and dynamic (baseline-relative) tolerances on
top of the fixed SGLang tolerances (fp32 1e-5; bf16/fp16 5e-2).

``make_cases()`` / ``baseline(case)`` / ``candidate(case)`` are reused by
``benchmark.py``.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from typing import Any, Callable, Optional

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None  # type: ignore


KERNEL_SLUG = "h200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"
KERNEL_DIR = Path(__file__).resolve().parents[1]
DEVICE = "cuda"
EPS = 1e-6

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 in the CUDA+SGLang env to run.",
)


# --------------------------------------------------------------------------- #
# Module loading helpers
# --------------------------------------------------------------------------- #
_REGISTER_MODULE = None


def _load_register_module():
    # Load once and cache: re-exec'ing the module on every call adds ~100us of
    # importlib overhead per call, which would contaminate candidate timing
    # (the baseline path has no such cost) and make the comparison unfair.
    global _REGISTER_MODULE
    if _REGISTER_MODULE is None:
        register_py = KERNEL_DIR / "src" / "register.py"
        spec = importlib.util.spec_from_file_location(
            f"kda_kernel_{KERNEL_SLUG}_register", register_py
        )
        assert spec is not None and spec.loader is not None, register_py
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _REGISTER_MODULE = module
    return _REGISTER_MODULE


def _sglang_norm_infer():
    from sglang.jit_kernel.diffusion.triton.norm import norm_infer

    return norm_infer


def _sglang_rms_norm():
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
        triton_one_pass_rms_norm,
    )

    return triton_one_pass_rms_norm


def _candidate_callable(entry: str) -> Optional[Callable[..., Any]]:
    """Resolve the candidate entry point (``norm_infer`` /
    ``triton_one_pass_rms_norm``) from src/register.py, or return None if the
    dispatcher has not been implemented yet (so baseline-vs-reference checks
    still run)."""
    module = _load_register_module()
    fn = getattr(module, entry, None)
    if fn is None:
        return None
    return fn


# --------------------------------------------------------------------------- #
# Case construction
# --------------------------------------------------------------------------- #
_DTYPE = {"fp16": "float16", "bf16": "bfloat16", "fp32": "float32"}


def _dtype(name: str):
    return getattr(torch, _DTYPE.get(name, name))


def _tol(dtype) -> tuple[float, float]:
    # Mirrors test_qwen_image_modulation.py
    if dtype == torch.float32:
        return 1e-5, 1e-5
    return 5e-2, 5e-2


def _norm_case(name, group, M, N, dt, *, is_rms_norm, has_weight, has_bias):
    return {
        "name": name,
        "group": group,
        "entry": "norm_infer",
        "dtype": _dtype(dt),
        "M": M,
        "N": N,
        "is_rms_norm": is_rms_norm,
        "has_weight": has_weight,
        "has_bias": has_bias,
        "eps": EPS,
        "warmup": 25,
        "iters": 100,
    }


def _rms_case(name, group, M, D, dt="bf16"):
    return {
        "name": name,
        "group": group,
        "entry": "triton_one_pass_rms_norm",
        "dtype": _dtype(dt),
        "M": M,
        "N": D,
        "is_rms_norm": True,
        "has_weight": True,
        "has_bias": False,
        "eps": EPS,
        "warmup": 25,
        "iters": 100,
    }


def perf_cases() -> list[dict[str, Any]]:
    """The six captured production shapes (the optimization targets)."""
    return [
        _norm_case("helios__f32__M8640N5120", "perf", 8640, 5120, "fp32",
                   is_rms_norm=False, has_weight=True, has_bias=True),
        _rms_case("hunyuan__bf16__M648720D128", "perf", 648720, 128),
        _rms_case("hunyuan__bf16__M1320D128", "perf", 1320, 128),
        _rms_case("hunyuan__bf16__M650040D128", "perf", 650040, 128),
        _rms_case("zimage__bf16__M16384D128", "perf", 16384, 128),
        _rms_case("zimage__bf16__M4096D128", "perf", 4096, 128),
    ]


def regression_cases() -> list[dict[str, Any]]:
    """Canonical regression grid from the SGLang oracle test, plus the RMS
    cross-validation tiles. Full grid under KDA_FULL_CORRECTNESS=1, else a CI
    subset to keep runtime bounded."""
    full = os.environ.get("KDA_FULL_CORRECTNESS") == "1"
    batch = [1, 2, 4] if full else [1, 2]
    seq = [6, 33, 128, 257] if full else [6, 128]
    hidden = [512, 1024, 1536, 3072] if full else [512, 3072]
    dtypes = ["fp16", "bf16", "fp32"] if full else ["fp16", "bf16"]

    cases: list[dict[str, Any]] = []
    for b in batch:
        for s in seq:
            for h in hidden:
                for dt in dtypes:
                    M = b * s
                    cases.append(_norm_case(
                        f"reg_ln__{dt}__B{b}S{s}D{h}", "regression", M, h, dt,
                        is_rms_norm=False, has_weight=True, has_bias=True))
    # RMS cross-validation on the same row counts (D from the grid) ...
    for b in batch:
        for s in seq:
            for h in hidden:
                cases.append(_rms_case(
                    f"reg_rms__bf16__M{b*s}D{h}", "regression", b * s, h))
    # ... and on the per-head tiles from Z-Image.
    cases.append(_rms_case("reg_rms__bf16__M4096D128", "regression", 4096, 128))
    cases.append(_rms_case("reg_rms__bf16__M16384D128", "regression", 16384, 128))
    return cases


def make_cases() -> list[dict[str, Any]]:
    """All cases. benchmark.py uses only the perf group (it filters by group).

    Returns an empty list when torch is unavailable: this function is evaluated at
    pytest COLLECTION time (it feeds ``@pytest.mark.parametrize``), before the
    module-level skip can apply, so it must not dereference ``torch`` (e.g. via
    ``_dtype``) on a lightweight/non-CUDA machine. An empty parametrize set makes the
    parametrized tests collect-and-skip cleanly; benchmark.py only calls this in a
    CUDA env where torch is present.
    """
    if torch is None:
        return []
    return perf_cases() + regression_cases()


# --------------------------------------------------------------------------- #
# Inputs (built once per case, reused for timing)
# --------------------------------------------------------------------------- #
def _inputs(case: dict[str, Any]) -> dict[str, Any]:
    cached = case.get("_inputs")
    if cached is not None:
        return cached
    torch.manual_seed(0)
    dtype = case["dtype"]
    M, N = case["M"], case["N"]
    x = torch.randn(M, N, device=DEVICE, dtype=dtype)
    weight = torch.randn(N, device=DEVICE, dtype=dtype) if case["has_weight"] else None
    bias = torch.randn(N, device=DEVICE, dtype=dtype) if case["has_bias"] else None
    built = {"x": x, "weight": weight, "bias": bias}
    case["_inputs"] = built
    return built


def baseline(case: dict[str, Any]) -> Any:
    inp = _inputs(case)
    if case["entry"] == "norm_infer":
        return _sglang_norm_infer()(
            inp["x"], inp["weight"], inp["bias"], case["eps"],
            is_rms_norm=case["is_rms_norm"],
        )
    return _sglang_rms_norm()(inp["x"], inp["weight"], case["eps"])


def candidate(case: dict[str, Any]) -> Any:
    fn = _candidate_callable(case["entry"])
    if fn is None:
        raise NotImplementedError(f"candidate entry {case['entry']} not available")
    inp = _inputs(case)
    if case["entry"] == "norm_infer":
        return fn(inp["x"], inp["weight"], inp["bias"], case["eps"],
                  is_rms_norm=case["is_rms_norm"])
    return fn(inp["x"], inp["weight"], case["eps"])


def reference_fp32(case: dict[str, Any]) -> Any:
    """Pure-torch FP32 reference; output cast back to the case dtype (mirrors the
    kernel's fp32 accumulation + final cast)."""
    inp = _inputs(case)
    x = inp["x"].float()
    if case["is_rms_norm"]:
        rstd = torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + case["eps"])
        y = x * rstd
    else:
        mean = x.mean(-1, keepdim=True)
        var = (x - mean).pow(2).mean(-1, keepdim=True)
        y = (x - mean) * torch.rsqrt(var + case["eps"])
    if inp["weight"] is not None:
        y = y * inp["weight"].float()
    if inp["bias"] is not None:
        y = y + inp["bias"].float()
    return y.to(inp["x"].dtype)


# --------------------------------------------------------------------------- #
# Assertions
# --------------------------------------------------------------------------- #
def _assert_no_nan_inf(t: Any, *, path: str) -> None:
    assert isinstance(t, torch.Tensor), f"{path}: expected tensor"
    assert not torch.isnan(t).any(), f"{path} contains NaN"
    assert not torch.isinf(t).any(), f"{path} contains Inf"


def _max_abs_diff(a, b) -> float:
    return (a.float() - b.float()).abs().max().item()


def _assert_candidate(case: dict[str, Any]) -> None:
    ref = reference_fp32(case)
    base = baseline(case)
    cand = candidate(case)
    _assert_no_nan_inf(base, path=f"{case['name']}.baseline")
    _assert_no_nan_inf(cand, path=f"{case['name']}.candidate")
    assert cand.shape == base.shape, f"{case['name']} shape {cand.shape} != {base.shape}"
    assert cand.dtype == base.dtype, f"{case['name']} dtype {cand.dtype} != {base.dtype}"

    atol, rtol = _tol(case["dtype"])
    # Fixed SGLang tolerance vs the baseline.
    torch.testing.assert_close(cand.float(), base.float(), atol=atol, rtol=rtol)
    # Dynamic, baseline-relative tolerance vs the FP32 reference: the candidate
    # must not be materially worse than the baseline's own quantization error.
    base_err = _max_abs_diff(base, ref)
    cand_err = _max_abs_diff(cand, ref)
    floor = 1e-6 if case["dtype"] == torch.float32 else 5e-3
    assert cand_err <= 4.0 * base_err + floor, (
        f"{case['name']}: candidate vs fp32 err {cand_err:.3e} exceeds "
        f"4x baseline err {base_err:.3e} (+{floor})"
    )


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #
def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


@pytest.mark.parametrize("case", make_cases(), ids=lambda c: c["name"])
def test_baseline_matches_reference(case) -> None:
    """Validates the harness + FP32 reference against the SGLang baseline.
    Runnable before the candidate exists."""
    if torch is None or not torch.cuda.is_available():
        pytest.skip("CUDA required")
    ref = reference_fp32(case)
    base = baseline(case)
    _assert_no_nan_inf(base, path=f"{case['name']}.baseline")
    atol, rtol = _tol(case["dtype"])
    torch.testing.assert_close(base.float(), ref.float(), atol=atol, rtol=rtol)


@pytest.mark.parametrize("case", make_cases(), ids=lambda c: c["name"])
def test_candidate_matches_baseline(case) -> None:
    if torch is None or not torch.cuda.is_available():
        pytest.skip("CUDA required")
    if _candidate_callable(case["entry"]) is None:
        pytest.skip("candidate dispatcher not implemented yet")
    _assert_candidate(case)


def test_select01_modulation_oracle() -> None:
    """The candidate norm_infer must be correct inside the select01
    dual-modulation fused path, not only in isolation. Mirrors
    test_qwen_image_modulation.py's reference decomposition, swapping the
    isolated norm_infer for the candidate dispatcher."""
    if torch is None or not torch.cuda.is_available():
        pytest.skip("CUDA required")
    cand_norm = _candidate_callable("norm_infer")
    if cand_norm is None:
        pytest.skip("candidate dispatcher not implemented yet")

    base_norm = _sglang_norm_infer()
    torch.cuda.manual_seed(0)
    for dtype in (torch.float16, torch.bfloat16):
        for (b, s, h) in ((1, 6, 512), (2, 128, 3072)):
            x = torch.randn(b, s, h, device=DEVICE, dtype=dtype)
            weight = torch.randn(h, device=DEVICE, dtype=dtype)
            bias = torch.randn(h, device=DEVICE, dtype=dtype)
            scale = torch.randn(b, h, device=DEVICE, dtype=dtype)
            shift = torch.randn(b, h, device=DEVICE, dtype=dtype)

            def modulate(norm_fn):
                normed = norm_fn(
                    x.view(-1, h), weight, bias, EPS, is_rms_norm=False
                ).view_as(x)
                return normed * (1 + scale.unsqueeze(1)) + shift.unsqueeze(1)

            out_base = modulate(base_norm)
            out_cand = modulate(cand_norm)
            _assert_no_nan_inf(out_cand, path=f"oracle.{dtype}.{b}x{s}x{h}")
            atol, rtol = _tol(dtype)
            torch.testing.assert_close(
                out_cand.float(), out_base.float(), atol=atol, rtol=rtol
            )


def test_rms_noncontiguous_higher_rank_falls_back() -> None:
    """A higher-rank tensor whose last dim is 128 and last-dim-contiguous but whose
    overall layout is NOT contiguous must route to the SGLang baseline (reshape would
    otherwise copy and the kernel would write a discarded buffer). The optimized path
    is restricted to fully contiguous inputs; the result must match the baseline."""
    if torch is None or not torch.cuda.is_available():
        pytest.skip("CUDA required")
    cand = _candidate_callable("triton_one_pass_rms_norm")
    if cand is None:
        pytest.skip("candidate dispatcher not implemented yet")

    base = torch.randn(64, 4, 128, device=DEVICE, dtype=torch.bfloat16)
    x = base.permute(1, 0, 2)  # [4,64,128]: stride(-1)==1 but NOT contiguous overall
    assert x.stride(-1) == 1 and not x.is_contiguous()
    w = torch.randn(128, device=DEVICE, dtype=torch.bfloat16)

    out_cand = cand(x, w, EPS)
    out_base = _sglang_rms_norm()(x, w, EPS)
    _assert_no_nan_inf(out_cand, path="rms_noncontig")
    assert out_cand.shape == out_base.shape
    torch.testing.assert_close(out_cand.float(), out_base.float(), atol=5e-2, rtol=5e-2)


def test_optimized_wrapper_call_forms() -> None:
    """The generic register()['callable'] must preserve every recovered callsite
    form: triton_one_pass_rms_norm(x, w) with default eps (2 positional), (x, w, eps),
    keyword w=, and norm_infer's positional/keyword forms."""
    if torch is None or not torch.cuda.is_available():
        pytest.skip("CUDA required")
    mod = _load_register_module()
    ow = getattr(mod, "optimized_wrapper", None)
    rms = getattr(mod, "triton_one_pass_rms_norm", None)
    ninf = getattr(mod, "norm_infer", None)
    if ow is None or rms is None or ninf is None:
        pytest.skip("dispatcher not implemented yet")

    x = torch.randn(64, 128, device=DEVICE, dtype=torch.bfloat16)
    w = torch.randn(128, device=DEVICE, dtype=torch.bfloat16)
    # 2-positional RMS (default eps) -- the form the Round 1 wrapper wrongly rejected.
    torch.testing.assert_close(ow(x, w).float(), rms(x, w).float(), atol=1e-3, rtol=1e-3)
    torch.testing.assert_close(ow(x, w, EPS).float(), rms(x, w, EPS).float(), atol=1e-3, rtol=1e-3)
    torch.testing.assert_close(ow(x, w=w).float(), rms(x, w=w).float(), atol=1e-3, rtol=1e-3)

    xl = torch.randn(8, 512, device=DEVICE, dtype=torch.float32)
    wl = torch.randn(512, device=DEVICE, dtype=torch.float32)
    bl = torch.randn(512, device=DEVICE, dtype=torch.float32)
    # norm_infer routes: keyword form, 4-positional, and 3-positional + keyword eps
    # (x, weight, bias, eps=...) -- the last form must NOT be misrouted to RMS. (N=512 -> baseline.)
    torch.testing.assert_close(
        ow(xl, weight=wl, bias=bl, eps=EPS).float(),
        ninf(xl, wl, bl, EPS).float(), atol=1e-5, rtol=1e-5)
    torch.testing.assert_close(
        ow(xl, wl, bl, EPS).float(),
        ninf(xl, wl, bl, EPS).float(), atol=1e-5, rtol=1e-5)
    torch.testing.assert_close(
        ow(xl, wl, bl, eps=EPS).float(),
        ninf(xl, wl, bl, EPS).float(), atol=1e-5, rtol=1e-5)


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main([__file__, "-v", "-s"]))
