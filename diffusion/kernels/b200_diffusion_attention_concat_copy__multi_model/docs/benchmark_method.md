# Benchmark Method — b200_diffusion_attention_concat_copy__multi_model

## Harness
- `bench/benchmark.py` starts from `diffusion/docs/standalone_diffusion_benchmark_template.py` (the required standalone timing harness). Settings come from `config.toml` `[benchmark]`: `warmup_runs=10`, `iterations=200`, `num_trials=7`, `inner_iterations_min=1`, `inner_iterations_max=2048`, `target_sample_us=1000`, `timeout_seconds=900`, `use_isolated_runner=true`, `required_matched_ratio=1.0`.
- Only deviation from the verbatim template: the argparse defaults for `--inner-iterations-max` and `--timeout-seconds` are set to this task's `config.toml` caps (`2048`, `900`) instead of the template's generic `4096`/`600`, so a default invocation is config-compliant. Timing/scoring logic is unchanged. All documented commands also pass these values explicitly.
- Primary GPU time from CUDA events; interleaved A/B sampling per trial; inner-loop amplification until each event sample is ≳ `target_sample_us` or the inner cap is hit.
- Correctness (`bench/correctness.py`) runs before any timing and poisons output buffers.

## ABI Interpretation (single exported selector function)
Both baseline and candidate are driven through ONE exported function with the SAME signature (destination-passing, output last). The three op types are facets of one memory-movement pattern, and `config.toml` declares a single entry point per side, so a selector ABI (not per-op exports) is used.

Candidate (CUDA / TVM-FFI), `solution/kernel.cu`:
```cpp
void attention_concat_copy_candidate(
    int64_t op_type,                              // 0=copy_contiguous 1=concat_sequence 2=slice_heads_then_concat
    int64_t order,                                // 0=[a,b]  1=[b,a]  (sequence-dim concat order)
    int64_t h_start,                              // head-slice start (= sp_rank * h_local); slice op only
    int64_t h_local,                              // local head count kept from the full-head prefix; slice op only
    tvm::ffi::TensorView source_a,                // copy: src; concat: A; slice: full-head prefix [B,P,h_full,D]
    tvm::ffi::Optional<tvm::ffi::TensorView> source_b,   // concat: B; slice: shard [B,S,h_local,D]; copy: none
    tvm::ffi::Optional<tvm::ffi::TensorView> scratch,    // slice (baseline only): prefix-contiguous buffer; candidate ignores
    tvm::ffi::TensorView output);                 // preallocated destination
TVM_FFI_DLL_EXPORT_TYPED_FUNC(attention_concat_copy_candidate, attention_concat_copy_candidate);
```

Baseline (PyTorch / ATen), `baseline/binding.py::attention_concat_copy_baseline` — identical positional signature.

Selector constants (shared verbatim across `baseline/binding.py`, `bench/adapter.py`, `solution/kernel.cu`):
`OP_COPY_CONTIGUOUS=0`, `OP_CONCAT_SEQUENCE=1`, `OP_SLICE_HEADS_THEN_CONCAT=2`; `ORDER_AB=0`, `ORDER_BA=1`.

The `scratch` slot is included so the baseline can materialize the intermediate head-sliced prefix `.contiguous()` into a preallocated buffer (no allocation in the timed path). The candidate ignores `scratch` — its whole point is to write the output once without the intermediate prefix materialization.

## config.toml baseline_entry_point override
`config.toml` declares `baseline_entry_point = "baseline/kernel.cu::attention_concat_copy_baseline"` (the CUDA-baseline template default). The upstream USPAttention memory movement is **PyTorch/ATen**, not a CUDA kernel, so per `standalone_diffusion_benchmark.md` (Python-baseline rule) and the established sibling-task convention this is overridden to:

- Effective baseline entry: `baseline/binding.py::attention_concat_copy_baseline`
- Effective candidate entry: `solution/kernel.cu::attention_concat_copy_candidate` (unchanged)

Both sides are invoked through `bench/adapter.py` `call_baseline`/`call_candidate`, which pre-resolve their handles at import time so wrapper overhead is symmetric. The headline baseline is therefore the real ATen `copy_`/`CatArrayBatchedCopy` cost, not a strawman naive CUDA transcription.

## Timed-Path Policy
- `output` and (for slice rows) `scratch` are preallocated in `make_case`, outside the timed region.
- The timed region contains only the `call_baseline` / `call_candidate` op invocation.
- Input generation, layout/stride construction, JIT build, imports, and allocation are excluded from timing.
- Every launch uses PyTorch's current CUDA stream (`at::cuda::getCurrentCUDAStream()` on the candidate; ATen ops on the baseline use the current stream by default).

## Numerics Policy
- These ops are lossless memory movement (copy / slice / concat do not change values). The correctness oracle is **bit-exact**: `atol=0`, `rtol=0`.
- NaN/Inf inputs must be copied through bit-for-bit (value-preserving), not rejected. Output buffers are poisoned with a distinctive sentinel before each correctness run and must be fully overwritten; a skipped/partial launch is caught by a negative-control self-test.
- `bench/correctness.py` compares against an independent PyTorch indexing/contiguous/cat oracle on the same dtype, and cross-checks candidate vs baseline.

## Compile / Build Flags
- Build via `tvm_ffi.cpp.load` (matching the sibling-task convention), with include/library paths from `torch.utils.cpp_extension`. Gencode `sm_100` (B200), detected at runtime from `torch.cuda.get_device_capability()`.
- `-O3`, `-std=c++17` (or `c++20`), `--expt-relaxed-constexpr`; optional `-lineinfo` for NCU source attribution (no codegen change). **No `--use_fast_math`** (the PyTorch baseline does not use it; these are integer-addressed memory copies with no float math anyway).
- The baseline is plain ATen (no nvcc flags). Both sides go through the same `bench/adapter.py` call layer.
- (Exact final flag list is pinned at remote build time and recorded here.)

## Validity Gates
- A/A check: baseline-vs-baseline geomean must be ≈ 1.0 (harness sanity).
- GPU discipline: B200 (`ion-b200`), idle card selected, `REMOTE_GPU_ID` constant across baseline/candidate/correctness/profile; before/after idle state recorded in `docs/run_log.md`.
- Correctness is a hard prerequisite: any missing/failed row invalidates the benchmark.

## Scoring and Promotion Gate
- Per-row speedup = `baseline_median_us / candidate_median_us`.
- Headline = equal-weight geometric mean over `production` rows; arithmetic mean reported as a secondary metric.
- Promotion: candidate geomean `> 1.0` with `required_matched_ratio=1.0` (all production rows bit-exact), OR an evidence-backed no-go (frozen baseline numbers, ≥1 reasoned candidate, per-op bytes/bandwidth roofline, NCU where non-obvious, named bound). The draft's profiled millisecond figures are descriptive motivation, not acceptance thresholds.

## Run Protocol (remote)
- To be recorded in `docs/run_log.md` per session: host, container, workspace path, toolchain versions, selected GPU id/model, idle-before/after, and exact commands for correctness, freeze, benchmark, and summary.
