# Benchmark Method

## ABI Decision (allocation-return, symmetric on both sides)

The preferred contract for this repo is destination-passing
(`config.toml: destination_passing_style = true`, output tensors passed last). The vendored
upstream entry points cannot satisfy it without invasive local edits: both
`sglang::fused_norm_scale_shift` and `sglang::fused_scale_residual_norm_scale_shift` are
`torch.library.custom_op`s that allocate their outputs internally (`torch.empty_like`) and return
them; no destination parameters exist upstream. Per the standing decision for this task
(symmetric same-allocation-policy adapters when CuTe DSL cannot take destinations), both sides are
exposed through the SAME allocation-return ABI:

- Baseline callable: the upstream custom op from the vendored snapshot (`baseline/binding.py`),
  carrying the exact production host stack — custom-op dispatch, validation, BSFD broadcast,
  compile-cache lookup, CuTe launch on the current torch stream, internal output allocation.
- Candidate callable: a `torch.library.custom_op` in the local `kda_nss::` namespace
  (`solution/binding.py`) with `register_fake`, performing the same validation/classification,
  allocating outputs with the same `torch.empty_like` policy, and launching the native CUDA kernel
  on the current torch stream. Identical wrapper class, identical allocation policy.

Deviation from the template's "preallocated outputs" wording, and how the template contract is
kept: `make_case` passes each side an output **dict** (`{"y": None}` for `fused_norm_scale_shift`,
`{"y": None, "res_out": None}` for the residual variant). `call_baseline`/`call_candidate` store
the op's returned tensors into that dict (one dict assignment in the timed path, identical on both
sides; the adapter functions themselves allocate nothing). The template's poison/compare logic
operates on the dict contents. Under allocation-return semantics the poison check degenerates
(each call produces fresh tensors); uninitialized/stale-output detection is instead covered by
`bench/correctness.py`'s fp32-oracle value checks and NaN/Inf rejection, which run on every
production row and the canonical regression grid.

## Build Paths (one shared stack)

- Baseline: upstream's own JIT path, `cute.compile(kernel, ..., options="--enable-tvm-ffi")`,
  compile-cache keyed on (norm_type, per-tensor (dtype, ndim, D)).
- Candidate: the snapshot's `jit_kernel.utils.load_jit` (tvm-ffi `load_inline`) with default flags
  only: `-std=c++20 -O3 --expt-relaxed-constexpr` plus the device-derived arch define
  (`-DSGL_CUDA_ARCH=900` on H200) and `TVM_FFI_CUDA_ARCH_LIST=9.0` selected from the active device.
- No `--use_fast_math` on either side (upstream uses none). No side-only flags. Any flag change
  must be applied to both sides and recorded here.
- All JIT builds and compile-cache warming happen before timed regions (first correctness call +
  warmup runs precede calibration and measurement).

## Timing Policy

`bench/benchmark.py` is a verbatim copy of `../../docs/standalone_diffusion_benchmark_template.py`.
Policy (fixed by the template): isolated subprocess per workload (spawn), fresh seeded inputs per
trial, poison + one correctness call per trial before warmup, warmup runs, calibrated inner-loop
amplification toward `target_sample_us`, deterministic interleaved A/B order per trial, CUDA events
primary / wall-clock secondary, per-side median/mean/std/min/p10/p90 + raw samples, equal-weight
geometric mean over production workloads, provenance + before/after `nvidia-smi` in
`bench/results.jsonl`.

Parameters come from `config.toml [benchmark]`: `warmup_runs=10`, `num_trials=7`,
`inner_iterations_min=1`, `inner_iterations_max=4096`, `target_sample_us=1000`,
`timeout_seconds=600`, `use_isolated_runner=true` (passed as the template's CLI defaults match;
any override is recorded in `docs/run_log.md` with the exact command). Note: the `iterations = 200`
key in `config.toml` is not a template parameter — the effective per-sample iteration count is the
calibrated inner loop; the key is retained untouched for template provenance.

### Task-local provenance extensions (timing path untouched)

`bench/benchmark.py` extends the template's provenance/summary events and result rows with
machine-auditable evidence required by this task's contract; no timing, calibration,
interleaving, or scoring code is altered:

- Provenance event: `hostname`, `device_arg`, `cuda_visible_devices`, `selected_gpu`
  (visible index, resolved physical index, GPU UUID, model, memory), filtered environment
  (`KDA_*`, `CUDA_VISIBLE_DEVICES`, `TVM_FFI_CUDA_ARCH_LIST`), `baseline_source_commit` (parsed
  from `baseline/binding.py`), `candidate_src_hash` (sha1-12 of the kernel source), `run_seed`,
  `candidate_impl`, plus UUID-keyed `gpu_inventory_before` and `compute_apps_before` snapshots.
- Summary event: `gpu_inventory_after`, `compute_apps_after` (idle/process evidence after the run).
- Each result row: `run_seed`, `trial_seeds` (the exact per-trial seeds), `ab_orders` (the
  deterministic interleave order per trial), `candidate_impl`, `device_arg`, `selected_gpu`
  (per-instance audit anchor; calibrated inner-loop values were already emitted in the per-side
  stats as `inner_iterations`).

### Baseline-vs-baseline symmetry sanity

`bench/benchmark.py --candidate-impl baseline` routes the candidate side through
`adapter.call_baseline`, measuring baseline-vs-baseline under the identical isolation, warmup,
calibration, and interleaving policy. Expected outcome: per-row speedups ~1.0; this validates
that the harness itself introduces no side asymmetry. The executed run and its numbers are
recorded in `docs/run_log.md`.

## Comparison Policy

- Benchmark-level: template default compare (baseline vs candidate outputs, per-workload
  `atol`/`rtol` from `bench/workloads.json`: 5e-2 for non-fp32 rows, 1e-5 for fp32 rows), NaN/Inf
  rejection on candidate outputs.
- Correctness-level (`bench/correctness.py`): the upstream-canonical plain-fp32 oracle (all
  operands floated, layer/rms norm and `norm * (1 + scale) + shift` in fp32, one final round to
  the activation dtype; `res_out` = the fp32 pre-norm value rounded once — mirroring the
  reference functions in the vendored canonical test). Intermediate rounding boundaries are not
  modeled by the oracle; the candidate KERNEL implements upstream's rounding contract (pre-norm
  and post-norm values rounded to the activation dtype), and that agreement is enforced by the
  candidate-vs-baseline static-tolerance check plus the dynamic bound (candidate error <= 2x
  baseline error + 1e-6 vs the unrounded fp32 reference) on every checked output. Outputs
  poisoned where the allocation-return ABI allows, NaN/Inf rejection, canonical regression grid,
  and the negative-probe suite.

## GPU Discipline

Idle-GPU selection before any measurement (no active compute processes, no meaningful memory
occupancy), consistent `REMOTE_GPU_ID` across baseline/candidate/benchmark/profile/NCU commands in
a run, before/after `nvidia-smi` recorded by the harness and in `docs/run_log.md`. Performance data
from a non-idle card is discarded.
