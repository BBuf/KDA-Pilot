"""Optimized fused in-place QK-Norm + RoPE wrapper (H200 / SM90, Hopper).

Source lineage: ported from the promoted sibling B200 implementation
(`kda_kernels/diffusion/qknorm_rope/_impls/b200/`). The CUDA kernel is
SM-agnostic (warp shuffles, vectorized 64/128-bit loads, occupancy-based grid
sizing; no SM100-only `tcgen05`/TMEM), so it rebuilds for sm_90 unchanged; the
torch cpp_extension build auto-detects the H200 arch.

Exposes ``fused_inplace_qknorm_rope`` with the exact SGLang callsite contract.
Routes the production signature (bf16, contiguous, head_dim=128, rope_dim=128,
is_neox=False, equal Q/K heads, int32/int64 positions) to a workspace-owned
native CUDA kernel, and falls back to the SGLang baseline for everything else.

This module is what the promoted ``kda_kernels`` overlay imports
(``from kda_kernels.diffusion.qknorm_rope.wrapper import fused_inplace_qknorm_rope``),
so it uses no package-relative imports and locates its CUDA source by
``__file__``. The SGLang baseline is bound at import time, which keeps the
fallback non-recursive after ``kda_kernels.install()`` swaps the SGLang symbol
(install imports this module before the swap, capturing the original).
"""

from __future__ import annotations

import functools
from pathlib import Path
from typing import Optional

import torch

# Bind the SGLang baseline at import time (recursion-safe fallback).
try:
    from sglang.jit_kernel.diffusion.qknorm_rope import (
        fused_inplace_qknorm_rope as _SGLANG_BASELINE,
    )
except Exception:  # pragma: no cover - baseline only exists in the GPU env
    _SGLANG_BASELINE = None

_CSRC = Path(__file__).resolve().parent / "csrc" / "qknorm_rope_kernel.cu"

# Records the path taken by the most recent call ("cuda" | "fallback"), so
# tests can assert the production fast path actually ran (not inferred).
_LAST_DISPATCH: dict[str, Optional[str]] = {"path": None}


def last_dispatch_path() -> Optional[str]:
    return _LAST_DISPATCH["path"]


@functools.lru_cache(maxsize=1)
def _module():
    from torch.utils.cpp_extension import load

    return load(
        name="kda_qknorm_rope_h200",
        sources=[str(_CSRC)],
        extra_cuda_cflags=["-O3", "--use_fast_math", "-lineinfo"],
        verbose=False,
    )


def build() -> None:
    """Eagerly compile the CUDA extension (used to warm before benchmarking)."""
    _module()


def _supported(
    q, k, q_weight, k_weight, cos_sin_cache, positions, is_neox, head_dim, rope_dim
) -> bool:
    if is_neox:
        return False
    if not (q.is_cuda and k.is_cuda):
        return False
    if q.dtype is not torch.bfloat16 or k.dtype is not torch.bfloat16:
        return False
    if q.dim() != 3 or k.dim() != 3:
        return False
    if head_dim != 128 or rope_dim != 128:
        return False
    if q.size(-1) != 128 or k.size(-1) != 128:
        return False
    if q.size(0) != k.size(0):
        return False
    if q.size(1) != k.size(1):  # equal Q/K head counts
        return False
    if not (q.is_contiguous() and k.is_contiguous()):
        return False
    if q_weight.dtype is not torch.bfloat16 or k_weight.dtype is not torch.bfloat16:
        return False
    if q_weight.numel() != 128 or k_weight.numel() != 128:
        return False
    if not (q_weight.is_contiguous() and k_weight.is_contiguous()):
        return False
    if cos_sin_cache.dtype is not torch.float32 or not cos_sin_cache.is_contiguous():
        return False
    if cos_sin_cache.size(-1) != 128:
        return False
    if positions.dtype not in (torch.int32, torch.int64):
        return False
    if positions.dim() != 1 or positions.size(0) != q.size(0):
        return False
    if not positions.is_contiguous():
        return False
    if cos_sin_cache.dim() != 2:
        return False
    # TRUSTED PRECONDITION (not checked here): every value in `positions` must be
    # a valid row index into `cos_sin_cache` (i.e. < cos_sin_cache.size(0)). This
    # matches the SGLang baseline, which also computes `cos_sin_cache[pos]` with no
    # bounds check; verifying it would require a per-call device max-reduction +
    # host sync that would regress this latency-bound kernel below the baseline.
    # Malformed caches that ARE cheaply detectable (wrong rank/dtype/last-dim/
    # device/contiguity) are rejected above and route to the baseline fallback.
    # All tensors must live on the same CUDA device as q (the kernel dereferences
    # them directly); otherwise route to the baseline rather than read bad memory.
    dev = q.device
    if (
        k.device != dev
        or q_weight.device != dev
        or k_weight.device != dev
        or cos_sin_cache.device != dev
        or positions.device != dev
    ):
        return False
    # The fast path issues 16-byte (float4 / 8-byte float2) vectorized loads at
    # base + lane*width; fresh contiguous allocations are 16-byte aligned, but a
    # contiguous *view* starting at an odd storage offset is not. Reject those.
    for t in (q, k, q_weight, k_weight, cos_sin_cache):
        if t.data_ptr() % 16 != 0:
            return False
    # In-place q and k must not alias/overlap: the fused kernel writes both, and
    # a shared work queue over (q heads, k heads) would race on overlapping bytes.
    q_lo, k_lo = q.data_ptr(), k.data_ptr()
    q_hi = q_lo + q.numel() * q.element_size()
    k_hi = k_lo + k.numel() * k.element_size()
    if not (q_hi <= k_lo or k_hi <= q_lo):
        return False
    return True


