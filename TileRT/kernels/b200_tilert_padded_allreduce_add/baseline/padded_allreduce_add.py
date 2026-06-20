"""Golden baseline for TileRT padded_allreduce_add.

COMM kernel (not 1-GPU-isolatable). The real op allreduces a (possibly zero-padded)
partial buffer written by peers over NVLink, then adds the residual x_in. On a single
GPU the peers' partials are absent, so the golden reduces to: out = partial + x_in
(with partial = zeros when no peer contributed). Baseline returns partial + x_in.
"""
import torch


def padded_allreduce_add_baseline(partial, x_in):
    """partial [1,seq,7168] bf16 (peer-summed), x_in [1,seq,7168] residual -> sum."""
    return (partial.float() + x_in.float()).to(torch.bfloat16)


def make_inputs(shapes, dev, dim=7168):
    seq = shapes["seq"]
    g = torch.Generator(device=dev).manual_seed(0)
    partial = torch.randn(1, seq, dim, device=dev, dtype=torch.bfloat16, generator=g) / dim**0.5
    x_in = torch.randn(1, seq, dim, device=dev, dtype=torch.bfloat16, generator=g) / dim**0.5
    return {"partial": partial, "x_in": x_in}
