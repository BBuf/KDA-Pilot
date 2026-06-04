# Baseline Source Provenance

## Upstream

- Project: SGLang — https://github.com/sgl-project/sglang
- Pinned checkout: container `sglang_bbuf` on `ion8-h200`,
  `/home/sglang-omni/bbuf/repos/sglang`, HEAD `84e1108312` (branch `main`,
  clean tree at copy time, 2026-06-04).
- Locked-baseline equivalence: `git diff c47f0e7cd..84e1108312` is EMPTY for
  `python/sglang/jit_kernel/diffusion/triton/norm.py`,
  `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py`, and
  `python/sglang/srt/utils/custom_op.py` — the copied baseline is byte-identical
  to the locked baseline commit `c47f0e7cd` (see `docs/baseline_locked.json`).
  The only drifted file among the audited four is `python/sglang/jit_kernel/utils.py`
  (+7/−1: `is_musa_runtime()` guard in `is_arch_support_pdl()`, inert on CUDA H200).

## Copied files

| Local path | Upstream path | Copy mechanism |
|---|---|---|
| `baseline/upstream/norm.py` | `python/sglang/jit_kernel/diffusion/triton/norm.py` | `git archive HEAD` (pristine) |
| `baseline/upstream/rmsnorm_onepass.py` | `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` | `git archive HEAD` (pristine) |
| `baseline/triton_norm_baseline.py` | derived from the two files above | manual copy, edits below |

## Local edits in `baseline/triton_norm_baseline.py`

- Removed sglang-internal imports and platform overrides
  (`register_custom_op`, `current_platform`, `debug_kernel_api`, MPS/CPU
  fallback rebinding): the copy is CUDA-only and intentionally carries no
  registration layer so the local A/B legs share an identical host topology.
  The registration-preserving comparison is performed at the in-SGLang
  dispatch-symmetric arbiter step instead (see the plan, AC-6).
- Kept only the two inference entry points used by this task:
  `baseline_norm_infer` (verbatim body of `norm_infer`) and
  `baseline_one_pass_rms_norm` (verbatim body of the registered
  `_triton_one_pass_rms_norm_cuda`; upstream's public
  `triton_one_pass_rms_norm` is a thin pass-through to it).
- Renamed with a `baseline_` prefix; Triton kernels copied verbatim
  (`_norm_infer_kernel`, `_rms_norm_tiled_onepass`).
- Dropped the unused flash-attn-derived autotune kernels from `norm.py`
  (only `norm_infer`'s code path is exercised by this task).

## Why a copy exists

The task rules forbid patching/monkey-patching/installing into an SGLang
checkout during loop-time correctness/benchmark runs. The copied baseline gives
the symmetric local harness (`benchmark_symmetric.py`) a baseline leg with the
same host topology class as the candidate leg (plain local callable, fresh
output allocation, no custom-op layer on either side), keeping loop-round
numbers decomposable and predictive of the in-tree result.
