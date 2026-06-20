"""PyTorch golden baseline for b200_tilert_rmsnorm_expert_proj.

Pure-torch correctness oracle for the TileRT `RMSNormExpertProjDsv32` op (router).
Mirrors harness/tilert_oracle.py case_rmsnorm_expert_proj and
RMSNormExpertProj.golden_forward:
    norm_x = RMSNorm(x_in)                     # -> bf16
    scores = linear(norm_x.view(-1,dim).float(), proj_weight.float())
golden_forward returns (norm_x, scores); the compared / last element is `scores`.

RMSNorm here is tilert.models.common.RMSNorm (no residual):
    x = x.float(); var = mean(x^2, -1); x = x * rsqrt(var + eps); out = (gamma * x).to(bf16)

The oracle uses a bf16-rounded gate weight in BOTH golden and tilert (post_init
_fix_expert_proj), so we synthesize the gate weight in bf16 and matmul in float.

Inputs (ORACLE_RESULTS): x[1,s,7168]bf16 (/dim**0.5) -> scores[1,s,256]f32.
This is the ct=none (no-MMA) router; oracle rel ~1e-7. bf16 rel < 2e-2.
"""
from __future__ import annotations

import torch

DIM = 7168
N_ROUTED = 256
EPS = 1e-6


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    x = torch.randn(1, seq, DIM, generator=g, device=dev, dtype=torch.bfloat16) / DIM**0.5
    gamma = torch.randn(DIM, generator=g, device=dev, dtype=torch.float32)
    # gate weight: bf16 (matches oracle _fix_expert_proj which rounds to bf16)
    proj_weight = torch.randn(N_ROUTED, DIM, generator=g, device=dev, dtype=torch.bfloat16)
    return dict(x=x, gamma=gamma, proj_weight=proj_weight)


def _rmsnorm(x: torch.Tensor, gamma: torch.Tensor) -> torch.Tensor:
    xf = x.float()
    var = xf.pow(2).mean(-1, keepdim=True)
    xf = xf * torch.rsqrt(var + EPS)
    return (gamma * xf).to(torch.bfloat16)


def rmsnorm_expert_proj_baseline(
    x: torch.Tensor, gamma: torch.Tensor, proj_weight: torch.Tensor
):
    norm_x = _rmsnorm(x, gamma)
    scores = torch.nn.functional.linear(norm_x.view(-1, DIM).float(), proj_weight.float())
    scores = scores.view(x.shape[0], x.shape[1], N_ROUTED)
    return norm_x, scores
