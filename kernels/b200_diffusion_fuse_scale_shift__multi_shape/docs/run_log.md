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

## 2026-06-04 — Optimization iteration 1 (v1 kernels)

Context refresh: frozen per-row evidence (bench/results.jsonl v0 run) +
KernelWiki technique-vectorized-loads / pattern-memory-bound (already queried
this round; no new query needed — the v0 per-row table directly identifies the
bound per bucket: host-launch-bound small rows already won, streaming rows lose
on scalar per-element div/mod kernels).

Edit decisions (evidence -> design):
- EP1 large rows (v0 0.20-0.51x): one block per token row eliminates
  per-element div/mod; 16B vectors (8x bf16 / 4x fp32) with __ldcs/__stcs
  evict-first hints for x/out and full-shape scale/shift; __ldg read-only
  cache for modulation rows reused across tokens (sl==0). Runtime gates:
  C % vec == 0, 16B base alignment, unit channel stride, 16B-multiple row
  strides; generic v0 strided kernel kept as fallback (scalar/4D/odd-C).
- EP1 small rows (v0 already 4-8.9x): flat vectorized grid (32-bit indexing)
  below 512 rows so S=19..195 rows still cover the SMs.
- EP2/EP3 8424-rows (v0 0.61x/0.56x): exact-C single-block-per-row vectorized
  kernels, fp32 register cache of the loaded row between mean and variance
  passes (single global read of x / of the fp32 residual expression),
  modulation rows via __ldg, gate_out stored as raw 16B vectors (no fp32
  round trip), kRounds templated (1..4) so register usage matches C; threads
  picked per-C (C=3072 bf16 -> 384 threads, 1 round).
- wan-ti2v chunk2 row rides the rowgrid path (contiguous last dim, doubled row
  stride passes the 16B gates); wan-t2v/i2v fp32 broadcast rows ride the
  reuse path (fp32 rows read as float4 pairs).

## 2026-06-05 — v1/v2 benchmark sessions + final result (ion-b200 GPU0)

- v1 benchmark (`bench/results_v1.jsonl`): 25/25 PASSED, production geomean
  2.7289x, min row 1.011x (qwen_edit_gated). GPU0 idle before/after.
- Iteration context refresh for v2: v1 per-row evidence shows the two gated
  rows are the only near-parity rows; the EP2 kernel achieves 3.1 TB/s while
  EP3 reaches 5.3 TB/s with more streams -> barrier-bound, not DRAM-bound.
  No new KernelWiki query needed (the vectorized-loads/memory-bound pages
  already cover the applied techniques); edit chosen: fuse the mean/variance
  reductions into one one-pass (sum, sumsq) float2 block reduction (5
  barriers -> 2 per row), numerically safe at the contract tolerances with
  fp32 tree reduction (verified against the 1e-5 fp32 grid rows on-device).
- v2 correctness: 898/898 PASS (logs/correctness_v2.{log,json}).
- v2 FINAL benchmark (`bench/results_v2.jsonl`, canonical copy
  `bench/results.jsonl`): 25/25 PASSED, production geomean 2.7478x,
  arithmetic mean 3.818x, min row 1.0937x (qwen_edit_gated), max 8.99x
  (hunyuanvideo_s55). GPU0 idle before/after
  (logs/bench_v2_gpustate_{before,after}.txt; an unrelated 4.2 GiB allocation
  appeared on GPU1 after the run — different card, our measurements pinned to
  GPU0 via CUDA_VISIBLE_DEVICES=0).
- DEC-1 promotion gate satisfied: geomean > 1.0 and every production row
  >= 0.97x (in fact >= 1.0937x). Optimization stopped per the
  bounded-attempts policy; remaining EP2 headroom documented as a named bound
  in docs/dispatch.md.
- NCU evidence session: profile/ncu_v2/ in the remote task workspace
  (--set full, --launch-skip 2 --launch-count 2, via bench/profile_one.py)
  over: qwen_s19 (small EP1), qwen_edit_s8424 bcast + full3d, wan-ti2v
  chunk2 fp32, gated EP2 (candidate AND baseline), resgated EP3. First batch
  failed (profile_one.py not yet synced — rerun after sync). Raw .ncu-rep
  artifacts stay in the remote task workspace; extracted metrics below.

## 2026-06-05 — NCU evidence (filtered rerun, profile/ncu_v2/, GPU0)

Commands: `CUDA_VISIBLE_DEVICES=0 ncu --set full -k "regex:<kernel-family>"
--launch-count 2 --target-processes all -o profile/ncu_v2/reports/<id>_<side>
python bench/profile_one.py --id <id> --side <side> --iters 5`. Raw .ncu-rep
files stay in the remote task workspace (not staged for the PR).

