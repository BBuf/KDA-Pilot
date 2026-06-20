"""PyTorch golden baseline for b200_tilert_rotate.

Pure-torch correctness oracle for the TileRT `Rotate` op (RoPE on the first
qk_rope_head_dim dims of each indexer head, followed by a normalized Hadamard
transform over the full head_dim). Mirrors harness/tilert_oracle.py case_rotate
and Rotate.golden_forward:
    q_pe_idx, q_nope_idx = split(idx_q, [qk_rope_head_dim, head_dim-qk_rope_head_dim], -1)
    q_pe_idx = apply_rotary_emb(q_pe_idx, freqs_cis, interleaved=False)
    idx_q = cat([q_pe_idx, q_nope_idx], -1)
    out = rotate_activation(idx_q)   # normalized Walsh-Hadamard, scale=head_dim**-0.5

Dims: index_n_heads=64, index_head_dim=128, qk_rope_head_dim=64.
freqs_cis is complex (cf64) [s, 32] (DeepSeek-V3.2 YaRN, start_pos=0).

Inputs (ORACLE_RESULTS): idx_q[1,s,64,128]bf16, freqs_cis[s,32]cf64 -> [1,s,64,128]bf16.
oracle rel ~2.8e-3 < 2e-2.
"""
from __future__ import annotations

import math

import torch
import torch.nn.functional as F

INDEX_N_HEADS = 64
INDEX_HEAD_DIM = 128
QK_ROPE = 64
ROPE_THETA = 10000.0
ROPE_FACTOR = 40.0
BETA_FAST = 32
BETA_SLOW = 1
ORIGINAL_SEQ_LEN = 4096
MAX_SEQ_LEN = 160 * 1024


def _rope_freqs_cis(seq: int, dev) -> torch.Tensor:
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


def _hadamard_matrix(n: int, dtype, device) -> torch.Tensor:
    """Sylvester-ordered (unnormalized) Walsh-Hadamard matrix, n a power of 2."""
    assert (n & (n - 1)) == 0, "n must be a power of 2"
    H = torch.ones(1, 1, dtype=dtype, device=device)
    while H.shape[0] < n:
        H = torch.cat([torch.cat([H, H], dim=1), torch.cat([H, -H], dim=1)], dim=0)
    return H


def _rotate_activation(x: torch.Tensor) -> torch.Tensor:
    """Matches fast_hadamard_transform(x, scale=hidden_size**-0.5) / scipy fallback."""
    assert x.dtype == torch.bfloat16
    dim = x.size(-1)
    x_shape = x.shape
    xf = x.reshape(-1, dim)
    log_dim = math.ceil(math.log2(dim))
    dim_padded = 2 ** log_dim
    if dim != dim_padded:
        xf = F.pad(xf, (0, dim_padded - dim))
    Hd = _hadamard_matrix(dim_padded, xf.dtype, xf.device)
    out = F.linear(xf, Hd) * (dim ** -0.5)
    return out[..., :dim].reshape(*x_shape)


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    idx_q = torch.randn(
        1, seq, INDEX_N_HEADS, INDEX_HEAD_DIM, generator=g, device=dev, dtype=torch.bfloat16
    )
    freqs_cis = _rope_freqs_cis(seq, dev)  # [s, 32] complex
    return dict(idx_q=idx_q, freqs_cis=freqs_cis)


def rotate_baseline(idx_q: torch.Tensor, freqs_cis: torch.Tensor) -> torch.Tensor:
    q_pe_idx, q_nope_idx = torch.split(
        idx_q, [QK_ROPE, INDEX_HEAD_DIM - QK_ROPE], dim=-1
    )
    q_pe_idx = _apply_rotary_emb(q_pe_idx, freqs_cis, interleaved=False)
    idx_q = torch.cat([q_pe_idx, q_nope_idx], dim=-1)
    return _rotate_activation(idx_q)
