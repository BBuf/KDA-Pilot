"""Destination-passing launcher for the copied SGLang Triton baseline.

Faithful port of the upstream public wrapper ``fused_causal_conv3d_cat_pad``
(SGLang main @ 67b2a9ed0cfba8ec625d3f26548e502646fd914d) with exactly one
behavioral change, mirrored by the candidate ABI: the output tensor is provided
by the caller (passed last) instead of being allocated with ``torch.empty``
inside the call. All upstream validation, the ``depth_left -= cache_t``
adjustment, the output-shape computation, ``block_size``, the grid, the device
context, and the exact kernel arguments are preserved verbatim so the benchmark
times the upstream implementation's real per-call cost.

Calls only the copied Triton kernel in ``baseline/causal_conv3d_pad_triton.py``;
no ``sglang`` import anywhere in the runtime path.
"""

from __future__ import annotations

import torch
import triton  # type: ignore

from .causal_conv3d_pad_triton import _fused_cat_pad_5d_kernel


def fused_causal_conv3d_cat_pad(
    x: torch.Tensor,
    cache_x: torch.Tensor,
    padding,
    output: torch.Tensor,
) -> None:
    width_left, width_right, height_top, height_bottom, depth_left, depth_right = padding
    depth_left -= cache_x.shape[2]
    assert depth_left >= 0
    assert depth_right == 0
    assert width_left == width_right
    assert height_top == height_bottom

    # The upstream kernel reads x/cache with hardcoded C-contiguous stride
    # formulas, so it is only correct for contiguous inputs. Normalize here so the
    # standalone A/B comparison is well-defined for the non-contiguous regression
    # row; this is a no-op for the contiguous production workloads.
    x = x.contiguous()
    cache_x = cache_x.contiguous()

    bsz, channels, t_size, h_size, w_size = x.shape
    cache_t = cache_x.shape[2]
    expected_shape = (
        bsz,
        channels,
        t_size + cache_t + depth_left + depth_right,
        h_size + height_top + height_bottom,
        w_size + width_left + width_right,
    )
    assert tuple(output.shape) == expected_shape, (
        f"output shape {tuple(output.shape)} != expected {expected_shape}"
    )
    assert output.dtype == x.dtype
    assert output.device == x.device
    assert output.is_contiguous()

    block_size = 256
    total = output.numel()
    if total == 0:
        return
    grid = (triton.cdiv(total, block_size),)
    with torch.get_device_module().device(x.device):
        _fused_cat_pad_5d_kernel[grid](
            x,
            cache_x,
            output,
            total,
            channels,
            t_size,
            h_size,
            w_size,
            cache_t,
            output.shape[2],
            output.shape[3],
            output.shape[4],
            depth_left,
            height_top,
            width_left,
            block_size,
        )
