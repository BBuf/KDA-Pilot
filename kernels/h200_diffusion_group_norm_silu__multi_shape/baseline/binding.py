"""Local baseline entry points for the benchmark/correctness harnesses.

This is the single import surface for the copied SGLang baseline
(`docs/baseline_source.md`). The allocate-and-return callables keep the
upstream semantics verbatim, including the internal gating that can silently
route to the eager PyTorch implementation; `triton_path_active` re-exports
the upstream gate so harnesses can verify the Triton path is genuinely taken
for a workload instead of trusting it blindly.

The `*_into` callables are the destination-passing local ABI required by the
standard benchmark template (outputs preallocated by the harness; no output
allocation in the timed path). They replicate the copied launchers' bodies
line-for-line except that the output buffer is the caller's `out`; every
internal scratch allocation (chunked partials/stats) stays exactly as the
upstream code wrote it.
"""

from __future__ import annotations

import math

import torch
import triton  # type: ignore
from torch import nn

from .group_norm_silu_apply import apply_group_norm_silu
from .group_norm_silu_triton import (
    _BLOCK_SIZE,
    _BLOCKS_PER_PROGRAM,
    _can_use_triton_group_norm_silu,
    _CHUNK_SIZE,
    _group_norm_apply_kernel,
    _group_norm_apply_scalar_affine_kernel,
    _group_norm_finalize_stats_kernel,
    _group_norm_silu_contiguous_kernel,
    _group_norm_stats_kernel,
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


def _one_pass_into(x_contiguous, weight, bias, num_groups, eps, out) -> None:
    # Mirrors the copied _launch_one_pass except `out` replaces the
    # torch.empty_like output allocation.
    batch_size, channels = x_contiguous.shape[:2]
    spatial_size = math.prod(x_contiguous.shape[2:]) if x_contiguous.ndim > 2 else 1
    channels_per_group = channels // num_groups
    group_size = channels_per_group * spatial_size

    x_flat = x_contiguous.reshape(batch_size, channels, spatial_size, 1)
    y_flat = out.reshape(batch_size, channels, spatial_size, 1)
    block_size = min(4096, triton.next_power_of_2(max(1, min(group_size, 4096))))

    _group_norm_silu_contiguous_kernel[(num_groups, batch_size)](
        x_flat,
        weight,
        bias,
        y_flat,
        channels,
        spatial_size,
        channels_per_group,
        group_size,
        eps,
        BLOCK_SIZE=block_size,
    )


def _chunked_into(x_contiguous, weight, bias, num_groups, eps, out) -> None:
    # Mirrors the copied _launch_chunked except `out` replaces the
    # torch.empty_like output allocation; internal partial/stats scratch
    # allocations are kept exactly as upstream wrote them.
    batch_size, channels = x_contiguous.shape[:2]
    spatial_size = math.prod(x_contiguous.shape[2:]) if x_contiguous.ndim > 2 else 1
    channels_per_group = channels // num_groups
    group_size = channels_per_group * spatial_size
    rows = batch_size * num_groups
    chunks_per_row = triton.cdiv(group_size, _CHUNK_SIZE)

    x_flat = x_contiguous.reshape(-1)
    y_flat = out.reshape(-1)
    partial_sum = torch.empty(
        (rows, chunks_per_row), device=x_contiguous.device, dtype=torch.float32
    )
    partial_sq = torch.empty_like(partial_sum)
    stats = torch.empty((rows, 2), device=x_contiguous.device, dtype=torch.float32)

    _group_norm_stats_kernel[(rows, chunks_per_row)](
        x_flat,
        partial_sum,
        partial_sq,
        channels,
        spatial_size,
        num_groups,
        channels_per_group,
        group_size,
        chunks_per_row,
        BLOCK_SIZE=_BLOCK_SIZE,
        BLOCKS_PER_PROGRAM=_BLOCKS_PER_PROGRAM,
        num_warps=8,
        num_stages=3,
    )

    reduce_block = min(1024, triton.next_power_of_2(max(1, chunks_per_row)))
    _group_norm_finalize_stats_kernel[(rows,)](
        partial_sum,
        partial_sq,
        stats,
        chunks_per_row,
        group_size,
        eps,
        BLOCK_SIZE=reduce_block,
        num_warps=4,
        num_stages=2,
    )

    if spatial_size % _CHUNK_SIZE == 0 and chunks_per_row >= 64:
        _group_norm_apply_scalar_affine_kernel[(rows, chunks_per_row)](
            x_flat,
            weight,
            bias,
            y_flat,
            stats,
            channels,
            spatial_size,
            num_groups,
            channels_per_group,
            group_size,
            chunks_per_row,
            BLOCK_SIZE=_BLOCK_SIZE,
            BLOCKS_PER_PROGRAM=_BLOCKS_PER_PROGRAM,
            num_warps=4,
            num_stages=3,
        )
    else:
        _group_norm_apply_kernel[(rows, chunks_per_row)](
            x_flat,
            weight,
            bias,
            y_flat,
            stats,
            channels,
            spatial_size,
            num_groups,
            channels_per_group,
            group_size,
            chunks_per_row,
            BLOCK_SIZE=_BLOCK_SIZE,
            BLOCKS_PER_PROGRAM=_BLOCKS_PER_PROGRAM,
            num_warps=8,
            num_stages=3,
        )


def group_norm_silu_baseline_into(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    eps: float,
    out: torch.Tensor,
) -> None:
    """Destination-passing direct entry over the copied Triton kernels.

    Benchmark-only ABI: requires the upstream gate to admit the Triton path
    (the harness asserts this for every production row); raises otherwise so
    an eager fallback can never be timed silently.
    """
    if not _can_use_triton_group_norm_silu(x, weight, bias, num_groups):
        raise RuntimeError(
            "baseline destination-passing wrapper requires the Triton path"
        )
    if out.shape != x.shape or out.dtype != x.dtype or not out.is_contiguous():
        raise ValueError("out must be a contiguous tensor matching x")
    x_contiguous = x.contiguous()
    spatial_size = math.prod(x_contiguous.shape[2:]) if x_contiguous.ndim > 2 else 1
    channels_per_group = x_contiguous.shape[1] // num_groups
    group_size = channels_per_group * spatial_size
    with torch.cuda.device(x.device):
        if group_size >= _LARGE_GROUP_THRESHOLD:
            _chunked_into(x_contiguous, weight, bias, num_groups, eps, out)
        else:
            _one_pass_into(x_contiguous, weight, bias, num_groups, eps, out)


def group_norm_silu_baseline_apply_into(
    x: torch.Tensor,
    norm: nn.Module,
    activation: nn.Module,
    out: torch.Tensor,
) -> None:
    """Destination-passing wrapper entry: unpacks the module attributes per
    call (mirroring the copied apply wrapper's per-call unpacking) and runs
    the same destination-passing direct entry."""
    del activation  # gate parity is enforced by the harness for timed rows
    group_norm_silu_baseline_into(
        x, norm.weight, norm.bias, int(norm.num_groups), float(norm.eps), out
    )


__all__ = [
    "group_norm_silu_baseline",
    "group_norm_silu_baseline_apply",
    "group_norm_silu_baseline_into",
    "group_norm_silu_baseline_apply_into",
    "triton_path_active",
    "uses_chunked_path",
]
