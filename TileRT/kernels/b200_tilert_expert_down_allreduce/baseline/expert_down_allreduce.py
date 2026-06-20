"""Golden baseline for TileRT expert_down_allreduce (MoE expert down-proj + allreduce).

COMM kernel (not 1-GPU-isolatable; see ../../docs/benchmark_method.md). The real op
fuses: per-activated-expert down-projection, weighting by the routing scores, the
shared-expert contribution, and a flag-based NVLink allreduce over the 8 shards.
This baseline captures the per-shard weighted-sum compute (allreduce = identity on the
local partial for 1 GPU).
"""
import torch


def expert_down_allreduce_baseline(vec_in, down_w, scores, x_in):
    """vec_in [1,seq,E,inter] bf16 (E = n_act+shared expert hidden), down_w
    [E,7168,inter] bf16, scores [1,seq,E] f32, x_in [1,seq,7168] residual ->
    [1,seq,7168]. out = sum_e scores_e * (vec_in_e @ down_w_e.T) + residual."""
    s = vec_in.shape[1]; E = vec_in.shape[2]
    out = x_in.float().clone()
    for e in range(E):
        contrib = vec_in[:, :, e, :].float() @ down_w[e].float().T   # [1,seq,7168]
        out += scores[:, :, e].unsqueeze(-1).float() * contrib
    return out.to(torch.bfloat16)


def make_inputs(shapes, dev, inter=256, E=9):
    seq = shapes["seq"]
    g = torch.Generator(device=dev).manual_seed(0)
    vec_in = torch.randn(1, seq, E, inter, device=dev, dtype=torch.bfloat16, generator=g) / inter**0.5
    down_w = torch.randn(E, 7168, inter, device=dev, dtype=torch.bfloat16, generator=g) / inter**0.5
    scores = torch.rand(1, seq, E, device=dev, dtype=torch.float32, generator=g)
    x_in = torch.randn(1, seq, 7168, device=dev, dtype=torch.bfloat16, generator=g) / 7168**0.5
    return {"vec_in": vec_in, "down_w": down_w, "scores": scores, "x_in": x_in}
