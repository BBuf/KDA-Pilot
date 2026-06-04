"""CUDA fast paths for the two SGLang diffusion inference norm entry points.

Shipped copy for `python/sglang/jit_kernel/diffusion/cuda_norm_infer.py`
(the in-tree drop-in; see docs/sglang_jit_export.md). Builds the workspace
`.cuh` (placed at `python/sglang/jit_kernel/csrc/diffusion/diffusion_norm_infer.cuh`)
through the jit_kernel / tvm-ffi stack — flags match the surrounding kernels
(header-only `load_jit`, no fast-math).

Routing (B200-validated, evidence in the kernel workspace):
- LayerNorm fp32 `[8640,5120]` (+ validation shapes): float4 one-CTA-per-row.
- RMSNorm bf16 D=128, S in {1320, 4096, 16384}: one-warp-per-row.
- RMSNorm bf16 D=128, S in {648720, 650040}: tiled multi-row (32 rows/CTA,
  persistent whole-wave grid) — promoted on live steady-state interleaved A/B.
Anything outside the allowlists returns None and the caller falls through to
the Triton baseline, so behavior is unchanged for every other input.
"""

from __future__ import annotations

import os
from typing import Optional

import torch

from sglang.jit_kernel.utils import cache_once, load_jit, make_cpp_args

_KERNEL_VERSION = "v4"  # v4 = half-warp shuffle masks in the tiled RMS reduction (odd-tail safety)


def _disabled() -> bool:
    # Kill switch: set SGLANG_DIFFUSION_NORM_CUDA=0 to force the Triton path
    # while keeping the public op and its registration untouched. Read per call
    # so a single process can A/B the device paths under the identical op.
    return os.environ.get("SGLANG_DIFFUSION_NORM_CUDA", "1") == "0"

_SUPPORTED_LN = frozenset({
    (8640, 5120),
    (6, 512), (6, 3072), (12, 512), (12, 3072),
    (128, 512), (128, 3072), (256, 512), (256, 3072),
    (64, 1024), (256, 1024),
})
_SUPPORTED_RMS = frozenset({
    (1320, 128), (16384, 128), (4096, 128),
    (648720, 128), (650040, 128),
    (6, 128), (128, 128), (768, 128), (64, 128),
})
_RMS_LARGE_S = 100000
_RMS_TILED_ROWS = 32
_RMS_TILED_SCHEDULING = 1
_LN_ALIGN = 16
_RMS_ALIGN = 8
_RMS_TILED_ALIGN = 16


@cache_once
def _ln_module(dtype: torch.dtype):
    args = make_cpp_args(dtype)
    return load_jit(
        "diffusion_norm_infer_ln",
        _KERNEL_VERSION,
        *args,
        cuda_files=["diffusion/diffusion_norm_infer.cuh"],
        cuda_wrappers=[("norm_infer_ln", f"LayerNormInferKernel<{args}>::run")],
    )


@cache_once
def _rms_module(dim: int, k_unroll: int, dtype: torch.dtype):
    args = make_cpp_args(dim, k_unroll, dtype)
    return load_jit(
        "diffusion_norm_infer_rms",
        _KERNEL_VERSION,
        *args,
        cuda_files=["diffusion/diffusion_norm_infer.cuh"],
        cuda_wrappers=[("rms_onepass", f"RmsNormOnepassKernel<{args}>::run")],
    )


@cache_once
def _rms_tiled_module(dim: int, rows_per_cta: int, dtype: torch.dtype):
    args = make_cpp_args(dim, rows_per_cta, dtype)
    return load_jit(
        "diffusion_norm_infer_rms_tiled",
        _KERNEL_VERSION,
        *args,
        cuda_files=["diffusion/diffusion_norm_infer.cuh"],
        cuda_wrappers=[("rms_tiled", f"RmsNormTiledKernel<{args}>::run")],
    )


def _is_cuda_contig_2d(t) -> bool:
    return t is not None and getattr(t, "is_cuda", False) and t.dim() == 2 and t.is_contiguous()


def _aligned(t, nbytes: int) -> bool:
    return t is None or (t.data_ptr() % nbytes == 0)


def _valid_affine(t, n: int, x) -> bool:
    return (
        t is not None
        and t.is_contiguous()
        and tuple(t.shape) == (n,)
        and t.device == x.device
        and t.dtype == x.dtype
    )


def _valid_out(out, x) -> bool:
    return out is None or (
        tuple(out.shape) == tuple(x.shape)
        and out.device == x.device
        and out.dtype == x.dtype
        and out.is_contiguous()
    )


def maybe_norm_infer_cuda(x, weight, bias, eps, is_rms_norm=False, out=None) -> Optional[torch.Tensor]:
    """Returns the normalized output via the CUDA kernel, or None when the input
    is outside the validated envelope (caller falls through to Triton)."""
    if _disabled():
        return None
    if not (_is_cuda_contig_2d(x) and x.dtype == torch.float32 and not is_rms_norm):
        return None
    m, n = int(x.shape[0]), int(x.shape[1])
    if (m, n) not in _SUPPORTED_LN:
        return None
    if not (
        _valid_affine(weight, n, x)
        and _valid_affine(bias, n, x)
        and _valid_out(out, x)
        and _aligned(x, _LN_ALIGN)
        and _aligned(weight, _LN_ALIGN)
        and _aligned(bias, _LN_ALIGN)
        and _aligned(out, _LN_ALIGN)
    ):
        return None
    if out is None:
        out = torch.empty_like(x)
    _ln_module(x.dtype).norm_infer_ln(x, weight, bias, out, eps)
    return out


def maybe_rms_onepass_cuda(x, w, eps: float = 1e-6) -> Optional[torch.Tensor]:
    """Returns the RMS-normalized output via the CUDA kernel, or None when the
    input is outside the validated envelope (caller falls through to Triton)."""
    if _disabled():
        return None
    if not (_is_cuda_contig_2d(x) and x.dtype == torch.bfloat16):
        return None
    s, d = int(x.shape[0]), int(x.shape[1])
    if (s, d) not in _SUPPORTED_RMS:
        return None
    align = _RMS_TILED_ALIGN if s >= _RMS_LARGE_S else _RMS_ALIGN
    if not (_valid_affine(w, d, x) and _aligned(x, align) and _aligned(w, align)):
        return None
    out = torch.empty_like(x)
    if s >= _RMS_LARGE_S:
        _rms_tiled_module(d, _RMS_TILED_ROWS, x.dtype).rms_tiled(x, w, out, eps, _RMS_TILED_SCHEDULING)
    else:
        _rms_module(d, 1, x.dtype).rms_onepass(x, w, out, eps)
    return out
