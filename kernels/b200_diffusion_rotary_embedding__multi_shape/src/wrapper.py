"""Optimized B200 diffusion rotary-embedding wrappers.

Exposes ``apply_rotary_embedding`` and ``apply_ltx2_split_rotary_emb`` with the
exact recovered SGLang callsite contracts (both OUT-OF-PLACE, return a new
tensor; see ``interface.md``, pinned SGLang commit 0b65588c1). Each routes the
captured production signature to a workspace-owned native CUDA kernel and falls
back to the SGLang Triton baseline for everything else.

The SGLang baselines are bound at import time, which keeps the fallback
non-recursive after ``kda_kernels.install()`` swaps the SGLang symbols (install
imports this module before the swap, capturing the originals). No package-relative
imports: this module is also imported directly by the promoted kda_kernels overlay.
"""

from __future__ import annotations

import functools
from pathlib import Path
from typing import Optional

import torch

# Bind the SGLang baselines at import time (recursion-safe fallback).
try:
    from sglang.jit_kernel.diffusion.triton.rotary import (
        apply_rotary_embedding as _SGLANG_STD,
    )
except Exception:  # pragma: no cover - baseline only exists in the GPU env
    _SGLANG_STD = None
try:
    from sglang.jit_kernel.diffusion.triton.ltx2_rotary import (
        apply_ltx2_split_rotary_emb as _SGLANG_LTX2,
    )
except Exception:  # pragma: no cover
    _SGLANG_LTX2 = None

_CSRC = Path(__file__).resolve().parent / "csrc" / "rotary_embedding_kernel.cu"

# Records the path taken by the most recent call ("cuda" | "fallback") per fn,
# so tests can assert the production fast path actually ran (not inferred).
_LAST_DISPATCH: dict[str, Optional[str]] = {"standard": None, "ltx2": None}

_VEC = 8  # bf16 lanes per 128-bit word; LTX-2 cos/sin strides must be multiples of this

# Captured production signatures (the fixed optimization table from prompt.md /
# docs/captured_shapes_b200.jsonl). The CUDA fast path routes ONLY these to the native
# kernel; every other shape falls back to the SGLang baseline, per the plan's fixed-shape
# contract (never silently intercept a shape that was not profiled and benchmarked). The
# kernels are mathematically correct for the broader signature class, so this table can be
# widened in a later round only after new shapes are captured AND benchmarked.
_STD_CAPTURED = {(27030, 24, 128)}  # (num_tokens, num_heads, head_dim)
_LTX2_CAPTURED = {  # (batch, seq_len, half); num_heads is always 32, head_dim = 2*half
    (1, 1536, 64), (1, 126, 32), (1, 1536, 32), (1, 6144, 64), (1, 6144, 32),
    (2, 6144, 64), (2, 126, 32), (2, 6144, 32), (1, 24576, 64), (1, 24576, 32),
}


def _aligned16(t) -> bool:
    # The CUDA kernels reinterpret tensors as int4* (128-bit) and use the recorded
    # element strides (all multiples of 8 = 16 bytes), so the BASE pointer must be
    # 16-byte aligned. is_contiguous() does NOT guarantee this: a sliced / offset
    # workspace view can be contiguous yet have data_ptr() % 16 != 0. Such a tensor
    # must fall back to the SGLang baseline rather than fault / read misaligned.
    return t.data_ptr() % 16 == 0


def last_dispatch_path(which: str) -> Optional[str]:
    return _LAST_DISPATCH[which]


@functools.lru_cache(maxsize=1)
def _module():
    from torch.utils.cpp_extension import load

    return load(
        name="kda_rope_b200",
        sources=[str(_CSRC)],
        extra_cuda_cflags=["-O3", "--use_fast_math", "-lineinfo"],
        verbose=False,
    )


def build() -> None:
    """Eagerly compile the CUDA extension (warm before benchmarking)."""
    _module()


