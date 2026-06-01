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

KDA_ARCHES_fused_inplace_qknorm_rope = ('b200', 'h200')
KDA_TASK_fused_inplace_qknorm_rope = {'b200': 'b200_diffusion_qknorm_rope__multi_shape', 'h200': 'h200_diffusion_qknorm_rope__multi_shape'}
KDA_COMMIT_fused_inplace_qknorm_rope = {'b200': '68e921ceeca306093b55e776ffd0cb256e0e90ae', 'h200': '93ab0645a679bbb2ae4c60fc5bb605a6cbe71ea0'}
KDA_DATE_fused_inplace_qknorm_rope = {'b200': '2026-06-01', 'h200': '2026-06-01'}
KDA_SPEEDUP_fused_inplace_qknorm_rope = {'b200': '1.1113x', 'h200': '~1.11x'}
