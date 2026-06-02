"""Zero-overhead dispatcher for the fused GroupNorm+SiLU diffusion kernel.

Preserves the two public SGLang callable names (``triton_group_norm_silu`` and
``apply_group_norm_silu``) and routes only the supported, fixed production buckets
to the native-CUDA specialization (built through SGLang's jit_kernel / tvm-ffi
stack), falling back to the captured SGLang baseline for every other signature.

The SGLang baselines are bound ONCE at import time (``_baseline_triton`` /
``_baseline_apply``). This is what makes the public-name swap performed by
``kda_kernels.install()`` non-recursive: after install() rebinds the module
attributes, this dispatcher still calls the originals it captured before the swap.
"""

from __future__ import annotations

import os
import pathlib
from typing import Any

import torch
from torch import nn

from sglang.jit_kernel.utils import cache_once, load_jit, make_cpp_args

# SGLang baselines, captured at import (pre-swap) -> non-recursive fallback.
from sglang.jit_kernel.diffusion.triton.group_norm_silu import (
    triton_group_norm_silu as _baseline_triton,
)
from sglang.jit_kernel.diffusion.group_norm_silu import (
    apply_group_norm_silu as _baseline_apply,
)

_SRC = pathlib.Path(__file__).resolve().parent
_CUH = str(_SRC / "group_norm_silu.cuh")

# Native CUDA path supports fp16/bf16 (16-byte vector = 8 elems). fp32 and anything
# outside this set fall back to the SGLang baseline.
_SUPPORTED_DTYPES = {torch.float16, torch.bfloat16}
# Fixed workload uses num_groups=32 (all production + regression cases). Anything else
# is an unsupported signature and falls back to the SGLang baseline.
_SUPPORTED_NUM_GROUPS = {32}
_USE_PDL = False
# Dispatch: groups with >= _LARGE_THRESH elements use the multi-CTA 3-stage path; smaller
# groups use the single-CTA path. _CHUNK_ELEMS MUST match kChunkElems in group_norm_silu.cuh.
_LARGE_THRESH = 1 << 16
_CHUNK_ELEMS = 8192
# Bucket boundary (measured + NCU evidence): groups above ~0.9M elements are bandwidth-bound
# and the SGLang Triton chunked baseline is near-peak HBM, so route those to the baseline;
# below it the candidate wins on lower launch/scheduling overhead.
_GIANT_THRESH = 900_000

# Last dispatch decision, for integrated-install validation telemetry.
_LAST_PATH = "?"


@cache_once
def _module(dtype: torch.dtype, pdl: bool):
    args = make_cpp_args(dtype, pdl)
    return load_jit(
        "group_norm_silu_kda",
        *args,
        cuda_files=[_CUH],
        cuda_wrappers=[
            ("group_norm_silu", f"GroupNormSiluKernel<{args}>::run"),
            ("group_norm_silu_large", f"GroupNormSiluKernel<{args}>::run_large"),
        ],
    )


def _strict() -> bool:
    """KDA_STRICT_CANDIDATE=1 -> re-raise candidate-path exceptions instead of silently
    falling back, so correctness/benchmark prove the native kernel actually ran."""
    return os.environ.get("KDA_STRICT_CANDIDATE", "") == "1"


def _aligned(t: torch.Tensor) -> bool:
    # 16-byte base alignment required for the AlignedVector (LDG.128/STG.128) path; a
    # contiguous tensor can still have storage_offset != 0 -> a 2-byte-misaligned fp16
    # data_ptr, which would corrupt the vectorized path. Reject -> fall back to baseline.
    return t.storage_offset() == 0 and (t.data_ptr() % 16 == 0)


def _spatial(x: torch.Tensor) -> int:
    """Product of the spatial dims (everything past N, C); 1 when x is 2-D [N, C]."""
    spatial = 1
    for d in range(2, x.dim()):
        spatial *= x.shape[d]
    return spatial


def _can_use(x: Any, weight: Any, bias: Any, num_groups: Any) -> bool:
    return (
        isinstance(x, torch.Tensor)
        and x.is_cuda
        and not torch.is_grad_enabled()
        and not x.requires_grad
        and x.dtype in _SUPPORTED_DTYPES
        and x.dim() in (2, 3, 4, 5)
        and x.is_contiguous()
        and _aligned(x)
        and isinstance(num_groups, int)
        and num_groups in _SUPPORTED_NUM_GROUPS
        and x.shape[1] % num_groups == 0
        and isinstance(weight, torch.Tensor)
        and isinstance(bias, torch.Tensor)
        and weight.is_cuda
        and bias.is_cuda
        and weight.dtype == x.dtype
        and bias.dtype == x.dtype
        and weight.dim() == 1
        and bias.dim() == 1
        and tuple(weight.shape) == (x.shape[1],)
        and tuple(bias.shape) == (x.shape[1],)
        and _aligned(weight)
        and _aligned(bias)
    )


