"""Registration + dispatcher for the b200_diffusion_norm_infer__multi_shape task.

Two wrapped SGLang entry points are optimized behind one router:
- ``norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)``  (LayerNorm/RMSNorm)
- ``triton_one_pass_rms_norm(x, w, eps=1e-6)``                       (tiled one-pass RMSNorm)

``optimized_wrapper`` routes by ``dispatcher_hint`` (or infers from the call
shape) to the matching optimized path, and falls back to the SGLang baseline
for any shape/dtype/layout/device/norm-type/flag it does not support.

Native-CUDA kernels live in ``norm_cuda/diffusion_norm_infer.cuh`` and are built
through the SGLang jit_kernel / tvm-ffi stack (``load_jit``). Build/run happen on
the GPU host; this module stays importable without torch/sglang (lazy imports).

Validation note: set ``KDA_REQUIRE_CUDA=1`` to make the CUDA path raise on any
failure instead of silently falling back (so a broken build can't masquerade as a
passing test by falling back to the baseline). Unset, the dispatcher falls back.
Code here carries no plan/workflow terminology.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Optional


KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"

_CUDA_ENABLED = True
_HERE = Path(__file__).resolve().parent
_CUH = str(_HERE / "norm_cuda" / "diffusion_norm_infer.cuh")
_INCLUDE = str(_HERE / "norm_cuda")
_KERNEL_VERSION = "v0"  # bump to force a JIT rebuild (stale-JIT guard)
_LN_MAX_N = 8192  # LayerNorm CUDA kernel covers at most kLNThreads*kLNMaxElems cols

_MODULE_CACHE: dict = {}


def _require_cuda() -> bool:
    return os.environ.get("KDA_REQUIRE_CUDA") == "1"


# --- SGLang baselines (lazy import; the source of truth for fallback) --------
def _baseline_norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None):
    from sglang.jit_kernel.diffusion.triton.norm import norm_infer

    return norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)


def _baseline_rms_onepass(x, w, eps=1e-6):
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
        triton_one_pass_rms_norm,
    )

    return triton_one_pass_rms_norm(x, w, eps)


# --- JIT module builders (cached per dtype/dim) ------------------------------
def _ln_module(dtype):
    key = ("ln", str(dtype))
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        from sglang.jit_kernel.utils import load_jit, make_cpp_args

        args = make_cpp_args(dtype)
        mod = load_jit(
            "b200_diffnorm_ln",
            _KERNEL_VERSION,
            *args,
            cuda_files=[_CUH],
            cuda_wrappers=[("norm_infer_ln", f"LayerNormInferKernel<{args}>::run")],
            extra_include_paths=[_INCLUDE],
        )
        _MODULE_CACHE[key] = mod
    return mod


def _rms_module(dim, dtype):
    key = ("rms", int(dim), str(dtype))
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        from sglang.jit_kernel.utils import load_jit, make_cpp_args

        args = make_cpp_args(int(dim), dtype)
        mod = load_jit(
            "b200_diffnorm_rms",
            _KERNEL_VERSION,
            *args,
            cuda_files=[_CUH],
            cuda_wrappers=[("rms_onepass", f"RmsNormOnepassKernel<{args}>::run")],
            extra_include_paths=[_INCLUDE],
        )
        _MODULE_CACHE[key] = mod
    return mod


# --- Support predicates (only these route to CUDA; everything else falls back) ---
# Supported class (covers the six production shapes AND the correctness-regression
# coverage; anything outside falls back to the SGLang baseline):
#   norm_infer -> CUDA iff: fp32, 2-D, contiguous, is_rms_norm=False, weight+bias
#                 present & contiguous, and N <= _LN_MAX_N (kernel column coverage).
#   rms_onepass -> CUDA iff: bf16, contiguous, last dim D == 128, weight present.
# Unsupported (fp16/bf16 LN, is_rms_norm=True, non-contiguous, non-CUDA, missing
# weight/bias, N > 8192, D != 128, fp32 RMS, ...) all route to the baseline.
# Verified by tests/test_correctness.py::test_fallback_routing.
def _is_cuda_contig_2d(t) -> bool:
    return t is not None and getattr(t, "is_cuda", False) and t.dim() == 2 and t.is_contiguous()


def _norm_infer_supported(x, weight, bias, is_rms_norm) -> bool:
    import torch

    # fp32 LayerNorm with weight+bias, N within the kernel's coverage (helios).
    return (
        _is_cuda_contig_2d(x)
        and x.dtype == torch.float32
        and not is_rms_norm
        and x.shape[1] <= _LN_MAX_N
        and weight is not None
        and bias is not None
        and weight.is_contiguous()
        and bias.is_contiguous()
    )


def _rms_onepass_supported(x, w) -> bool:
    import torch

    # bf16, last-dim D == 128 (the hunyuanvideo/zimage production family).
    if not (x is not None and getattr(x, "is_cuda", False) and x.is_contiguous()):
        return False
    return x.dtype == torch.bfloat16 and x.shape[-1] == 128 and w is not None and w.is_contiguous()


# --- CUDA paths --------------------------------------------------------------
def _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None):
    import torch

    if out is None:
        out = torch.empty_like(x)
    _ln_module(x.dtype).norm_infer_ln(x, weight, bias, out, eps)
    return out


def _cuda_rms_onepass(x, w, eps=1e-6):
    import torch

    shape = x.shape
    x2d = x.reshape(-1, shape[-1])
    out = torch.empty_like(x)
    out2d = out.reshape(-1, shape[-1])
    _rms_module(shape[-1], x.dtype).rms_onepass(x2d, w, out2d, eps)
    return out


# --- Public optimized entry points (preserve the SGLang signatures) ----------
def optimized_norm_infer(x, weight, bias, eps, is_rms_norm: bool = False, out=None):
    if _CUDA_ENABLED and _norm_infer_supported(x, weight, bias, is_rms_norm):
        if _require_cuda():
            return _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)
        try:
            return _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)
        except Exception:
            pass  # safe baseline fallback
    return _baseline_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)


def optimized_triton_one_pass_rms_norm(x, w, eps: float = 1e-6):
    if _CUDA_ENABLED and _rms_onepass_supported(x, w):
        if _require_cuda():
            return _cuda_rms_onepass(x, w, eps)
        try:
            return _cuda_rms_onepass(x, w, eps)
        except Exception:
            pass
    return _baseline_rms_onepass(x, w, eps)


def _infer_hint(args: tuple, kwargs: dict) -> str:
    """Infer which entry point a bare call targets when no hint is given."""
    if "is_rms_norm" in kwargs or "bias" in kwargs or len(args) >= 4:
        return "norm_infer"
    if len(args) >= 2 and hasattr(args[1], "dim") and args[1].dim() == 1:
        return "rms_onepass"
    return "norm_infer"


def optimized_wrapper(*args: Any, dispatcher_hint: Optional[str] = None, **kwargs: Any) -> Any:
    hint = dispatcher_hint or _infer_hint(args, kwargs)
    if hint == "rms_onepass":
        return optimized_triton_one_pass_rms_norm(*args, **kwargs)
    if hint == "norm_infer":
        return optimized_norm_infer(*args, **kwargs)
    raise ValueError(f"unknown dispatcher_hint {hint!r}")


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }
