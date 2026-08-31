"""Low-latency BF16 GEMMs for the Kimi-K3 decode path."""

from __future__ import annotations

import functools
from pathlib import Path

import torch
from torch.utils.cpp_extension import load_inline


_CPP_SOURCE = r"""
#include <torch/extension.h>

torch::Tensor tiny_n_cuda(torch::Tensor x, torch::Tensor w);
torch::Tensor tiny_k_cuda(torch::Tensor x, torch::Tensor w);
torch::Tensor fallback_small_k_cuda(torch::Tensor x, torch::Tensor w);
torch::Tensor accurate_linear_cuda(torch::Tensor x, torch::Tensor w);
"""


@functools.lru_cache(maxsize=1)
def _extension():
    cuda_source = Path(__file__).with_name("kernel_cuda.cu").read_text()
    return load_inline(
        name="kda_kimi_k3_tiny_gemm_h200_v451",
        cpp_sources=_CPP_SOURCE,
        cuda_sources=cuda_source,
        functions=[
            "tiny_n_cuda",
            "tiny_k_cuda",
            "fallback_small_k_cuda",
            "accurate_linear_cuda",
        ],
        extra_cflags=("-O3",),
        extra_cuda_cflags=("-O3", "-lineinfo"),
        with_cuda=True,
        verbose=False,
    )


@torch.no_grad()
def run(x: torch.Tensor, w: torch.Tensor, op: int) -> torch.Tensor:
    ext = _extension()
    if op == 1:
        return ext.tiny_n_cuda(x, w)
    if op == 2:
        return ext.tiny_k_cuda(x, w)
    if op != 0:
        raise ValueError(f"unknown op code: {op}")

    m, k = x.shape
    n = w.shape[0]
    if (n, k) == (144, 7168) and 0 < m <= 16:
        return ext.tiny_n_cuda(x, w)
    if (n, k) == (896, 7168) and 0 < m <= 8:
        return ext.tiny_n_cuda(x, w)
    if (n, k) == (1536, 128):
        if 0 < m <= 12:
            return ext.tiny_k_cuda(x, w)
        if 0 < m <= 16:
            return ext.fallback_small_k_cuda(x, w)
    if (n, k) == (144, 7168):
        return ext.accurate_linear_cuda(x, w)

    # Preserve a mathematically accurate fallback for shapes outside the
    # production trace.
    return torch.nn.functional.linear(x.double(), w.double()).to(torch.bfloat16)
