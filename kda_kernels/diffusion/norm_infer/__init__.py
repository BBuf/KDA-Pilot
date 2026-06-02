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

# Source lineage (see _impls/h200/KDA_EXPORTS.json for machine-readable detail):
#   KDA_COMMIT_*             = export-source commit (git HEAD at export). The IMPLEMENTATION
#                             files (register.py, wrapper.py, norm_dispatch.py, *.cuh) are
#                             byte-identical to this commit and reproduce from it. The
#                             lineage-metadata files (KDA_EXPORTS.json, KDA_STATUS.md, the
#                             stamps below) were added in a later commit and are NOT
#                             reproduced by this commit.
#   KDA_BENCHMARKED_COMMIT_* = commit the geomean reflects; the candidate kernels are
#                             byte-identical from 149392da2 through the export-source commit.
KDA_BENCHMARKED_COMMIT_norm_infer = 'b9dcb121ea4c9a1eaf153442548972f5da4704f1'
KDA_BENCHMARKED_COMMIT_triton_one_pass_rms_norm = 'b9dcb121ea4c9a1eaf153442548972f5da4704f1'

KDA_ARCHES_norm_infer = ('h200',)
KDA_TASK_norm_infer = 'h200_diffusion_norm_infer__multi_shape'
KDA_COMMIT_norm_infer = '75d4a0ab8fbbaca3ca67b9ca2a979e5078cdd07f'
KDA_DATE_norm_infer = '2026-06-02'
KDA_SPEEDUP_norm_infer = '1.4223x'
KDA_ARCHES_triton_one_pass_rms_norm = ('h200',)
KDA_TASK_triton_one_pass_rms_norm = 'h200_diffusion_norm_infer__multi_shape'
KDA_COMMIT_triton_one_pass_rms_norm = '75d4a0ab8fbbaca3ca67b9ca2a979e5078cdd07f'
KDA_DATE_triton_one_pass_rms_norm = '2026-06-02'
KDA_SPEEDUP_triton_one_pass_rms_norm = '1.4223x'
