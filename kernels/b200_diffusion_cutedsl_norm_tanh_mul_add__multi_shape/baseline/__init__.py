"""Self-contained copy of the SGLang CuTe-DSL fused norm-tanh-mul-add baseline.

Upstream source: python/sglang/jit_kernel/diffusion/cutedsl/ in sgl-project/sglang
(exact lineage in docs/baseline_source.md). The torch.library.custom_op
registration is stripped: these are the raw kernel callables, exposed through the
same low-overhead local entry ABI as the candidate wrapper so local A/B
comparisons stay symmetric. No sglang import happens at runtime.
"""

from .norm_tanh_mul_add_norm_scale import (
    fused_norm_tanh_mul_add,
    fused_norm_tanh_mul_add_norm_scale,
)

__all__ = [
    "fused_norm_tanh_mul_add",
    "fused_norm_tanh_mul_add_norm_scale",
]
