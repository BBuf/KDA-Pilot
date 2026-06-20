"""PyTorch golden baseline for b200_tilert_rmsnorm_kv.

Pure-torch correctness oracle for the TileRT `RmsnormKv` op. Mirrors
harness/tilert_oracle.py case_rmsnorm_kv and KVRMSNorm.golden_forward:
    out = rms_norm(kv.float(), [kv.size(-1)], gamma, eps).to(kv.dtype)
    kv_cache[:bsz, start_pos:end_pos] = out
The compared quantity is the written cache slice kv_cache[:, :seq] (bf16, bit-exact
== 0.0 in the oracle).

Inputs (ORACLE_RESULTS): kv[1,s,512]bf16, gamma[512]f32; kv_cache[1,>=16,512]bf16.
start_pos = 0. Output = updated kv_cache slice [1,s,512] bf16. bf16 rel < 2e-2.

torch.nn.functional.rms_norm(x, normalized_shape, weight, eps) computes
    x / sqrt(mean(x^2, last dims) + eps) * weight
"""
from __future__ import annotations

import torch

KV_LORA = 512
EPS = 1e-6


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    kv = torch.randn(1, seq, KV_LORA, generator=g, device=dev, dtype=torch.bfloat16)
    gamma = torch.randn(KV_LORA, generator=g, device=dev, dtype=torch.float32)
    cache_len = max(seq, 16)
    kv_cache = torch.zeros(1, cache_len, KV_LORA, device=dev, dtype=torch.bfloat16)
    return dict(kv=kv, gamma=gamma, kv_cache=kv_cache, start_pos=0)


def rmsnorm_kv_baseline(
    kv: torch.Tensor, gamma: torch.Tensor, kv_cache: torch.Tensor, start_pos: int = 0
) -> torch.Tensor:
    bsz, seqlen, _ = kv.shape
    end_pos = start_pos + seqlen
    out = torch.nn.functional.rms_norm(
        kv.float(), [kv.size(-1)], gamma, EPS
    ).to(kv.dtype)
    kv_cache = kv_cache.clone()
    kv_cache[:bsz, start_pos:end_pos].copy_(out)
    return kv_cache[:, start_pos:end_pos]