def _baseline_can_run(q, k, q_weight, k_weight, cos_sin_cache, positions) -> bool:
    """The bound SGLang baseline is itself a vectorized in-place CUDA kernel, so it is safe
    only for the same LOW-LEVEL layout the fast path needs -- CUDA, same device, bf16 q/k,
    int32/int64 positions, contiguous + 16-byte-aligned + non-overlapping q/k -- it just also
    covers the broader SHAPE/FLAG domain (head_dim/rope_dim/is_neox). Misaligned input makes
    the baseline raise an async cudaErrorMisalignedAddress (uncatchable, poisons the context),
    so anything outside this low-level layout (CPU, device-mismatch, non-contiguous, misaligned,
    aliased, fp16, exotic position dtype) must go to the portable PyTorch reference instead."""
    if _SGLANG_BASELINE is None or _SGLANG_BASELINE is fused_inplace_qknorm_rope:
        return False
    if q.dtype is not torch.bfloat16 or k.dtype is not torch.bfloat16:
        return False
    if positions.dtype not in (torch.int32, torch.int64):
        return False
    tensors = (q, k, q_weight, k_weight, cos_sin_cache, positions)
    if not all(t.is_cuda for t in tensors):
        return False
    dev = q.device
    if not all(t.device == dev for t in tensors):
        return False
    if not all(t.is_contiguous() for t in (q, k, q_weight, k_weight, cos_sin_cache)):
        return False
    if any(t.data_ptr() % 16 != 0 for t in (q, k, q_weight, k_weight, cos_sin_cache)):
        return False
    q_lo, k_lo = q.data_ptr(), k.data_ptr()
    if not (q_lo + q.numel() * q.element_size() <= k_lo or k_lo + k.numel() * k.element_size() <= q_lo):
        return False  # q/k overlap -> reference handles it safely
    return True


def _is_recursive_baseline(fn) -> bool:
    """True if the bound 'baseline' would recurse back into a KDA wrapper/dispatcher for this
    family (a double-install / mis-bound install): exact identity with this wrapper, the
    path-loaded local ``wrapper`` module, or any ``kda_kernels.diffusion.qknorm_rope`` overlay
    wrapper or dispatcher. The legitimate SGLang baseline lives in
    ``sglang.jit_kernel.diffusion.qknorm_rope`` and is never matched here."""
    if fn is None:
        return False
    if fn is fused_inplace_qknorm_rope:
        return True
    mod = getattr(fn, "__module__", "") or ""
    return mod == "wrapper" or mod.startswith("kda_kernels.diffusion.qknorm_rope")


