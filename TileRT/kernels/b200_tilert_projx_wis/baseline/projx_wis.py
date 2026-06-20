"""PyTorch golden baseline for b200_tilert_projx_wis.

Pure-torch correctness oracle for the TileRT `ProjXWis` op (indexer weight/score
projection). Mirrors harness/tilert_oracle.py case_projx_wis and
ProjxWis.golden_forward:
    out = F.linear(x_norm, w)        # w: [index_n_heads, dim]  bf16
i.e. out = x_norm @ w.T.

Dims: dim=7168, index_n_heads=64. w shape [64, 7168] bf16.

Inputs (ORACLE_RESULTS): x_norm[1,s,7168]bf16 (/dim**0.5) -> idx_scores[1,s,64]bf16.
oracle rel ~5.9e-3 < 2e-2.
"""
from __future__ import annotations

import torch

DIM = 7168
INDEX_N_HEADS = 64


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    x_norm = torch.randn(1, seq, DIM, generator=g, device=dev, dtype=torch.bfloat16) / DIM**0.5
    w = torch.randn(INDEX_N_HEADS, DIM, generator=g, device=dev, dtype=torch.bfloat16)
    return dict(x_norm=x_norm, w=w)


def projx_wis_baseline(x_norm: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    return torch.nn.functional.linear(x_norm, w)