Speed-of-light extraction (NCU locks clocks below live boost — durations are
NOT comparable to the interleaved benchmark; used for bound attribution only):

| kernel (workload) | dur us | DRAM% | SM% | regs | occ% |
|---|---|---|---|---|---|
| baseline Triton fused_layernorm_select01, EP2 s8424 | 48.9 | 29.7-30.1 | 58.3-58.9 | 63 | 45.3 |
| cand ln_select01_vec<bf16,i32,1> 384thr, EP2 s8424 | 73.4 | 19.9-20.4 | 65.8 | 40 | 67.3 |
| cand residual_ln_select01_vec<bf16,i32,1>, EP3 s8424 | 86.0 | 45.5-46.0 | 68.5 | 40 | 68.2 |
| cand scale_shift_rowgrid<bf16,bf16,reuse>, bcast11 s8424 | 31.5 | 28.1-28.5 | 60.5 | 27 | 77.9 |
| cand scale_shift_rowgrid<bf16,bf16,stream>, full3d s8424 | 39.0 | 67.8-68.8 | 48.8 | 27 | 80.6 |
| cand scale_shift_flatvec<bf16,bf16,reuse>, s19 | 6.6 | 0.3 | 0.8 | 28 | 11.9 |
| cand scale_shift_rowgrid<bf16,f32,stream>, wan-ti2v | 116.2 | 82.0-83.2 | 28.1 | 32 | 81.7 |

Bound attribution per row class:

- wan-ti2v (and the wan fp32-broadcast class): **DRAM-bandwidth-bound** —
  82-83% DRAM utilization at 81.7% occupancy; live 6.54 TB/s. Little headroom.
- full3d s8424: **DRAM-bound** (68-69% under NCU; live 7.60 TB/s = ~95% of
  nominal peak). At the roof.
- bcast11 s8424: issue/conversion-bound at base clock (28.5% DRAM, 60.5% SM);
  live 4.99 TB/s. Some headroom in principle; gains here would not change the
  promotion outcome (row already 1.64-1.68x).
- EP2 gated: **not DRAM-bound on either side** (baseline 30% / candidate 20%
  DRAM; both >58% SM throughput) — barrier/issue-limited at one row per block,
  C=3072. NOTE the NCU-isolated durations INVERT the live ranking here
  (candidate 73.4us vs baseline 48.9us under locked clocks, while the live
  interleaved arbiter gives candidate 45.8us vs baseline 50.1us). Consistent
  with the established B200 lesson that NCU isolation can invert pipeline-
  kernel rankings; NCU durations are therefore EXCLUDED from ranking for this
  row — the steady-state interleaved A/B run is the only promotion arbiter,
  and NCU is used strictly for bound attribution. The "barrier" component of
  the EP2 attribution is partly inferred from the kernel structure (one row
  per block, two block-wide reductions) on top of the SOL counters; explicit
  stall-barrier counters were not separately extracted.
