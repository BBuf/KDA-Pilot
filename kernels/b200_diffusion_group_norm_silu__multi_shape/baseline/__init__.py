"""Local baseline package: copied upstream SGLang GroupNorm+SiLU sources.

Copied files (see docs/baseline_source.md for provenance and the local-edit
log):
- ``group_norm_silu.py``  <- python/sglang/jit_kernel/diffusion/group_norm_silu.py
- ``triton/group_norm_silu.py`` <- python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py

Local files: ``_sglang_shims.py``, package ``__init__`` files.

``group_norm_silu_baseline`` is the destination-passing benchmark entry used by
``bench/adapter.py``; it exposes the exact upstream Triton dispatch (gating,
``.contiguous()`` materialization, one-pass/chunked branch selection) with the
final output written into the caller-provided contiguous buffer.
"""

from __future__ import annotations

import torch

from .group_norm_silu import apply_group_norm_silu
from .triton.group_norm_silu import triton_group_norm_silu


def group_norm_silu_baseline(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    eps: float,
    out: torch.Tensor,
) -> torch.Tensor:
    """Benchmark ABI entry: upstream Triton baseline with destination passing."""
    return triton_group_norm_silu(x, weight, bias, num_groups, eps, out=out)


__all__ = [
    "apply_group_norm_silu",
    "triton_group_norm_silu",
    "group_norm_silu_baseline",
]
