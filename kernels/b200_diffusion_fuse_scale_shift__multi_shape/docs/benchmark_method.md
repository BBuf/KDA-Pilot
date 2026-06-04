# Benchmark Method — b200_diffusion_fuse_scale_shift__multi_shape

## Harness

- `bench/benchmark.py` starts from
  `../../docs/standalone_diffusion_benchmark_template.py`
  (template sha256 `6844257357c47330fc75ca8f3232f4bfe0fb598f442373261eb7efca188ff6fa`).
  The benchmark policy (isolated subprocess per workload, fresh inputs per
  trial, poisoned outputs, correctness-before-timing, deterministic interleaved
  A/B order, CUDA-event timing with inner-loop amplification, per-row
  median/mean/std/min/p10/p90, equal-weight geomean headline) is unchanged.
- One documented, additive delta from the template: `_provenance()` merges an
  `_extended_provenance()` block recording `CUDA_VISIBLE_DEVICES` and
  `REMOTE_GPU_ID`, Triton/tvm-ffi versions, nvcc/gcc/driver versions, the
  upstream baseline commit (parsed from `docs/baseline_source.md`), the
  candidate compile flags (from `solution/build.py::candidate_compile_flags`),
  and sha256 hashes of `solution/kernel.cu`, the copied baseline sources,
  `bench/adapter.py`, `bench/benchmark.py` itself, the workloads file, and
  `config.toml`. Every field is best-effort (guarded) so provenance can never
  affect or fail a run; no timing, workload-selection, tolerance, or scoring
  code is touched. The current file's own sha256 is recorded inside each
  `results.jsonl` under `source_sha256.bench_benchmark_py`.
- Workload rows are self-describing: every tensor spec in
  `bench/workloads.json` records `shape`, `dtype`, `stride` (source-tensor
  strides, pre-broadcast), and `storage_offset_elems` where non-zero (the
  wan-ti2v chunk2 views). `bench/adapter.py` validates every constructed
  input tensor against this metadata in `make_case` (untimed) and fails
  before benchmarking on divergence.
- Settings come from `config.toml [benchmark]`: warmup 10, 7 trials,
  inner-loop calibration to ~1000us samples (1..4096), 600s timeout,
  isolated runner on.
- `bench/workloads.json` is frozen (19 production rows + 6 non-production
  regression riders); see `docs/benchmark_preset_audit.md`.

## Wrapper-overhead policy (both sides symmetric at the adapter layer)

- Output allocation is excluded from timing on both sides: outputs are
  preallocated by `make_case` and passed last (destination passing).
- The baseline's per-call cost is the upstream implementation's faithful cost:
  the copied Triton kernels plus the upstream wrapper's Python work (broadcast
  normalization, expand/stride extraction, grid computation, Triton launch),
  ported verbatim into `baseline/binding.py` with only output allocation
  hoisted out.
- The candidate's per-call cost is its own faithful cost: one tvm-ffi call into
  `solution/kernel.cu`, whose host code performs equivalent validation/layout
  normalization in C++ before launching.
- `bench/adapter.py` routes both sides through one shared dispatch helper over
  pre-resolved function tables, so the adapter layer itself adds byte-identical
  overhead to both sides. Neither side allocates, copies inputs, or synchronizes
  in the timed path (the scalar-scalar fast path, which syncs by upstream
  design, is correctness-only and not a production row).

## Compile flags (symmetric policy)

- Baseline: upstream Triton kernels exactly as copied; `@triton.autotune` on
  the 4D path and the upstream-set `num_warps`/`num_stages` are part of the
  baseline. Triton compiles with its defaults — no extra flags injected.
- Candidate: built by `solution/build.py` via `tvm_ffi.cpp.load` with
  `-std=c++17 -O3` and the device's native gencode
  (`-gencode=arch=compute_100,code=sm_100` on B200), plus torch include/lib
  paths for `at::cuda::getCurrentCUDAStream`. **No `--use_fast_math`** (the
  upstream baseline does not use it). No other numerics-affecting flags.
- Exact toolchain versions (CUDA, PyTorch, Triton, tvm-ffi, driver) are
  recorded per run in `bench/results.jsonl` and `docs/run_log.md`.

## Numerics policy

- Candidate computes scale/shift arithmetic in fp32 and stores in x's dtype;
  the baseline's 3D Triton path computes in the promoted input dtype. Parity
  is enforced by the contract tolerances (atol=rtol=5e-2 non-fp32, 1e-5 fp32)
  against both the copied baseline and an independent fp32 torch oracle in
  `bench/correctness.py`, confirmed on-device.
- LayerNorm statistics are fp32 on both sides. The baseline and the
  candidate's generic/fp32 paths use the reference's centered two-pass form;
  the candidate's vectorized bf16/fp16 production rows use shifted-data
  one-pass moments (offset-robust, single fused reduction — see
  `docs/dispatch.md`). The residual variant normalizes the fp32 pre-downcast
  residual values on both sides.
- `gate_out` is a raw-dtype pass-through on both sides (no fp32 round trip).
- The upstream scalar-scalar all-zero fast path copies `x` through unchanged
  regardless of `scale_constant`; the candidate and the oracle reproduce this
  reference behavior exactly (correctness-only class).

## Run protocol on the remote host

- Every GPU command (correctness, benchmark, profiling, NCU) pins the selected
  idle device with `CUDA_VISIBLE_DEVICES=$REMOTE_GPU_ID`, so `cuda:0` inside
  the process is always the pinned card. This also makes the candidate's
  build-time gencode detection (`torch.cuda.get_device_capability()` at module
  load) read the pinned device. ion-b200 is homogeneous (8x B200), so the
  flag is `sm_100` regardless.
- `nvidia-smi` state is captured before and after every measurement; data
  collected while the pinned card had other compute processes is discarded.

## Restrictions the candidate host validation adds (documented deviations)

- `scale`/`shift` must share one dtype (upstream Triton would accept mixed
  dtypes via promotion; no production or contract row uses mixed scale/shift
  dtypes).
- `weight`/`bias` accept any strided 1-D `[C]` view (matching the reference,
  which normalizes them with `.contiguous()`): the candidate reads them
  strided through its generic path; only the vectorized fast path requires
  unit stride and falls back automatically otherwise.
- `index` must be int32/int64 (the dtypes the contract and coverage rows use).
