"""kda_kernels.diffusion.group_norm_silu — CUDA-only KDA-optimized overlay.

This package contributes the following swap functions:

  - `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu`
  - `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu`

Stub status: each function is either re-exported from SGLang
(`KDA_OPTIMIZED_<fn> = False`) or routed through the generated
architecture dispatcher (`KDA_OPTIMIZED_<fn> = True`). Promotion is
driven by `scripts/export_kda_kernels/export.py <task-slug>`.
"""

from kda_kernels.diffusion.group_norm_silu._dispatcher import _preload_kda_impls  # noqa: F401
from kda_kernels.diffusion.group_norm_silu._dispatcher import triton_group_norm_silu  # noqa: F401
from kda_kernels.diffusion.group_norm_silu._dispatcher import apply_group_norm_silu  # noqa: F401

KDA_OPTIMIZED_triton_group_norm_silu = True
KDA_OPTIMIZED_apply_group_norm_silu = True

# Source lineage (machine-readable detail in _impls/h200/KDA_EXPORTS.json):
#   KDA_COMMIT_*             = the kernel-pilot git HEAD when the export tool ran (the source
#                             tree the export was generated against). The exported task src/ in
#                             this package is committed in the kernel-pilot commit that introduces
#                             this package update -- typically the immediate SUCCESSOR of this
#                             stamp -- so the stamp identifies the generation point, not a commit
#                             whose tree byte-matches this package.
#   KDA_BENCHMARKED_COMMIT_* = the reproducibility anchor for the perf claim: group_norm_silu.cuh is
#                             byte-identical from 53a6fd2de onward and the canonical benchmark.csv
#                             (geomean 1.4487x, v5-dispatch-final, ion8-h200 GPU7) was produced at
#                             this commit; only the wrapper/validation/metadata changed afterward.
KDA_BENCHMARKED_COMMIT_triton_group_norm_silu = '4b2a6c258e9115e019daaf33add3024ef5479867'
KDA_BENCHMARKED_COMMIT_apply_group_norm_silu = '4b2a6c258e9115e019daaf33add3024ef5479867'

KDA_ARCHES_triton_group_norm_silu = ('h200',)
KDA_TASK_triton_group_norm_silu = 'h200_diffusion_group_norm_silu__multi_shape'
KDA_COMMIT_triton_group_norm_silu = '187b4578141a34938bef1dc47cebf150d8b0fab0'
KDA_DATE_triton_group_norm_silu = '2026-06-02'
KDA_SPEEDUP_triton_group_norm_silu = '1.4487x'
KDA_ARCHES_apply_group_norm_silu = ('h200',)
KDA_TASK_apply_group_norm_silu = 'h200_diffusion_group_norm_silu__multi_shape'
KDA_COMMIT_apply_group_norm_silu = '187b4578141a34938bef1dc47cebf150d8b0fab0'
KDA_DATE_apply_group_norm_silu = '2026-06-02'
KDA_SPEEDUP_apply_group_norm_silu = '1.4487x'
