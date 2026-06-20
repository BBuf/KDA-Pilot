"""PyTorch golden baseline for b200_tilert_rmsnorm_projq_wqb.

Pure-torch correctness oracle for the TileRT `RmsnormProjQWqbHMMA` op
(rmsnorm(q_a) + Wq_b -> q[20,192], split into q_nope[128] + q_pe[64]).
Mirrors harness/tilert_oracle.py case_rmsnorm_projq_wqb and
RmsnormProjqWqb.golden_forward:
    qr = rms_norm(q.float(), [q_lora], q_norm, eps).to(q.dtype)
    q_out = matmul(qr, wq_b.T).view(1, s, n_local_heads, qk_head_dim)
    q_nope, q_pe = split(q_out, [qk_nope_head_dim, qk_rope_head_dim], dim=-1)
golden_forward returns (q_nope, q_pe) and the oracle compares q_nope (out_idx=0).
Here we return (q_pe, q_nope) so the LAST tuple element (what the generated
correctness.py compares) is the validated quantity q_nope.

The real weight is fp8 dequantized then (per oracle post_init) rounded to bf16, so
we synthesize ref_wq_b directly in bf16 (== correctness oracle for the fp8 path).

Dims: q_lora=1536, n_local_heads=20 (7-worker padded), qk_nope=128, qk_rope=64
=> qk_head_dim=192, wq_b shape [20*192, 1536] = [3840, 1536].

Inputs (ORACLE_RESULTS): q[1,s,1536]bf16 (/8) -> q_nope[1,s,20,128], q_pe[1,s,20,64].
fp8 path, oracle rel ~3.3e-3 < 5e-2.
"""
from __future__ import annotations

import torch

Q_LORA = 1536
N_LOCAL_HEADS = 20
QK_NOPE = 128
QK_ROPE = 64
QK_HEAD_DIM = QK_NOPE + QK_ROPE  # 192
QK_LOCAL_DIM = QK_HEAD_DIM * N_LOCAL_HEADS  # 3840
EPS = 1e-6


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    q = torch.randn(1, seq, Q_LORA, generator=g, device=dev, dtype=torch.bfloat16) / 8
    q_norm = torch.randn(Q_LORA, generator=g, device=dev, dtype=torch.float32)
    wq_b = torch.randn(QK_LOCAL_DIM, Q_LORA, generator=g, device=dev, dtype=torch.bfloat16)
    return dict(q=q, q_norm=q_norm, wq_b=wq_b)


def rmsnorm_projq_wqb_baseline(q: torch.Tensor, q_norm: torch.Tensor, wq_b: torch.Tensor):
    bsz, seqlen, _ = q.shape
    qr = torch.nn.functional.rms_norm(q.float(), [q.size(-1)], q_norm, EPS).to(q.dtype)
    q_out = torch.matmul(qr, wq_b.T)
    q_out = q_out.view(bsz, seqlen, N_LOCAL_HEADS, QK_HEAD_DIM)
    q_nope, q_pe = torch.split(q_out, [QK_NOPE, QK_ROPE], dim=-1)
    # NOTE: the validated oracle quantity is q_nope (out_idx=0). The generated
    # correctness.py compares the LAST element of a returned tuple, so we put
    # q_nope last while still returning both halves of the projection.
    return q_pe, q_nope
