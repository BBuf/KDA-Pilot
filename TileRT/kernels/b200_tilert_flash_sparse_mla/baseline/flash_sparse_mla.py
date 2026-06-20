"""PyTorch golden baseline for b200_tilert_flash_sparse_mla.

Pure-torch correctness oracle for the TileRT `PureMlaDsv32` / `FlashSparseMlaDSv32`
op (sparse MLA decode over a top-2048 KV gather, in compressed latent space).
Mirrors harness/tilert_oracle.py case_flash_sparse_mla and
FlashSparseMLACombine.golden_forward:

    start_pos = int(cur_pos.item())
    mask = full((seq, kv_len), -inf).triu_(start_pos + 1)   if seq > 1 else None
    scores = (einsum("bshc,btc->bsht", q_nope, kv_cache)        # latent QK^T (nope part)
            + einsum("bshr,btr->bsht", q_pe,   pe_cache)) * softmax_scale
    index_mask = full((b, seq, kv_len), -inf).scatter_(-1, topk_indices, 0)
    if mask is not None: index_mask += mask
    scores += index_mask.unsqueeze(2)
    scores = scores.softmax(-1, dtype=float32)
    out = einsum("bsht,btc->bshc", scores.to(bf16), kv_cache)   # latent O = P @ V

softmax_scale = (qk_nope + qk_rope) ** -0.5 * mscale^2,
  mscale = 0.1 * log(rope_factor) + 1.0   (rope_factor = 40).

topk_indices = arange(kv_len) (dense for kv_len == topk == 2048) so the index_mask
is all-selected; cur_pos = kv_len - seq drives the causal mask when seq > 1.

Dims (ORACLE_RESULTS): q_nope[1,s,16,512], q_pe[1,s,16,64], kv_cache[1,2048,512],
pe_cache[1,2048,64] bf16, idx[1,s,2048]i32, cur_pos[1]i32 -> o[1,s,16,512]bf16.
oracle rel ~3.0e-3 < 2e-2.
"""
from __future__ import annotations

import math

import torch

HEADS = 16
KV_LORA = 512
QK_NOPE = 128
QK_ROPE = 64
KV_LEN = 2048
ROPE_FACTOR = 40.0

_SCALE = (QK_NOPE + QK_ROPE) ** -0.5
_MSCALE = 0.1 * math.log(ROPE_FACTOR) + 1.0
SOFTMAX_SCALE = _SCALE * _MSCALE * _MSCALE


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    q_nope = torch.randn(1, seq, HEADS, KV_LORA, generator=g, device=dev, dtype=torch.bfloat16) / 8
    q_pe = torch.randn(1, seq, HEADS, QK_ROPE, generator=g, device=dev, dtype=torch.bfloat16) / 8
    kv_cache = torch.randn(1, KV_LEN, KV_LORA, generator=g, device=dev, dtype=torch.bfloat16) / 8
    pe_cache = torch.randn(1, KV_LEN, QK_ROPE, generator=g, device=dev, dtype=torch.bfloat16) / 8
    idx = (
        torch.arange(KV_LEN, device=dev, dtype=torch.int32)
        .view(1, 1, KV_LEN)
        .expand(1, seq, KV_LEN)
        .contiguous()
    )
    cur_pos = torch.tensor([KV_LEN - seq], device=dev, dtype=torch.int32)
    return dict(
        q_nope=q_nope,
        q_pe=q_pe,
        kv_cache=kv_cache,
        pe_cache=pe_cache,
        topk_indices=idx,
        cur_pos=cur_pos,
    )


def flash_sparse_mla_baseline(
    q_nope: torch.Tensor,
    q_pe: torch.Tensor,
    kv_cache: torch.Tensor,
    pe_cache: torch.Tensor,
    topk_indices: torch.Tensor,
    cur_pos: torch.Tensor,
) -> torch.Tensor:
    batch_size = q_nope.shape[0]
    seqlen = q_nope.shape[1]
    seqlen_kv = kv_cache.shape[1]

    start_pos = int(cur_pos.item())
    mask = (
        torch.full((seqlen, seqlen_kv), float("-inf"), device=q_nope.device).triu_(start_pos + 1)
        if seqlen > 1
        else None
    )

    scores = (
        torch.einsum("bshc,btc->bsht", q_nope.float(), kv_cache.float())
        + torch.einsum("bshr,btr->bsht", q_pe.float(), pe_cache.float())
    ) * SOFTMAX_SCALE

    index_mask = torch.full(
        (batch_size, seqlen, seqlen_kv), float("-inf"), device=q_nope.device
    ).scatter_(-1, topk_indices.long(), 0)
    if mask is not None:
        index_mask += mask

    scores += index_mask.unsqueeze(2)
    scores = scores.softmax(dim=-1, dtype=torch.float32)
    return torch.einsum("bsht,btc->bshc", scores.to(torch.bfloat16), kv_cache)
