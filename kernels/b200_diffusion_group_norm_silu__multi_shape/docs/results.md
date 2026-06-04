# Results — `b200_diffusion_group_norm_silu__multi_shape`

## Headline (frozen harness, definitive run 2026-06-05)

- Equal-weight geometric mean speedup over all **160 production rows**:
  **2.2835x** (arithmetic mean 2.4866x, secondary metric).
- 172/172 workloads PASSED in-benchmark correctness
  (`required_matched_ratio = 1.0`); the standalone correctness suite
  (`bench/correctness.py`, both sides, all sections) passed with 0 failing
  checks in the same configuration (Run 10, `docs/run_log.md`).
- Command: `CUDA_VISIBLE_DEVICES=1 python3 bench/benchmark.py --device cuda:0
  --out bench/results_headline.jsonl` (workloads frozen,
  `bench/gen_workloads.py --check` green, sha256
  `1255972107562ab14e9b04c3e433a9a5334b169eadf43e6b0f50f1cf7c46eeb8`).
- Environment: ion-b200 / container `sglang_bbuf`, NVIDIA B200 (GPU 1,
  pinned via `CUDA_VISIBLE_DEVICES=1`; idle before/after — provenance block
  embedded in `bench/results_headline.jsonl`), Python 3.12.3,
  torch 2.11.0+cu130, CUDA 13.0, triton 3.6.0, tvm-ffi 0.1.9.
- Baseline: copied upstream SGLang Triton implementation @ `main`
  `133254086bf1f5b887c8c99d311719102d58a7eb` (see `docs/baseline_source.md`).
- Candidate source: `solution/kernel.cu` + `solution/binding.py` at the
  commit carrying this document.

## Promotion Gates

