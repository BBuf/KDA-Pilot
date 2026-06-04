# Results — b200_diffusion_fuse_scale_shift__multi_shape

## Outcome

**Promoted.** The CUDA candidate beats the copied upstream Triton baseline on
every production row. Headline from the canonical final run (equal-weight
geometric mean over the 19 production workloads, candidate vs baseline medians
from the same interleaved run): **2.7972x**, arithmetic mean 3.937x, min row
1.0906x, max row 9.05x. This satisfies the agreed promotion gate
(geomean > 1.0 AND every production row >= 0.97x; no per-row fallback
dispatch needed — the candidate wins every row outright).

## Environment and provenance

- Host: ion-b200 (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`,
  task workspace `/home/sglang-omni/bbuf/kernel_pilot/k11_b200_fuse_scale_shift`.
- GPU: NVIDIA B200 (sm_100, 183359 MiB), `REMOTE_GPU_ID=0`, pinned via
  `CUDA_VISIBLE_DEVICES=0` for every command; GPU 0 idle before/after each
  measurement (0 MiB, no compute processes; logs
  `logs/bench_final_gpustate_{before,after}.txt`).
- Toolchain (all recorded per run inside the results JSONL): torch
  2.11.0+cu130, triton 3.6.0, tvm-ffi 0.1.9, nvcc CUDA 13.0 (build
  36424714), gcc 13.3.0, driver 580.126.20.
- Baseline source: SGLang `main` @ `133254086bf1f5b887c8c99d311719102d58a7eb`
  (see `docs/baseline_source.md`); recorded as `upstream_baseline_commit` in
  the run provenance.
- Candidate source: `solution/kernel.cu`, sha256
  `9fc610cd31225b1091a470854c3536a0e02b1c2fa17b73279997d65eb52d6fd5`
  (recorded as `source_sha256.solution_kernel_cu` in the run provenance,
  together with hashes of the copied baseline sources, adapter, benchmark
  file, frozen workloads, and config, plus the candidate compile flags and
  `CUDA_VISIBLE_DEVICES`/`REMOTE_GPU_ID`; see `docs/benchmark_method.md`).
- Benchmark: `bench/benchmark.py` (template-derived; one documented additive
  provenance delta, timing policy unchanged), frozen `bench/workloads.json`
  (19 production rows + 6 regression riders, every tensor spec
  self-describing with shape/dtype/stride/storage-offset metadata validated
  by the adapter before each trial), isolated subprocess per workload, 7
  interleaved A/B trials, CUDA events with inner-loop amplification to
  ~1000us, fresh inputs per trial, poisoned-output correctness gate before
  timing in every trial.

Exact final command:

```bash
CUDA_VISIBLE_DEVICES=0 REMOTE_GPU_ID=0 python bench/benchmark.py --device cuda:0 --out bench/results.jsonl
```

Correctness gate (before any benchmark number counted):

```bash
CUDA_VISIBLE_DEVICES=0 REMOTE_GPU_ID=0 python bench/correctness.py --device cuda:0 --impl both --rows all
# -> 898/898 rows PASS (canonical grid + production rows + poison self-test
#    + rejection tests + frozen-stride validation), at v0, v1, v2, and the
#    canonical final configuration
```

Artifact lineage (benchmark JSONLs are kept out of the PR per the repo
artifact rule; they live in the remote task workspace and the local loop
artifacts, regenerable with the command above):

- `results_v0.jsonl` — baseline-freeze run with the v0 reference candidate
  (geomean 0.9392).
- `results_v1.jsonl` — v1 vectorized kernels (geomean 2.7289).
- `results_v2.jsonl` — v2 one-pass reduction kernels (geomean 2.7478).
- `results.jsonl` — **canonical final run** of the promoted v2 kernels with
  enriched provenance and stride-validated workloads (geomean 2.7972; the
  numbers below).

## Per-row results (canonical final run; medians over 7 interleaved trials)

GB = bytes moved per call (all tensor reads + writes). TB/s = GB / median.

| workload (production) | GB | baseline us | candidate us | base TB/s | cand TB/s | speedup |
|---|---|---|---|---|---|---|
| qwen_s19_c3072_bcast11 | 0.0004 | 34.00 | 4.51 | 0.01 | 0.05 | **7.55x** |
| qwen_s47_c3072_bcast11 | 0.001 | 34.56 | 4.44 | 0.02 | 0.13 | **7.79x** |
| qwen_s4096_c3072_bcast11 | 0.050 | 33.63 | 10.69 | 1.50 | 4.71 | **3.14x** |
| qwen_edit_s189_c3072_bcast11 | 0.002 | 34.48 | 4.31 | 0.07 | 0.54 | **8.01x** |
| qwen_edit_s195_c3072_bcast11 | 0.002 | 33.85 | 4.35 | 0.07 | 0.55 | **7.78x** |
| qwen_edit_s8424_c3072_bcast11 | 0.104 | 35.13 | 20.72 | 2.95 | 5.00 | **1.70x** |
| qwen_edit_s8424_c3072_full3d | 0.207 | 37.89 | 27.24 | 5.46 | 7.60 | **1.39x** |
| qwen_edit_gated_s8424_c3072 | 0.155 | 49.98 | 45.83 | 3.11 | 3.39 | **1.09x** |
| qwen_edit_resgated_s8424_c3072 | 0.311 | 67.05 | 56.45 | 4.63 | 5.50 | **1.19x** |
| firered10_s8424_c3072_bcast11 | 0.104 | 33.66 | 20.70 | 3.08 | 5.00 | **1.63x** |
| firered11_s189_c3072_bcast11 | 0.002 | 33.59 | 4.36 | 0.07 | 0.54 | **7.71x** |
| firered11_s195_c3072_bcast11 | 0.002 | 37.38 | 4.79 | 0.06 | 0.50 | **7.80x** |
| firered11_s8424_c3072_bcast11 | 0.104 | 33.94 | 20.75 | 3.05 | 4.99 | **1.64x** |
| hunyuanvideo_s55_c3072_bcast2d | 0.001 | 39.45 | 4.36 | 0.02 | 0.16 | **9.05x** |
| hunyuanvideo_s27030_c3072_bcast2d | 0.332 | 71.18 | 61.55 | 4.67 | 5.40 | **1.16x** |
| hunyuanvideo_s27085_c3072_bcast2d | 0.333 | 71.40 | 61.61 | 4.66 | 5.40 | **1.16x** |
| wan_ti2v_s18144_c3072_full_nc_fp32 | 0.669 | 127.68 | 102.18 | 5.24 | 6.55 | **1.25x** |
| wan_t2v_s37800_c5120_bcast11_fp32 | 0.774 | 263.99 | 138.36 | 2.93 | 5.60 | **1.91x** |
| wan_i2v_s37044_c5120_bcast11_fp32 | 0.759 | 257.26 | 135.97 | 2.95 | 5.58 | **1.89x** |

Non-production regression riders (correctness visibility through the full
benchmark machinery; not part of the headline): 4D per-frame 7.05x, fp16
2D-broadcast 8.74x, fp32 full3d 5.48x, EP2 with affine 7.68x, EP2 int64 index
7.90x, EP3 fp32 with affine 8.03x — all PASSED.

Full per-row distribution statistics (median/mean/std/min/p10/p90, raw
samples, inner-loop counts) and the complete provenance record are in the
canonical `results.jsonl` artifact described above.

## Why the candidate wins (roofline-style analysis)

Reference peak: B200 HBM3e ~= 8 TB/s. All three entry points are pure
memory-streaming kernels (arithmetic intensity << 1 FLOP/byte), so the bound
per row is bytes-moved / achievable bandwidth, plus per-call launch overhead.

1. **Small/medium rows (S = 19..4096; 9 of 19 rows, speedups 3.14-9.05x).**
   The Triton baseline is host-launch-bound: its wrapper performs Python
   broadcast normalization, expand/stride extraction, and Triton JIT launch
   machinery on every call — a measured ~33-40us floor per call (the device
   kernels themselves are microseconds). The candidate's whole host path is a
   single tvm-ffi call into C++ dispatch (~4.3-4.5us floor measured at S=19,
   where device time is negligible). This is real production overhead in
   back-to-back diffusion graphs, measured here under CUDA events with
   inner-loop amplification (gaps between back-to-back launches count). NCU
   confirms the row class is not device-bound (0.3% DRAM, 0.8% SM).
2. **Large streaming rows (S = 8424..37800; 10 of 19 rows, 1.09-1.91x).**
   The candidate's 16B-vectorized kernels with evict-first hints for streams
   and read-only caching for reused modulation rows reach 4.99-7.60 TB/s
   (62-95% of nominal peak) versus the baseline's 2.93-5.46 TB/s. The largest
   gains are where the baseline is least efficient: the bf16-x/fp32-scale wan
   rows (2.93 -> 5.6 TB/s, 1.89-1.91x) and the 8424-token broadcast rows
   (3.0 -> 5.0 TB/s, 1.63-1.70x). The full-shape qwen-edit row, where the
   baseline is already strong (5.46 TB/s), still improves to 7.60 TB/s
   (NCU: 68-69% DRAM-bound — at the roof). The non-contiguous wan-ti2v fp32
   row reaches 6.55 TB/s (NCU: 82-83% DRAM-bound).
3. **Gated LayerNorm rows (1.09x / 1.19x).** Both sides must read x (and the
   residual pair) once and write 2 (3) full outputs. The candidate's exact-C
   single-block-per-row kernel (384 threads, one 16B-vector round, fp32
   register cache between passes, fused one-pass (sum, sumsq) block reduction
   with two barriers) removes the Triton version's 25% masked-lane waste at
   BLOCK_N=4096 and its extra reduction barriers. Achieved bandwidth: EP2
   3.11 -> 3.39 TB/s, EP3 4.63 -> 5.50 TB/s. NCU shows neither side is
   DRAM-bound on EP2 (baseline 30% / candidate 20% DRAM, both >58% SM) —
   the row class is barrier/issue-limited on both sides, which is why the
   honest win here is structural-overhead removal (~1.1-1.2x); details and
   the NCU-isolation ranking caveat are in `docs/run_log.md` and
   `docs/dispatch.md`.

## Optimization history (bounded attempts, all on the frozen workloads)

| version | change | production geomean | min row |
|---|---|---|---|
| v0 | generic correct port (scalar strided kernels, lean host path) | 0.9392 | 0.199 (hunyuanvideo 27k) |
| v1 | 16B-vectorized row-grid/flat EP1 paths with cache hints + runtime gates; exact-C register-cached vectorized EP2/EP3 row kernels | 2.7289 | 1.011 (gated EP2) |
| v2 | fused one-pass (sum, sumsq) block reduction in the vectorized EP2/EP3 kernels (5 barriers -> 2 per row) | 2.7478 | 1.0937 (gated EP2) |
| final (canonical) | identical v2 kernels; workloads schema enriched with frozen stride metadata + adapter validation; benchmark provenance extended (env pinning, toolchain versions, source hashes, compile flags); full dual remeasurement per the workload-change rule | **2.7972** | **1.0906 (gated EP2)** |

Ideas considered and not kept (recorded for audit): 256-bit `ld.global.v4.u64`
loads (no headroom left on the rows that matter — full3d already at 7.6 TB/s,
gated rows barrier-bound, small rows host-bound); persistent/CLC-style
scheduling and multi-row blocks for EP2 (the remaining EP2 gap is bounded by
a barrier/issue limit shared with the baseline; structural complexity and
re-validation cost outweigh the bounded expected gain after the gate was met
on every row — documented as the named remaining bound, not pursued).

## Conclusion

The candidate is promoted under the agreed gate: headline geomean **2.7972x**
with every production row at or above **1.0906x** (no row below the 0.97
floor, no fallback dispatch needed). The dominant effects are (a) removal of
the baseline's ~33-40us per-call Python/Triton launch overhead on the many
small and medium production rows, and (b) 16B-vectorized streaming kernels at
5.0-7.6 TB/s on the large rows where the Triton tiles ran at 2.9-5.5 TB/s.
