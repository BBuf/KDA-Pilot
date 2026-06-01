"""Registration + dispatcher for the b200_diffusion_norm_infer__multi_shape task.

Two wrapped SGLang entry points are optimized behind one router:
- ``norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)``  (LayerNorm/RMSNorm)
- ``triton_one_pass_rms_norm(x, w, eps=1e-6)``                       (tiled one-pass RMSNorm)

``optimized_wrapper`` routes by ``dispatcher_hint`` (or infers from the call
shape) to the matching optimized path, and falls back to the SGLang baseline
for any shape/dtype/layout/device/norm-type/flag it does not support.

NOTE (round 0): the native-CUDA kernels are not wired yet (``_CUDA_ENABLED`` is
False), so every call falls back to the SGLang baseline. The support predicates
and routing below are the stable contract; round 1 flips ``_CUDA_ENABLED`` and
points ``_cuda_norm_infer`` / ``_cuda_rms_onepass`` at the jit_kernel build. Code
here intentionally carries no plan/workflow terminology.
"""

from __future__ import annotations

from typing import Any, Optional


KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"

# Flip to True once the jit_kernel .cuh build is wired and validated on B200.
_CUDA_ENABLED = False


# --- SGLang baselines (lazy import; the source of truth for fallback) --------
def _baseline_norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None):
    from sglang.jit_kernel.diffusion.triton.norm import norm_infer

    return norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)


def _baseline_rms_onepass(x, w, eps=1e-6):
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
        triton_one_pass_rms_norm,
    )

    return triton_one_pass_rms_norm(x, w, eps)


# --- Support predicates (when CUDA is wired, only these route to CUDA) --------
def _is_cuda_contig_2d(t) -> bool:
    return (
        t is not None
        and getattr(t, "is_cuda", False)
        and t.dim() == 2
        and t.is_contiguous()
    )


def _norm_infer_supported(x, weight, bias, is_rms_norm) -> bool:
    import torch

    # fp32 LayerNorm with weight+bias (the helios production family).
    return (
        _is_cuda_contig_2d(x)
        and x.dtype == torch.float32
        and not is_rms_norm
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
    return x.dtype == torch.bfloat16 and x.shape[-1] == 128 and w is not None


# --- CUDA paths (round 1 wires these to the jit_kernel build) ----------------
def _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None):
    raise NotImplementedError("CUDA norm_infer not wired yet (round 1).")


def _cuda_rms_onepass(x, w, eps=1e-6):
    raise NotImplementedError("CUDA rms one-pass not wired yet (round 1).")


# --- Public optimized entry points (preserve the SGLang signatures) ----------
def optimized_norm_infer(x, weight, bias, eps, is_rms_norm: bool = False, out=None):
    if _CUDA_ENABLED:
        try:
            if _norm_infer_supported(x, weight, bias, is_rms_norm):
                return _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)
        except Exception:
            pass  # any failure -> safe baseline fallback
    return _baseline_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)


def optimized_triton_one_pass_rms_norm(x, w, eps: float = 1e-6):
    if _CUDA_ENABLED:
        try:
            if _rms_onepass_supported(x, w):
                return _cuda_rms_onepass(x, w, eps)
        except Exception:
            pass
    return _baseline_rms_onepass(x, w, eps)


def _infer_hint(args: tuple, kwargs: dict) -> str:
    """Infer which entry point a bare call targets when no hint is given."""
    if "is_rms_norm" in kwargs or "bias" in kwargs or len(args) >= 4:
        return "norm_infer"
    # rms_onepass: (x, w, eps?) with a 1-D weight
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
