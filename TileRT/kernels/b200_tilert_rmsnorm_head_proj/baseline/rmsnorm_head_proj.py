"""PyTorch golden baseline for b200_tilert_rmsnorm_head_proj.

Pure-torch correctness oracle for the TileRT `RMSNormHeadProj` op (fused final
norm + LM-head GEMM). Mirrors harness/tilert_oracle.py case_rmsnorm_head_proj and
RMSNormHeadProj.golden_forward:
    hidden_rmsnorm = rms_norm(hidden.float(), [dim], gamma, eps)   # float32
    logits = hidden_rmsnorm.float() @ head_proj.T.float()

The head_proj is sharded per device: lm_head[vocab, dim] reshaped to
(num_devices, vocab//num_devices, dim); device 0 takes the first
vocab//num_devices = 16160 rows (num_devices=8).

Inputs (ORACLE_RESULTS): hidden[1,s,7168]bf16 (/dim**0.5) -> logits[1,s,16160]f32.
bf16 rel ~5.4e-3 < 2e-2.
"""
from __future__ import annotations

import torch

DIM = 7168
VOCAB = 129280
NUM_DEVICES = 8
VOCAB_PER_DEV = VOCAB // NUM_DEVICES  # 16160
EPS = 1e-6


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    hidden = torch.randn(1, seq, DIM, generator=g, device=dev, dtype=torch.bfloat16) / DIM**0.5
    gamma = torch.randn(DIM, generator=g, device=dev, dtype=torch.float32)
    # full lm_head, device-0 shard = first VOCAB_PER_DEV rows
    head_proj = torch.randn(
        VOCAB_PER_DEV, DIM, generator=g, device=dev, dtype=torch.bfloat16
    )
    return dict(hidden=hidden, gamma=gamma, head_proj=head_proj)


def rmsnorm_head_proj_baseline(
    hidden: torch.Tensor, gamma: torch.Tensor, head_proj: torch.Tensor
) -> torch.Tensor:
    hidden_rmsnorm = torch.nn.functional.rms_norm(
        hidden.float(), [hidden.size(-1)], gamma, EPS
    )
    return hidden_rmsnorm.float() @ head_proj.T.float()
