"""JIT driver for the native fused norm-tanh-modulation CUDA kernel.

Builds ``norm_tanh_mul_add.cuh`` through SGLang's jit_kernel / tvm-ffi stack
(``load_jit`` + ``make_cpp_args`` + ``cache_once``) with SGLang's default nvcc
flags (no ``--use_fast_math``). The installed ``sglang`` package is used purely
as a build utility — nothing in SGLang is imported-for-patching or modified.

Public functions mirror the baseline signatures exactly. Unused kernel ABI
slots (weight/bias under effective-plain affine, second-norm tensors for the
single-norm entry point) receive ``x`` as an inert placeholder: the template
instantiation neither verifies nor dereferences them.

Effective affine semantics (mirroring the baseline kernels):
- rms: affine iff ``weight is not None`` (bias is ignored);
- layer: affine iff BOTH ``weight`` and ``bias`` are tensors (one-sided
  affine degrades to plain normalization, with the provided tensor ignored).
For the second-norm entry point the dispatcher only routes here when the
effective affine pattern of (weight2, bias2) matches (weight, bias).

Env knobs:
- ``KDA_ROWS_PER_CTA`` (default 8): rows processed per CTA.
- ``KDA_ENABLE_PDL=1``: opt-in programmatic dependent launch (default off).
- ``KDA_NVCC_LINEINFO=1``: adds ``-lineinfo`` for profiling builds (separate
  module cache key; never used for benchmark/promotion builds).
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Optional, Tuple

import torch

from sglang.jit_kernel.utils import cache_once, load_jit, make_cpp_args

_CUH_PATH = str((Path(__file__).resolve().parent / "norm_tanh_mul_add.cuh"))


def _rows_per_cta() -> int:
    return max(1, int(os.environ.get("KDA_ROWS_PER_CTA", "8")))


def _use_pdl() -> bool:
    return os.environ.get("KDA_ENABLE_PDL") == "1"


def _lineinfo() -> bool:
    return os.environ.get("KDA_NVCC_LINEINFO") == "1"


@cache_once
def _jit_module(
    D: int,
    rows_per_cta: int,
    is_rms: bool,
    has_affine: bool,
    second_norm: bool,
    use_pdl: bool,
    dtype: torch.dtype,
    lineinfo: bool,
):
    args = make_cpp_args(D, rows_per_cta, is_rms, has_affine, second_norm, use_pdl, dtype)
    return load_jit(
        "kda_norm_tanh_modulation",
        "li1" if lineinfo else "li0",
        *args,
        cuda_files=[_CUH_PATH],
        cuda_wrappers=[("run", f"FusedNormTanhModulationKernel<{args}>::run")],
        extra_cuda_cflags=(["-lineinfo"] if lineinfo else []),
    )


def _effective_affine(weight: Optional[torch.Tensor], bias: Optional[torch.Tensor], norm_type: str) -> bool:
    if norm_type == "rms":
        return weight is not None
    return weight is not None and bias is not None


def fused_norm_tanh_mul_add(
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
    D = x.shape[-1]
    y = torch.empty_like(x)
    module = _jit_module(
        int(D), _rows_per_cta(), is_rms, has_affine, False, _use_pdl(), x.dtype, _lineinfo()
    )
    w = weight if has_affine else x
    b = bias if (has_affine and not is_rms) else x
    module.run(y, y, x, w, b, scale, shift, x, x, x, float(eps))
    return y


def fused_norm_tanh_mul_add_norm_scale(
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
    if _effective_affine(weight2, bias2, norm_type) != has_affine:
        raise RuntimeError(
            "native kernel requires matching effective affine patterns for both norms; "
            "the dispatcher should have routed this call to the baseline"
        )
    D = x.shape[-1]
    y = torch.empty_like(x)
    y2 = torch.empty_like(x)
    module = _jit_module(
        int(D), _rows_per_cta(), is_rms, has_affine, True, _use_pdl(), x.dtype, _lineinfo()
    )
    w = weight if has_affine else x
    b = bias if (has_affine and not is_rms) else x
    w2 = weight2 if has_affine else x
    b2 = bias2 if (has_affine and not is_rms) else x
    module.run(y, y2, x, w, b, scale, shift, w2, b2, scale2, float(eps))
    return y, y2
