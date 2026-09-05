"""SM120 FP8 streaming projections for Qwen3.8 decode and verify."""

from __future__ import annotations

import torch

from cutlass_fp8 import fp8_m1 as _fp8_m1
from cutlass_fp8 import fp8_m9 as _fp8_m9
from fp8_ext import fp8_gemv as _fp8_gemv_cuda
from fp8_ext import fp8_quantize as _fp8_quantize_cuda


def fp8_gemv(
    x_fp8: torch.Tensor,
    w_fp8: torch.Tensor,
    alpha: torch.Tensor,
) -> torch.Tensor:
    """Compute ``x @ w.T * alpha`` with the bandwidth-tuned decode path."""

    output = torch.empty(
        (1, w_fp8.shape[0]), dtype=torch.bfloat16, device=x_fp8.device
    )
    if w_fp8.shape[0] == 16384:
        _fp8_m1(output, x_fp8, w_fp8, alpha)
    else:
        _fp8_gemv_cuda(output, x_fp8, w_fp8, alpha)
    return output


def fp8_linear(
    input: torch.Tensor,
    weight: torch.Tensor,
    weight_scale: torch.Tensor,
    input_scale: torch.Tensor,
) -> torch.Tensor:
    """Quantize nine verify tokens and reuse each streamed weight across them."""

    rows, inner = input.shape
    columns = weight.shape[1]
    quantized_bytes = rows * inner
    storage = torch.empty(
        quantized_bytes + 2 * rows * columns,
        dtype=torch.uint8,
        device=input.device,
    )
    quantized = storage[:quantized_bytes].view(torch.float8_e4m3fn).view_as(input)
    output = storage[quantized_bytes:].view(torch.bfloat16).view(rows, columns)
    _fp8_quantize_cuda(quantized, input, input_scale, weight)
    _fp8_m9(output, quantized, weight, input_scale, weight_scale)
    return output


OPS = {
    "qwen38_fp8_gemv": fp8_gemv,
    "qwen38_fp8_linear": fp8_linear,
}
