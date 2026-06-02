"""Pure-PyTorch FP32 references for the two SGLang diffusion RoPE kernels.

These mirror the exact SGLang triton numerics and are used in two places:
  * `tests/test_correctness.py` as the independent correctness cross-check;
  * `src/wrapper.py` as the 3rd-level fallback (CUDA -> SGLang baseline -> this).

Device-agnostic (runs on CPU or CUDA). Standard rounds to bf16 only on the final
store; LTX-2 reproduces the deliberate intermediate ``(x*cos)->bf16`` rounding.
"""

from __future__ import annotations

import torch


def std_rope_ref_fp32(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, interleaved: bool = False
) -> torch.Tensor:
    """Adjacent-pair RoPE reference (returns fp32).

    ``x``: (B,T,H,D) or (T,H,D). ``cos``/``sin``: fp32, shape (T, D//2) — or
    (T, D) when ``interleaved`` and then sub-sampled like the baseline. cos/sin are
    shared across heads and indexed by ``bt % T``.
    """
    orig_shape = x.shape
    if x.dim() == 4:
        B, T, H, D = x.shape
    else:
        T, H, D = x.shape
        B = 1
    assert D % 2 == 0, "head_size must be even"

    if interleaved and cos.shape[-1] == D:
        cos = cos[..., ::2]
        sin = sin[..., ::2]
    half = D // 2
    assert cos.shape[-1] == half and sin.shape[-1] == half, (cos.shape, sin.shape, half)

    rows = cos.shape[0]
    xv = x.reshape(B * T, H, D).float()
    pos = torch.arange(B * T, device=x.device) % rows
    c = cos.index_select(0, pos).float().view(B * T, 1, half)
    s = sin.index_select(0, pos).float().view(B * T, 1, half)

    x1 = xv[..., 0::2]
    x2 = xv[..., 1::2]

    out = torch.empty_like(xv)
    out[..., 0::2] = x1 * c - x2 * s
    out[..., 1::2] = x1 * s + x2 * c
    return out.reshape(orig_shape)


def ltx2_rope_ref_fp32(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
    """Split-half RoPE reference (returns fp32).

    ``x``: (B,S,H*2*half) bf16. ``cos``/``sin``: (B,H,S,half) bf16, possibly
    non-contiguous. Reproduces the intermediate ``(x*cos)->bf16`` rounding.
    """
    B, S, inner = x.shape
    CB, H, CS, half = cos.shape
    assert (CB, CS) == (B, S), (cos.shape, (B, S))
    assert sin.shape == cos.shape, (sin.shape, cos.shape)
    D = half * 2
    assert inner == H * D, (inner, H * D)

    xv = x.view(B, S, H, D)
    x_first = xv[..., :half].float()
    x_second = xv[..., half:].float()

    c = cos.permute(0, 2, 1, 3).float()  # (B,S,H,half)
    s = sin.permute(0, 2, 1, 3).float()

    first_cos = (x_first * c).to(torch.bfloat16).float()
    second_cos = (x_second * c).to(torch.bfloat16).float()

    out = torch.empty((B, S, H, D), device=x.device, dtype=torch.float32)
    out[..., :half] = first_cos - x_second * s
    out[..., half:] = second_cos + x_first * s
    return out.reshape_as(x)


def standard_rope_reference(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, interleaved: bool = False
) -> torch.Tensor:
    """Functional fallback: same dtype as ``x``."""
    return std_rope_ref_fp32(x, cos, sin, interleaved=interleaved).to(x.dtype)


def ltx2_split_rope_reference(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
    """Functional fallback: same dtype as ``x``."""
    return ltx2_rope_ref_fp32(x, cos, sin).to(x.dtype)
