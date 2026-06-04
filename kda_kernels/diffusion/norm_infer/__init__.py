"""kda_kernels.diffusion.norm_infer — CUDA-only KDA-optimized overlay.

This package contributes the following swap functions:

  - `sglang.jit_kernel.diffusion.triton.norm:norm_infer`
  - `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm`

Stub status: each function is either re-exported from SGLang
(`KDA_OPTIMIZED_<fn> = False`) or routed through the generated
architecture dispatcher (`KDA_OPTIMIZED_<fn> = True`). Promotion is
driven by `scripts/export_kda_kernels/export.py <task-slug>`.
"""

from kda_kernels.diffusion.norm_infer._dispatcher import _preload_kda_impls  # noqa: F401
from kda_kernels.diffusion.norm_infer._dispatcher import norm_infer  # noqa: F401
from kda_kernels.diffusion.norm_infer._dispatcher import triton_one_pass_rms_norm  # noqa: F401

KDA_OPTIMIZED_norm_infer = True
KDA_OPTIMIZED_triton_one_pass_rms_norm = True

KDA_ARCHES_norm_infer = ('h200',)
KDA_TASK_norm_infer = 'h200_diffusion_norm_infer__multi_shape'
KDA_COMMIT_norm_infer = '76cd0a0de3ed29306d774ebc9921359e2d573974'
KDA_DATE_norm_infer = '2026-06-04'
KDA_SPEEDUP_norm_infer = '1.4458x'
KDA_ARCHES_triton_one_pass_rms_norm = ('h200',)
KDA_TASK_triton_one_pass_rms_norm = 'h200_diffusion_norm_infer__multi_shape'
KDA_COMMIT_triton_one_pass_rms_norm = '76cd0a0de3ed29306d774ebc9921359e2d573974'
KDA_DATE_triton_one_pass_rms_norm = '2026-06-04'
KDA_SPEEDUP_triton_one_pass_rms_norm = '1.4458x'
