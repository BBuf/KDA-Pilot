"""Golden baseline for TileRT down_allreduce (dense MLP down-proj + NVLink allreduce).

COMM kernel: the real `tilert::down_allreduce_op` fuses the down projection with a
flag-based NVLink allreduce across the 8 TP shards (peer_bufs/ll_buf + flag), so it is
NOT isolatable on 1 GPU. This baseline captures the **per-shard compute** that the
candidate must get right: down-project the local expert hidden, then add residual.
The cross-GPU sum (allreduce) reduces the 8 shards' partials — on 1 GPU it is identity
on the local partial. See ../../docs/benchmark_method.md (comm kernels use the
in-graph profiler time as the latency target).
"""
import torch


def down_allreduce_baseline(vec_in, down_w, x_in):
    """vec_in [1,seq,inter_shard] bf16 (local MLP hidden), down_w [7168, inter_shard]
    bf16, x_in [1,seq,7168] bf16 residual -> [1,seq,7168] (local partial + residual)."""
    local = vec_in.float() @ down_w.float().T            # [1,seq,7168] local-shard down-proj
    return (local + x_in.float()).to(torch.bfloat16)


def make_inputs(shapes, dev, inter_shard=2304):
    seq = shapes["seq"]
    g = torch.Generator(device=dev).manual_seed(0)
    vec_in = torch.randn(1, seq, inter_shard, device=dev, dtype=torch.bfloat16, generator=g) / inter_shard**0.5
    down_w = torch.randn(7168, inter_shard, device=dev, dtype=torch.bfloat16, generator=g) / inter_shard**0.5
    x_in = torch.randn(1, seq, 7168, device=dev, dtype=torch.bfloat16, generator=g) / 7168**0.5
    return {"vec_in": vec_in, "down_w": down_w, "x_in": x_in}
