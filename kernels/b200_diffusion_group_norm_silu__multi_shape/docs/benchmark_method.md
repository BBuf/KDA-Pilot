# Benchmark Method — `b200_diffusion_group_norm_silu__multi_shape`

## Harness

- `bench/benchmark.py` starts from
  `../../docs/standalone_diffusion_benchmark_template.py`
  (sha1 `84a260f8ab799b85cdf8e3a6478bcccb719548d0` at copy time). The timing
  policy, per-trial interleaved A/B order (deterministic seeded
  randomization), CUDA-event timing, inner-loop amplification, stats, and
  geomean aggregation are unmodified. The ONLY task-glue delta vs the
  template is an optional, untimed reporting hook: if `bench/adapter.py`
  defines `describe_paths(workload, inputs, outputs)`, its returned per-row
  dispatch metadata (`candidate_path` / `candidate_regime` /
  `matched_status`, captured from the same tensors used for timing) is merged
  into each result record — required by the per-row evidence table
  (dispatch path and matched/fallback status). All other task-specific
  behavior lives in `bench/adapter.py`.
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
  generation. NO `--use_fast_math` (the upstream baseline does not use it).
  Numerics classes in device code: the fp32 generic path uses IEEE
  `expf`/`sqrt` (double accumulation); the 16-bit production regimes use the
  SFU exp class via an explicit per-call `__expf` (`silu_fast` in
  `solution/kernel.cu`) — the same accuracy class the upstream Triton
  baseline's `tl.sigmoid` lowers to (ex2.approx). This is an intrinsic
  choice in source, not a compile flag, and is gated by the full correctness
  suite at contract tolerances.
- Both sides launch on PyTorch's current CUDA stream.
- (The exact flag list and toolchain versions are re-recorded from the remote
  build log in `docs/run_log.md` at bring-up time.)

## Validity Gates

- A/A gate (before tuning): run the harness with
  `GNS_CANDIDATE_ALIAS_BASELINE=1` (candidate aliased to the baseline
  implementation) on a representative workload subset; the headline geomean
  must land in 0.98–1.02. **Result: PASS — geomean 1.0005, per-row
  0.9956–1.0127 over 8 rows (4 contiguous + 4 channels-last spanning
  min/33%/66%/max group sizes, both entry points); raw in
  `bench/results_aa.jsonl`, log in `docs/run_log.md` Run 3.**
- GPU discipline: host `ion-b200`, idle B200 selected via `nvidia-smi`
  (no active compute processes, no meaningful memory occupancy), id exported
  as `REMOTE_GPU_ID` and used consistently; `nvidia-smi` checked before and
  after every benchmark/profile run (evidence in `docs/run_log.md`).
- Correctness (`bench/correctness.py`) must be green on the selected GPU
  before any benchmark number is treated as valid.

## fp32 Stress Rows (task-local hardening additions)

The offset / low-variance / zero-variance stress rows in
`bench/correctness.py` are task-local additions beyond the contract grid. On
their fp32 variants, measured on B200 (GPU 1, 2026-06-04):

- The copied upstream baseline cannot meet the fp32 contract tolerance by
  design: `E[x^2]-E[x]^2` fp32 cancellation gives output max_abs ~9e-5 on the
  offset row and ~2.4 on the low-variance row (variance overestimated 100x;
  NaN possible since upstream does not clamp negative variance), and its
  sigmoid implementation class differs from the torch oracle by ~3e-5 on the
  zero-variance row. Baseline results on these three fp32 rows are therefore
  recorded as INFO (known upstream limitation), not suite failures.
- The candidate IS strictly gated on all stress rows. Its generic fp32 path
  accumulates in double (production 16-bit paths keep fp32 accumulation, the
  same numerics class as the baseline). Two fp32 rows carry documented atol
  overrides because no fp32 implementation pair can do better: low-variance
  atol 2e-3 (1-ulp fp32 mean disagreement amplified by rstd ~1e3; candidate
  measured 4.95e-4 vs baseline 2.4) and zero-variance atol 1e-4 (pure fp32
  silu-implementation-class difference, candidate measured ~3e-5).
- Production rows (fp16) and the canonical contract grid are gated at
  unmodified contract tolerances on BOTH sides.

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
