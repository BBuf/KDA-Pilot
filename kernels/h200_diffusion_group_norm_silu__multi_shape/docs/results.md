# Final Results — h200_diffusion_group_norm_silu__multi_shape

**Headline (frozen 48-row production set, equal-weight geomean): 1.5010**
(arithmetic mean 1.5921, min 0.9449, max 4.0150; sum-of-medians wall
3424 us -> 2798 us = 1.2237x). 57/57 workloads PASSED; correctness suite
**210/210** green before timing. **Every timed row executes solution-owned
CUDA kernels** — the candidate contains no baseline routing of any kind.

- Run: ion8-h200 (NVIDIA H200, `REMOTE_GPU_ID=3`, idle before/after — see
  results.jsonl provenance), container `sglang_bbuf`, torch 2.11.0+cu130,
  CUDA 13.0, triton 3.6.0, tvm-ffi 0.1.9.
- Command: `CUDA_VISIBLE_DEVICES=3 python3 bench/benchmark.py --device cuda:0
  --out bench/results.jsonl` (frozen template policy: 7 trials, warmup 10,
  inner-loop to ~1000 us, deterministic interleaved A/B, isolated
  subprocesses, preallocated outputs on BOTH sides — see
  docs/benchmark_method.md).
- Baseline: upstream sglang main `133254086b` Triton kernels, copied locally
  (docs/baseline_source.md), driven through destination-passing local
  wrappers that replicate the copied launchers byte-for-byte except for the
  output buffer (verified bit-identical to the allocate-and-return entries).
- Harness validation under this exact contract: A/A geomean **0.9990**
  (8 spread rows, band 0.98-1.02).

## Per-regime summary (all solution-owned CUDA; dispatch in docs/dispatch.md)

| route | n | geomean | min | max |
|---|---:|---:|---:|---:|
| cuda one-pass, 256-thread blocks (gs < 32K) | 7 | 1.7141 | 1.2912 | 1.8843 |
| cuda one-pass, 1024-thread blocks (32K <= gs < 64K) | 5 | 1.8034 | 1.6928 | 1.8951 |
| cuda chunked 3-kernel (large) | 20 | 1.8689 | 1.1866 | 4.0150 |
| cuda giant 2-kernel (streaming hints) | 16 | 1.0167 | 0.9449 | 1.1715 |

## Per-row floor status (honest statement)

40/48 production rows are >= 0.97 (39 >= 1.0). **8 rows sit in
[0.9449, 0.9696]** — all of them, and only them, belong to one precisely
characterized class: giant groups whose per-channel spatial extent is a
multiple of 8192, where the copied baseline's chunked Triton kernels run
straddle-free with a hoisted-affine apply at their measured best (~81-85% of
H200 peak HBM). Ten measured candidate variants attacked this class
(occupancy fix to the 32-reg full-occupancy boundary, exact grids, fused
last-block finalize, zero-straddle per-shape tiles, `__ldcs`/`__stcs`
streaming hints, stats-tile sweeps, ILP split accumulators — history in
docs/dispatch.md); the best stable result is 3-6% short on these rows with
+-2-4% run-to-run swing. On the SAME giant bucket the candidate WINS wherever
the baseline straddles its chunk (0.99-1.17). The named bound: both
implementations sit near the same memory roofline on this class; the
baseline's single-kernel-family apply has a small structural edge there that
the two-kernel pipeline did not close within the bounded budget.

Resolution options surfaced for arbitration (the user's earlier DEC-6 ruling
sanctioned dispatch in exactly this situation; the round-0 review enforced
the immutable all-CUDA/0.97 text): (a) promote at 1.5010 with this documented
8-row bound; (b) re-instate rule-based local-baseline dispatch ONLY for
`gs >= 900K and spatial % 8192 == 0` (those rows become ~1.0; headline
~1.52; no row below ~0.97); (c) no-go (disproportionate at 1.50x overall).

## Roofline conclusion

- Largest production row `[1,256,17,256,256]` (group_size 8.9M, 570 MB fp16):
  traffic floor = 2 reads + 1 write = 1.71 GB. Baseline ~441 us = 3.88 TB/s
  ~= 81% of the 4.8 TB/s peak; candidate ~462 us = 3.70 TB/s ~= 77%
  (giant stats ~68-72% DRAM with ILP+streaming, giant apply ~85%).
- Candidate structural wins: small groups 1.29-1.89x (one CTA per group;
  1024-thread blocks for the crossover band lift per-SM memory parallelism
  where 32 resident CTAs starve the part — 0.90 -> 1.69-1.90 on those rows);
  large groups up to 4.02x (persistent chunked pipeline); straddle giants
  0.99-1.17x (two-segment vectorized tiles where the baseline drops to
  per-element affine).

## LTX upsampler diagnostics (production=false, wrapper path)

| diagnostic | speedup |
|---|---:|
| ltx 1x1024x16x8x12 bf16 | 1.7510 |
| ltx 1x1024x16x8x12 fp32 | 1.8453 |
| ltx 1x1024x16x16x24 bf16 | 3.1234 |
| ltx 1x1024x16x16x24 fp32 | 4.8878 |
| ltx 1x1024x16x32x48 bf16 | 1.2170 |

## Per-shape production table (48 rows, group_size ascending)

