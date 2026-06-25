# Benchmark Method

## Harness
`bench/benchmark.py` starts from the repository standalone timing harness
(`../../docs/standalone_diffusion_benchmark_template.py`). The timing/scoring
logic is unchanged; the only deltas are (1) an additive provenance merge in
`_provenance` (it calls the optional `adapter.extra_provenance()` hook), which
does not affect measurement, and (2) `torch.cuda.set_device(args.device)` is
called before the adapter is imported in `_run_one_workload`, so a non-default
`--device` builds/reports the candidate for the intended GPU. It provides
CUDA-event timing, interleaved A/B sampling per trial, inner-loop
amplification toward `target_sample_us`, fresh random inputs per trial,
preallocated + poisoned outputs, the equal-weight geometric-mean headline
(`baseline_median_us / candidate_median_us`), and per-row
median/mean/std/min/p10/p90 with full provenance in `results.jsonl`.

The task-specific `bench/adapter.py` supplies only `make_case`, `call_baseline`,
and `call_candidate`, routed through one shared `_dispatch` so both sides pay
byte-identical adapter overhead. Outputs are preallocated in `make_case`; nothing
is allocated in the timed path. `bench/adapter.py` asserts no `sglang` import at
runtime.

## ABI
Both sides use a destination-passing ABI with the output tensor passed last:
- `residual_gate_add(residual, update, gate, out)`
- `broadcast_add_4d(a, b, out)`

Both ops are batch-1 only (every production row is B=1); a true B>1 broadcast is
deliberately out of scope and rejected symmetrically on both sides (see
`docs/baseline_source.md`).

Baseline (`baseline/binding.py`) is the faithful PyTorch-eager path:
`residual_gate_add` runs `torch.mul(update, gate, out=scratch)` then
`torch.add(residual, scratch, out=out)` — the profiled two-launch `mul`+`add`
pattern — with a cached, preallocated scratch buffer so the timed steady state
contains only the two real kernel launches; `broadcast_add_4d` is a single eager
`torch.add`. Candidate (`solution/kernel.cu`, built by `solution/build.py` via
`tvm_ffi.cpp.load`) fuses each into a single CUDA pass. Every launch uses
`at::cuda::getCurrentCUDAStream()`.

## Compile flags (symmetric)
- Candidate CUDA: `-std=c++17 -O3` and the device's native gencode
  (`-gencode=arch=compute_100,code=sm_100` on B200). No `--use_fast_math` (the
  eager baseline does not use fast math, so the candidate must not either).
- Baseline: pure torch eager ops; no extra compile flags. Both sides are invoked
  through one Python adapter dispatch with matched overhead.

## Workloads
`bench/workloads.json` is the frozen source of truth (8 production rows matching
the `diffusion_residual_gate_add__multi_shape` section of
`../../docs/diffusion_benchmark_shape_coverage.md`). Workloads, tolerances,
scoring, and timing rules are frozen before tuning; changing any of them requires
deleting old results and remeasuring both baseline and candidate.

## Numerics / tolerances
Candidate accumulates in fp32 and rounds once. Correctness compares candidate vs
an fp32 one-round oracle and vs the baseline, within bf16/fp16 `atol=rtol=5e-2`
and fp32 `atol=rtol=1e-5`, with NaN/Inf rejection.

## Reporting (per the contract)
Headline: equal-weight geomean over all 8 production rows. Secondary diagnostics
(a residual-gate-only geomean and a call-count-weighted view) and the per-row
speed-of-light/roofline table with NCU-derived bounds are reported in
`docs/results.md` (the 4D broadcast row has little fusion headroom and is
reported with its speed-of-light ceiling).

## Remote / GPU
All correctness, benchmark, profiler, and NCU runs execute on B200 (host
`ion-b200`). An idle GPU is selected via `nvidia-smi`, its id exported as
`REMOTE_GPU_ID`, and reused across baseline/candidate/correctness/benchmark/
profile; host/id/model and before/after idle state are recorded in
`docs/results.md`/`docs/run_log.md`.
