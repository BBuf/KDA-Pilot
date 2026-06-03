# Standalone Diffusion Benchmark Contract

This repository optimizes SGLang diffusion kernels without interacting with an
SGLang checkout at benchmark runtime. SGLang is only a source-code provider for
the local baseline.

## Hard Rules

- Do not patch, import, monkey-patch, or install into SGLang during correctness
  or benchmark runs.
- Copy the relevant upstream SGLang kernel source into `baseline/` before
  implementing the candidate. Record the upstream repository URL, commit, and
  copied file list in `docs/baseline_source.md`.
- Baseline and candidate must expose matching local entry points. Any wrapper
  overhead included for one side must be included for the other side.
- Prefer AKO4X-style CUDA direct export for both sides:
  `TVM_FFI_DLL_EXPORT_TYPED_FUNC`, `tvm::ffi::TensorView` arguments, output
  tensors passed last, and `destination_passing_style = true`.
- Every CUDA launch must use PyTorch's current stream:
  `at::cuda::getCurrentCUDAStream()`.
- If the copied SGLang implementation is Triton, CuTe DSL, or Python, keep it
  local and build a local baseline adapter with the same benchmark ABI used by
  the candidate. The benchmark must not compare a heavy Python wrapper against a
  lean CUDA wrapper.
- Workloads are frozen before tuning. Changing workloads, tolerances, scoring,
  or benchmark timing rules requires deleting old results and remeasuring both
  baseline and candidate.
- Diffusion workloads must be audited against
  `docs/diffusion_benchmark_shape_coverage.md` and the current
  `sglang-diffusion-benchmark-profile/benchmark-and-profile.md` presets before
  any optimization work starts.

## Required Directory Contents After First Agent Milestone

```text
baseline/
  copied upstream source files
  kernel.cu or binding.py exposing the baseline ABI
solution/
  kernel.cu or binding.py exposing the candidate ABI
bench/
  workloads.json
  benchmark.py
  correctness.py
  results.jsonl
docs/
  baseline_source.md
  benchmark_method.md
  run_log.md
config.toml
```

## ABI Pattern

For pure CUDA, use the AKO4X direct-symbol pattern:

```cuda
#include <ATen/cuda/CUDAContext.h>
#include <tvm/ffi/container/tensor.h>

void my_kernel(tvm::ffi::TensorView input, tvm::ffi::TensorView output) {
    cudaStream_t stream = at::cuda::getCurrentCUDAStream();
    // launch <<<grid, block, shmem, stream>>>
}

TVM_FFI_DLL_EXPORT_TYPED_FUNC(my_kernel, my_kernel);
```

The task may use one exported function per upstream public entry point, or a
single exported function with an explicit selector argument. Baseline and
candidate must use the same choice.

## Workload Rules

- `bench/workloads.json` is the source of truth.
- `bench/workloads.json` must be populated from the target task family in
  `docs/diffusion_benchmark_shape_coverage.md` before tuning begins.
- Include every production shape the task is expected to optimize and a small
  regression grid for unsupported layouts/dtypes.
- If a current SGLang diffusion benchmark preset is not represented by retained
  shape rows, either add fresh live capture rows or record a live no-call proof
  in `docs/benchmark_preset_audit.md`.
- Each workload records the function/selector, tensor shapes, dtypes, strides,
  scalar parameters, tolerance, random seed, and whether it is included in the
  headline score.
- Do not silently skip a production workload. Any missing baseline, missing
  candidate, compile failure, runtime failure, or correctness failure makes the
  benchmark invalid.

## Timing Rules

- Run each workload in an isolated subprocess when possible.
- Generate fresh random inputs for each trial; inputs may be stable inside a
  trial but must change between trials.
- Preallocate output tensors before timing. Timed regions must not include input
  generation, Python setup, JIT build, imports, allocation, or data restoration.
- Warm both baseline and candidate before measurement.
- Use CUDA events for GPU time. Use wrapper-inclusive wall-clock only as a
  secondary diagnostic.
- Use inner-loop amplification: record N back-to-back invocations inside one
  event pair and divide by N. Increase N until the sample is at least about
  1000 us or N reaches the configured cap.
- Use interleaved A/B sampling per trial to cancel clock and thermal drift:
  baseline, candidate, baseline, candidate, or the reverse order selected by a
  deterministic seed.
- Report median, mean, std, min, p10, p90 for both sides on every workload.
- Primary speedup per workload is `baseline_median_us / candidate_median_us`.
- Primary headline is equal-weight geometric mean over all production workloads.
  Also report arithmetic mean as a secondary tracking metric.

Recommended defaults:

```toml
[benchmark]
warmup_runs = 10
iterations = 200
num_trials = 7
inner_iterations_min = 1
inner_iterations_max = 4096
target_sample_us = 1000
timeout_seconds = 600
use_isolated_runner = true
```

## Correctness Rules

- Compare candidate and baseline against an independent PyTorch/math oracle when
  practical. If a full oracle is expensive, at minimum compare candidate against
  the copied baseline plus targeted oracle rows.
- Check shapes, dtypes, NaN/Inf, and tolerance per output.
- Poison output buffers before each correctness run so stale-output and skipped
  kernel bugs are visible.
- If CUDA graph capture is used, add zero-output replay, poison-cell, and
  varying-input checks to prove kernels actually replay.
- Fallback behavior must be explicit and tested. If candidate falls back to the
  copied baseline for some supported workload, that workload still counts in the
  headline score.

## Provenance

Every benchmark result must record:

- task slug and target GPU
- upstream baseline commit and copied files
- candidate source hash
- exact command
- CUDA, PyTorch, compiler, and TVM-FFI versions
- GPU model, GPU id, and idle state before/after
- workload count and trial/iteration/inner-loop settings
- correctness summary

Do not keep benchmark numbers without this provenance.
