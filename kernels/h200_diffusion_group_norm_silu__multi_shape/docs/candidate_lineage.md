# Candidate Lineage

The candidate seeds from this repository's own prior art: the kernel promoted
for this task family in PR #21 (repo commit `02b54f9f2`, merged 2026-06-02,
geomean 1.4487x under the since-deleted `kda_kernels`/sglang-jit contract).
That number is prior art, not evidence under the current standalone contract;
this round re-validates everything against a freshly locked baseline.

## Source mapping

| This round | Prior round (recover via `git show 02b54f9f2:<path>`) |
|---|---|
| `solution/kernel.cu` device code (`gns_one_pass_kernel`, `gns_stats_kernel`, `gns_finalize_kernel`, `gns_apply_kernel`, `accumulate_stats`, `apply_affine_silu`, `block_reduce2`, `siluf`) | `kernels/h200_diffusion_group_norm_silu__multi_shape/src/group_norm_silu.cuh` (`GroupNormSiluKernel<DType,kUsePDL>::run` / `run_large` and the same-named device functions) |
| `solution/binding.py` dispatch (small/large threshold `1<<16`, chunk 8192, per-call fp32 scratch) | `src/group_norm_dispatch.py` (`_LARGE_THRESH`, `_CHUNK_ELEMS`, scratch allocation) |

## What changed for the standalone rebuild

- **Header stack replaced.** The prior kernel included six `sgl_kernel/*`
  headers (`tensor.h`, `runtime.cuh`, `type.cuh`, `utils.cuh`, `vec.cuh`,
  `warp.cuh`). `solution/kernel.cu` carries small local equivalents instead:
  `Pack<T,N>` (16-byte aligned vector with load/store), `warp_reduce_sum`
  (butterfly shuffle, full-mask-safe sub-warp width), `to_f32`/`from_f32`
  dtype casts, `expf`/`rsqrtf`/`fmaxf` for the `math::*` wrappers, and
  hand-rolled host-side TensorView validation replacing
  `TensorMatcher`/`SymbolicSize`/`RuntimeCheck`.
- **Build path replaced.** Previously built through
  `sglang.jit_kernel.utils.load_jit` (sglang's jit/tvm-ffi stack); now a
  direct `nvcc -shared` build in `solution/binding.py` loaded with
  `tvm_ffi.load_module`, exporting `gns_candidate_small` /
  `gns_candidate_large` via `TVM_FFI_DLL_EXPORT_TYPED_FUNC`. Launches stay on
  `at::cuda::getCurrentCUDAStream()`.
- **PDL removed.** The prior template parameter `kUsePDL` was compiled `false`
  (and the copied Triton baseline has no comparable PDL path, so the rules
  exclude PDL from the comparison); the dead branches are dropped.
- **Dispatch policy (DEC-1, then amended by the promotion decision
  DEC-6).** The round began all-CUDA on every timed row (DEC-1): a new
  register-lean giant pipeline replaced the prior round's baseline fallback
  and took the giant bucket from 0.76 to 0.94-0.99 geomean. After bounded
  NCU-driven attempts left a 3-6% gap only where the baseline's chunked
  kernels run straddle-free near peak HBM, the user-approved DEC-6 dispatch
  routes those two measured regimes to the LOCAL copied baseline (rules and
  per-regime evidence in docs/dispatch.md). Unsupported layouts take a
  solution-internal normalize-and-run path.
- **fp32 coverage added.** The prior production dispatcher gated to
  fp16/bf16; the standalone candidate compiles and dispatches fp16, bf16 and
  fp32 (`Pack` width 4) so the full correctness contract runs through
  solution code.
- **Device code otherwise verbatim.** Reduction order, chunking (8192),
  block size (256), the one-channel affine fast path, biased variance with
  clamp, and the sigmoid form `z/(1+exp(-z))` are unchanged, so the prior
  round's numerics carry over.
