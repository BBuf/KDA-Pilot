"""PyTorch golden baseline for b200_tilert_projo_wkvb.

Pure-torch correctness oracle for the TileRT `ProjOWkvbDevBHMMA` op (absorbed W_UV:
attention output o in kv-lora space contracted with the value half of kv_b ->
o in v-head space). Mirrors harness/tilert_oracle.py case_projo_wkvb and
ProjoWKVb.golden_forward:
    out = einsum("bshc,hdc->bshd", o, wkv_b)
where wkv_b is the per-head v-head slice of kv_b_proj, shape
[n_local_heads, v_head_dim, kv_lora_rank].

The real weight is fp8 dequantized then (per oracle post_init) rounded to bf16, so
we synthesize wkv_b directly in bf16 (== correctness oracle for the fp8 path).

Dims: n_local_heads=20 (7-worker padded), v_head_dim=128, kv_lora_rank=512.

Inputs (ORACLE_RESULTS): o[1,s,20,512]bf16 (/8) -> [1,s,20,128]bf16.
fp8 path, oracle rel ~3.2e-3 < 5e-2.
"""
from __future__ import annotations

import torch

N_LOCAL_HEADS = 20
V_HEAD = 128
KV_LORA = 512


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    o = torch.randn(
        1, seq, N_LOCAL_HEADS, KV_LORA, generator=g, device=dev, dtype=torch.bfloat16
    ) / 8
    wkv_b = torch.randn(
        N_LOCAL_HEADS, V_HEAD, KV_LORA, generator=g, device=dev, dtype=torch.bfloat16
    )
    return dict(o=o, wkv_b=wkv_b)


def projo_wkvb_baseline(o: torch.Tensor, wkv_b: torch.Tensor) -> torch.Tensor:
    return torch.einsum("bshc,hdc->bshd", o, wkv_b)
