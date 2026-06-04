"""kda_kernels.diffusion.rotary_embedding — CUDA-only KDA-optimized overlay.

This package contributes the following swap functions:

  - `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`
  - `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb`

Stub status: each function is either re-exported from SGLang
(`KDA_OPTIMIZED_<fn> = False`) or routed through the generated
architecture dispatcher (`KDA_OPTIMIZED_<fn> = True`). Promotion is
driven by `scripts/export_kda_kernels/export.py <task-slug>`.
"""

from kda_kernels.diffusion.rotary_embedding._dispatcher import _preload_kda_impls  # noqa: F401
from kda_kernels.diffusion.rotary_embedding._dispatcher import apply_rotary_embedding  # noqa: F401
from kda_kernels.diffusion.rotary_embedding._dispatcher import apply_ltx2_split_rotary_emb  # noqa: F401

KDA_OPTIMIZED_apply_rotary_embedding = True
KDA_OPTIMIZED_apply_ltx2_split_rotary_emb = True

KDA_ARCHES_apply_rotary_embedding = ('b200', 'h200')
KDA_TASK_apply_rotary_embedding = {'b200': 'b200_diffusion_rotary_embedding__multi_shape', 'h200': 'h200_diffusion_rotary_embedding__multi_shape'}
KDA_COMMIT_apply_rotary_embedding = {'b200': 'afb416adff0765da3bf610826631b6d5704d5381', 'h200': '4e4229fd7f442773bf54753a6a3845c077f2f01c'}
KDA_DATE_apply_rotary_embedding = {'b200': '2026-06-04', 'h200': '2026-06-02'}
KDA_SPEEDUP_apply_rotary_embedding = {'b200': '1.466x vs sglang main 8933ec877 (measured geomean over the 11 captured signatures, 3 idle-gated sessions; standard 1.92x, LTX-2 1.00-1.67x; replacement gate vs prior promoted cuda-v4: standard 1.071x)', 'h200': '1.295504x'}
KDA_ARCHES_apply_ltx2_split_rotary_emb = ('b200', 'h200')
KDA_TASK_apply_ltx2_split_rotary_emb = {'b200': 'b200_diffusion_rotary_embedding__multi_shape', 'h200': 'h200_diffusion_rotary_embedding__multi_shape'}
KDA_COMMIT_apply_ltx2_split_rotary_emb = {'b200': 'afb416adff0765da3bf610826631b6d5704d5381', 'h200': '4e4229fd7f442773bf54753a6a3845c077f2f01c'}
KDA_DATE_apply_ltx2_split_rotary_emb = {'b200': '2026-06-04', 'h200': '2026-06-02'}
KDA_SPEEDUP_apply_ltx2_split_rotary_emb = {'b200': '1.466x vs sglang main 8933ec877 (measured geomean over the 11 captured signatures, 3 idle-gated sessions; standard 1.92x, LTX-2 1.00-1.67x; replacement gate vs prior promoted cuda-v4: standard 1.071x)', 'h200': '1.295504x'}