| workload | route | base med (us) | cand med (us) | speedup |
|---|---|---:|---:|---:|
| 1x512x2x12x10 | cuda one-pass (256 thr) | 21.62 | 11.47 | 1.8843 |
| 1x512x5x12x10 | cuda one-pass (256 thr) | 21.66 | 11.61 | 1.8653 |
| 1x512x2x32x10 | cuda one-pass (256 thr) | 21.34 | 11.41 | 1.8697 |
| 1x512x2x12x32 | cuda one-pass (256 thr) | 21.66 | 11.63 | 1.8625 |
| 1x512x2x24x20 | cuda one-pass (256 thr) | 21.47 | 11.41 | 1.8809 |
| 1x512x5x32x10 | cuda one-pass (256 thr) | 21.68 | 14.83 | 1.4626 |
| 1x512x5x12x32 | cuda one-pass (256 thr) | 21.71 | 16.81 | 1.2912 |
| 1x512x2x32x32 | cuda one-pass (1024 thr) | 21.46 | 11.53 | 1.8607 |
| 1x512x5x24x20 | cuda one-pass (1024 thr) | 21.83 | 11.52 | 1.8951 |
| 1x512x2x64x20 | cuda one-pass (1024 thr) | 21.47 | 11.54 | 1.8607 |
| 1x256x3x48x40 | cuda one-pass (1024 thr) | 21.51 | 12.53 | 1.7174 |
| 1x512x2x24x64 | cuda one-pass (1024 thr) | 22.10 | 13.06 | 1.6928 |
| 1x512x5x32x32 | cuda chunked 3-kernel | 33.53 | 25.39 | 1.3205 |
| 1x512x3x48x40 | cuda chunked 3-kernel | 38.70 | 25.92 | 1.4931 |
| 1x512x5x64x20 | cuda chunked 3-kernel | 42.81 | 25.63 | 1.6705 |
| 1x256x3x128x40 | cuda chunked 3-kernel | 51.94 | 25.78 | 2.0147 |
| 1x512x5x24x64 | cuda chunked 3-kernel | 51.93 | 25.37 | 2.0469 |
| 1x512x2x64x64 | cuda chunked 3-kernel | 55.39 | 25.82 | 2.1451 |
| 1x256x9x48x40 | cuda chunked 3-kernel | 58.75 | 25.52 | 2.3020 |
| 1x256x3x48x128 | cuda chunked 3-kernel | 63.25 | 25.56 | 2.4743 |
| 1x128x5x96x80 | cuda chunked 3-kernel | 66.82 | 25.86 | 2.5833 |
| 1x512x3x128x40 | cuda chunked 3-kernel | 103.37 | 25.75 | 4.0150 |
| 1x512x9x48x40 | cuda chunked 3-kernel | 59.12 | 27.56 | 2.1454 |
| 1x512x3x48x128 | cuda chunked 3-kernel | 57.98 | 28.10 | 2.0632 |
| 1x256x5x96x80 | cuda chunked 3-kernel | 58.47 | 28.88 | 2.0249 |
| 1x512x5x64x64 | cuda chunked 3-kernel | 58.19 | 29.90 | 1.9463 |
| 1x256x9x128x40 | cuda chunked 3-kernel | 59.20 | 34.60 | 1.7111 |
| 1x256x3x128x128 | cuda chunked 3-kernel | 57.54 | 35.89 | 1.6030 |
| 1x128x5x256x80 | cuda chunked 3-kernel | 57.92 | 38.25 | 1.5143 |
| 1x256x9x48x128 | cuda chunked 3-kernel | 59.67 | 41.13 | 1.4508 |
| 1x128x5x96x256 | cuda chunked 3-kernel | 58.66 | 46.60 | 1.2587 |
| 1x128x17x96x80 | cuda chunked 3-kernel | 58.58 | 49.37 | 1.1866 |
| 1x512x9x128x40 | cuda giant 2-kernel | 59.87 | 51.11 | 1.1715 |
| 1x512x3x128x128 | cuda giant 2-kernel | 60.47 | 54.50 | 1.1094 |
| 1x256x5x256x80 | cuda giant 2-kernel | 59.97 | 55.38 | 1.0830 |
| 1x512x9x48x128 | cuda giant 2-kernel | 65.43 | 58.02 | 1.1276 |
| 1x256x5x96x256 | cuda giant 2-kernel | 61.48 | 64.60 | 0.9517 |
| 1x256x17x96x80 | cuda giant 2-kernel | 72.99 | 68.69 | 1.0627 |
| 1x256x9x128x128 | cuda giant 2-kernel | 73.27 | 76.44 | 0.9586 |
| 1x128x5x256x256 | cuda giant 2-kernel | 79.85 | 82.07 | 0.9729 |
| 1x128x17x256x80 | cuda giant 2-kernel | 92.08 | 86.05 | 1.0701 |
| 1x128x17x96x256 | cuda giant 2-kernel | 96.76 | 100.22 | 0.9655 |
| 1x512x9x128x128 | cuda giant 2-kernel | 132.32 | 137.07 | 0.9653 |
| 1x256x5x256x256 | cuda giant 2-kernel | 144.50 | 149.04 | 0.9696 |
| 1x256x17x256x80 | cuda giant 2-kernel | 168.20 | 160.34 | 1.0491 |
| 1x256x17x96x256 | cuda giant 2-kernel | 176.90 | 187.21 | 0.9449 |
| 1x128x17x256x256 | cuda giant 2-kernel | 227.99 | 239.61 | 0.9515 |
| 1x256x17x256x256 | cuda giant 2-kernel | 440.82 | 461.62 | 0.9549 |

Raw per-trial samples and provenance (GPU state before/after, versions, settings) live in `bench/results.jsonl` (kept local + remote; excluded from the PR per the artifact policy — this table is the committed record).
