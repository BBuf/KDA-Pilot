# Benchmark Method

## Operator
Fused 5D causal-Conv3D cat/pad copy (`fused_causal_conv3d_cat_pad`): concatenate a
required `cache_x` tensor with `x` along depth (dim=2), then constant-zero F.pad the
trailing W/H/D borders, where the cache consumes the innermost `cache_t` of the
`depth_left` left-depth planes. Pure data movement; no arithmetic.

## ABI (baseline and candidate, matched)
- Destination-passing: the output tensor is the last argument; nothing is allocated in the timed path.
- Baseline: `baseline/binding.py::fused_causal_conv3d_cat_pad(x, cache_x, padding_list, output)` — a faithful destination-passing port of the upstream Triton wrapper that calls only the copied Triton kernel in `baseline/causal_conv3d_pad_triton.py`.
- Candidate: `solution/kernel.cu::causal_conv3d_cat_pad_candidate(x, cache, w_l, w_r, h_t, h_b, d_l, d_r, output)` exported via `TVM_FFI_DLL_EXPORT_TYPED_FUNC`, `tvm::ffi::TensorView` args, launched on `at::cuda::getCurrentCUDAStream()`.
- `bench/adapter.py` routes both sides through thin, allocation-free forwarders so wrapper overhead is equivalent.

## Compile flags (candidate)
- `extra_cflags`: `-std=c++17 -O3`
- `extra_cuda_cflags`: `-std=c++17 -O3 -gencode=arch=compute_XY,code=sm_XY` (XY = device native capability, sm_100 on B200)
- `ldlibs`: `-lc10 -lc10_cuda -ltorch_cpu -ltorch_cuda`
- **No `--use_fast_math`** (the upstream Triton baseline does not use fast math; flags are kept symmetric and cannot change numerics for a pure copy).
- Built via `tvm_ffi.cpp.load` (see `solution/build.py`), the same builder the production jit stack uses.

## Workload freeze policy
- `bench/workloads.json` is the frozen source of truth: 8 bf16 production rows (headline, `production:true`) from `docs/diffusion_benchmark_shape_coverage.md`, plus low-weight regression rows (`production:false`: cache-null, no-pad/cat-only, and any captured non-contiguous rows from `cosmos3-nano-t2v_no_compile_v2.jsonl`).
- Workloads, tolerances, scoring, and timing rules are frozen before tuning. Changing them requires deleting old results and remeasuring both baseline and candidate.

## Comparison policy
- Tolerance is **bitwise exact**: `atol=0, rtol=0`. The op is a pure copy + zero-fill, so baseline, candidate, and the torch oracle (`F.pad(cat([cache,x],dim=2), [...,depth_left-cache_t,depth_right], value=0)`) are bit-identical, and NaN/Inf must be preserved bit-for-bit.
- The benchmark A/B comparison uses `bench/adapter.py::compare_outputs`, which compares raw element bits via an integer view (overriding the template's float-tolerance default that would reject NaN/Inf).
- `bench/correctness.py` is the stronger gate: candidate vs the copied baseline AND vs the independent torch oracle, plus a poison self-test and rejection tests, over production + regression rows.

## Timing rules
- Starts from `docs/standalone_diffusion_benchmark_template.py` (used verbatim as `bench/benchmark.py`).
- CUDA-event GPU time; inner-loop amplification to a >=~1000 us sample; interleaved A/B sampling per trial; fresh per-trial inputs with stable in-trial tensors; outputs preallocated outside timing.
- Reports per-row median/mean/std/min/p10/p90; per-row speedup `baseline_median / candidate_median`; headline = equal-weight geometric mean over production rows.

## Build / run commands (remote B200)
- Build is implicit on first `solution.build.load_candidate_module()` import (cached under `solution/.build`).
- Correctness: `python bench/correctness.py`
- Benchmark: `python bench/benchmark.py --workloads bench/workloads.json --out bench/results.jsonl`

## Baseline provenance
Upstream SGLang `main` @ `67b2a9ed0cfba8ec625d3f26548e502646fd914d` (resolved 2026-06-25T01:28:34Z); see `docs/baseline_source.md`. The resolved commit is frozen at recovery time and is not refreshed after tuning begins.