def selected_path(x: Any, weight: Any, bias: Any, num_groups: Any) -> str:
    """Which path the dispatcher takes for this signature (diagnostic / validation)."""
    if not _can_use(x, weight, bias, num_groups):
        return "baseline_unsupported"
    group_size = (x.shape[1] // int(num_groups)) * _spatial(x)
    if group_size >= _GIANT_THRESH:
        return "baseline_giant"
    return "large" if group_size >= _LARGE_THRESH else "small"


def last_dispatch() -> str:
    """The path taken by the most recent public call (for integrated validation)."""
    return _LAST_PATH


def _run_kernel(x: torch.Tensor, weight: torch.Tensor, bias: torch.Tensor, num_groups: int, eps: float) -> torch.Tensor:
    batch, channels = x.shape[0], x.shape[1]
    spatial = _spatial(x)
    num_groups = int(num_groups)
    group_size = (channels // num_groups) * spatial
    # BW-bound giants: route to the near-peak SGLang Triton baseline (see _GIANT_THRESH).
    if group_size >= _GIANT_THRESH:
        return _baseline_triton(x, weight, bias, num_groups=num_groups, eps=eps)
    x3 = x.reshape(batch, channels, spatial)
    y3 = torch.empty_like(x3)
    module = _module(x.dtype, _USE_PDL)
    w = weight.contiguous()
    b = bias.contiguous()
    if group_size >= _LARGE_THRESH:
        num_rows = batch * num_groups
        chunks_per_row = (group_size + _CHUNK_ELEMS - 1) // _CHUNK_ELEMS
        total_tasks = num_rows * chunks_per_row
        f32 = {"device": x.device, "dtype": torch.float32}
        partial_sum = torch.empty(total_tasks, **f32)
        partial_sumsq = torch.empty(total_tasks, **f32)
        mean = torch.empty(num_rows, **f32)
        rstd = torch.empty(num_rows, **f32)
        module.group_norm_silu_large(
            x3, w, b, y3, partial_sum, partial_sumsq, mean, rstd, num_groups, float(eps)
        )
    else:
        module.group_norm_silu(x3, w, b, y3, num_groups, float(eps))
    return y3.reshape(x.shape)


def triton_group_norm_silu(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    eps: float = 1e-5,
) -> torch.Tensor:
    """Drop-in for sglang triton_group_norm_silu: native candidate for supported signatures,
    captured SGLang Triton baseline otherwise."""
    global _LAST_PATH
    _LAST_PATH = selected_path(x, weight, bias, num_groups)
    if _can_use(x, weight, bias, num_groups):
        try:
            return _run_kernel(x, weight, bias, num_groups, eps)
        except Exception:
            if _strict():
                raise
            _LAST_PATH = "baseline_error"
            return _baseline_triton(x, weight, bias, num_groups=num_groups, eps=eps)
    return _baseline_triton(x, weight, bias, num_groups=num_groups, eps=eps)


def apply_group_norm_silu(x: torch.Tensor, norm: nn.Module, activation: nn.Module) -> torch.Tensor:
    """Drop-in for sglang apply_group_norm_silu: native candidate for supported signatures,
    captured SGLang baseline (original gating + eager fallback) otherwise."""
    global _LAST_PATH
    if (
        isinstance(x, torch.Tensor)
        and x.is_cuda
        and not torch.is_grad_enabled()
        and not x.requires_grad
        and isinstance(norm, nn.GroupNorm)
        and isinstance(activation, nn.SiLU)
        and not activation.inplace
        and norm.affine
        and norm.weight is not None
        and norm.bias is not None
        and _can_use(x, norm.weight, norm.bias, norm.num_groups)
    ):
        _LAST_PATH = selected_path(x, norm.weight, norm.bias, norm.num_groups)
        try:
            return _run_kernel(x, norm.weight, norm.bias, norm.num_groups, norm.eps)
        except Exception:
            if _strict():
                raise
            _LAST_PATH = "baseline_error"
            return _baseline_apply(x, norm, activation)
    _LAST_PATH = "baseline"
    return _baseline_apply(x, norm, activation)
