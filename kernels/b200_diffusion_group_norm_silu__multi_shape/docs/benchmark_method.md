# Benchmark Method — `b200_diffusion_group_norm_silu__multi_shape`

## Harness

- `bench/benchmark.py` is a verbatim copy of
  `../../docs/standalone_diffusion_benchmark_template.py`
  (sha1 `84a260f8ab799b85cdf8e3a6478bcccb719548d0` at copy time); the timing
  policy, per-trial interleaved A/B order (deterministic seeded
  randomization), CUDA-event timing, inner-loop amplification, stats, and
  geomean aggregation are unmodified. Task-specific behavior lives only in
  `bench/adapter.py`.
- Benchmark settings come from `config.toml`: warmup 10, iterations 200,
  trials 7, inner iterations 1..4096 calibrated to >= ~1000 us samples,
  isolated subprocess per workload, timeout 600 s,
  `required_matched_ratio = 1.0`.
- Workloads are frozen before tuning: `bench/workloads.json`
  (160 production rows + 12 regression-grid rows), generated programmatically
  by `bench/gen_workloads.py` from the retained live capture in git history
  (`git show 35bc2c6b4~1:kernels/b200_diffusion_group_norm_silu__multi_shape/docs/captured_shapes_b200.jsonl`).
  Frozen file sha256:
  `1255972107562ab14e9b04c3e433a9a5334b169eadf43e6b0f50f1cf7c46eeb8`.
  Verify any time with `python3 bench/gen_workloads.py --check`.

## ABI Interpretation

- `config.toml` names `baseline/kernel.cu::group_norm_silu_baseline` /
  `solution/kernel.cu::group_norm_silu_candidate` as build entry points; the
  upstream implementation for this family is Triton/Python, so per
  `docs/diffusion_kernel_rules.md` and `docs/standalone_diffusion_benchmark.md`
  ("kernel.cu **or binding.py** exposing the ABI") the baseline is the copied
  Triton source behind `baseline/__init__.py::group_norm_silu_baseline`, and
  the candidate is CUDA behind `solution/binding.py::group_norm_silu_candidate`
  (kernel source in `solution/kernel.cu`).
- Single exported call per side (user decision DEC-2):
  `(x, weight, bias, num_groups, eps, out)`, output passed last, contiguous
  output layout on both sides (the upstream baseline returns a contiguous
  tensor for every supported input). Each workload row's `function` field
  records which upstream entry point (`triton_group_norm_silu` or
  `apply_group_norm_silu`) the row was captured from; both route to the same
  local call so wrapper overhead is identical across rows and sides. The
  `apply_group_norm_silu` module-gate semantics are validated separately in
  `bench/correctness.py` (untimed).

## Timed-Path Policy (user decision DEC-1)

- The baseline keeps the upstream behavior inside the timed call:
  `x.contiguous()` materialization (the full copy paid by channels-last rows,
  allocator-inclusive) and the chunked path's internal scratch allocations.
- The only timed-path local edit on the baseline is destination passing of the
  final output (mirrored on the candidate); the benchmark template forbids
  timed-path OUTPUT allocation and preallocates `out` on both sides.
- The candidate never materializes a contiguous copy of `x`; strided inputs
  are read natively.

## Compile / Build Flags

- Baseline: upstream Triton kernels JIT-compiled by Triton with upstream
  meta-parameters (BLOCK sizes, `num_warps`, `num_stages`) — no task-added
  compiler flags, no fast-math.
- Candidate: `solution/kernel.cu` built standalone via `tvm_ffi.cpp.load`
  (no SGLang import) with:
  `-gencode=arch=compute_100,code=sm_100 -std=c++20 -O3 --expt-relaxed-constexpr -lineinfo`
  plus torch include/library paths for `at::cuda::getCurrentCUDAStream()`.
  `-lineinfo` is for NCU source attribution and does not change code
  generation. NO `--use_fast_math` (the upstream baseline does not use it);
  device code uses plain `expf`/`rsqrtf` without fast-math flags.
- Both sides launch on PyTorch's current CUDA stream.
- (The exact flag list and toolchain versions are re-recorded from the remote
  build log in `docs/run_log.md` at bring-up time.)

## Validity Gates

- A/A gate (before tuning): run the harness with
  `GNS_CANDIDATE_ALIAS_BASELINE=1` (candidate aliased to the baseline
  implementation) on a representative workload subset; the headline geomean
  must land in 0.98–1.02. Result recorded here after the remote run.
- GPU discipline: host `ion-b200`, idle B200 selected via `nvidia-smi`
  (no active compute processes, no meaningful memory occupancy), id exported
  as `REMOTE_GPU_ID` and used consistently; `nvidia-smi` checked before and
  after every benchmark/profile run (evidence in `docs/run_log.md`).
- Correctness (`bench/correctness.py`) must be green on the selected GPU
  before any benchmark number is treated as valid.

## Cache-State Policy

- Within a trial the same tensors are reused back-to-back (steady-state,
  warm-L2 where the working set fits); fresh random inputs are generated for
  every trial. This steady-state interleaved A/B policy is the promotion
  arbiter. Note: the largest production rows move ~0.5 GB+ per tensor and
  exceed B200's L2 regardless; small rows may be L2-resident — identically so
  for baseline and candidate due to interleaving.

## Scoring and Promotion Gate

- Per-row speedup = `baseline_median_us / candidate_median_us`; headline =
  equal-weight geometric mean over all 160 production rows (no dedupe across
  the two entry points, user decision DEC-4); arithmetic mean reported as a
  secondary metric.
- Promotion requires headline geomean > 1.0 AND no production row below
  0.97x (user decision DEC-3 + standing standalone gate ruling); shape buckets
  where the optimized path loses are routed to a baseline-equivalent path by
  the candidate dispatcher (`docs/dispatch.md` records buckets when used).
  Fallback-routed rows are counted, marked in results, and included in the
  geomean.
