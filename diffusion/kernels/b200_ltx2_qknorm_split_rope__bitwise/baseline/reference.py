"""Task-local PyTorch eager baseline (the correctness oracle).

Mirrors the LTX2 attention forward exactly (upstream ltx_2.py LTX2Attention,
non-tensor-parallel path):

    q = q_norm(q)        # torch.nn.RMSNorm(H, eps) over the full hidden dim H
    k = k_norm(k)
    q_out = apply_split_rotary_emb(q, (q_cos, q_sin))   # forced-eager
    k_out = apply_split_rotary_emb(k, (k_cos, k_sin))

The candidate must be byte-for-byte equal (torch.equal, zero tolerance) to the
tensors returned here. This module imports nothing from sglang at runtime.
"""

from typing import Tuple

import torch

from .ltx2_split_rope import apply_split_rotary_emb_eager


def build_rms_norm(weight: torch.Tensor, eps: float) -> torch.nn.RMSNorm:
    """Construct the production norm module: torch.nn.RMSNorm(H, eps) with the
    given (bf16) weight, on the weight's device/dtype. Matches the upstream
    `self.q_norm = torch.nn.RMSNorm(inner_dim, eps=norm_eps)` callsite.
    """
    hidden = int(weight.shape[-1])
    module = torch.nn.RMSNorm(
        hidden, eps=eps, elementwise_affine=True,
        device=weight.device, dtype=weight.dtype,
    )
    with torch.no_grad():
        module.weight.copy_(weight)
    return module


@torch.no_grad()
def qknorm_split_rope_reference(
    q: torch.Tensor,
    k: torch.Tensor,
    q_norm: torch.nn.Module,
    k_norm: torch.nn.Module,
    q_freqs: Tuple[torch.Tensor, torch.Tensor],
    k_freqs: Tuple[torch.Tensor, torch.Tensor],
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Eager oracle. q/k: [B, S, H] bf16 contiguous; q_norm/k_norm:
    torch.nn.RMSNorm(H, eps) modules with bf16 weights; q_freqs/k_freqs:
    (cos, sin) each [B, num_heads, S, head_dim/2] bf16, last-dim stride 1.
    Returns (q_out, k_out), both [B, S, H] bf16.
    """
    q_normed = q_norm(q)
    k_normed = k_norm(k)
    q_out = apply_split_rotary_emb_eager(q_normed, q_freqs)
    k_out = apply_split_rotary_emb_eager(k_normed, k_freqs)
    return q_out, k_out
