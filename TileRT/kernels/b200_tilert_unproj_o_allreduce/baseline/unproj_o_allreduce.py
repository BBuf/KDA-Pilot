"""Golden baseline for TileRT unproj_o_allreduce (attention o-unproj + allreduce).

COMM kernel (not 1-GPU-isolatable; see ../../docs/benchmark_method.md). The real op
fuses the MLA output unprojection (o @ Wo^T over the local head shard) with a
flag-based NVLink allreduce across 8 shards. This baseline captures the per-shard
unproj GEMM + residual (allreduce = identity on the local partial for 1 GPU).
"""
import torch


def unproj_o_allreduce_baseline(o_in, wo, x_in):
    """o_in [1,seq,H_local,v_head] bf16, wo [7168, H_local*v_head] bf16,
    x_in [1,seq,7168] residual -> [1,seq,7168] (local unproj + residual)."""
    s = o_in.shape[1]
    o_flat = o_in.reshape(1, s, -1).float()          # [1,seq,H_local*v_head]
    local = o_flat @ wo.float().T                    # [1,seq,7168]
    return (local + x_in.float()).to(torch.bfloat16)


def make_inputs(shapes, dev, H_local=20, v_head=128):
    seq = shapes["seq"]
    g = torch.Generator(device=dev).manual_seed(0)
    o_in = torch.randn(1, seq, H_local, v_head, device=dev, dtype=torch.bfloat16, generator=g) / v_head**0.5
    wo = torch.randn(7168, H_local * v_head, device=dev, dtype=torch.bfloat16, generator=g) / (H_local * v_head)**0.5
    x_in = torch.randn(1, seq, 7168, device=dev, dtype=torch.bfloat16, generator=g) / 7168**0.5
    return {"o_in": o_in, "wo": wo, "x_in": x_in}
