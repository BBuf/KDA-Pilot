"""PyTorch golden baseline for b200_tilert_rmsnorm_projq_wqi.

Pure-torch correctness oracle for the TileRT `RmsnormProjQWqiHMMA` op (GPU0 indexer
q_i projection: rmsnorm(q_a) + W_qi -> iq[64,128]). Mirrors
harness/tilert_oracle.py case_rmsnorm_projq_wqi and RmsnormProjqWqi.golden_forward:
    qr = rms_norm(q.float(), [q_lora], q_norm, eps).to(q.dtype)
    iq = rearrange(matmul(qr, wqi.T), "b s (h d) -> b s h d", d=index_head_dim)

The real weight is fp8 dequantized then (per oracle post_init) rounded to bf16, so
we synthesize ref_wqi directly in bf16 (== correctness oracle for the fp8 path).

Dims: q_lora=1536, index_n_heads=64, index_head_dim=128
=> index_head_dim_total = 64*128 = 8192, wqi shape [8192, 1536].

Inputs (ORACLE_RESULTS): q[1,s,1536]bf16 (/8) -> iq[1,s,64,128]bf16.
fp8 path, oracle rel ~3.2e-3 < 5e-2.
"""
from __future__ import annotations

import torch

Q_LORA = 1536
INDEX_N_HEADS = 64
INDEX_HEAD_DIM = 128
INDEX_DIM_TOTAL = INDEX_N_HEADS * INDEX_HEAD_DIM  # 8192
EPS = 1e-6


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    q = torch.randn(1, seq, Q_LORA, generator=g, device=dev, dtype=torch.bfloat16) / 8
    q_norm = torch.randn(Q_LORA, generator=g, device=dev, dtype=torch.float32)
    wqi = torch.randn(INDEX_DIM_TOTAL, Q_LORA, generator=g, device=dev, dtype=torch.bfloat16)
    return dict(q=q, q_norm=q_norm, wqi=wqi)


def rmsnorm_projq_wqi_baseline(
    q: torch.Tensor, q_norm: torch.Tensor, wqi: torch.Tensor
) -> torch.Tensor:
    bsz, seqlen, _ = q.shape
    qr = torch.nn.functional.rms_norm(q.float(), [q.size(-1)], q_norm, EPS).to(q.dtype)
    out = torch.matmul(qr, wqi.T)  # [b, s, index_dim_total]
    # rearrange "b s (h d) -> b s h d" with d=INDEX_HEAD_DIM
    return out.view(bsz, seqlen, INDEX_N_HEADS, INDEX_HEAD_DIM)
