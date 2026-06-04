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


_MAX_GRID_ROWS = 2**31 - 1  # CUDA grid.x limit; also guards the uint32 cast


def _aligned16(t: torch.Tensor) -> bool:
    # The kernel issues 128-bit vector loads/stores from the row base; fresh
    # torch allocations are 256B-aligned but offset VIEWS can be contiguous
    # yet misaligned — fall back for those (the vendored baseline rejects
    # them too via CuTe assumed_align=32, so fallback preserves its error).
    return t.data_ptr() % 16 == 0


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
    if B * S > _MAX_GRID_ROWS:
        return False
    if not (_aligned16(x) and _aligned16(weight) and _aligned16(scale) and _aligned16(shift)):
        return False
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
        and shift.dim() == 3
        and shift.shape[0] == B
        and shift.shape[1] == S
        and shift.shape[2] == D
        and shift.stride(-1) == 1
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


def _fast_dual_extras_ok(x: torch.Tensor, weight2, bias2, scale2) -> bool:
    D = x.shape[-1]
    return (
        bias2 is None
        and weight2 is not None
        and isinstance(weight2, torch.Tensor)
        and weight2.is_cuda
        and weight2.dtype is _FAST_DTYPE
        and weight2.shape == (D,)
        and weight2.stride(-1) == 1
        and isinstance(scale2, torch.Tensor)
        and scale2.is_cuda
        and scale2.dtype is _FAST_DTYPE
        and scale2.dim() == 3
        and scale2.shape == (1, 1, D)
        and scale2.stride(-1) == 1
        and _aligned16(weight2)
        and _aligned16(scale2)
    )


def _normalize_call(args: tuple, kwargs: dict) -> tuple[tuple, dict]:
    """Mirror the baseline's ``eps: float = 1e-5`` default for positional
    calls: a 6-arg single call or 9-arg dual call is valid public usage and
    gets the default appended. Keyword-style calls are left untouched (the
    baseline custom op binds its own defaults)."""

    if not kwargs and len(args) in (6, 9):
        return args + (1e-5,), kwargs
    return args, kwargs


def dispatch_decision(*args: Any, **kwargs: Any) -> str:
    """Single source of truth for routing. Returns one of ``fast_single``,
    ``fast_dual``, ``fallback_single``, ``fallback_dual`` — the exact branch
    ``optimized_wrapper`` will take for the same call."""

    args, kwargs = _normalize_call(args, kwargs)
    if kwargs or len(args) not in (7, 10):
        # Keyword-style or unrecognized arity: route to the baseline, which
        # binds defaults or raises its own TypeError (contract-faithful).
        is_dual = (
            any(k in kwargs for k in ("weight2", "bias2", "scale2"))
            or len(args) + len(kwargs) > 7
        )
        return "fallback_dual" if is_dual else "fallback_single"
    if len(args) == 7:
        x, weight, bias, scale, shift, norm_type, _eps = args
        if isinstance(x, torch.Tensor) and _fast_path_ok(x, weight, bias, scale, shift, norm_type):
            return "fast_single"
        return "fallback_single"
    x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, _eps = args
    if (
        isinstance(x, torch.Tensor)
        and _fast_path_ok(x, weight, bias, scale, shift, norm_type)
        and _fast_dual_extras_ok(x, weight2, bias2, scale2)
    ):
        return "fast_dual"
    return "fallback_dual"


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Public dispatch preserving the SGLang callsite contract.

    Accepts the baseline arities (6/7 positional for the single op, 9/10 for
    the dual op — ``eps`` defaults to 1e-5) and keyword-style calls. Routing
    is decided by :func:`dispatch_decision`; unsupported signatures fall back
    to the vendored pinned baseline (including its error behavior)."""

    args, kwargs = _normalize_call(args, kwargs)
    decision = dispatch_decision(*args, **kwargs)
    if decision == "fast_single":
        x, weight, _bias, scale, shift, _norm_type, eps = args
        return _fast_single(x, weight, scale, shift, float(eps))
    if decision == "fast_dual":
        x, weight, _bias, scale, shift, weight2, _bias2, scale2, _norm_type, eps = args
        return _fast_dual(x, weight, scale, shift, weight2, scale2, float(eps))
    if decision == "fallback_single":
        return _vendored_baseline.fused_norm_tanh_mul_add(*args, **kwargs)
    return _vendored_baseline.fused_norm_tanh_mul_add_norm_scale(*args, **kwargs)


EXPORTS = {
    "fused_norm_tanh_mul_add": optimized_wrapper,
    "fused_norm_tanh_mul_add_norm_scale": optimized_wrapper,
}
