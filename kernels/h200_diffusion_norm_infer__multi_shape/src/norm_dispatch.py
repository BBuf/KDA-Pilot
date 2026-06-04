"""Zero-overhead dispatcher for the diffusion inference-only norm kernels.

Preserves the two public SGLang callable names and routes only the exact
captured buckets to the native-CUDA specializations (built through SGLang's
jit_kernel / tvm-ffi stack), falling back to the SGLang baseline for every
other signature.

Design notes (the small RMS shapes are CPU launch/dispatch-bound, ~32us in the
baseline): the hot path does only cheap attribute checks, reuses a cache_once'd
compiled module, and allocates a single output tensor. No per-call dict
building, no try/except in the hot path, no extra device syncs.
"""

from __future__ import annotations

import pathlib
from typing import Optional

import torch

from sglang.jit_kernel.utils import cache_once, load_jit, make_cpp_args

# SGLang baselines (fallback path + the semantic oracle).
from sglang.jit_kernel.diffusion.triton.norm import norm_infer as _baseline_norm_infer
from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
    triton_one_pass_rms_norm as _baseline_rms_norm,
)

_SRC = pathlib.Path(__file__).resolve().parent
_RMS_CUH = str(_SRC / "rms_norm_d128.cuh")
_RMS_TILE_CUH = str(_SRC / "rms_norm_d128_tile16.cuh")
_LN_CUH = str(_SRC / "layer_norm_n5120.cuh")

_RMS_DIM = 128
# Multi-row tile config: 8 rows x 128 cols per 128-thread CTA (16 lanes/row,
# one 128-bit chunk each), grid = ceil(M/8) like the Triton baseline's program
# grid. Measured on H200: device parity-plus vs the Triton kernel at M~650k
# (where the prior persistent warp kernel regressed ~9%) AND faster than the
# warp kernel at small M, so one kernel serves every captured RMS shape.
_RMS_TILE_ROWS = 8
_RMS_TILE_THREADS = 128
_RMS_TILE_STREAM = False  # __ldcs/__stcs hints: ~0.6% device gain but ~1.6% wall loss; rejected
_LN_N = 5120
_USE_PDL = False  # PDL hurt isolated latency in the qknorm pilot; opt-in only.


# --------------------------------------------------------------------------- #
# JIT module loaders (memoized; one compile per (kernel, template) tuple)
# --------------------------------------------------------------------------- #
@cache_once
def _rms_module(dim: int, dtype: torch.dtype, use_pdl: bool):
    """Prior persistent two-rows-per-warp kernel (kept for reference/AB use)."""
    targs = make_cpp_args(dim, use_pdl, dtype)
    return load_jit(
        "kda_rms_norm",
        *targs,
        cuda_files=[_RMS_CUH],
        cuda_wrappers=[("rms_norm", f"RmsNormKernel<{targs}>::run")],
    )


@cache_once
def _rms_tile_module(dim: int, dtype: torch.dtype, use_pdl: bool):
    targs = make_cpp_args(dim, _RMS_TILE_ROWS, _RMS_TILE_THREADS, _RMS_TILE_STREAM, use_pdl, dtype)
    return load_jit(
        "kda_rms_norm_tile",
        *targs,
        cuda_files=[_RMS_TILE_CUH],
        cuda_wrappers=[("rms_norm_tile", f"RmsNormTileKernel<{targs}>::run")],
    )


@cache_once
def _ln_module(n: int, dtype: torch.dtype, has_bias: bool, use_pdl: bool):
    targs = make_cpp_args(n, has_bias, use_pdl, dtype)
    return load_jit(
        "kda_layer_norm",
        *targs,
        cuda_files=[_LN_CUH],
        cuda_wrappers=[("layer_norm", f"LayerNormKernel<{targs}>::run")],
    )


@cache_once
def _ln_available() -> bool:
    """True only if the LayerNorm specialization source exists and compiles for
    the helios config; otherwise the dispatcher transparently uses the baseline."""
    if not pathlib.Path(_LN_CUH).exists():
        return False
    try:
        _ln_module(_LN_N, torch.float32, True, _USE_PDL)
        return True
    except Exception:
        return False


@cache_once
def _rms_available(dtype: torch.dtype) -> bool:
    try:
        _rms_tile_module(_RMS_DIM, dtype, _USE_PDL)
        return True
    except Exception:
        return False


# --------------------------------------------------------------------------- #
# Public entry points (drop-in for the SGLang baselines)
# --------------------------------------------------------------------------- #
def triton_one_pass_rms_norm(x: torch.Tensor, w: torch.Tensor, eps: float = 1e-6):
    # Restricted to bf16: every captured and regression RMS shape is bf16. fp16
    # D=128 would compile (the kernel templates it) but is out of the validated
    # shape set, so it falls back to the SGLang baseline rather than run untested.
    # Require a fully contiguous input: then x.reshape(-1, D) and the fresh
    # empty_like(x).reshape(-1, D) are guaranteed views (row stride == D), so the
    # kernel writes into the returned tensor. A merely last-dim-contiguous but
    # otherwise non-contiguous higher-rank tensor would make reshape allocate a
    # copy and the kernel would write into a discarded buffer -> route to baseline.
    if (
        x.is_cuda
        and x.dtype == torch.bfloat16
        and x.shape[-1] == _RMS_DIM
        and x.is_contiguous()
        and w.dtype == x.dtype
        and w.numel() == _RMS_DIM
        and w.is_contiguous()
        and _rms_available(x.dtype)
    ):
        y = torch.empty_like(x)
        _rms_tile_module(_RMS_DIM, x.dtype, _USE_PDL).rms_norm_tile(
            x.reshape(-1, _RMS_DIM), w, y.reshape(-1, _RMS_DIM), float(eps)
        )
        return y
    return _baseline_rms_norm(x, w, eps)


def norm_infer(
    x: torch.Tensor,
    weight: Optional[torch.Tensor],
    bias: Optional[torch.Tensor],
    eps: float,
    is_rms_norm: bool = False,
    out: Optional[torch.Tensor] = None,
):
    if (
        not is_rms_norm
        and out is None  # the optimized path is validated only for fresh-output calls
        and x.is_cuda
        and x.dtype == torch.float32
        and x.shape[-1] == _LN_N
        and x.is_contiguous()  # guarantees reshape/empty_like give kernel-writable views
        and weight is not None
        and bias is not None
        and weight.dtype == x.dtype
        and bias.dtype == x.dtype
        and weight.numel() == _LN_N
        and bias.numel() == _LN_N
        and weight.is_contiguous()
        and bias.is_contiguous()
        and _ln_available()
    ):
        y = torch.empty_like(x)
        _ln_module(_LN_N, x.dtype, True, _USE_PDL).layer_norm(
            x.reshape(-1, _LN_N), weight, bias, y.reshape(-1, _LN_N), float(eps)
        )
        return y
    return _baseline_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)