- `geomean > 1.0`: **PASS** (2.2835).
- `no production row < 0.97x`: 158/160 rows pass directly. The two readings
  below the floor are `hv_apply_1x512x9x128x128_C` (0.9587) and
  `hv_triton_1x512x9x128x128_C` (0.9665) — both in the ROUTED bucket where
  the candidate resolves to the *identical* baseline callable, so a real
  regression is impossible by construction. The readings are the
  characterized dirty-L2 order-debt measurement artifact on ~75-150 MB-output
  rows: the direct steady-state interleaved probe on this exact shape
  measures the candidate path at 0.997 of baseline (delta 0.21-0.37 us /call),
  and the identical-code twin read 0.9810 in the 21-trial order-balanced run.
  Full characterization with raw evidence: `docs/dispatch.md` ("Measured
  Residual on Routed Giant Rows"), `bench/results_marginal21.jsonl`,
  `bench/results_routed.jsonl`. Reported as explained residuals per the
  no-regression ruling (DEC-3 / AC-5.2 language: residuals must be explained
  with evidence).

## Per-Bucket Geomeans (production rows)

| Layout | Size bucket | n | geomean | min | max |
|---|---|---|---|---|---|
| C | small | 24 | 2.4240 | 1.4027 | 3.8218 |
| C | mid | 52 | 3.1122 | 1.6834 | 4.9335 |
| C | large | 20 | 1.1320 | 0.9587 | 1.6249 |
| NC | small | 24 | 2.3239 | 1.8680 | 3.0692 |
| NC | mid | 30 | 2.2979 | 1.4468 | 3.1573 |
| NC | large | 10 | 1.5137 | 1.1544 | 3.6131 |

## Where the Speedup Comes From (roofline-style accounting)

- **Contiguous mid (64K-1M elems, n=52, 3.11x)**: the upstream one-pass
  Triton path launches only `B*G = 32` CTAs at `B=1` — under 22% of B200's
  148 SMs. The candidate splits each group across CTAs (vectorized stats with
  a deterministic last-CTA finalize + a division-free apply), filling the
  machine. This is an occupancy/latency win, not a traffic win: both sides
  move 2 reads + 1 write.
- **Contiguous small (<64K, n=24, 2.42x)**: same underfill effect at smaller
  sizes plus 16-byte vectorization; one CTA per group remains optimal below
  `GNS_SMALL_MAX = 65536` (re-derived on B200).
- **Channels-last rows (n=64, 1.51-2.32x)**: the baseline materializes
  `x.contiguous()` before its kernel — on the NCU probe row the copy alone
  was 121.6 us of the 186 us baseline (NC->C transpose copy, ~3.6% DRAM
  utilization). The candidate reads the channels-last layout natively
  (position-major 16B vectors), computes all 32 groups' statistics in one
  sweep, and writes the contiguous output through padded shared-memory tiles
  (2-way max bank conflicts) — 3 passes instead of 5, plus better access
  patterns on both remaining passes.
- **Contiguous giant (>2M elems)**: the baseline chunked pipeline already
  runs this 2R+1W pattern near the achievable bandwidth (~5 TB/s-class
  effective); after three NCU-backed optimization rounds the split path
  still measured 0.93-0.96x, so the bucket routes to the baseline-equivalent
  path (`GNS_CONT_FALLBACK_MIN = 2,000,000`), giving ~1.00x by construction.
  A one-read-pass algorithm is excluded: affine+silu cannot be applied before
  the group statistics exist, and giant groups cannot be cached on-chip.
  Bounded-attempt evidence trail: `docs/dispatch.md`.
- fp32 rows exist only in the correctness grid (never production) and run
  the generic strided kernel with double accumulation.

## Dispatch Summary

See `docs/dispatch.md` for bucket conditions, per-bucket evidence, env knobs
(`GNS_SMALL_MAX`, `GNS_CHUNK`, `GNS_CONT_FALLBACK_MIN`), the
NCU-evidence-backed bounded attempts on the giant-contiguous bucket, and the
order-debt residual characterization. Routed rows are counted in the geomean
like every other row.

## Reproduction

```bash
# correctness (both sides, all sections)
CUDA_VISIBLE_DEVICES=<idle B200> python3 bench/correctness.py --device cuda:0 --side both
# workload freeze check
python3 bench/gen_workloads.py --check
# full benchmark
CUDA_VISIBLE_DEVICES=<idle B200> python3 bench/benchmark.py --device cuda:0 --out bench/results_headline.jsonl
# summary / gates / table
python3 bench/summarize_results.py bench/results_headline.jsonl --markdown
```

## Per-Row Results (production, definitive run)

Columns: per-side stats are median/mean/std/min/p10/p90 in microseconds;
speedup = baseline_median / candidate_median.

| id | layout | function | baseline (us) | candidate (us) | speedup |
|---|---|---|---|---|---|
| hv_apply_1x128x17x256x256_C | C | apply_group_norm_silu | 171.98/172.34/0.95/171.13/171.47/173.42 | 173.08/173.30/0.83/172.39/172.39/174.28 | 0.9937 |
| hv_apply_1x128x17x256x256_NC | NC | apply_group_norm_silu | 2751.74/2751.20/3.26/2746.88/2747.23/2754.41 | 761.60/761.37/2.37/757.44/758.42/763.53 | 3.6131 |
| hv_apply_1x128x17x256x80_C | C | apply_group_norm_silu | 96.50/96.79/1.22/95.27/95.48/98.10 | 71.01/70.95/0.32/70.40/70.57/71.26 | 1.3590 |
| hv_apply_1x128x17x256x80_NC | NC | apply_group_norm_silu | 273.98/273.66/0.93/272.25/272.71/274.59 | 212.07/212.21/0.76/211.07/211.36/213.06 | 1.2920 |
| hv_apply_1x128x17x96x256_C | C | apply_group_norm_silu | 94.15/94.74/2.62/92.03/92.48/97.29 | 82.38/82.30/0.44/81.67/81.78/82.72 | 1.1428 |
| hv_apply_1x128x17x96x256_NC | NC | apply_group_norm_silu | 302.97/303.04/0.64/302.23/302.43/303.75 | 262.44/263.89/2.12/262.14/262.21/266.29 | 1.1544 |
| hv_apply_1x128x17x96x80_C | C | apply_group_norm_silu | 95.77/95.56/1.53/93.81/94.01/97.04 | 28.96/28.95/0.04/28.87/28.90/28.98 | 3.3074 |
| hv_apply_1x128x17x96x80_NC | NC | apply_group_norm_silu | 113.94/113.23/1.69/110.31/111.47/114.66 | 78.30/78.05/0.61/76.85/77.46/78.52 | 1.4550 |
| hv_apply_1x128x5x256x256_C | C | apply_group_norm_silu | 97.28/96.76/1.28/94.86/95.34/98.01 | 67.71/67.79/0.44/67.15/67.38/68.35 | 1.4368 |
| hv_apply_1x128x5x256x256_NC | NC | apply_group_norm_silu | 238.83/238.77/0.27/238.33/238.44/239.03 | 201.91/201.86/0.35/201.32/201.51/202.17 | 1.1828 |
| hv_apply_1x128x5x256x80_C | C | apply_group_norm_silu | 95.19/95.03/1.37/92.43/93.87/96.11 | 26.87/26.87/0.03/26.82/26.84/26.91 | 3.5429 |
| hv_apply_1x128x5x256x80_NC | NC | apply_group_norm_silu | 108.46/108.26/1.56/106.15/106.64/109.89 | 64.65/64.47/0.35/64.02/64.05/64.78 | 1.6778 |
| hv_apply_1x128x5x96x256_C | C | apply_group_norm_silu | 93.11/93.03/1.87/90.05/90.78/94.99 | 28.93/28.93/0.03/28.90/28.90/28.96 | 3.2183 |
| hv_apply_1x128x5x96x256_NC | NC | apply_group_norm_silu | 108.01/107.99/2.10/105.22/105.63/110.56 | 74.65/74.55/0.30/74.11/74.18/74.84 | 1.4468 |
| hv_apply_1x128x5x96x80_C | C | apply_group_norm_silu | 70.67/70.63/0.18/70.40/70.44/70.85 | 16.65/16.65/0.03/16.59/16.61/16.67 | 4.2433 |
| hv_apply_1x128x5x96x80_NC | NC | apply_group_norm_silu | 100.89/100.93/0.18/100.75/100.78/101.16 | 35.05/35.08/0.05/35.03/35.03/35.14 | 2.8783 |
| hv_apply_1x256x17x256x256_C | C | apply_group_norm_silu | 330.22/330.32/4.51/325.42/326.24/335.50 | 331.10/330.59/2.80/327.48/327.50/333.58 | 0.9973 |
| hv_apply_1x256x17x256x80_C | C | apply_group_norm_silu | 154.19/154.50/0.68/153.88/153.88/155.32 | 155.66/155.58/0.75/154.60/154.68/156.30 | 0.9906 |
| hv_apply_1x256x17x96x256_C | C | apply_group_norm_silu | 136.65/136.92/0.88/135.76/136.01/137.89 | 137.07/137.65/1.20/136.46/136.75/138.93 | 0.9969 |
| hv_apply_1x256x17x96x80_C | C | apply_group_norm_silu | 93.88/94.10/1.84/91.52/92.12/96.16 | 55.77/55.79/0.04/55.75/55.75/55.84 | 1.6834 |
| hv_apply_1x256x3x128x128_C | C | apply_group_norm_silu | 96.96/96.78/1.91/94.36/94.56/98.75 | 26.89/26.88/0.02/26.84/26.86/26.90 | 3.6056 |
| hv_apply_1x256x3x128x128_NC | NC | apply_group_norm_silu | 109.79/110.19/1.24/108.42/109.14/111.82 | 56.54/56.47/0.20/56.07/56.26/56.62 | 1.9417 |
| hv_apply_1x256x3x128x40_C | C | apply_group_norm_silu | 54.79/54.81/0.20/54.63/54.66/54.98 | 16.66/16.81/0.40/16.61/16.62/17.12 | 3.2881 |
| hv_apply_1x256x3x128x40_NC | NC | apply_group_norm_silu | 81.67/81.72/1.00/80.79/80.83/82.73 | 25.95/25.96/0.07/25.88/25.88/26.03 | 3.1474 |
| hv_apply_1x256x3x48x128_C | C | apply_group_norm_silu | 66.57/66.61/0.24/66.37/66.40/66.84 | 16.66/16.66/0.02/16.63/16.63/16.68 | 3.9959 |
| hv_apply_1x256x3x48x128_NC | NC | apply_group_norm_silu | 94.97/94.98/0.57/94.31/94.50/95.61 | 30.08/30.09/0.04/30.03/30.05/30.14 | 3.1573 |
| hv_apply_1x256x3x48x40_C | C | apply_group_norm_silu | 34.42/34.51/0.48/33.76/34.07/35.09 | 22.70/22.65/0.11/22.46/22.52/22.75 | 1.5163 |
| hv_apply_1x256x3x48x40_NC | NC | apply_group_norm_silu | 46.37/46.75/1.69/44.93/45.25/48.93 | 23.78/23.76/0.10/23.53/23.67/23.82 | 1.9502 |
| hv_apply_1x256x5x256x256_C | C | apply_group_norm_silu | 108.34/108.41/0.37/108.14/108.15/108.74 | 108.70/109.57/1.64/108.17/108.18/111.78 | 0.9967 |
| hv_apply_1x256x5x256x80_C | C | apply_group_norm_silu | 96.00/97.19/2.71/95.03/95.17/100.13 | 43.59/43.60/0.14/43.45/43.46/43.73 | 2.2022 |
| hv_apply_1x256x5x96x256_C | C | apply_group_norm_silu | 93.59/93.23/1.20/91.13/91.95/94.33 | 52.73/52.74/0.35/52.31/52.33/53.10 | 1.7748 |
| hv_apply_1x256x5x96x80_C | C | apply_group_norm_silu | 94.06/94.28/2.24/91.36/91.88/96.88 | 24.83/24.82/0.04/24.75/24.78/24.86 | 3.7887 |
| hv_apply_1x256x9x128x128_C | C | apply_group_norm_silu | 97.22/97.92/1.70/95.86/96.28/99.91 | 60.86/60.98/0.56/60.26/60.53/61.66 | 1.5974 |
| hv_apply_1x256x9x128x128_NC | NC | apply_group_norm_silu | 212.33/212.22/0.34/211.62/211.85/212.54 | 169.25/169.21/0.95/168.17/168.21/170.27 | 1.2545 |
| hv_apply_1x256x9x128x40_C | C | apply_group_norm_silu | 93.11/93.04/1.59/90.73/91.35/94.65 | 24.85/24.86/0.04/24.82/24.82/24.91 | 3.7472 |
| hv_apply_1x256x9x128x40_NC | NC | apply_group_norm_silu | 111.11/110.78/2.05/108.71/108.72/113.12 | 56.46/56.49/0.13/56.35/56.38/56.64 | 1.9680 |
| hv_apply_1x256x9x48x128_C | C | apply_group_norm_silu | 97.58/97.38/1.50/95.32/95.65/98.96 | 26.92/26.92/0.03/26.89/26.90/26.95 | 3.6250 |
| hv_apply_1x256x9x48x128_NC | NC | apply_group_norm_silu | 106.84/106.37/1.00/104.70/105.14/107.26 | 61.92/62.03/0.36/61.49/61.69/62.39 | 1.7255 |
| hv_apply_1x256x9x48x40_C | C | apply_group_norm_silu | 62.82/62.86/0.41/62.37/62.48/63.33 | 16.63/16.64/0.03/16.59/16.61/16.68 | 3.7780 |
| hv_apply_1x256x9x48x40_NC | NC | apply_group_norm_silu | 90.69/90.79/0.32/90.38/90.46/91.16 | 28.94/28.94/0.03/28.90/28.90/28.97 | 3.1339 |
| hv_apply_1x512x2x12x10_C | C | apply_group_norm_silu | 33.72/34.00/0.61/33.36/33.46/34.78 | 9.48/9.44/0.20/9.19/9.22/9.68 | 3.5566 |
| hv_apply_1x512x2x12x10_NC | NC | apply_group_norm_silu | 44.72/44.43/0.69/43.39/43.45/44.96 | 16.61/16.62/0.03/16.59/16.59/16.65 | 2.6922 |
| hv_apply_1x512x2x12x32_C | C | apply_group_norm_silu | 32.86/33.11/0.49/32.68/32.74/33.74 | 9.31/9.34/0.21/9.06/9.12/9.61 | 3.5280 |
| hv_apply_1x512x2x12x32_NC | NC | apply_group_norm_silu | 54.57/58.47/10.53/46.73/48.44/71.00 | 17.78/17.76/0.06/17.67/17.69/17.84 | 3.0692 |
| hv_apply_1x512x2x24x20_C | C | apply_group_norm_silu | 44.86/46.43/9.53/34.16/36.52/58.45 | 11.74/12.44/2.00/10.31/10.32/14.75 | 3.8218 |
| hv_apply_1x512x2x24x20_NC | NC | apply_group_norm_silu | 44.85/44.88/0.86/43.89/43.98/45.98 | 17.67/17.68/0.02/17.65/17.66/17.70 | 2.5380 |
| hv_apply_1x512x2x24x64_C | C | apply_group_norm_silu | 31.95/32.19/0.45/31.76/31.77/32.75 | 22.78/22.77/0.02/22.75/22.75/22.80 | 1.4027 |
| hv_apply_1x512x2x24x64_NC | NC | apply_group_norm_silu | 44.04/44.42/1.41/43.13/43.20/46.16 | 20.73/20.72/0.04/20.67/20.67/20.76 | 2.1241 |
| hv_apply_1x512x2x32x10_C | C | apply_group_norm_silu | 32.94/33.02/0.63/32.42/32.43/33.74 | 8.84/8.90/0.15/8.73/8.73/9.09 | 3.7274 |
| hv_apply_1x512x2x32x10_NC | NC | apply_group_norm_silu | 44.40/44.49/1.04/43.09/43.29/45.68 | 20.62/20.60/0.07/20.47/20.52/20.65 | 2.1533 |
| hv_apply_1x512x2x32x32_C | C | apply_group_norm_silu | 33.21/32.98/0.40/32.16/32.56/33.24 | 16.59/16.61/0.05/16.57/16.57/16.66 | 2.0019 |
| hv_apply_1x512x2x32x32_NC | NC | apply_group_norm_silu | 43.39/43.46/0.74/42.12/42.72/44.13 | 18.70/18.69/0.04/18.64/18.65/18.72 | 2.3206 |
| hv_apply_1x512x2x64x20_C | C | apply_group_norm_silu | 33.25/33.49/0.53/33.01/33.08/34.11 | 19.04/19.04/0.08/18.95/18.95/19.12 | 1.7462 |
| hv_apply_1x512x2x64x20_NC | NC | apply_group_norm_silu | 44.06/43.82/1.12/42.27/42.72/44.92 | 21.73/21.75/0.02/21.73/21.73/21.77 | 2.0272 |
| hv_apply_1x512x2x64x64_C | C | apply_group_norm_silu | 58.88/58.89/0.10/58.78/58.79/58.98 | 16.65/16.66/0.04/16.64/16.64/16.70 | 3.5357 |
| hv_apply_1x512x2x64x64_NC | NC | apply_group_norm_silu | 85.82/85.77/0.31/85.40/85.43/86.10 | 27.32/27.34/0.09/27.20/27.25/27.45 | 3.1411 |
| hv_apply_1x512x3x128x128_C | C | apply_group_norm_silu | 94.92/94.69/1.02/92.92/93.64/95.59 | 41.59/41.55/0.10/41.42/41.43/41.65 | 2.2820 |
| hv_apply_1x512x3x128x40_C | C | apply_group_norm_silu | 107.45/107.45/0.18/107.23/107.27/107.67 | 21.80/21.79/0.03/21.72/21.76/21.82 | 4.9286 |
| hv_apply_1x512x3x48x128_C | C | apply_group_norm_silu | 95.90/95.57/1.16/93.11/94.46/96.42 | 22.37/22.43/0.16/22.19/22.29/22.61 | 4.2860 |
| hv_apply_1x512x3x48x40_C | C | apply_group_norm_silu | 40.81/40.77/0.21/40.45/40.54/41.01 | 16.64/16.64/0.03/16.60/16.60/16.66 | 2.4522 |
| hv_apply_1x512x5x12x10_C | C | apply_group_norm_silu | 32.59/34.23/2.42/32.15/32.33/37.47 | 9.40/9.48/0.33/9.20/9.20/9.83 | 3.4660 |
| hv_apply_1x512x5x12x10_NC | NC | apply_group_norm_silu | 45.71/46.50/2.68/44.45/44.76/48.80 | 17.98/17.94/0.11/17.77/17.82/18.05 | 2.5420 |
| hv_apply_1x512x5x12x32_C | C | apply_group_norm_silu | 32.65/33.06/0.72/32.41/32.41/33.87 | 16.64/16.64/0.02/16.61/16.62/16.67 | 1.9623 |
| hv_apply_1x512x5x12x32_NC | NC | apply_group_norm_silu | 44.29/44.29/0.66/43.40/43.43/44.92 | 18.67/18.67/0.02/18.63/18.65/18.70 | 2.3725 |
| hv_apply_1x512x5x24x20_C | C | apply_group_norm_silu | 34.11/34.06/0.23/33.72/33.76/34.27 | 18.69/18.68/0.03/18.63/18.64/18.71 | 1.8249 |
| hv_apply_1x512x5x24x20_NC | NC | apply_group_norm_silu | 44.82/44.89/1.17/43.25/43.78/46.21 | 18.72/18.73/0.03/18.69/18.70/18.75 | 2.3941 |
| hv_apply_1x512x5x24x64_C | C | apply_group_norm_silu | 54.82/54.90/0.23/54.69/54.73/55.12 | 16.64/16.65/0.04/16.60/16.61/16.70 | 3.2937 |
| hv_apply_1x512x5x24x64_NC | NC | apply_group_norm_silu | 80.95/80.74/0.45/80.01/80.21/81.14 | 26.88/26.88/0.03/26.84/26.84/26.92 | 3.0109 |
| hv_apply_1x512x5x32x10_C | C | apply_group_norm_silu | 33.61/33.53/0.48/32.80/32.92/34.04 | 14.44/14.85/1.06/14.43/14.44/15.58 | 2.3272 |
| hv_apply_1x512x5x32x10_NC | NC | apply_group_norm_silu | 44.21/44.61/1.35/43.40/43.55/46.06 | 20.73/20.72/0.05/20.67/20.67/20.78 | 2.1325 |
| hv_apply_1x512x5x32x32_C | C | apply_group_norm_silu | 36.50/36.54/0.33/36.10/36.22/36.92 | 16.64/16.63/0.04/16.56/16.59/16.68 | 2.1942 |
| hv_apply_1x512x5x32x32_NC | NC | apply_group_norm_silu | 53.09/54.63/3.64/52.86/52.87/57.84 | 24.83/24.83/0.03/24.79/24.80/24.86 | 2.1377 |
| hv_apply_1x512x5x64x20_C | C | apply_group_norm_silu | 44.70/44.71/0.20/44.45/44.50/44.95 | 16.65/16.64/0.04/16.58/16.60/16.69 | 2.6843 |
| hv_apply_1x512x5x64x20_NC | NC | apply_group_norm_silu | 68.15/68.28/0.26/68.01/68.04/68.60 | 26.09/26.14/0.16/25.97/26.01/26.31 | 2.6116 |
| hv_apply_1x512x5x64x64_C | C | apply_group_norm_silu | 97.06/95.99/3.02/92.41/92.47/98.83 | 25.09/25.11/0.10/24.99/25.01/25.23 | 3.8686 |
| hv_apply_1x512x5x64x64_NC | NC | apply_group_norm_silu | 105.79/105.10/2.27/101.81/101.95/107.16 | 51.67/51.65/0.08/51.51/51.55/51.73 | 2.0476 |
| hv_apply_1x512x9x128x128_C | C | apply_group_norm_silu | 99.96/99.92/0.36/99.49/99.53/100.34 | 104.27/104.08/2.18/100.66/102.00/106.27 | 0.9587 |
| hv_apply_1x512x9x128x40_C | C | apply_group_norm_silu | 101.16/102.86/8.08/97.55/98.00/109.37 | 39.64/39.54/0.13/39.38/39.40/39.65 | 2.5521 |
| hv_apply_1x512x9x48x128_C | C | apply_group_norm_silu | 95.06/94.74/1.20/92.87/93.11/95.86 | 47.75/47.79/0.19/47.57/47.59/48.00 | 1.9907 |
| hv_apply_1x512x9x48x40_C | C | apply_group_norm_silu | 93.11/94.37/2.72/91.87/92.07/98.17 | 22.77/22.78/0.06/22.70/22.72/22.83 | 4.0900 |
| hv_triton_1x128x17x256x256_C | C | triton_group_norm_silu | 172.56/172.44/0.49/171.68/171.87/172.92 | 172.41/172.83/1.03/171.98/172.02/173.99 | 1.0009 |
| hv_triton_1x128x17x256x256_NC | NC | triton_group_norm_silu | 2749.09/2748.88/3.90/2744.77/2745.31/2753.50 | 767.46/764.96/4.63/757.58/759.98/769.17 | 3.5821 |
| hv_triton_1x128x17x256x80_C | C | triton_group_norm_silu | 96.69/96.54/0.66/95.52/95.75/97.14 | 71.01/71.01/0.29/70.47/70.75/71.26 | 1.3617 |
| hv_triton_1x128x17x256x80_NC | NC | triton_group_norm_silu | 273.56/273.33/0.88/271.48/272.41/273.95 | 212.35/212.54/0.83/211.44/211.61/213.38 | 1.2883 |
| hv_triton_1x128x17x96x256_C | C | triton_group_norm_silu | 99.41/100.40/2.82/97.83/97.84/103.13 | 82.20/82.26/0.34/81.90/81.90/82.72 | 1.2093 |
| hv_triton_1x128x17x96x256_NC | NC | triton_group_norm_silu | 302.54/302.46/0.55/301.57/301.79/303.00 | 261.66/261.94/1.53/259.51/260.37/263.57 | 1.1562 |
| hv_triton_1x128x17x96x80_C | C | triton_group_norm_silu | 93.91/93.82/1.49/91.64/92.10/95.41 | 28.96/28.97/0.04/28.91/28.93/29.01 | 3.2426 |
| hv_triton_1x128x17x96x80_NC | NC | triton_group_norm_silu | 123.93/123.00/3.91/117.12/118.49/126.21 | 78.10/78.13/0.56/77.09/77.67/78.73 | 1.5868 |
| hv_triton_1x128x5x256x256_C | C | triton_group_norm_silu | 96.03/96.88/2.14/94.05/94.94/99.50 | 67.58/67.61/0.38/67.14/67.18/67.99 | 1.4209 |
| hv_triton_1x128x5x256x256_NC | NC | triton_group_norm_silu | 239.33/239.32/0.42/238.66/238.94/239.69 | 202.30/201.99/0.75/200.88/200.97/202.62 | 1.1831 |
| hv_triton_1x128x5x256x80_C | C | triton_group_norm_silu | 94.40/95.73/2.40/93.58/93.60/98.35 | 26.88/26.89/0.01/26.87/26.87/26.90 | 3.5117 |
| hv_triton_1x128x5x256x80_NC | NC | triton_group_norm_silu | 107.11/107.45/0.98/106.34/106.53/108.43 | 64.47/64.45/0.19/64.15/64.23/64.66 | 1.6613 |
| hv_triton_1x128x5x96x256_C | C | triton_group_norm_silu | 96.68/97.19/2.97/94.73/95.23/99.80 | 28.95/28.95/0.03/28.92/28.93/28.98 | 3.3397 |
| hv_triton_1x128x5x96x256_NC | NC | triton_group_norm_silu | 109.32/109.59/1.67/106.95/108.22/111.10 | 74.17/74.11/0.37/73.41/73.75/74.45 | 1.4740 |
| hv_triton_1x128x5x96x80_C | C | triton_group_norm_silu | 70.54/70.58/0.16/70.38/70.44/70.79 | 16.63/16.65/0.03/16.61/16.62/16.68 | 4.2410 |
| hv_triton_1x128x5x96x80_NC | NC | triton_group_norm_silu | 100.66/100.75/0.23/100.53/100.56/101.05 | 34.99/35.03/0.13/34.82/34.91/35.15 | 2.8768 |
| hv_triton_1x256x17x256x256_C | C | triton_group_norm_silu | 329.15/329.35/3.53/326.04/326.07/333.10 | 332.02/331.76/3.03/327.58/328.28/334.92 | 0.9914 |
| hv_triton_1x256x17x256x80_C | C | triton_group_norm_silu | 155.72/155.53/0.62/154.35/154.80/156.00 | 156.01/156.55/1.25/155.28/155.59/157.99 | 0.9981 |
| hv_triton_1x256x17x96x256_C | C | triton_group_norm_silu | 136.78/136.87/0.74/135.53/136.13/137.60 | 137.59/137.67/0.67/136.74/136.90/138.47 | 0.9941 |
| hv_triton_1x256x17x96x80_C | C | triton_group_norm_silu | 96.75/96.52/1.89/94.10/94.47/98.63 | 55.77/55.80/0.07/55.73/55.75/55.88 | 1.7347 |
| hv_triton_1x256x3x128x128_C | C | triton_group_norm_silu | 93.94/94.25/2.15/91.73/92.27/96.38 | 26.88/26.87/0.03/26.82/26.83/26.89 | 3.4950 |
| hv_triton_1x256x3x128x128_NC | NC | triton_group_norm_silu | 106.02/107.11/2.31/105.11/105.13/109.70 | 56.59/56.53/0.13/56.28/56.36/56.62 | 1.8735 |
| hv_triton_1x256x3x128x40_C | C | triton_group_norm_silu | 55.14/55.34/0.63/54.62/54.72/55.99 | 16.80/17.24/1.03/16.64/16.67/18.23 | 3.2813 |
| hv_triton_1x256x3x128x40_NC | NC | triton_group_norm_silu | 81.12/80.96/0.42/80.39/80.41/81.38 | 25.91/25.91/0.05/25.85/25.85/25.96 | 3.1303 |
| hv_triton_1x256x3x48x128_C | C | triton_group_norm_silu | 66.73/66.69/0.10/66.54/66.58/66.79 | 16.65/16.66/0.02/16.63/16.63/16.68 | 4.0080 |
| hv_triton_1x256x3x48x128_NC | NC | triton_group_norm_silu | 94.56/94.63/0.28/94.40/94.42/94.96 | 30.16/30.15/0.04/30.08/30.12/30.19 | 3.1359 |
| hv_triton_1x256x3x48x40_C | C | triton_group_norm_silu | 34.29/36.06/4.65/33.11/33.60/40.05 | 22.71/22.62/0.17/22.37/22.37/22.74 | 1.5099 |
| hv_triton_1x256x3x48x40_NC | NC | triton_group_norm_silu | 44.43/44.49/0.62/43.64/43.87/45.20 | 23.78/23.76/0.10/23.55/23.65/23.84 | 1.8680 |
| hv_triton_1x256x5x256x256_C | C | triton_group_norm_silu | 108.40/108.63/0.46/108.10/108.19/109.19 | 109.55/110.81/2.65/108.18/108.56/113.76 | 0.9896 |
| hv_triton_1x256x5x256x80_C | C | triton_group_norm_silu | 95.48/95.87/1.11/94.42/94.76/97.19 | 43.68/43.66/0.10/43.52/43.55/43.77 | 2.1860 |
| hv_triton_1x256x5x96x256_C | C | triton_group_norm_silu | 102.40/101.98/4.29/94.46/97.24/106.27 | 52.65/52.75/0.26/52.42/52.50/53.01 | 1.9449 |
| hv_triton_1x256x5x96x80_C | C | triton_group_norm_silu | 94.78/96.61/2.79/94.17/94.22/99.95 | 24.84/24.84/0.05/24.78/24.79/24.89 | 3.8155 |
| hv_triton_1x256x9x128x128_C | C | triton_group_norm_silu | 99.04/99.12/2.00/96.01/96.98/101.38 | 60.95/60.95/0.33/60.45/60.58/61.34 | 1.6249 |
| hv_triton_1x256x9x128x128_NC | NC | triton_group_norm_silu | 211.73/211.89/0.65/211.20/211.24/212.67 | 169.28/169.05/0.71/167.77/168.30/169.66 | 1.2508 |
| hv_triton_1x256x9x128x40_C | C | triton_group_norm_silu | 96.23/96.19/1.71/93.34/94.09/97.81 | 24.87/24.88/0.07/24.80/24.82/24.97 | 3.8696 |
| hv_triton_1x256x9x128x40_NC | NC | triton_group_norm_silu | 108.83/109.14/1.55/106.82/107.92/110.70 | 56.52/56.53/0.16/56.32/56.35/56.72 | 1.9256 |
| hv_triton_1x256x9x48x128_C | C | triton_group_norm_silu | 97.27/96.50/2.19/93.83/94.04/98.63 | 26.91/26.90/0.04/26.82/26.86/26.94 | 3.6152 |
| hv_triton_1x256x9x48x128_NC | NC | triton_group_norm_silu | 109.04/109.16/1.92/106.20/107.32/111.41 | 61.87/61.91/0.20/61.68/61.72/62.13 | 1.7624 |
| hv_triton_1x256x9x48x40_C | C | triton_group_norm_silu | 63.38/63.25/0.41/62.78/62.78/63.68 | 16.66/16.66/0.04/16.62/16.62/16.71 | 3.8049 |
| hv_triton_1x256x9x48x40_NC | NC | triton_group_norm_silu | 90.54/90.65/0.37/90.27/90.29/91.13 | 28.93/28.93/0.04/28.85/28.88/28.96 | 3.1293 |
| hv_triton_1x512x2x12x10_C | C | triton_group_norm_silu | 33.64/33.77/0.36/33.26/33.44/34.21 | 9.36/9.44/0.20/9.22/9.25/9.70 | 3.5939 |
| hv_triton_1x512x2x12x10_NC | NC | triton_group_norm_silu | 44.77/44.97/0.45/44.56/44.63/45.50 | 16.62/16.63/0.05/16.58/16.58/16.68 | 2.6944 |
| hv_triton_1x512x2x12x32_C | C | triton_group_norm_silu | 32.43/32.49/0.44/31.99/32.06/32.98 | 8.72/8.72/0.11/8.63/8.63/8.84 | 3.7198 |
| hv_triton_1x512x2x12x32_NC | NC | triton_group_norm_silu | 45.79/46.06/0.68/45.12/45.42/46.81 | 17.68/17.68/0.02/17.66/17.66/17.71 | 2.5900 |
| hv_triton_1x512x2x24x20_C | C | triton_group_norm_silu | 35.83/35.87/0.65/35.04/35.18/36.59 | 10.40/10.49/0.19/10.33/10.34/10.77 | 3.4461 |
| hv_triton_1x512x2x24x20_NC | NC | triton_group_norm_silu | 43.63/43.61/0.77/42.70/42.87/44.34 | 17.68/17.68/0.02/17.66/17.66/17.69 | 2.4678 |
| hv_triton_1x512x2x24x64_C | C | triton_group_norm_silu | 33.01/33.00/0.78/31.94/32.01/33.89 | 22.77/22.77/0.02/22.73/22.75/22.79 | 1.4496 |
| hv_triton_1x512x2x24x64_NC | NC | triton_group_norm_silu | 44.50/44.50/1.01/42.73/43.43/45.55 | 20.71/20.71/0.03/20.67/20.68/20.74 | 2.1487 |
| hv_triton_1x512x2x32x10_C | C | triton_group_norm_silu | 32.06/32.10/0.34/31.72/31.74/32.52 | 8.60/8.64/0.13/8.50/8.52/8.79 | 3.7296 |
| hv_triton_1x512x2x32x10_NC | NC | triton_group_norm_silu | 44.62/44.70/0.91/43.66/43.77/45.66 | 20.66/20.64/0.05/20.56/20.58/20.69 | 2.1592 |
| hv_triton_1x512x2x32x32_C | C | triton_group_norm_silu | 33.34/33.63/0.58/33.23/33.28/34.18 | 16.63/16.62/0.02/16.59/16.60/16.64 | 2.0044 |
| hv_triton_1x512x2x32x32_NC | NC | triton_group_norm_silu | 44.11/44.03/0.71/42.95/43.10/44.66 | 18.67/18.68/0.05/18.63/18.63/18.74 | 2.3627 |
| hv_triton_1x512x2x64x20_C | C | triton_group_norm_silu | 35.83/35.26/1.50/33.12/33.22/36.59 | 19.14/19.17/0.08/19.06/19.09/19.27 | 1.8720 |
| hv_triton_1x512x2x64x20_NC | NC | triton_group_norm_silu | 45.94/45.58/0.79/44.64/44.73/46.38 | 21.80/21.79/0.02/21.76/21.78/21.81 | 2.1076 |
| hv_triton_1x512x2x64x64_C | C | triton_group_norm_silu | 58.80/58.84/0.11/58.73/58.76/58.95 | 16.63/16.63/0.04/16.58/16.59/16.67 | 3.5362 |
| hv_triton_1x512x2x64x64_NC | NC | triton_group_norm_silu | 86.04/85.91/0.31/85.47/85.58/86.19 | 27.41/27.43/0.13/27.29/27.30/27.56 | 3.1394 |
| hv_triton_1x512x3x128x128_C | C | triton_group_norm_silu | 94.58/95.79/2.87/92.65/93.37/98.88 | 41.58/41.54/0.07/41.43/41.46/41.60 | 2.2747 |
| hv_triton_1x512x3x128x40_C | C | triton_group_norm_silu | 107.54/107.70/0.56/107.30/107.31/108.22 | 21.80/21.78/0.04/21.71/21.73/21.81 | 4.9335 |
| hv_triton_1x512x3x48x128_C | C | triton_group_norm_silu | 94.24/94.94/1.58/93.41/93.69/96.84 | 22.51/22.47/0.14/22.25/22.28/22.58 | 4.1860 |
| hv_triton_1x512x3x48x40_C | C | triton_group_norm_silu | 40.97/41.01/0.30/40.66/40.68/41.32 | 16.63/16.64/0.03/16.58/16.61/16.67 | 2.4631 |
| hv_triton_1x512x5x12x10_C | C | triton_group_norm_silu | 33.40/33.35/0.49/32.79/32.84/33.83 | 9.54/9.55/0.17/9.34/9.37/9.77 | 3.5020 |
| hv_triton_1x512x5x12x10_NC | NC | triton_group_norm_silu | 44.67/44.78/1.02/43.57/43.84/46.09 | 17.96/17.96/0.11/17.76/17.86/18.07 | 2.4874 |
| hv_triton_1x512x5x12x32_C | C | triton_group_norm_silu | 33.11/33.21/0.53/32.54/32.63/33.74 | 16.62/16.62/0.04/16.56/16.58/16.66 | 1.9915 |
| hv_triton_1x512x5x12x32_NC | NC | triton_group_norm_silu | 45.00/45.04/0.56/44.29/44.49/45.73 | 18.70/18.69/0.02/18.65/18.66/18.71 | 2.4062 |
| hv_triton_1x512x5x24x20_C | C | triton_group_norm_silu | 33.01/33.22/0.75/32.32/32.44/34.11 | 18.69/18.69/0.02/18.65/18.66/18.71 | 1.7661 |
| hv_triton_1x512x5x24x20_NC | NC | triton_group_norm_silu | 44.32/44.10/0.70/43.01/43.19/44.78 | 18.70/18.70/0.03/18.65/18.67/18.72 | 2.3700 |
| hv_triton_1x512x5x24x64_C | C | triton_group_norm_silu | 55.51/55.59/0.79/54.63/54.80/56.50 | 16.77/17.44/1.13/16.63/16.65/18.97 | 3.3108 |
| hv_triton_1x512x5x24x64_NC | NC | triton_group_norm_silu | 80.50/80.68/0.63/80.09/80.13/81.42 | 26.86/26.85/0.03/26.80/26.83/26.88 | 2.9966 |
| hv_triton_1x512x5x32x10_C | C | triton_group_norm_silu | 36.69/36.52/0.34/36.06/36.15/36.83 | 14.46/14.46/0.01/14.45/14.45/14.48 | 2.5371 |
| hv_triton_1x512x5x32x10_NC | NC | triton_group_norm_silu | 44.66/44.80/1.00/43.52/43.59/45.83 | 20.72/20.72/0.05/20.66/20.67/20.78 | 2.1549 |
| hv_triton_1x512x5x32x32_C | C | triton_group_norm_silu | 36.40/36.55/0.38/36.24/36.25/37.06 | 16.60/16.61/0.04/16.56/16.57/16.65 | 2.1929 |
| hv_triton_1x512x5x32x32_NC | NC | triton_group_norm_silu | 60.13/64.66/10.33/54.09/56.84/77.66 | 24.89/24.91/0.06/24.82/24.85/24.98 | 2.4154 |
| hv_triton_1x512x5x64x20_C | C | triton_group_norm_silu | 44.99/45.24/0.65/44.61/44.71/46.13 | 16.68/16.69/0.06/16.62/16.63/16.75 | 2.6971 |
| hv_triton_1x512x5x64x20_NC | NC | triton_group_norm_silu | 68.44/68.41/0.40/67.86/68.01/68.87 | 26.17/26.21/0.13/26.05/26.09/26.36 | 2.6155 |
| hv_triton_1x512x5x64x64_C | C | triton_group_norm_silu | 91.71/92.87/2.98/89.60/90.43/95.96 | 25.16/25.17/0.11/25.04/25.05/25.30 | 3.6456 |
| hv_triton_1x512x5x64x64_NC | NC | triton_group_norm_silu | 122.34/131.92/25.22/108.74/109.89/166.57 | 51.77/51.84/0.14/51.68/51.73/52.02 | 2.3631 |
| hv_triton_1x512x9x128x128_C | C | triton_group_norm_silu | 100.14/100.51/0.95/99.95/99.98/101.31 | 103.62/103.67/1.38/101.72/102.17/105.23 | 0.9665 |
| hv_triton_1x512x9x128x40_C | C | triton_group_norm_silu | 93.44/93.79/1.01/92.64/93.00/94.88 | 39.48/39.47/0.09/39.31/39.35/39.55 | 2.3667 |
| hv_triton_1x512x9x48x128_C | C | triton_group_norm_silu | 95.07/94.95/1.83/93.12/93.16/97.07 | 47.84/47.81/0.17/47.63/47.64/47.98 | 1.9872 |
| hv_triton_1x512x9x48x40_C | C | triton_group_norm_silu | 103.25/103.77/1.76/101.05/102.18/105.86 | 22.81/22.83/0.04/22.80/22.80/22.87 | 4.5260 |

Non-production regression-grid rows (12, contract shapes x dtypes) all PASSED in-benchmark correctness; their timings are tracked in `bench/results_headline.jsonl` but excluded from the headline by design.
