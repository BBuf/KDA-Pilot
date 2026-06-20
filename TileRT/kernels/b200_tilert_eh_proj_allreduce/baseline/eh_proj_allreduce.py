"""Golden baseline for TileRT eh_proj_allreduce (MTP eh_proj + allreduce).

COMM kernel (not 1-GPU-isolatable). The real op projects the MTP combined hidden
(cat of two RMSNorms, 2*7168=14336) down to 7168 over the local shard, then NVLink
allreduces across 8 shards. Baseline = per-shard eh_proj GEMM (allreduce = identity
on the local partial for 1 GPU). See ../../docs/benchmark_method.md.
"""
import torch


def eh_proj_allreduce_baseline(combined, eh_proj_w):
    """combined [1,seq,14336] bf16, eh_proj_w [7168,14336] bf16 -> [1,seq,7168]."""
    return (combined.float() @ eh_proj_w.float().T).to(torch.bfloat16)


def make_inputs(shapes, dev, dim=7168):
    seq = shapes["seq"]
    g = torch.Generator(device=dev).manual_seed(0)
    combined = torch.randn(1, seq, 2 * dim, device=dev, dtype=torch.bfloat16, generator=g) / (2 * dim)**0.5
    eh_proj_w = torch.randn(dim, 2 * dim, device=dev, dtype=torch.bfloat16, generator=g) / (2 * dim)**0.5
    return {"combined": combined, "eh_proj_w": eh_proj_w}
