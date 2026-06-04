"""kda_kernels.diffusion.qknorm_rope — CUDA-only KDA-optimized overlay.

This package contributes the following swap functions:

  - `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope`

Stub status: each function is either re-exported from SGLang
(`KDA_OPTIMIZED_<fn> = False`) or routed through the generated
architecture dispatcher (`KDA_OPTIMIZED_<fn> = True`). Promotion is
driven by `scripts/export_kda_kernels/export.py <task-slug>`.
"""

from kda_kernels.diffusion.qknorm_rope._dispatcher import _preload_kda_impls  # noqa: F401
from kda_kernels.diffusion.qknorm_rope._dispatcher import fused_inplace_qknorm_rope  # noqa: F401

KDA_OPTIMIZED_fused_inplace_qknorm_rope = True

KDA_ARCHES_fused_inplace_qknorm_rope = ('h200',)
KDA_TASK_fused_inplace_qknorm_rope = 'h200_diffusion_qknorm_rope__multi_shape'
KDA_COMMIT_fused_inplace_qknorm_rope = '72fdfaa3b9a8f68db29ca26cfc135af832f7158f'
KDA_DATE_fused_inplace_qknorm_rope = '2026-06-04'
KDA_SPEEDUP_fused_inplace_qknorm_rope = '1.0677x'
