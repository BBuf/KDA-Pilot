"""Task-local PyTorch eager baseline for LTX2 dual modulation (destination-passing).

The upstream SGLang LTX2 dual-modulation path is pure PyTorch eager: normalization
is `RMSNormNoWeight`, which on CUDA resolves to `F.rms_norm(x, (D,), eps)` (see
docs/baseline_source.md), followed by the dual affine. These launchers run that
exact eager sequence and write into caller-provided output tensors (the single
behavioral change vs. the upstream callsite: `y0`/`y1` are passed in, not
allocated inside), exposing the same destination-passing ABI as the candidate so
the benchmark times the real per-call eager cost.

No sglang import anywhere (standalone benchmark contract).
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

# Supported-input contract (mirrors prompt.md / docs/baseline_source.md).
_MAX_HIDDEN = 8192
_HIDDEN_MULTIPLE = 256


def _check_x(x: torch.Tensor) -> int:
    if not x.is_cuda:
        raise ValueError("x must be a CUDA tensor")
    if x.dtype != torch.bfloat16:
        raise ValueError("x must be bfloat16")
    if x.dim() != 3:
        raise ValueError("x must be rank-3 [B, S, D]")
    if x.stride(-1) != 1:
        raise ValueError("x last dimension must be contiguous")
    d = int(x.shape[-1])
    if d % _HIDDEN_MULTIPLE != 0 or d > _MAX_HIDDEN:
        raise ValueError(
            f"hidden size {d} must be divisible by {_HIDDEN_MULTIPLE} and <= {_MAX_HIDDEN}"
        )
    return d


def _check_param(p: torch.Tensor, d: int, name: str) -> None:
    if not p.is_cuda:
        raise ValueError(f"{name} must be a CUDA tensor")
    if p.dtype != torch.bfloat16:
        raise ValueError(f"{name} must be bfloat16")
    if int(p.shape[-1]) != d:
        raise ValueError(f"{name} hidden size {int(p.shape[-1])} != x hidden size {d}")
    if p.stride(-1) != 1:
        raise ValueError(f"{name} last dimension must be contiguous")


def ltx2_dual_modulate_baseline(
    x: torch.Tensor,
    scale0: torch.Tensor,
    shift0: torch.Tensor,
    scale1: torch.Tensor,
    shift1: torch.Tensor,
    eps: float,
    y0: torch.Tensor,
    y1: torch.Tensor,
) -> None:
    """Explicit dual modulation: rms_norm(x) then two affines, written to y0/y1."""
    d = _check_x(x)
    for name, p in (("scale0", scale0), ("shift0", shift0), ("scale1", scale1), ("shift1", shift1)):
        _check_param(p, d, name)
    normed = F.rms_norm(x, normalized_shape=(d,), eps=float(eps))
    # Destination-passing: final op writes straight into the preallocated output.
    torch.add(normed * (1 + scale0.expand_as(x)), shift0.expand_as(x), out=y0)
    torch.add(normed * (1 + scale1.expand_as(x)), shift1.expand_as(x), out=y1)


def ltx2_ca_dual_modulate_from_temb_baseline(
    x: torch.Tensor,
    temb_scale_shift: torch.Tensor,
    scale_shift_table: torch.Tensor,
    eps: float,
    y0: torch.Tensor,
    y1: torch.Tensor,
) -> None:
    """Cross-attention dual modulation: derive scale/shift from table+temb, then
    rms_norm(x) and two affines, written to y0/y1."""
    d = _check_x(x)
    b, s, _ = x.shape
    if temb_scale_shift.dtype != torch.bfloat16:
        raise ValueError("temb_scale_shift must be bfloat16")
    if scale_shift_table.dtype not in (torch.bfloat16, torch.float32):
        raise ValueError("scale_shift_table must be bfloat16 or float32")
    temb_seq = int(temb_scale_shift.shape[1])
    if temb_seq not in (1, s):
        raise ValueError(f"temb_seq {temb_seq} must be 1 or S={s}")
    if int(temb_scale_shift.shape[-1]) != 4 * d:
        raise ValueError("temb_scale_shift last dimension must be 4*D")
    if tuple(scale_shift_table.shape) != (4, d):
        raise ValueError("scale_shift_table must be [4, D] with matching D")
    scale0, shift0, scale1, shift1 = (
        scale_shift_table.to(dtype=x.dtype).view(1, 1, 4, d)
        + temb_scale_shift.reshape(b, temb_seq, 4, d)
    ).unbind(dim=2)
    normed = F.rms_norm(x, normalized_shape=(d,), eps=float(eps))
    torch.add(normed * (1 + scale0), shift0, out=y0)
    torch.add(normed * (1 + scale1), shift1, out=y1)
