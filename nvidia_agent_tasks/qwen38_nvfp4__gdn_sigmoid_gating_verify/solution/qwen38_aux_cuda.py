"""JIT loader for fixed-shape SM120 auxiliary kernels."""

from __future__ import annotations

import os
from pathlib import Path

from torch.utils.cpp_extension import load


os.environ.setdefault("TORCH_CUDA_ARCH_LIST", "12.0")

_EXTENSION = load(
    name="qwen38_gdn_aux_cuda_ext",
    sources=[str(Path(__file__).with_name("qwen38_aux_cuda_ext.cu"))],
    extra_cflags=["-O3"],
    extra_cuda_cflags=["-O3", "-lineinfo"],
    verbose=False,
)

conv1d_t9_w4_pair_fast = _EXTENSION.conv1d_t9_w4_pair_fast
qkvzba_copy_flat_96 = _EXTENSION.qkvzba_copy_flat_96
