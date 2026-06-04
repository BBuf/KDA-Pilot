"""Vendored SGLang CuTe-DSL baseline for the norm-tanh-modulation kernels.

Source: sglang @ 0689ba84b88c991684b0f99ee9b50c3ce485b483
(python/sglang/jit_kernel/diffusion/cutedsl/). See docs/baseline_source.md
for the copied-file list and the exact local edits.
"""

from .norm_tanh_mul_add_norm_scale import (
    fused_norm_tanh_mul_add,
    fused_norm_tanh_mul_add_norm_scale,
)

__all__ = [
    "fused_norm_tanh_mul_add",
    "fused_norm_tanh_mul_add_norm_scale",
]
