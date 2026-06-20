"""PyTorch golden baseline for b200_tilert_projq_wqb.

Pure-torch correctness oracle for the TileRT `ProjQWkvbDevBHMMA` op (absorbed W_UK:
q_nope contracted with the nope half of kv_b -> q in kv-lora space). Mirrors
harness/tilert_oracle.py case_projq_wqb and ProjqWqb.golden_forward:
    out = einsum("bshd,hdc->bshc", q_nope, wkv_b)
where wkv_b is the per-head nope-half slice of kv_b_proj, shape
[n_local_heads, qk_nope_head_dim, kv_lora_rank].

The real weight is fp8 dequantized then (per oracle post_init) rounded to bf16, so
we synthesize wkv_b directly in bf16 (== correctness oracle for the fp8 path).

Dims: n_local_heads=20 (7-worker padded), qk_nope_head_dim=128, kv_lora_rank=512.

Inputs (ORACLE_RESULTS): q_nope[1,s,20,128]bf16 (/8) -> [1,s,20,512]bf16.
fp8 path, oracle rel ~3.5e-3 < 5e-2.
"""
from __future__ import annotations

import torch

N_LOCAL_HEADS = 20
QK_NOPE = 128
KV_LORA = 512


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    q_nope = torch.randn(
        1, seq, N_LOCAL_HEADS, QK_NOPE, generator=g, device=dev, dtype=torch.bfloat16
    ) / 8
    wkv_b = torch.randn(
        N_LOCAL_HEADS, QK_NOPE, KV_LORA, generator=g, device=dev, dtype=torch.bfloat16
    )
    return dict(q_nope=q_nope, wkv_b=wkv_b)


def projq_wqb_baseline(q_nope: torch.Tensor, wkv_b: torch.Tensor) -> torch.Tensor:
    return torch.einsum("bshd,hdc->bshc", q_nope, wkv_b)
