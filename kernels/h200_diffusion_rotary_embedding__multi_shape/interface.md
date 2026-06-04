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
- Built through SGLang `jit_kernel`: `src/wrapper.py` drives `load_jit` + `make_cpp_args` + `cache_once` (`cuda_files=[str(_WORKSPACE_CUH)]` — the absolute path to `src/csrc/rotary_embedding.cuh`, compiled in place so nothing is written into the SGLang checkout; `cuda_wrappers=[("standard_rope", "StandardRopeKernel<bf16_t>::run"), ("ltx2_split_rope", "Ltx2SplitRopeKernel<bf16_t>::run")]`). Compile flags match the SGLang jit build (`-DSGL_CUDA_ARCH=900 -std=c++20 -O3 --expt-relaxed-constexpr`); **no `--use_fast_math`**. Profiling builds add `-lineinfo` only (`KDA_PROFILE=1`).
- Design: one block per token (standard) / per `(b,s)` (LTX-2); power-of-2 shift/mask indexing (no runtime div/mod); 128-bit vectorized bf16 loads/stores; standard cos/sin reused per token via shared memory; v3 adds streaming-cache accesses (`__ldcs`/`__stcs`, evict-first) on every read-once/write-once global stream (pattern: KernelWiki `technique-vectorized-loads`).

## Per-shape dispatch table
See `docs/dispatch.md`. All 6 deduplicated production buckets are promoted to the CUDA route (faster than baseline). Everything else falls back.

## Fallback cases (non-recursive: CUDA → captured SGLang baseline → PyTorch reference)
fp16; `interleaved=True`; 3D standard input; non-production head sizes; non-bf16 LTX-2; non-captured LTX-2 `S`/`B`/`num_heads`/`half`; contiguous LTX-2 cos/sin; CPU tensors / device mismatch (raises like the baseline). The baseline is captured at import (never resolves to our wrapper).

## Tolerance methodology
Oracle = SGLang diffusion triton baselines pinned at HEAD `6965fe0ee` (the remote `c47f0e7cd` checkout's `rotary.py`/`ltx2_rotary.py` are sha1-verified byte-identical: `81fb5ff…`/`3408d90…`), cross-checked vs a PyTorch FP32 reference (`src/reference.py`) that reproduces the standard adjacent-pair fp32 math (round only on store) and the LTX-2 `(x*cos)->bf16` intermediate rounding over the captured non-contiguous strides. Pass = candidate within a dynamic bf16-noise bound (`err ≤ 3× ‖ref_bf16 − ref_fp32‖`, plus `1e-2` abs/rel) and NaN/Inf-free, on all 6 shapes; supported cases must take the `"cuda"` route.

## Benchmark command + latency formula
`CUDA_VISIBLE_DEVICES=<idle> PYTHONPATH=<sglang>/python python benchmark.py --mode both --device-batch 10` inside the `sglang_bbuf` container on an idle H200. Legacy mode: sequential per-shape median/mean/std/min/p10/p90 (µs), warmup 25 / iters 100, allocation included on both paths, register module cached. Interleaved mode (the shipping-symmetric evidence): same-process alternating A/B wall samples plus pipelined CUDA-event device-only timing and a DEVICE-vs-HOST decomposition (`wall_speedup`, `device_speedup`, host residuals) per shape. Headline = geometric mean of per-shape median-latency wall speedups over the 6 deduplicated shapes; device numbers are diagnostic (small-LTX-2 baseline event timings carry launch starvation — NCU kernel time is the arbiter there). Auto provenance: torch/CUDA/Triton versions, imported SGLang HEAD, rotary file sha1 vs the pinned oracle.

## Final result (v3 continuation, 2026-06-04)
Correct on all 6 shapes (CUDA route) with `native_cuda_v3_streamcache`. **Interleaved wall geomean 1.2977× (legacy-mode 1.2775×)** vs the autotuned SGLang Triton baseline on `ion-h200-8` GPU 0, SGLang `84e110831` (≡ pin `6965fe0ee`); per-shape wall 1.168×–1.497×. Decomposition: std is a real kernel win (NCU 153.5→89.4µs, 1.72×); `ltx2 S6144 h64` is kernel-parity (NCU 0.98×) with a host-path wall win (kept per the re-measure rule, labeled host); `S6144 h32` small kernel win (NCU 1.04×) + host; the three small LTX-2 buckets win on wall (1.24–1.35×) purely via the cheaper host path while Triton's kernels are faster kernel-only (queued: small-S grid undersubscription). Active bound = HBM memory bandwidth (74–76% DRAM, 81–88% of roofline) — near the attainable bound (`profile/ncu_v3_20260604/REPORT.md`). In-SGLang drop-in re-verified (`EXPORT_TEST: PASS`, smoke geomean 1.228×). Prior-round v2 result (1.296× wall on GPU 7) preserved in `benchmark.csv` history and `profile/ncu_v2_20260602_065439/`.

## Source lineage
- Launcher / `host::TensorMatcher` / `host::LaunchKernel` / `SymbolicSize` pattern mirrored from `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`.
- `AlignedVector`/`packed_t`/`load_as`/`store_as`/`device::cast` from `sgl_kernel/{type,utils,vec}.cuh`.
- `load_jit`/`make_cpp_args`/`cache_once`/`is_arch_support_pdl` from `sglang.jit_kernel.utils`.

## Export path (AC-8)
The `.cuh` compiles in place from its absolute workspace path via `load_jit` (`cuda_files=[<abs path to rotary_embedding.cuh>]`); pathlib keeps the absolute path as-is so nothing is written into the SGLang checkout, and the `sgl_kernel` headers still resolve through `load_jit`'s default include dirs. The promoted `kda_kernels` overlay builds the same way from its own `_impls/<arch>/csrc/`. In-SGLang drop-in replacement + smoke benchmark + fallback recorded in `docs/sglang_jit_export.md`.
