"""Candidate wrapper: native CUDA fast path + vendored-baseline fallback.

Fast path (the 4 captured production signatures, and any row count with the
same per-row layout): CUDA bf16 rms with weight=[D], bias=None,
scale(/scale2)=[1,1,D], shift=[B,S,D], D=3840, unit stride on D. Everything
else falls back to the vendored pinned baseline.

Host-layer parity: the fast path is wrapped in ``torch.library.custom_op``
(+ fake registration) mirroring the baseline's wrapper machinery, so local
A/B compares like-for-like host layers. The compiled module loads through
SGLang's own ``load_jit`` (read-only import of the unmodified package; the
candidate ``.cuh`` source lives in this task folder and is passed by absolute
path), with default jit_kernel flags — no ``--use_fast_math``.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Optional, Tuple

import torch

_SRC_DIR = Path(__file__).resolve().parent
_KERNEL_DIR = _SRC_DIR.parents[0]
_CANDIDATE_CUH = _SRC_DIR / "norm_tanh_mul_add_candidate.cuh"

if str(_KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(_KERNEL_DIR))

import baseline as _vendored_baseline  # noqa: E402  (vendored pinned baseline)

PROD_D = 3840
_FAST_DTYPE = torch.bfloat16


_JIT_MODULE = None


def _jit_module():
    """Compile/load the candidate through SGLang's jit_kernel stack.

    Cached at MODULE level: a per-call cache (e.g. decorating a closure with
    ``cache_once`` inside this function) would re-enter ``load_inline``'s
    build check on every kernel call (~6 ms no-op ninja probe — observed as a
    0.015x "slowdown" in the first A/B run before this fix)."""

    global _JIT_MODULE
    if _JIT_MODULE is None:
        from sglang.jit_kernel.utils import load_jit

        _JIT_MODULE = load_jit(
            "kda_h200_norm_tanh_mul_add_candidate",
            cuda_files=[str(_CANDIDATE_CUH)],
            cuda_wrappers=[
                ("norm_tanh_mul_add_fast", "NormTanhMulAddSingleKernel<bf16_t>::run"),
                ("norm_tanh_mul_add_norm_scale_fast", "NormTanhMulAddDualKernel<bf16_t>::run"),
            ],
        )
    return _JIT_MODULE


def _is_fast_3d(t: torch.Tensor, B: int, S: int, D: int) -> bool:
    return (
        t.dim() == 3
        and t.shape[0] in (1, B)
        and t.shape[1] in (1, S)
        and t.shape[2] == D
        and t.stride(-1) == 1
    )


def _fast_path_ok(
    x: torch.Tensor,
    weight: Optional[torch.Tensor],
    bias: Optional[torch.Tensor],
    scale: torch.Tensor,
    shift: torch.Tensor,
    norm_type: str,
) -> bool:
    if norm_type != "rms" or bias is not None or weight is None:
        return False
    if not (isinstance(x, torch.Tensor) and x.is_cuda and x.dtype is _FAST_DTYPE):
        return False
    if x.dim() != 3 or x.shape[-1] != PROD_D or not x.is_contiguous():
        return False
    B, S, D = x.shape
    if not (
        weight.is_cuda
        and weight.dtype is _FAST_DTYPE
        and weight.shape == (D,)
        and weight.stride(-1) == 1
    ):
        return False
    # Production scale layout: row-invariant [1, 1, D].
    if not (
        scale.is_cuda
        and scale.dtype is _FAST_DTYPE
        and scale.dim() == 3
        and scale.shape == (1, 1, D)
        and scale.stride(-1) == 1
    ):
        return False
    # Production shift layout: a full per-row tensor [B, S, D].
    if not (
        shift.is_cuda
        and shift.dtype is _FAST_DTYPE
        and _is_fast_3d(shift, B, S, D)
        and shift.shape[0] == B
        and shift.shape[1] == S
        and shift.is_contiguous()
    ):
        return False
    return True


@torch.library.custom_op("kda_candidate::fused_norm_tanh_mul_add", mutates_args=())
def _fast_single(
    x: torch.Tensor,
    weight: torch.Tensor,
    scale: torch.Tensor,
    shift: torch.Tensor,
    eps: float,
) -> torch.Tensor:
    y = torch.empty_like(x)
    D = x.shape[-1]
    mod = _jit_module()
    mod.norm_tanh_mul_add_fast(
        x.view(-1, D),
        weight,
        scale.view(D),
        shift.view(-1, D),
        y.view(-1, D),
        float(eps),
    )
    return y


@_fast_single.register_fake
def _fast_single_fake(x, weight, scale, shift, eps):
    return x.new_empty(x.shape)


@torch.library.custom_op("kda_candidate::fused_norm_tanh_mul_add_norm_scale", mutates_args=())
def _fast_dual(
    x: torch.Tensor,
    weight: torch.Tensor,
    scale: torch.Tensor,
    shift: torch.Tensor,
    weight2: torch.Tensor,
    scale2: torch.Tensor,
    eps: float,
) -> Tuple[torch.Tensor, torch.Tensor]:
    y = torch.empty_like(x)
    y2 = torch.empty_like(x)
    D = x.shape[-1]
    mod = _jit_module()
    mod.norm_tanh_mul_add_norm_scale_fast(
        x.view(-1, D),
        weight,
        scale.view(D),
        shift.view(-1, D),
        weight2,
        scale2.view(D),
        y.view(-1, D),
        y2.view(-1, D),
        float(eps),
    )
    return y, y2


@_fast_dual.register_fake
def _fast_dual_fake(x, weight, scale, shift, weight2, scale2, eps):
    return x.new_empty(x.shape), x.new_empty(x.shape)


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Public dispatch preserving the SGLang callsite contract.

    7 positional args -> ``fused_norm_tanh_mul_add``; 10 -> the dual variant
    (same as the public SGLang signatures). Unsupported signatures fall back
    to the vendored pinned baseline.
    """

    if kwargs:
        # The public ops are positional in production; route any kwarg use to
        # the baseline untouched.
        if len(args) + len(kwargs) <= 7:
            return _vendored_baseline.fused_norm_tanh_mul_add(*args, **kwargs)
        return _vendored_baseline.fused_norm_tanh_mul_add_norm_scale(*args, **kwargs)

    if len(args) == 7:
        x, weight, bias, scale, shift, norm_type, eps = args
        if _fast_path_ok(x, weight, bias, scale, shift, norm_type):
            return _fast_single(x, weight, scale, shift, float(eps))
        return _vendored_baseline.fused_norm_tanh_mul_add(*args)

    if len(args) == 10:
        x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps = args
        if (
            _fast_path_ok(x, weight, bias, scale, shift, norm_type)
            and bias2 is None
            and weight2 is not None
            and weight2.is_cuda
            and weight2.dtype is _FAST_DTYPE
            and weight2.shape == (x.shape[-1],)
            and weight2.stride(-1) == 1
            and scale2.is_cuda
            and scale2.dtype is _FAST_DTYPE
            and scale2.dim() == 3
            and scale2.shape == (1, 1, x.shape[-1])
            and scale2.stride(-1) == 1
        ):
            return _fast_dual(x, weight, scale, shift, weight2, scale2, float(eps))
        return _vendored_baseline.fused_norm_tanh_mul_add_norm_scale(*args)

    raise TypeError(
        f"optimized_wrapper expects 7 (single) or 10 (dual) positional args, got {len(args)}"
    )


EXPORTS = {
    "fused_norm_tanh_mul_add": optimized_wrapper,
    "fused_norm_tanh_mul_add_norm_scale": optimized_wrapper,
}
