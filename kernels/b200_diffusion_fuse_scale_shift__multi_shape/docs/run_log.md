# Run Log — b200_diffusion_fuse_scale_shift__multi_shape

Chronological log of context refreshes, remote sessions, GPU state evidence,
and exact commands. Times are local (CST) unless marked UTC.

## 2026-06-04 — RLCR Round 0, iteration 1 (local scaffold)

Context refresh (per diffusion_kernel_rules.md):

- Re-read: task `prompt.md`, `../../docs/standalone_diffusion_benchmark.md`,
  `../../docs/diffusion_kernel_rules.md`,
  `../../docs/diffusion_correctness_contract.md` (Scale Shift section),
  `../../docs/diffusion_benchmark_shape_coverage.md` (fuse_scale_shift family
  + fresh-capture audit), `external/KernelWiki/SKILL.md`,
  `external/ncu-report-skill/SKILL.md`.
- KernelWiki: no query needed for the scaffold milestone (no kernel-design
  decision taken yet beyond the plan's v0 skeleton); first design-affecting
  queries are scheduled for the optimization milestone (memory-bound /
  vectorized-load guidance, elementwise + row-reduction patterns on sm_100).
- ncu-report-skill: noted mandatory run-directory convention
  (`profile/<run_name>/` per run), `-lineinfo` requirement for source-level
  views, and sm_100 metric-name deviations; profiling deferred until a correct
  candidate exists on-device (rules: no NCU before RLCR optimization needs it).

Actions:

- Resolved upstream SGLang main `1332540` (2026-06-04T13:46:36Z, resolution
  2026-06-04T14:59:05Z UTC) via GitHub API; copied
  `python/sglang/jit_kernel/diffusion/triton/scale_shift.py` (679 lines,
  sha256 `b51d0a2...`) into `baseline/scale_shift_triton.py` with recorded
  edits; verified byte-identical to the local sglang checkout copy.
- Wrote `baseline/binding.py` destination-passing launchers,
  `bench/workloads.json` (19 production rows + 6 riders),
  `docs/benchmark_preset_audit.md`, `bench/benchmark.py` (template copy,
  sha256-verified), `bench/adapter.py`, `bench/correctness.py`,
  `solution/kernel.cu` candidate v0, `solution/build.py`; updated
  `config.toml` build entries.
- `python3 -m py_compile` clean on all harness/baseline/build files;
  `bench/workloads.json` parses (25 rows, 19 production).

GPU state: no GPU work yet (local scaffold only; macOS host has no CUDA).

## 2026-06-04 — Pre-GPU contract review (Codex, gpt-5.5:high)

- Verdict: READY_FOR_GPU, no P0 blockers. Response archived under the local
  loop state directory.
- P1 fixes applied: dropped the speculative `tvm/ffi/optional.h`/`tvm/ffi/error.h`
  includes (Optional comes transitively with `tvm/ffi/container/tensor.h`;
  `tvm/ffi/function.h` now guarded by `__has_include`); host failures now throw
  `std::runtime_error` via a fold-expression `cand_fail` (also fixes the
  CAND_CHECK comma-operator diagnostics bug); added `<cstring>`.
- P1 consciously accepted (documented in benchmark_method.md): build-time
  gencode detection reads the current device — covered by the
  `CUDA_VISIBLE_DEVICES=$REMOTE_GPU_ID` pinning protocol on the homogeneous
  ion-b200 host.
- P1 consciously accepted: no NaN/Inf *input* injection rows — the contract
  grid does not include them; poison-detection covers stale/skipped-launch
  outputs, and outputs are NaN/Inf-checked on every row.
- P2 noted: baseline keeps upstream `.contiguous()` calls inside the timed
  launcher (no-ops for every frozen row; faithful upstream cost otherwise).

## 2026-06-04 — Remote bring-up + baseline freeze (ion-b200)

- Host `innomatrix-us-adc-smb200-0003`, container `sglang_bbuf` (Up 2 days),
  task workspace `/home/sglang-omni/bbuf/kernel_pilot/k11_b200_fuse_scale_shift`.
- Toolchain: torch 2.11.0+cu130, triton 3.6.0, tvm_ffi 0.1.9, nvcc CUDA 13.0
  (build 36424714), driver 580.126.20. GPU: NVIDIA B200, 183359 MiB.
- GPU selection: GPUs 0-3 idle (0% util, 0 MiB, no compute procs; GPUs 4-7
  occupied ~149 GiB). Selected REMOTE_GPU_ID=0; all commands pinned with
  CUDA_VISIBLE_DEVICES=0.
- Candidate build: first attempt failed (tvm-ffi 0.1.9 TensorView has size(i),
  not shape(i)); fixed accessors + byte_offset-aware data pointers; second
  build clean (logs/build_v0.log, EXIT=0).
- Correctness gate: `python bench/correctness.py --impl both --rows all`
  → 898/898 rows PASS, 0 failures, incl. poison self-test and rejection tests
  (logs/correctness_v0.log, correctness_v0.json).
- Baseline freeze benchmark: `python bench/benchmark.py --device cuda:0 --out
  bench/results.jsonl` (template defaults = config.toml). GPU idle before and
  after (logs/bench_v0_gpustate_{before,after}.txt). All 25 workloads PASSED
  correctness inside the benchmark; baseline medians frozen in
  bench/results.jsonl (mirrored to local loop artifacts).
- v0 reference headline: geomean 0.9392 (19 production rows; min 0.199 on
  hunyuanvideo 27k rows, max 8.89 on hunyuanvideo s55). Reading: the Triton
  baseline is HOST-LAUNCH-BOUND (~33-37us floor) on every row except the
  27k/37k-token rows; candidate v0 host floor is ~4.3us, but its scalar
  div/mod grid-stride kernels lose 2-5x on streaming rows.
- Iteration context refresh: KernelWiki `technique-vectorized-loads` (128/256-bit
  loads to saturate ~8TB/s, differentiated L1 cache policies, register
  budgeting) and `pattern-memory-bound`; upstream provenance of these kernels
  confirmed via KernelWiki pr-sglang-14717. Next edit: vectorized per-row-grid
  EP1 kernels (streaming __ldcs/__stcs for x/out, __ldg for reused modulation
  rows), flat-vec small-row variant, exact-C register-cached EP2/EP3 row
  kernels (ROUNDS-templated), generic v0 kernels kept as fallback paths.
