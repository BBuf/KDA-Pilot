# Interface: h200_diffusion_rotary_embedding__multi_shape

- Kernel slug: `h200_diffusion_rotary_embedding__multi_shape`
- Op type: `rotary_embedding`
- Target GPU: NVIDIA H200 (Hopper, SM90)
- Wrapped SGLang entry points (public names preserved):
  - `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`
  - `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb`

## Final wrapper signatures (functional; return a new tensor; never mutate inputs)
- `apply_rotary_embedding(x, cos, sin, interleaved=False) -> Tensor` — standard adjacent-pair RoPE. x `(B,T,H,D)`/`(T,H,D)`; cos/sin `(T, D/2)` fp32.
- `apply_ltx2_split_rotary_emb(x, cos, sin) -> Tensor` — LTX-2 split-half. x `(B,S,H*2*half)` bf16; cos/sin `(B,H,S,half)` bf16, possibly non-contiguous.
- `optimized_wrapper(*args, **kwargs)` — compatibility entry: dispatches by `cos.dim()` (2D→standard, 4D→LTX-2).

`src/register.py` exposes `EXPORTS = {"apply_rotary_embedding": ..., "apply_ltx2_split_rotary_emb": ...}` + `register()`.

## Native CUDA candidate
- `src/csrc/rotary_embedding.cuh`: `StandardRopeKernel<DType>::run(out,x,cos,sin)` + `Ltx2SplitRopeKernel<DType>::run(out,x,cos,sin)` (templated `XxxKernel<...>::run(tvm::ffi::TensorView...)` launchers).
- Built through SGLang `jit_kernel`: `src/wrapper.py` drives `load_jit` + `make_cpp_args` + `cache_once` (`cuda_files=["diffusion/kda_rotary_embedding.cuh"]`, `cuda_wrappers=[("standard_rope", "StandardRopeKernel<bf16_t>::run"), ("ltx2_split_rope", "Ltx2SplitRopeKernel<bf16_t>::run")]`). Compile flags match the SGLang jit build (`-DSGL_CUDA_ARCH=900 -std=c++20 -O3 --expt-relaxed-constexpr`); **no `--use_fast_math`**. Profiling builds add `-lineinfo` only (`KDA_PROFILE=1`).
- Design: one block per token (standard) / per `(b,s)` (LTX-2); power-of-2 shift/mask indexing (no runtime div/mod); 128-bit vectorized bf16 loads/stores; standard cos/sin reused per token via shared memory.

## Per-shape dispatch table
See `docs/dispatch.md`. All 6 deduplicated production buckets are promoted to the CUDA route (faster than baseline). Everything else falls back.

## Fallback cases (non-recursive: CUDA → captured SGLang baseline → PyTorch reference)
fp16; `interleaved=True`; 3D standard input; non-production head sizes; non-bf16 LTX-2; non-captured LTX-2 `S`/`B`/`num_heads`/`half`; contiguous LTX-2 cos/sin; CPU tensors / device mismatch (raises like the baseline). The baseline is captured at import (never resolves to our wrapper).

## Tolerance methodology
Oracle = SGLang diffusion triton baselines pinned at HEAD `6965fe0ee` (the remote `c47f0e7cd` checkout's `rotary.py`/`ltx2_rotary.py` are sha1-verified byte-identical: `81fb5ff…`/`3408d90…`), cross-checked vs a PyTorch FP32 reference (`src/reference.py`) that reproduces the standard adjacent-pair fp32 math (round only on store) and the LTX-2 `(x*cos)->bf16` intermediate rounding over the captured non-contiguous strides. Pass = candidate within a dynamic bf16-noise bound (`err ≤ 3× ‖ref_bf16 − ref_fp32‖`, plus `1e-2` abs/rel) and NaN/Inf-free, on all 6 shapes; supported cases must take the `"cuda"` route.

## Benchmark command + latency formula
`CUDA_VISIBLE_DEVICES=<idle> PYTHONPATH=<sglang>/python python benchmark.py` inside the `sglang_bbuf` container on an idle H200. Per shape: median/mean/std/min/p10/p90 (µs) for baseline and candidate (warmup 25, iters 100), allocation included on both paths, register module cached. Headline = geometric mean of per-shape median-latency speedups over the 6 deduplicated shapes.

## Final result
Correct on all 6 shapes (CUDA route). **Geomean speedup 1.296× wall-clock (1.297× GPU-kernel)** vs the autotuned SGLang Triton baseline; per-shape 1.123×–1.492× (see `benchmark.csv`). NCU: active bound = HBM memory bandwidth (75–79% DRAM, ~80–90% of the H200 roofline) — near the attainable bound (`profile/ncu_v2_20260602_065439/REPORT.md`).

## Source lineage
- Launcher / `host::TensorMatcher` / `host::LaunchKernel` / `SymbolicSize` pattern mirrored from `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`.
- `AlignedVector`/`packed_t`/`load_as`/`store_as`/`device::cast` from `sgl_kernel/{type,utils,vec}.cuh`.
- `load_jit`/`make_cpp_args`/`cache_once`/`is_arch_support_pdl` from `sglang.jit_kernel.utils`.

## Export path (AC-8)
The `.cuh` compiles in place from its absolute workspace path via `load_jit` (`cuda_files=[<abs path to rotary_embedding.cuh>]`); pathlib keeps the absolute path as-is so nothing is written into the SGLang checkout, and the `sgl_kernel` headers still resolve through `load_jit`'s default include dirs. The promoted `kda_kernels` overlay builds the same way from its own `_impls/<arch>/csrc/`. In-SGLang drop-in replacement + smoke benchmark + fallback recorded in `docs/sglang_jit_export.md`.
