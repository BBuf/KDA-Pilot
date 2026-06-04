"""Native CUDA fast path for the fused norm-tanh-modulation diffusion kernels.

Destined for ``python/sglang/jit_kernel/diffusion/norm_tanh_modulation.py``.
The public entry points stay the ``torch.library.custom_op``s defined in
``diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py``; their bodies call
``native_supported(...)`` and route eligible signatures here, falling through
to the original CuTe-DSL implementation otherwise. Device code lives in
``csrc/diffusion/norm_tanh_modulation.cuh`` (built with jit_kernel default
flags; no fast-math; exact fp32 tanhf; PDL off by default).

Eligibility mirrors the kernel's verified contract: uniform dtype in
{bf16, fp16, fp32}, contiguous x, 3-D [1|B, 1|S, D] modulation tensors with
unit D-stride and 8-element-aligned non-broadcast strides, weight-likes None
or contiguous [D], D % 256 == 0 and D <= 8192, 8-element-aligned base
pointers, and (for the second entry point) matching effective affine patterns
for both norms (rms: weight-only; layer: weight AND bias).
"""

from __future__ import annotations

import os
from typing import Optional, Tuple

import torch

from sglang.jit_kernel.utils import cache_once, load_jit, make_cpp_args

_SUPPORTED_DTYPES = (torch.float16, torch.bfloat16, torch.float32)
_VECTOR_ELEMS = 8

# Per-entry-point routing switches (set from the drop-in A/B evidence; the
# second entry point only ships natively if the integrated benchmark shows
# parity-or-better).
NATIVE_V1_ENABLED = os.environ.get("SGLANG_NATIVE_NORM_TANH_V1", "1") == "1"
NATIVE_V2_ENABLED = os.environ.get("SGLANG_NATIVE_NORM_TANH_V2", "1") == "1"


def _rows_per_cta() -> int:
    return max(1, int(os.environ.get("SGLANG_NORM_TANH_ROWS_PER_CTA", "8")))


@cache_once
def _jit_module(
    D: int,
    rows_per_cta: int,
    is_rms: bool,
    has_affine: bool,
    second_norm: bool,
    use_pdl: bool,
    dtype: torch.dtype,
):
    args = make_cpp_args(D, rows_per_cta, is_rms, has_affine, second_norm, use_pdl, dtype)
    return load_jit(
        "norm_tanh_modulation",
        *args,
        cuda_files=["diffusion/norm_tanh_modulation.cuh"],
        cuda_wrappers=[("run", f"FusedNormTanhModulationKernel<{args}>::run")],
    )


def _effective_affine(weight, bias, norm_type: str) -> bool:
    if norm_type == "rms":
        return weight is not None
    return weight is not None and bias is not None


def _modulation_ok(t, x) -> bool:
    if not isinstance(t, torch.Tensor) or t.ndim != 3:
        return False
    B, S, D = x.shape
    if t.shape[0] not in (1, B) or t.shape[1] not in (1, S) or t.shape[2] != D:
        return False
    if t.stride(-1) != 1 or t.dtype != x.dtype or not t.is_cuda or t.device != x.device:
        return False
    for dim in (0, 1):
        if t.shape[dim] != 1 and t.stride(dim) % _VECTOR_ELEMS != 0:
            return False
    return t.data_ptr() % (_VECTOR_ELEMS * t.element_size()) == 0


def _weight_ok(t, x) -> bool:
    if t is None:
        return True
    D = x.shape[-1]
    return (
        isinstance(t, torch.Tensor)
        and t.ndim == 1
        and t.shape == (D,)
        and t.stride(-1) == 1
        and t.dtype == x.dtype
        and t.is_cuda
        and t.device == x.device
        and t.data_ptr() % (_VECTOR_ELEMS * t.element_size()) == 0
    )


def native_supported(
    x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type: str
) -> bool:
    """True when the native kernel can take this call (second-norm tensors are
    None for the single-norm entry point)."""

    second = scale2 is not None
    if second and not NATIVE_V2_ENABLED:
        return False
    if not second and not NATIVE_V1_ENABLED:
        return False
    if not isinstance(x, torch.Tensor) or not x.is_cuda or x.ndim != 3:
        return False
    if x.dtype not in _SUPPORTED_DTYPES or norm_type not in ("layer", "rms"):
        return False
    D = x.shape[-1]
    if D % 256 != 0 or D > 8192 or not x.is_contiguous():
        return False
    if x.data_ptr() % (_VECTOR_ELEMS * x.element_size()) != 0:
        return False
    if not (_modulation_ok(scale, x) and _modulation_ok(shift, x)):
        return False
    if not (_weight_ok(weight, x) and _weight_ok(bias, x)):
        return False
    if second:
        if not _modulation_ok(scale2, x):
            return False
        if not (_weight_ok(weight2, x) and _weight_ok(bias2, x)):
            return False
        if _effective_affine(weight2, bias2, norm_type) != _effective_affine(
            weight, bias, norm_type
        ):
            return False
    return True


def native_fused_norm_tanh_mul_add(
    x: torch.Tensor,
    weight: Optional[torch.Tensor],
    bias: Optional[torch.Tensor],
    scale: torch.Tensor,
    shift: torch.Tensor,
    norm_type: str,
    eps: float = 1e-5,
) -> torch.Tensor:
    is_rms = norm_type == "rms"
    has_affine = _effective_affine(weight, bias, norm_type)
    y = torch.empty_like(x)
    module = _jit_module(
        int(x.shape[-1]), _rows_per_cta(), is_rms, has_affine, False, False, x.dtype
    )
    w = weight if has_affine else x
    b = bias if (has_affine and not is_rms) else x
    module.run(y, y, x, w, b, scale, shift, x, x, x, float(eps))
    return y


def native_fused_norm_tanh_mul_add_norm_scale(
    x: torch.Tensor,
    weight: Optional[torch.Tensor],
    bias: Optional[torch.Tensor],
    scale: torch.Tensor,
    shift: torch.Tensor,
    weight2: Optional[torch.Tensor],
    bias2: Optional[torch.Tensor],
    scale2: torch.Tensor,
    norm_type: str,
    eps: float = 1e-5,
) -> Tuple[torch.Tensor, torch.Tensor]:
    is_rms = norm_type == "rms"
    has_affine = _effective_affine(weight, bias, norm_type)
    y = torch.empty_like(x)
    y2 = torch.empty_like(x)
    module = _jit_module(
        int(x.shape[-1]), _rows_per_cta(), is_rms, has_affine, True, False, x.dtype
    )
    w = weight if has_affine else x
    b = bias if (has_affine and not is_rms) else x
    w2 = weight2 if has_affine else x
    b2 = bias2 if (has_affine and not is_rms) else x
    module.run(y, y2, x, w, b, scale, shift, w2, b2, scale2, float(eps))
    return y, y2
