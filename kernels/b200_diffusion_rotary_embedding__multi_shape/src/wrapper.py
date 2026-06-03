"""Dispatch + build glue for the native-CUDA diffusion rotary-embedding kernels.

Two public callables preserve the exact SGLang names and route only the captured
production signatures to the CUDA fast path; every other shape/dtype/layout/flag
falls back to the SGLang diffusion Triton baseline. The baseline callables are
captured once at import time so that, after the public symbols are swapped to
point here, fallback does not recurse into this module.

Build/export goes through SGLang's jit_kernel / tvm-ffi stack (load_jit +
make_cpp_args), compiling the workspace-owned ``csrc/rotary_embedding.cuh`` in
place via an absolute ``cuda_files`` path (no torch.utils.cpp_extension, no
``--use_fast_math``). The source content hash is embedded in the jit module name
so editing the kernel forces a rebuild.
"""

from __future__ import annotations

import hashlib
import os
from typing import Callable, Optional

import torch

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
_CSRC_DIR = os.path.join(_THIS_DIR, "csrc")
_CUH = os.path.join(_CSRC_DIR, "rotary_embedding.cuh")


def _src_hash() -> str:
    with open(_CUH, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()[:12]


_SRC_HASH = _src_hash()

# First candidate (cuda-v1) ships without PDL: the qknorm pilot showed PDL can
# hurt isolated-launch latency, so it is validated as a separate A/B lever.
USE_PDL = False

_MODULE_CACHE: dict = {}


def _load_kernel(tag: str, export_name: str, kernel_class: str, dim: int, dtype: torch.dtype, use_pdl: bool):
    """Build (or reuse the cached) jit_kernel module for one kernel variant.
    The jit module name embeds the source hash so editing the .cuh forces a rebuild."""
    key = (tag, dim, str(dtype), use_pdl, _SRC_HASH)
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        from sglang.jit_kernel.utils import load_jit, make_cpp_args

        args = make_cpp_args(dim, use_pdl, dtype)
        mod = load_jit(
            f"kda_diffrope_{tag}_{_SRC_HASH}",
            *args,
            cuda_files=[_CUH],
            cuda_wrappers=[(export_name, f"kda_diffusion_rotary::{kernel_class}<{args}>::run")],
            extra_include_paths=[_CSRC_DIR],
        )
        _MODULE_CACHE[key] = mod
    return mod


def _load_standard(head_dim: int, dtype: torch.dtype, use_pdl: bool):
    return _load_kernel("std", "apply_rotary", "StandardRotaryKernel", head_dim, dtype, use_pdl)


def _load_ltx2(half_dim: int, dtype: torch.dtype, use_pdl: bool):
    return _load_kernel("ltx2", "apply_ltx2", "Ltx2SplitRotaryKernel", half_dim, dtype, use_pdl)


# --------------------------------------------------------------------------
# Original baseline capture (recursion-safe fallback)
# --------------------------------------------------------------------------
_original_rotary: Optional[Callable] = None
_original_ltx2: Optional[Callable] = None


def _capture_baselines() -> None:
    """Bind the ORIGINAL baseline callables once, before any symbol swap."""
    global _original_rotary, _original_ltx2
    if _original_rotary is None:
        from sglang.jit_kernel.diffusion.triton.rotary import (
            apply_rotary_embedding as _r,
        )

        _original_rotary = _r
    if _original_ltx2 is None:
        from sglang.jit_kernel.diffusion.triton.ltx2_rotary import (
            apply_ltx2_split_rotary_emb as _l,
        )

        _original_ltx2 = _l


try:
    _capture_baselines()
except Exception:
    # SGLang not importable in this environment (e.g. local CPU box). On the
    # remote B200 the capture runs at import, before install() swaps symbols.
    pass


# --------------------------------------------------------------------------
# Exact captured production signatures (docs/captured_shapes_b200.jsonl). ONLY
# these take the CUDA fast path; everything else falls back to the SGLang
# baseline. Tight gating is required by the plan ("only captured -> CUDA") AND
# for safety: the 128-bit vectorized loads assume the 16-byte-aligned offsets
# that only the captured shapes/strides guarantee.
# --------------------------------------------------------------------------
_STD_TOKENS = 27030
_STD_HEADS = 24
_STD_HEAD_DIM = 128
_LTX2_HEADS = 32
# captured (batch, seq, inner) tuples; inner = 2 * heads * half, half = inner // 64
_LTX2_SIGS = frozenset(
    {
        (1, 1536, 4096), (1, 126, 2048), (1, 1536, 2048), (1, 6144, 4096), (1, 6144, 2048),
        (2, 6144, 4096), (2, 126, 2048), (2, 6144, 2048), (1, 24576, 4096), (1, 24576, 2048),
    }
)


def _is_standard_fast(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, interleaved: bool
) -> bool:
    if interleaved or not (x.is_cuda and cos.is_cuda and sin.is_cuda):
        return False
    if x.dtype != torch.bfloat16 or cos.dtype != torch.float32 or sin.dtype != torch.float32:
        return False
    # exact captured shape: 4D (B=1, S, H, D) or 3D (S, H, D)
    if x.dim() == 4:
        if tuple(x.shape) != (1, _STD_TOKENS, _STD_HEADS, _STD_HEAD_DIM):
            return False
    elif x.dim() == 3:
        if tuple(x.shape) != (_STD_TOKENS, _STD_HEADS, _STD_HEAD_DIM):
            return False
    else:
        return False
    # inner (heads, head_dim) contiguous; the size-1 outer batch stride is a don't-care
    if x.stride(-1) != 1 or x.stride(-2) != _STD_HEAD_DIM or x.stride(-3) != _STD_HEADS * _STD_HEAD_DIM:
        return False
    half = _STD_HEAD_DIM // 2
    if tuple(cos.shape) != (_STD_TOKENS, half) or tuple(sin.shape) != (_STD_TOKENS, half):
        return False
    if tuple(cos.stride()) != (half, 1) or tuple(sin.stride()) != (half, 1):
        return False
    return True


def _is_ltx2_fast(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> bool:
    if not (x.is_cuda and cos.is_cuda and sin.is_cuda):
        return False
    if x.dtype != torch.bfloat16 or cos.dtype != torch.bfloat16 or sin.dtype != torch.bfloat16:
        return False
    if x.dim() != 3 or cos.dim() != 4 or sin.dim() != 4:
        return False
    b, s, inner = (int(v) for v in x.shape)
    if (b, s, inner) not in _LTX2_SIGS:
        return False
    half = inner // (2 * _LTX2_HEADS)
    if half not in (32, 64) or 2 * _LTX2_HEADS * half != inner:
        return False
    # x contiguous (B, S, inner)
    if tuple(x.stride()) != (s * inner, inner, 1):
        return False
    # cos/sin: captured structured NON-contiguous (B, H=32, S, half) view of a
    # contiguous (B, S, H, half) buffer -> strides (S*H*half, half, H*half, 1).
    # A contiguous (B,H,S,half) tensor has different strides and correctly fails here.
    want_shape = (b, _LTX2_HEADS, s, half)
    want_stride = (s * _LTX2_HEADS * half, half, _LTX2_HEADS * half, 1)
    if tuple(cos.shape) != want_shape or tuple(sin.shape) != want_shape:
        return False
    if tuple(cos.stride()) != want_stride or tuple(sin.stride()) != want_stride:
        return False
    return True


# --------------------------------------------------------------------------
# Public callables (preserve the exact SGLang names)
# --------------------------------------------------------------------------
def apply_rotary_embedding(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, interleaved: bool = False
) -> torch.Tensor:
    if _is_standard_fast(x, cos, sin, interleaved):
        head_dim = x.shape[-1]
        heads = x.shape[-2]
        out = torch.empty_like(x)
        mod = _load_standard(head_dim, x.dtype, USE_PDL)
        mod.apply_rotary(out.reshape(-1, heads, head_dim), x.reshape(-1, heads, head_dim), cos, sin)
        return out
    if _original_rotary is None:
        _capture_baselines()
    return _original_rotary(x, cos, sin, interleaved)


def apply_ltx2_split_rotary_emb(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor
) -> torch.Tensor:
    if _is_ltx2_fast(x, cos, sin):
        half = cos.shape[-1]
        out = torch.empty_like(x)
        mod = _load_ltx2(half, x.dtype, USE_PDL)
        mod.apply_ltx2(out, x, cos, sin)
        return out
    if _original_ltx2 is None:
        _capture_baselines()
    return _original_ltx2(x, cos, sin)


EXPORTS = {
    "apply_rotary_embedding": apply_rotary_embedding,
    "apply_ltx2_split_rotary_emb": apply_ltx2_split_rotary_emb,
}
