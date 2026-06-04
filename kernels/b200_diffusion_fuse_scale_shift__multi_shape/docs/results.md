# Results — b200_diffusion_fuse_scale_shift__multi_shape

## Outcome

**Promoted.** The CUDA candidate beats the copied upstream Triton baseline on
every production row. Headline (equal-weight geometric mean over the 19
production workloads, candidate vs baseline medians from the same interleaved
run): **2.7478x**, arithmetic mean 3.818x, min row 1.0937x, max row 8.99x.
This satisfies the agreed promotion gate (geomean > 1.0 AND every production
row >= 0.97x; no per-row fallback dispatch needed — the candidate wins every
row outright).

## Environment and provenance

- Host: ion-b200 (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`,
  task workspace `/home/sglang-omni/bbuf/kernel_pilot/k11_b200_fuse_scale_shift`.
- GPU: NVIDIA B200 (sm_100, 183359 MiB), `REMOTE_GPU_ID=0`, pinned via
  `CUDA_VISIBLE_DEVICES=0` for every command; idle before/after each
  measurement (0 MiB, no compute processes on GPU 0; logs
  `logs/bench_v2_gpustate_{before,after}.txt` — an unrelated 4.2 GiB
  allocation appeared on GPU 1 after the final run, never on GPU 0).
- Toolchain: torch 2.11.0+cu130, triton 3.6.0, tvm-ffi 0.1.9, nvcc CUDA 13.0
  (build 36424714), driver 580.126.20.
- Baseline source: SGLang `main` @ `133254086bf1f5b887c8c99d311719102d58a7eb`
  (see `docs/baseline_source.md`).
- Candidate source: `solution/kernel.cu` at the commit containing this
  document (see git history of this folder).
- Benchmark: `bench/benchmark.py` (byte-identical template copy), frozen
  `bench/workloads.json` (19 production rows + 6 regression riders),
  isolated subprocess per workload, 7 interleaved A/B trials, CUDA events
  with inner-loop amplification to ~1000us, fresh inputs per trial,
  poisoned-output correctness gate before timing in every trial.

Exact final command:

```bash
CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --device cuda:0 --out bench/results.jsonl
```

Correctness gate (before any benchmark number counted):

```bash
CUDA_VISIBLE_DEVICES=0 python bench/correctness.py --device cuda:0 --impl both --rows all
# -> 898/898 rows PASS (canonical grid + production rows + poison self-test
#    + rejection tests), at v0, v1, and the final v2 kernels
```

## Per-row results (final run; medians over 7 interleaved trials)

GB = bytes moved per call (all tensor reads + writes). TB/s = GB / median.

| workload (production) | GB | baseline us | candidate us | base TB/s | cand TB/s | speedup |
|---|---|---|---|---|---|---|
| qwen_s19_c3072_bcast11 | 0.0004 | 34.17 | 4.43 | 0.01 | 0.06 | **7.71x** |
| qwen_s47_c3072_bcast11 | 0.001 | 33.69 | 4.53 | 0.02 | 0.13 | **7.43x** |
| qwen_s4096_c3072_bcast11 | 0.050 | 34.26 | 10.66 | 1.47 | 4.72 | **3.21x** |
| qwen_edit_s189_c3072_bcast11 | 0.002 | 33.53 | 4.38 | 0.07 | 0.53 | **7.66x** |
| qwen_edit_s195_c3072_bcast11 | 0.002 | 33.80 | 4.61 | 0.07 | 0.52 | **7.33x** |
| qwen_edit_s8424_c3072_bcast11 | 0.104 | 34.86 | 20.73 | 2.97 | 4.99 | **1.68x** |
| qwen_edit_s8424_c3072_full3d | 0.207 | 36.91 | 27.25 | 5.61 | 7.60 | **1.35x** |
| qwen_edit_gated_s8424_c3072 | 0.155 | 50.08 | 45.79 | 3.10 | 3.39 | **1.09x** |
| qwen_edit_resgated_s8424_c3072 | 0.311 | 63.71 | 56.52 | 4.88 | 5.50 | **1.13x** |
| firered10_s8424_c3072_bcast11 | 0.104 | 34.01 | 20.68 | 3.04 | 5.01 | **1.64x** |
| firered11_s189_c3072_bcast11 | 0.002 | 33.50 | 4.39 | 0.07 | 0.53 | **7.63x** |
| firered11_s195_c3072_bcast11 | 0.002 | 34.44 | 5.19 | 0.07 | 0.46 | **6.64x** |
| firered11_s8424_c3072_bcast11 | 0.104 | 34.51 | 20.75 | 3.00 | 4.99 | **1.66x** |
| hunyuanvideo_s55_c3072_bcast2d | 0.001 | 40.41 | 4.49 | 0.02 | 0.15 | **8.99x** |
| hunyuanvideo_s27030_c3072_bcast2d | 0.332 | 71.12 | 61.58 | 4.67 | 5.39 | **1.16x** |
| hunyuanvideo_s27085_c3072_bcast2d | 0.333 | 71.33 | 61.57 | 4.67 | 5.41 | **1.16x** |
| wan_ti2v_s18144_c3072_full_nc_fp32 | 0.669 | 127.58 | 102.22 | 5.24 | 6.54 | **1.25x** |
| wan_t2v_s37800_c5120_bcast11_fp32 | 0.774 | 264.18 | 138.29 | 2.93 | 5.60 | **1.91x** |
| wan_i2v_s37044_c5120_bcast11_fp32 | 0.759 | 258.77 | 136.15 | 2.93 | 5.57 | **1.90x** |

Non-production regression riders (correctness visibility through the full
benchmark machinery; not part of the headline): 4D per-frame 7.06x, fp16
2D-broadcast 9.16x, fp32 full3d 5.47x, EP2 with affine 7.50x, EP2 int64 index
7.95x, EP3 fp32 with affine 8.17x — all PASSED.

Full per-row distribution statistics (median/mean/std/min/p10/p90, raw
samples, inner-loop counts) are in the benchmark artifact
`bench/results.jsonl` (kept out of the PR per the repo's artifact policy;
regenerate with the command above).

## Why the candidate wins (roofline-style analysis)

Reference peak: B200 HBM3e ~= 8 TB/s. All three entry points are pure
memory-streaming kernels (arithmetic intensity << 1 FLOP/byte), so the bound
per row is bytes-moved / achievable bandwidth, plus per-call launch overhead.

1. **Small/medium rows (S = 19..4096; 9 of 19 rows, speedups 3.2-9.0x).**
   The Triton baseline is host-launch-bound: its wrapper performs Python
   broadcast normalization, expand/stride extraction, and Triton JIT launch
   machinery on every call — a measured ~33-40us floor per call (the device
   kernels themselves are microseconds). The candidate's whole host path is a
   single tvm-ffi call into C++ dispatch (~4.3-4.6us floor measured at S=19,
   where device time is negligible). This is real production overhead in
   back-to-back diffusion graphs, measured here under CUDA events with
   inner-loop amplification (gaps between back-to-back launches count).
2. **Large streaming rows (S = 8424..37800; 10 of 19 rows, 1.09-1.91x).**
   The candidate's 16B-vectorized kernels with evict-first hints for streams
   and read-only caching for reused modulation rows reach 4.99-7.60 TB/s
   (62-95% of nominal peak) versus the baseline's 2.93-5.61 TB/s. The largest
   gains are where the baseline is least efficient: the bf16-x/fp32-scale wan
   rows (2.93 -> 5.6 TB/s, 1.9x) and the 8424-token broadcast rows
   (3.0 -> 5.0 TB/s, 1.65-1.68x). The full-shape qwen-edit row, where the
   baseline is already strong (5.61 TB/s), still improves to 7.60 TB/s.
3. **Gated LayerNorm rows (1.09x / 1.13x).** Both sides must read x (and the
   residual pair) once and write 2 (3) full outputs. The candidate's exact-C
   single-block-per-row kernel (384 threads, one 16B-vector round, fp32
   register cache between passes, fused one-pass (sum, sumsq) block reduction
   with two barriers) removes the Triton version's 25% masked-lane waste at
   BLOCK_N=4096 and its extra reduction barriers. Achieved bandwidth: EP2
   3.10 -> 3.39 TB/s, EP3 4.88 -> 5.50 TB/s. NCU evidence on the active bound
   for these two kernels is summarized in `docs/dispatch.md` and the run log
   (both sides are far from the pure-streaming roof because per-row barrier
   latency, not DRAM, is the limiter at C=3072 with one block per row — the
   same structural bound applies to the baseline, which is why the honest win
   here is structural-overhead removal, ~1.1x).

## Optimization history (bounded attempts, all on the frozen workloads)

| version | change | production geomean | min row |
|---|---|---|---|
| v0 | generic correct port (scalar strided kernels, lean host path) | 0.9392 | 0.199 (hunyuanvideo 27k) |
| v1 | 16B-vectorized row-grid/flat EP1 paths with cache hints + runtime gates; exact-C register-cached vectorized EP2/EP3 row kernels | 2.7289 | 1.011 (gated EP2) |
| v2 (final) | fused one-pass (sum, sumsq) block reduction in the vectorized EP2/EP3 kernels (5 barriers -> 2 per row) | **2.7478** | **1.0937 (gated EP2)** |

Ideas considered and not kept (recorded for audit): 256-bit `ld.global.v4.u64`
loads (no headroom left on the rows that matter — full3d already at 7.6 TB/s,
gated rows barrier-bound, small rows host-bound); persistent/CLC-style
scheduling and multi-row blocks for EP2 (the remaining EP2 gap is ~1.4x of a
~46us row; structural complexity and re-validation cost outweigh the bounded
expected gain after the gate was met on every row — documented as the named
remaining bound, not pursued).

## Conclusion

The candidate is promoted under the agreed gate: headline geomean **2.7478x**
with every production row at or above **1.0937x** (no row below the 0.97
floor, no fallback dispatch needed). The dominant effects are (a) removal of
the baseline's ~33-40us per-call Python/Triton launch overhead on the many
small and medium production rows, and (b) 16B-vectorized streaming kernels at
5.0-7.6 TB/s on the large rows where the Triton tiles ran at 2.9-5.6 TB/s.
