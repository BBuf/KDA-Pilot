"""PyTorch golden baseline for b200_tilert_qkv_rope.

Pure-torch correctness oracle for the TileRT `QkvRope` op (QKV + RoPE; rotates the
query PE and writes the rotated key PE into pe_cache). Mirrors
harness/tilert_oracle.py case_qkv_rope and QKVRoPE.golden_forward:
    k_pe = pe_cache[:bsz, start:end]
    k_pe = apply_rotary_emb(k_pe.unsqueeze(2), freqs_cis)      # interleaved=True
    pe_cache[:bsz, start:end] = k_pe.squeeze(2)
    return apply_rotary_emb(q_pe, freqs_cis)                   # interleaved=True

golden_forward returns the rotated q_pe (the compared quantity). We return
(pe_cache_updated, q_pe_rot) so the LAST tuple element matches the oracle's
primary comparison (rotated q_pe). qkv_rope is bit-exact (oracle rel = 0.0).

Dims: n_local_heads = n_heads/8 = 16, qk_rope_head_dim = 64.
freqs_cis is complex (cf64) [1, s, 32] (DeepSeek-V3.2 YaRN, start_pos=0).

Inputs (ORACLE_RESULTS): q_pe[1,s,16,64]bf16, pe_cache[1,s,64]bf16, freqs[1,s,32]cf64.
"""
from __future__ import annotations

import math

import torch

N_LOCAL_HEADS = 16
QK_ROPE = 64
# DeepSeek-V3.2 rope params (model_args defaults)
ROPE_THETA = 10000.0
ROPE_FACTOR = 40.0
BETA_FAST = 32
BETA_SLOW = 1
ORIGINAL_SEQ_LEN = 4096
MAX_SEQ_LEN = 160 * 1024


def _rope_freqs_cis(seq: int, dev) -> torch.Tensor:
    """DeepSeek-V3.2 precompute_freqs_cis for the first `seq` positions (dim=64)."""
    dim = QK_ROPE

    def find_correction_dim(num_rotations, d, base, msl):
        return d * math.log(msl / (num_rotations * 2 * math.pi)) / (2 * math.log(base))

    def find_correction_range(low_rot, high_rot, d, base, msl):
        low = math.floor(find_correction_dim(low_rot, d, base, msl))
        high = math.ceil(find_correction_dim(high_rot, d, base, msl))
        return max(low, 0), min(high, d - 1)

    def linear_ramp_factor(mn, mx, n):
        if mn == mx:
            mx += 0.001
        lf = (torch.arange(n, dtype=torch.float32) - mn) / (mx - mn)
        return torch.clamp(lf, 0, 1)

    freqs = 1.0 / (ROPE_THETA ** (torch.arange(0, dim, 2, dtype=torch.float32) / dim))
    if ROPE_FACTOR is not None and MAX_SEQ_LEN > ORIGINAL_SEQ_LEN:
        low, high = find_correction_range(BETA_FAST, BETA_SLOW, dim, ROPE_THETA, ORIGINAL_SEQ_LEN)
        smooth = 1 - linear_ramp_factor(low, high, dim // 2)
        freqs = freqs / ROPE_FACTOR * (1 - smooth) + freqs * smooth
    t = torch.arange(seq, dtype=torch.float32)
    freqs = torch.outer(t, freqs)
    return torch.polar(torch.ones_like(freqs), freqs).to(dev)


def _apply_rotary_emb(x_in: torch.Tensor, freqs_cis: torch.Tensor, interleaved: bool = True):
    dtype = x_in.dtype
    shape = x_in.shape
    if not interleaved:
        x_in = x_in.view(*shape[:-1], 2, -1).transpose(-1, -2).contiguous()
    x_in = torch.view_as_complex(x_in.float().view(*shape[:-1], -1, 2))
    freqs_cis = freqs_cis.view(1, x_in.size(1), 1, x_in.size(-1))
    y_out = torch.view_as_real(x_in * freqs_cis).flatten(3)
    if not interleaved:
        y_out = torch.cat([y_out[..., 0::2], y_out[..., 1::2]], dim=-1)
    return y_out.to(dtype)


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    q_pe = torch.randn(1, seq, N_LOCAL_HEADS, QK_ROPE, generator=g, device=dev, dtype=torch.bfloat16)
    pe_cache = torch.randn(1, seq, QK_ROPE, generator=g, device=dev, dtype=torch.bfloat16)
    freqs_cis = _rope_freqs_cis(seq, dev).unsqueeze(0)  # [1, s, 32] complex
    return dict(q_pe=q_pe, pe_cache=pe_cache, freqs_cis=freqs_cis, start_pos=0)


def qkv_rope_baseline(
    q_pe: torch.Tensor, pe_cache: torch.Tensor, freqs_cis: torch.Tensor, start_pos: int = 0
):
    bsz, seqlen = q_pe.shape[0], q_pe.shape[1]
    end_pos = start_pos + seqlen
    pe_cache = pe_cache.clone()
    k_pe = pe_cache[:bsz, start_pos:end_pos]
    k_pe = _apply_rotary_emb(k_pe.unsqueeze(2), freqs_cis)
    pe_cache[:bsz, start_pos:end_pos] = k_pe.squeeze(2)
    q_pe_rot = _apply_rotary_emb(q_pe, freqs_cis)
    return pe_cache, q_pe_rot