- Independent review of this interpretation (Codex, gpt-5.5:high, archived in
  the local loop state dir): ATTRIBUTION_VERDICT SOUND, INVERSION_VERDICT
  ACCEPTABLE, STOP_DECISION AGREE ("stop decision defensible under bounded
  attempts; gate met on every production row").
- EP3 resgated: mixed (46% DRAM, 68.5% SM) — close to balanced; live 5.50 TB/s.
- s19 (small class): nothing on-device is the bottleneck (0.3% DRAM, 0.8% SM,
  29 blocks) — the row is launch/host-path-bound, which is exactly where the
  candidate's lean tvm-ffi dispatch wins 7.7x.

GPU state before/after the NCU session recorded in profile/ncu_v2/
gpustate_{before,after}.txt (GPU0 idle, 0 MiB).

## 2026-06-05 — Round 1: evidence-gap repair + canonical final run (ion-b200 GPU0)

Review-driven scope (round-0 Codex review): (1) AC-3 — workload rows lacked
explicit stride metadata; (2) AC-5/AC-7 — benchmark JSONL provenance was
missing env/toolchain/source-hash fields and the canonical artifact pointer
was ambiguous (local archived results.jsonl was the v0 run).

Changes:

- `bench/workloads.json`: every tensor spec now records `stride`
  (source-tensor strides, pre-broadcast) and `storage_offset_elems` where
  non-zero; the wan-ti2v chunk2 views record `[111476736, 6144, 1]` with
  scale offset 3072 (shapes/dtypes/seeds/tolerances byte-identical — schema
  enrichment only).
- `bench/adapter.py`: `_validate_against_spec` checks every constructed input
  tensor's shape/stride/storage offset against the frozen metadata inside
  `make_case` (untimed); benchmarking fails fast on divergence.
- `bench/benchmark.py`: `_provenance()` now merges `_extended_provenance()`
  (env pinning, triton/tvm-ffi/nvcc/gcc/driver versions, upstream baseline
  commit parsed from docs/baseline_source.md, candidate compile flags from
  solution/build.py, sha256 of kernel.cu/baseline sources/adapter/benchmark
  file/workloads/config). Timing policy untouched; delta documented in
  docs/benchmark_method.md; the file's own sha256 is self-recorded per run.
- `solution/build.py`: flags factored into `candidate_compile_flags()` (same
  values; now recordable).

Re-validation (workload-schema change -> dual remeasurement per the frozen-
workload rule; kernels unchanged from the promoted v2 source, sha
`9fc610cd...`):

- Correctness: 898/898 PASS, 0 failures (logs/correctness_final.{log,json}),
  now including the frozen-stride validation on every row.
- Canonical FINAL benchmark (`bench/results.jsonl`, GPU0 idle before/after,
  `CUDA_VISIBLE_DEVICES=0 REMOTE_GPU_ID=0`): 25/25 PASSED, production
  geomean **2.7972x**, arithmetic mean 3.937x, min row 1.0906x
  (qwen_edit_gated), max 9.05x (hunyuanvideo_s55). DEC-1 gate met on every
  row. Verified the enriched provenance block in the JSONL (env, versions,
  upstream commit 1332540, compile flags, 7 source hashes; kernel hash
  matches the committed promoted source).
- Artifact lineage fixed: local loop artifacts now hold results_v0.jsonl
  (baseline-freeze run), results_v1.jsonl, results_v2.jsonl, and
  results.jsonl = the canonical final run; docs/results.md and
  docs/dispatch.md updated to the canonical numbers and lineage.

Context refresh for this iteration: round-0 review findings + bitlesson
KB (selector: R1-task2 NONE; R1-task10 BL-20260605-ncu-kernel-filter — no new
NCU captures were needed since the kernels are unchanged; the round-0 NCU
evidence remains valid for bound attribution). No new KernelWiki query needed
(no kernel-design decision in this round).

## 2026-06-05 — Round 2 (review phase): numerics + ABI fixes, canonical re-run

Code review findings fixed (both classified blocking):

1. Vectorized gated kernels' one-pass variance E[x^2]-mean^2 was vulnerable to
   catastrophic fp32 cancellation at large common offsets. Fix evolution,
   recorded honestly:
   - Added offset-stress correctness rows (EP2/EP3, fp32 offset 16384, bf16
     offset 64). First run showed the fp32 rows at 1e-5 tolerance fail for
     BOTH sides (baseline max_abs 1.6e-2, candidate 9.4e-3): at offset 16384
     the fp32 input ulp (~1e-3) dominates every implementation — tolerance
     re-set to 5e-2 with the rationale in the test comment (the cancellation
     failure mode this row targets produces O(1)-O(1e3) errors and is still
     caught decisively).
   - Pure shifted-data one-pass (K = row's first element) then left two
     regular fp32 EP3 grid rows marginally over 1e-5 (5.2e-5/3.1e-5): the
     shift sample can land a few sigma from the mean, amplifying rounding by
     (1+z0^2). Final form: statistics by dtype — fp32 rows use the
     reference's centered two-pass from the register cache (1e-5 class);
     bf16/fp16 rows (all production) use the shifted one-pass (offset-robust,
     single fused reduction, two barriers).
2. Strided 1-D weight/bias views are now accepted like the reference: the
   generic gated kernels index by stride; the vectorized fast path requires
   unit stride and falls back automatically; the contiguity rejection was
   removed (benchmark_method.md deviation note updated). New strided-affine
   positive tests pass on both sides.

Re-validation (kernel source changed -> full dual remeasurement):

- Correctness: 902/902 PASS, 0 failures (898 prior rows + 4 offset-stress
  rows + strided-affine tests; logs/correctness_r2.{log,json}).
- Canonical FINAL benchmark (bench/results.jsonl, GPU0 idle 0 MiB
  before/after, logs/bench_r2_gpustate_{before,after}.txt): 25/25 PASSED,
  production geomean 2.7570x, arithmetic 3.895x, min row 1.0391x
  (qwen_edit_gated), max 8.99x. DEC-1 met on every row. The robustness fix
  costs the two gated rows ~5-12% vs the rejected raw form (EP2 1.09->1.04,
  EP3 1.19->1.05) — accepted: correctness class beats the marginal speed of
  a cancellation-prone form. New candidate kernel sha256
  23e6ee015982ed98a4b227c47a544066eb2bbc6aee792ad1e37e3168086d1117 (recorded
  in the run provenance; docs updated).
