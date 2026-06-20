"""PyTorch golden baseline for b200_tilert_rmsnorm.

Pure-torch correctness oracle for the TileRT `RMSNorm` op (plain RMSNorm, no
quant). Mirrors harness/tilert_oracle.py case_rmsnorm and the
`rmsnorm_op` reference math:
    x = hidden.float()
    out = (x * rsqrt(mean(x^2, -1) + eps)) * gamma

Inputs (ORACLE_RESULTS): hidden[1,s,7168]bf16, gamma[7168]f32. Output compared as
float32 hidden_out [1,s,7168]. bf16 rel < 2e-2.
"""
from __future__ import annotations

import torch

DIM = 7168
EPS = 1e-6


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    hidden = torch.randn(1, seq, DIM, generator=g, device=dev, dtype=torch.bfloat16)
    gamma = torch.randn(DIM, generator=g, device=dev, dtype=torch.float32)
    return dict(hidden=hidden, gamma=gamma)


def rmsnorm_baseline(hidden: torch.Tensor, gamma: torch.Tensor) -> torch.Tensor:
    x = hidden.float()
    out = x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + EPS)
    return out * gamma
