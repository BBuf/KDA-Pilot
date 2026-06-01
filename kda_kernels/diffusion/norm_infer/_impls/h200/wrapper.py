"""Optimized H200 diffusion norm wrappers (native CUDA + strict fallback).

Exposes ``norm_infer`` and ``triton_one_pass_rms_norm`` with the exact recovered
SGLang callsite contracts (both OUT-OF-PLACE, return a new tensor; pinned SGLang
commit c47f0e7cd, see interface.md). Each routes ONLY the captured production
signatures to a workspace-owned native CUDA kernel and falls back to the SGLang
Triton baseline for everything else.

The SGLang baselines are bound at import time, which keeps the fallback
non-recursive after ``kda_kernels.install()`` swaps the SGLang symbols. No
package-relative imports: this module is also imported directly by the promoted
kda_kernels overlay.
"""

from __future__ import annotations

import functools
from pathlib import Path
from typing import Optional

import torch

# Bind SGLang baselines at import time (recursion-safe fallback). In the bare
# test/bench container the harness installs the platform shim first; in a real
# sglang checkout the diffusion deps are present.
try:
    from sglang.jit_kernel.diffusion.triton.norm import norm_infer as _BASE_norm_infer
except Exception:  # pragma: no cover - baseline only in the GPU/sglang env
    _BASE_norm_infer = None
try:
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
        triton_one_pass_rms_norm as _BASE_rms,
    )
except Exception:  # pragma: no cover
    _BASE_rms = None

_CSRC = Path(__file__).resolve().parent / "csrc" / "norm_kernels.cu"

# Captured production signatures (the fixed optimization table from
# docs/captured_shapes_h200.jsonl). The CUDA fast path intercepts ONLY these;
# every other shape/dtype/layout/flag falls back to the SGLang baseline.
_LN_CAPTURED_MN = {(8640, 5120)}            # fp32 LayerNorm, weight+bias, is_rms_norm=False
_RMS_CAPTURED_M = {1320, 4096, 16384, 648720, 650040}  # bf16 RMSNorm, N=128, weight only

# Records the path taken by the most recent call ("cuda" | "fallback") per fn,
# so tests can assert the production fast path actually ran (not inferred).
_LAST_DISPATCH: dict[str, Optional[str]] = {"norm_infer": None, "rms": None}


_TARGET_CC = (9, 0)  # Hopper / H200; the only arch these kernels were benchmarked on
_CAPTURED_EPS = 1e-6  # the only eps in the captured production signatures


def _aligned16(t) -> bool:
    # The CUDA kernels reinterpret rows as float4 / uint4 (128-bit) using the
    # recorded contiguous strides, so the BASE pointer must be 16-byte aligned.
    # is_contiguous() does NOT guarantee this for a sliced/offset view.
    return t.data_ptr() % 16 == 0


def _on_target_arch(t) -> bool:
    # Only intercept on the validated arch (H200/SM90). The promoted kda_kernels
    # dispatcher already routes by capability, but the task-local wrapper guards
    # itself too so it never runs unvalidated on another CUDA device.
    try:
        return tuple(torch.cuda.get_device_capability(t.device)) == _TARGET_CC
    except Exception:
        return False


def last_dispatch(which: str) -> Optional[str]:
    if which in ("rms", "triton_one_pass_rms_norm"):
        return _LAST_DISPATCH["rms"]
    return _LAST_DISPATCH["norm_infer"]


@functools.lru_cache(maxsize=1)
def _module():
    from torch.utils.cpp_extension import load

    # No --use_fast_math: keeps the fp32 LayerNorm 1/sqrtf IEEE-precise for the
    # strict 1e-5 tolerance (the bf16 RMS path uses rsqrtf, matching the baseline).
    return load(
        name="kda_norm_infer_h200",
        sources=[str(_CSRC)],
        extra_cuda_cflags=["-O3", "-lineinfo"],
        verbose=False,
    )


def build() -> None:
    """Eagerly compile the CUDA extension (warm before benchmarking)."""
    _module()


# ---------------------------------------------------------------------------
# Strict dispatch gates (only the captured production signatures pass)
# ---------------------------------------------------------------------------
def supported_norm_infer(x, weight, bias, eps, is_rms_norm) -> bool:
    if is_rms_norm:
        return False  # only the captured LayerNorm signature has a CUDA fast path
    if weight is None or bias is None:
        return False
    if not (x.is_cuda and weight.is_cuda and bias.is_cuda):
        return False
    if x.dtype is not torch.float32 or weight.dtype is not torch.float32 or bias.dtype is not torch.float32:
        return False
    if x.dim() != 2 or (int(x.size(0)), int(x.size(1))) not in _LN_CAPTURED_MN:
        return False
    n = int(x.size(1))
    # Require rank-1 [N] weight/bias exactly (reject (1,N)/(N,1) reshapes that
    # share numel but are not the captured 1-D signature).
    if weight.dim() != 1 or weight.size(0) != n or bias.dim() != 1 or bias.size(0) != n:
        return False
    if not (x.is_contiguous() and weight.is_contiguous() and bias.is_contiguous()):
        return False
    if not (_aligned16(x) and _aligned16(weight) and _aligned16(bias)):
        return False
    if float(eps) != _CAPTURED_EPS or not _on_target_arch(x):
        return False
    dev = x.device
    return weight.device == dev and bias.device == dev


def supported_rms(x, w, eps) -> bool:
    if w is None:
        return False
    if not (x.is_cuda and w.is_cuda):
        return False
    if x.dtype is not torch.bfloat16 or w.dtype is not torch.bfloat16:
        return False
    if x.dim() != 2 or int(x.size(1)) != 128 or int(x.size(0)) not in _RMS_CAPTURED_M:
        return False
    if w.dim() != 1 or w.size(0) != 128:  # rank-1 [128] exactly (reject (1,128)/(128,1))
        return False
    if not (x.is_contiguous() and w.is_contiguous()):
        return False
    if not (_aligned16(x) and _aligned16(w)):
        return False
    if float(eps) != _CAPTURED_EPS or not _on_target_arch(x):
        return False
    return w.device == x.device


# ---------------------------------------------------------------------------
# Public wrappers (match the recovered SGLang signatures exactly)
# ---------------------------------------------------------------------------
def norm_infer(
    x: torch.Tensor,
    weight: Optional[torch.Tensor],
    bias: Optional[torch.Tensor],
    eps: float,
    is_rms_norm: bool = False,
    out: Optional[torch.Tensor] = None,
):
    if out is None and supported_norm_infer(x, weight, bias, eps, is_rms_norm):
        _LAST_DISPATCH["norm_infer"] = "cuda"
        return _module().layer_norm_fp32(x, weight, bias, float(eps))
    _LAST_DISPATCH["norm_infer"] = "fallback"
    if _BASE_norm_infer is None or _BASE_norm_infer is norm_infer:
        raise RuntimeError("Unsupported norm_infer signature and no non-recursive SGLang baseline available")
    return _BASE_norm_infer(x, weight, bias, eps, is_rms_norm, out)


def triton_one_pass_rms_norm(x: torch.Tensor, w: torch.Tensor, eps: float = 1e-6):
    if supported_rms(x, w, eps):
        _LAST_DISPATCH["rms"] = "cuda"
        return _module().rms_norm_bf16_n128(x, w, float(eps))
    _LAST_DISPATCH["rms"] = "fallback"
    if _BASE_rms is None or _BASE_rms is triton_one_pass_rms_norm:
        raise RuntimeError("Unsupported triton_one_pass_rms_norm signature and no non-recursive SGLang baseline available")
    return _BASE_rms(x, w, eps)
