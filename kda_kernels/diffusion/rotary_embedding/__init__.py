"""kda_kernels.diffusion.rotary_embedding — CUDA-only KDA-optimized overlay.

This package contributes the following swap functions:

  - `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`
  - `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb`

Stub status: each function is either re-exported from SGLang
(`KDA_OPTIMIZED_<fn> = False`) or pulled from a promoted KDA impl
(`KDA_OPTIMIZED_<fn> = True`). Promotion is driven by
`scripts/export_kda_kernels/export.py <task-slug>`.
"""

from kda_kernels.diffusion.rotary_embedding.wrapper import apply_rotary_embedding  # noqa: F401
from kda_kernels.diffusion.rotary_embedding.wrapper import apply_ltx2_split_rotary_emb  # noqa: F401

KDA_OPTIMIZED_apply_rotary_embedding = True
KDA_OPTIMIZED_apply_ltx2_split_rotary_emb = True

KDA_TASK_apply_rotary_embedding = 'b200_diffusion_rotary_embedding__multi_shape'
KDA_COMMIT_apply_rotary_embedding = 'fb74277933d3d04d6fe48d9f2b4650a52467ab09'
KDA_DATE_apply_rotary_embedding = '2026-05-31'
KDA_SPEEDUP_apply_rotary_embedding = '1.77x (captured hunyuanvideo [1,27030,24,128]); B200, idle-gated'
KDA_TASK_apply_ltx2_split_rotary_emb = 'b200_diffusion_rotary_embedding__multi_shape'
KDA_COMMIT_apply_ltx2_split_rotary_emb = 'fb74277933d3d04d6fe48d9f2b4650a52467ab09'
KDA_DATE_apply_ltx2_split_rotary_emb = '2026-05-31'
KDA_SPEEDUP_apply_ltx2_split_rotary_emb = '1.06-1.54x over 10 captured shapes; all-fn geomean 1.3676x; B200, idle-gated'