def _reference_qknorm_rope(
    q, k, q_weight, k_weight, cos_sin_cache, positions, *, is_neox, eps, head_dim, rope_dim
) -> None:
    """Portable PyTorch in-place reference matching the SGLang split oracle: fp32 per-head
    RMSNorm over head_dim (x * rsqrt(mean(x^2)+eps) * weight) followed by RoPE on the first
    rope_dim lanes (interleaved/GPT-J for is_neox=False, rotate-half for is_neox=True), with
    cos = cache[pos, :rope_dim/2] and sin = cache[pos, rope_dim/2:]. Device/dtype/layout
    agnostic safety net for inputs the CUDA baseline cannot execute; mutates q and k in place
    and never raises for a well-formed call."""
    half = rope_dim // 2
    # Process q and k INDEPENDENTLY, each on its own device, so a true q/k device mismatch
    # (q on CUDA, k on CPU, or vice versa) never mixes devices: positions, cache, and the
    # matching weight are moved to that output tensor's device.
    for x, w in ((q, q_weight), (k, k_weight)):
        xd = x.device
        pos = positions.to(xd).long()
        cache = cos_sin_cache.to(device=xd, dtype=torch.float32)
        cos = cache[pos, :half].unsqueeze(1)            # [T, 1, half]
        sin = cache[pos, half:rope_dim].unsqueeze(1)    # [T, 1, half]
        xf = x.float()                                  # [T, H, head_dim]
        inv_rms = torch.rsqrt(xf.pow(2).mean(dim=-1, keepdim=True) + eps)
        xf = xf * inv_rms * w.to(device=xd, dtype=torch.float32)
        rot = xf[..., :rope_dim]
        rest = xf[..., rope_dim:]
        if is_neox:
            x1, x2 = rot[..., :half], rot[..., half:rope_dim]
            rot_out = torch.cat((x1 * cos - x2 * sin, x2 * cos + x1 * sin), dim=-1)
        else:
            x_even, x_odd = rot[..., 0::2], rot[..., 1::2]
            rot_out = torch.stack(
                (x_even * cos - x_odd * sin, x_odd * cos + x_even * sin), dim=-1
            ).flatten(-2)
        x.copy_(torch.cat((rot_out, rest), dim=-1).to(x.dtype))


def fused_inplace_qknorm_rope(
    q: torch.Tensor,
    k: torch.Tensor,
    q_weight: torch.Tensor,
    k_weight: torch.Tensor,
    cos_sin_cache: torch.Tensor,
    positions: torch.Tensor,
    *,
    is_neox: bool,
    eps: float = 1e-6,
    head_dim: int = 0,
    rope_dim: int = 0,
) -> None:
    resolved_head_dim = head_dim or q.size(-1)
    resolved_rope_dim = rope_dim or cos_sin_cache.size(-1)
    if _supported(
        q, k, q_weight, k_weight, cos_sin_cache, positions,
        is_neox, resolved_head_dim, resolved_rope_dim,
    ):
        _LAST_DISPATCH["path"] = "cuda"
        _module().fused_qknorm_rope(
            q, k, q_weight, k_weight, cos_sin_cache, positions,
            float(eps), bool(is_neox),
        )
        return None
    _LAST_DISPATCH["path"] = "fallback"
    # Recursive-baseline guard (double install): if the bound baseline resolves back into a KDA wrapper or
    # dispatcher for this family, calling it would recurse -- raise a clear error rather than
    # recurse infinitely or silently mask the misconfiguration with the reference.
    if _is_recursive_baseline(_SGLANG_BASELINE):
        raise RuntimeError(
            "Recursive SGLang baseline binding detected (double install): the bound baseline "
            "resolves back into a KDA wrapper/dispatcher for qknorm_rope. Refusing to recurse; "
            "install must bind the original SGLang baseline before swapping symbols."
        )
    # Prefer the SGLang CUDA baseline for unsupported-but-CUDA signatures it handles (is_neox,
    # head_dim/rope_dim outside the fast path). For inputs it cannot safely run (CPU, device
    # mismatch, non-contiguous, misaligned, aliased, fp16, exotic position dtype) -- or if it
    # raises -- use a device/dtype-agnostic PyTorch reference. The wrapper never raises for a
    # well-formed non-recursive call.
    if _baseline_can_run(q, k, q_weight, k_weight, cos_sin_cache, positions):
        try:
            return _SGLANG_BASELINE(
                q, k, q_weight, k_weight, cos_sin_cache, positions,
                is_neox=is_neox, eps=eps, head_dim=head_dim, rope_dim=rope_dim,
            )
        except Exception:
            pass  # fall through to the portable reference
    _reference_qknorm_rope(
        q, k, q_weight, k_weight, cos_sin_cache, positions,
        is_neox=is_neox, eps=eps, head_dim=resolved_head_dim, rope_dim=resolved_rope_dim,
    )
    return None