# ---------------------------------------------------------------------------
# Dispatch gates (strict; only the captured production signatures pass)
# ---------------------------------------------------------------------------
def _supported_standard(x, cos, sin, interleaved) -> bool:
    if interleaved:
        return False
    if not (x.is_cuda and cos.is_cuda and sin.is_cuda):
        return False
    if x.dtype is not torch.bfloat16:
        return False
    if x.dim() not in (3, 4) or not x.is_contiguous():
        return False
    if x.dim() == 4 and x.size(0) != 1:  # only the size-1-batch captured signature
        return False
    head_size = x.size(-1)
    num_heads = x.size(-2)
    num_tokens = x.size(-3)  # == size(0) for the 3-D (S,H,D) form; dim already gated to {3,4}
    if (int(num_tokens), int(num_heads), int(head_size)) not in _STD_CAPTURED:
        return False
    if cos.dtype is not torch.float32 or sin.dtype is not torch.float32:
        return False
    if not (cos.is_contiguous() and sin.is_contiguous()):
        return False
    if cos.dim() != 2 or sin.dim() != 2:
        return False
    if cos.size(0) != num_tokens or sin.size(0) != num_tokens:
        return False
    if cos.size(1) != head_size // 2 or sin.size(1) != head_size // 2:
        return False
    if not _aligned16(x):  # x is int4-loaded; cos/sin are scalar fp32 loads (no 16B requirement)
        return False
    dev = x.device
    return cos.device == dev and sin.device == dev


def _supported_ltx2(x, cos, sin) -> bool:
    if not (x.is_cuda and cos.is_cuda and sin.is_cuda):
        return False
    if x.dtype is not torch.bfloat16 or cos.dtype is not torch.bfloat16 or sin.dtype is not torch.bfloat16:
        return False
    if x.dim() != 3 or not x.is_contiguous():
        return False
    if cos.dim() != 4 or sin.dim() != 4 or tuple(cos.shape) != tuple(sin.shape):
        return False
    batch, num_heads, seq_len, half = cos.shape
    if num_heads != 32 or half not in (32, 64):
        return False
    if (int(batch), int(seq_len), int(half)) not in _LTX2_CAPTURED:
        return False
    if cos.size(0) != x.size(0) or cos.size(2) != x.size(1):
        return False
    if x.size(2) != num_heads * 2 * half:
        return False
    # innermost half must be contiguous, and the (b,h,t) strides must be 128-bit
    # aligned (multiples of 8 bf16) for the vectorized loads.
    for t in (cos, sin):
        if t.stride(3) != 1:
            return False
        if any(t.stride(d) % _VEC != 0 for d in (0, 1, 2)):
            return False
    if not (_aligned16(x) and _aligned16(cos) and _aligned16(sin)):  # all int4-loaded by the kernel
        return False
    dev = x.device
    return cos.device == dev and sin.device == dev


# ---------------------------------------------------------------------------
# Public wrappers (match the recovered SGLang signatures exactly)
# ---------------------------------------------------------------------------
def apply_rotary_embedding(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, interleaved: bool = False
) -> torch.Tensor:
    if _supported_standard(x, cos, sin, interleaved):
        _LAST_DISPATCH["standard"] = "cuda"
        return _module().apply_rotary_embedding(x, cos, sin, bool(interleaved))
    _LAST_DISPATCH["standard"] = "fallback"
    if _SGLANG_STD is None or _SGLANG_STD is apply_rotary_embedding:
        raise RuntimeError("Unsupported signature and no non-recursive SGLang baseline available")
    return _SGLANG_STD(x, cos, sin, interleaved)


def apply_ltx2_split_rotary_emb(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor
) -> torch.Tensor:
    if _supported_ltx2(x, cos, sin):
        _LAST_DISPATCH["ltx2"] = "cuda"
        return _module().apply_ltx2_split_rotary_emb(x, cos, sin)
    _LAST_DISPATCH["ltx2"] = "fallback"
    if _SGLANG_LTX2 is None or _SGLANG_LTX2 is apply_ltx2_split_rotary_emb:
        raise RuntimeError("Unsupported signature and no non-recursive SGLang baseline available")
    return _SGLANG_LTX2(x, cos, sin)
