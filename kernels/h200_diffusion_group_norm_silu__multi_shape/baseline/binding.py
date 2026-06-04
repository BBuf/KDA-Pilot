"""Local baseline entry points for the benchmark/correctness harnesses.

This is the single import surface for the copied SGLang baseline
(`docs/baseline_source.md`). Both callables keep the upstream semantics
verbatim, including the internal gating that can silently route to the eager
PyTorch implementation; `triton_path_active` re-exports the upstream gate so
harnesses can verify the Triton path is genuinely taken for a workload
instead of trusting it blindly.
"""

from __future__ import annotations

import torch
from torch import nn

from .group_norm_silu_apply import apply_group_norm_silu
from .group_norm_silu_triton import (
    _can_use_triton_group_norm_silu,
    _LARGE_GROUP_THRESHOLD,
    triton_group_norm_silu,
)


def group_norm_silu_baseline(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    eps: float,
) -> torch.Tensor:
    """Direct-entry baseline: the copied upstream Triton public callable."""
    return triton_group_norm_silu(x, weight, bias, num_groups, eps=eps)


def group_norm_silu_baseline_apply(
    x: torch.Tensor,
    norm: nn.Module,
    activation: nn.Module,
) -> torch.Tensor:
    """Wrapper-entry baseline: the copied upstream module-level callable."""
    return apply_group_norm_silu(x, norm, activation)


def triton_path_active(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
) -> bool:
    """True iff the copied baseline would run its Triton kernels (not eager)."""
    return _can_use_triton_group_norm_silu(x, weight, bias, num_groups)


def uses_chunked_path(x: torch.Tensor, num_groups: int) -> bool:
    """True iff the baseline routes this shape to the two-kernel chunked path."""
    spatial = 1
    for dim in x.shape[2:]:
        spatial *= dim
    group_size = (x.shape[1] // num_groups) * spatial
    return group_size >= _LARGE_GROUP_THRESHOLD


__all__ = [
    "group_norm_silu_baseline",
    "group_norm_silu_baseline_apply",
    "triton_path_active",
    "uses_chunked_path",
]
