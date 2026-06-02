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

# Source lineage (machine-readable detail in _impls/h200/KDA_EXPORTS.json):
#   KDA_COMMIT_*             = the kernel-pilot git HEAD when the export tool ran (the source
#                             tree the export was generated against). The exported task src/ in
#                             this package is committed in the kernel-pilot commit that introduces
#                             this package update -- typically the immediate SUCCESSOR of this
#                             stamp -- so the stamp identifies the generation point, not a commit
#                             whose tree byte-matches this package.
#   KDA_BENCHMARKED_COMMIT_* = the reproducibility anchor for the perf claim: the candidate
#                             kernels (rms_norm_d128.cuh, layer_norm_n5120.cuh) are byte-identical
#                             from 149392da2 onward, so the geomean reproduces from any commit since.
KDA_BENCHMARKED_COMMIT_norm_infer = 'b9dcb121ea4c9a1eaf153442548972f5da4704f1'
KDA_BENCHMARKED_COMMIT_triton_one_pass_rms_norm = 'b9dcb121ea4c9a1eaf153442548972f5da4704f1'

KDA_ARCHES_norm_infer = ('h200',)
KDA_TASK_norm_infer = 'h200_diffusion_norm_infer__multi_shape'
KDA_COMMIT_norm_infer = '613f780dd77eb5356379bfbd43c3f96009b4ca6f'
KDA_DATE_norm_infer = '2026-06-02'
KDA_SPEEDUP_norm_infer = '1.4223x'
KDA_ARCHES_triton_one_pass_rms_norm = ('h200',)
KDA_TASK_triton_one_pass_rms_norm = 'h200_diffusion_norm_infer__multi_shape'
KDA_COMMIT_triton_one_pass_rms_norm = '613f780dd77eb5356379bfbd43c3f96009b4ca6f'
KDA_DATE_triton_one_pass_rms_norm = '2026-06-02'
KDA_SPEEDUP_triton_one_pass_rms_norm = '1.4223x'
