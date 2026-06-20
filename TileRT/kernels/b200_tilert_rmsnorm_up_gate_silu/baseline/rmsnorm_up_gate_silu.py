"""PyTorch golden baseline for b200_tilert_rmsnorm_up_gate_silu.

Pure-torch correctness oracle for the TileRT `RMSNormUpGateSiLUDSv32` op (dense MLP:
RMSNorm + per-expert up/gate projections + SiLU gating, fp8 path). Mirrors
harness/tilert_oracle.py case_rmsnorm_up_gate_silu and
RMSNormUpGateSiLU.golden_forward:
    x_rmsnorm = rms_norm(x_in.float(), [dim], norm_gamma, eps)        # float32
    for each seq position s, for each expert i in [0, n_experts):
        w1 = x_rmsnorm[0,s] @ ref_gate[i].T                          # float
        w3 = x_rmsnorm[0,s] @ ref_up[i].T                            # float
        hidden[i] = (silu(w1) * w3).to(bf16)
    out = stack over (s, expert) -> [1, seq, n_experts, moe_inter_dim_per_device]

The op shards the dense MLP intermediate over num_devices=8 and groups each device's
slice into n_experts groups of moe_inter_dim_per_device rows. The per-expert gate/up
weights are fp8 (e4m3) with 128x128 block scales; the golden consumes the
block-dequantized (float) weights. We synthesize fp8 weights + block scales and
dequantize them so the reference reflects the fp8 weight precision the candidate
must match (the fp8 MMA path; oracle rel ~3.4e-2 < 5e-2).

Dims: dim=7168, inter_dim=18432, moe_inter_dim=2048, num_devices=8, block=128
  => moe_inter_dim_per_device = 256, inter_dim_per_device = 2304,
     n_experts = inter_dim_per_device / moe_inter_dim_per_device = 9.
  per-expert gate/up: [256, 7168] fp8, scales [256//128=2, 7168//128=56].

Inputs (ORACLE_RESULTS): x[1,s,7168]bf16 (/dim**0.5) -> [1,s,9,256]bf16.
"""
from __future__ import annotations

import torch
import torch.nn.functional as F

DIM = 7168
INTER_DIM = 18432
MOE_INTER_DIM = 2048
NUM_DEVICES = 8
BLOCK = 128
EPS = 1e-6

MOE_INTER_PER_DEV = MOE_INTER_DIM // NUM_DEVICES      # 256
INTER_PER_DEV = INTER_DIM // NUM_DEVICES              # 2304
N_EXPERTS = INTER_PER_DEV // MOE_INTER_PER_DEV        # 9


def _weight_dequant(x_fp8: torch.Tensor, scale: torch.Tensor, block: int = BLOCK) -> torch.Tensor:
    """Block-wise (block x block) dequant: y[m,n] = x_fp8[m,n] * scale[m//b, n//b]."""
    M, N = x_fp8.shape
    y = x_fp8.float().reshape(M // block, block, N // block, block)
    y = y * scale.float()[:, None, :, None]
    return y.reshape(M, N)


def make_inputs(shapes: dict, dev) -> dict:
    seq = int(shapes["seq"])
    g = torch.Generator(device=dev).manual_seed(0)
    x = torch.randn(1, seq, DIM, generator=g, device=dev, dtype=torch.bfloat16) / DIM**0.5
    gamma = torch.randn(DIM, generator=g, device=dev, dtype=torch.float32)

    m = MOE_INTER_PER_DEV
    sm = m // BLOCK          # 2
    sn = DIM // BLOCK        # 56
    # per-expert fp8 gate/up weights + 128x128 block scales (-> dequantized below)
    gate_fp8 = torch.randn(
        N_EXPERTS, m, DIM, generator=g, device=dev, dtype=torch.bfloat16
    ).to(torch.float8_e4m3fn)
    up_fp8 = torch.randn(
        N_EXPERTS, m, DIM, generator=g, device=dev, dtype=torch.bfloat16
    ).to(torch.float8_e4m3fn)
    gate_scales = torch.randn(N_EXPERTS, sm, sn, generator=g, device=dev, dtype=torch.bfloat16)
    up_scales = torch.randn(N_EXPERTS, sm, sn, generator=g, device=dev, dtype=torch.bfloat16)

    ref_gate = torch.stack(
        [_weight_dequant(gate_fp8[i], gate_scales[i]) for i in range(N_EXPERTS)], dim=0
    )
    ref_up = torch.stack(
        [_weight_dequant(up_fp8[i], up_scales[i]) for i in range(N_EXPERTS)], dim=0
    )
    return dict(x=x, gamma=gamma, gate=ref_gate, up=ref_up)


def rmsnorm_up_gate_silu_baseline(
    x: torch.Tensor, gamma: torch.Tensor, gate: torch.Tensor, up: torch.Tensor
) -> torch.Tensor:
    bsz, seq_len = x.shape[0], x.shape[1]
    x_rmsnorm = torch.nn.functional.rms_norm(x.float(), [x.size(-1)], gamma, EPS)
    hidden_out_list = []
    for s in range(seq_len):
        w1_list = []
        w3_list = []
        for i in range(N_EXPERTS):
            w1_list.append(x_rmsnorm[0, s].float() @ gate[i].float().T)
            w3_list.append(x_rmsnorm[0, s].float() @ up[i].float().T)
        w1 = torch.stack(w1_list, dim=0)
        w3 = torch.stack(w3_list, dim=0)
        hidden = (F.silu(w1.float()) * w3.float()).to(torch.bfloat16)
        hidden_out_list.append(hidden)
    out = torch.stack(hidden_out_list, dim=0)  # [seq, n_experts, moe_inter_pd]
    return out[None, ...]                      # [1, seq, n_experts, moe_inter_pd]
