# Results — `b200_diffusion_group_norm_silu__multi_shape`

## Headline (frozen harness, definitive run 2026-06-05)

- Equal-weight geometric mean speedup over all **160 production rows**:
  **2.2880x** (arithmetic mean 2.4944x, secondary metric).
- 172/172 workloads PASSED in-benchmark correctness
  (`required_matched_ratio = 1.0`); the standalone correctness suite
  (`bench/correctness.py --side both`, all sections) passed with 0 failing
  checks immediately before this run in the same configuration
  (`docs/run_log.md` Run 13).
- Command as executed (chained after correctness in the same detached remote
  session): `CUDA_VISIBLE_DEVICES=1 python3 bench/benchmark.py --device
  cuda:0 --out bench/results_r1.jsonl`; the output was copied byte-identically
  to the tracked canonical evidence file `bench/results.jsonl`. Workloads
  frozen (`bench/gen_workloads.py --check` green the same day, sha256
  `1255972107562ab14e9b04c3e433a9a5334b169eadf43e6b0f50f1cf7c46eeb8`).
- Environment: ion-b200 / container `sglang_bbuf`, NVIDIA B200 (GPU 1, pinned
  via `CUDA_VISIBLE_DEVICES=1`; idle before/after — embedded provenance block
  in `bench/results.jsonl`), Python 3.12.3, torch 2.11.0+cu130, CUDA 13.0,
  triton 3.6.0, tvm-ffi 0.1.9.
- Baseline: copied upstream SGLang Triton implementation @ `main`
  `133254086bf1f5b887c8c99d311719102d58a7eb` (see `docs/baseline_source.md`).
- Candidate source (exact content measured): `solution/kernel.cu` sha256
  `2c1ca71d78e0fdde45bcc1898f22ca80b84afa6c2e1a9de7fe0ec491ab28bf4b`,
  `solution/binding.py` sha256
  `4c5587507d622fea57c31a8314d120cbeb9df7b768895a4bee32ddacab0a458a`.

## Promotion Gates (verbatim from `python3 bench/summarize_results.py bench/results.jsonl`)

```
headline geomean (production, equal weight): 2.2880
arithmetic mean (secondary): 2.4944
gate geomean>1.0: PASS
gate no row <0.97: PASS (strict)
```

- Strict pass this run: zero production rows below the 0.97 floor (worst row
  `hv_triton_1x512x9x128x128_C` at 0.9724, dispatch path
  `baseline_fallback`).
- The gate tooling also supports a second, machine-checked outcome for runs
  where the characterized order-debt measurement artifact pushes a ROUTED row
  below the floor: `PASS (explained residual)` is reported only when every
  below-floor row carries `matched_status = baseline_equivalent` (identical
  implementation on both sides — regression impossible by construction); a
  below-floor row on an optimized path is a hard FAIL. Artifact
  characterization and raw evidence: `docs/dispatch.md` ("Measured Residual
  on Routed Giant Rows"), `bench/results_marginal21.jsonl`,
  `bench/results_routed.jsonl`.

## Dispatch Distribution (production rows, from per-row metadata)

- candidate_path: 148 cuda_kernel / 12 baseline_fallback
- candidate_regime: 64 nchw_last, 60 cont_split, 24 cont_small, 12 baseline_fallback
- Every routed (`baseline_fallback`) row is `matched_status =
  baseline_equivalent` and is counted in the geomean like every other row.

## Provenance (contract checklist, `docs/standalone_diffusion_benchmark.md`)

- Task slug / target GPU: `b200_diffusion_group_norm_silu__multi_shape` /
  NVIDIA B200.
- Upstream baseline commit and copied files:
  `133254086bf1f5b887c8c99d311719102d58a7eb`,
  `python/sglang/jit_kernel/diffusion/group_norm_silu.py` +
  `python/sglang/jit_kernel/diffusion/triton/group_norm_silu.py`
  (verbatim blob shasums + complete local-edit log in
  `docs/baseline_source.md`).
- Candidate source hashes: see above.
- Exact command: see "Command as executed" above; the JSONL's embedded
  provenance record carries the in-process command line, Python/torch
  versions, and the full `nvidia-smi` snapshot.
- Versions: CUDA 13.0 (nvcc V13.0.88), PyTorch 2.11.0+cu130, Triton 3.6.0,
  tvm-ffi 0.1.9, Python 3.12.3 (toolchain verification in `docs/run_log.md`
  "Environment"). Candidate compile flags in `docs/benchmark_method.md`
  "Compile / Build Flags".
- GPU model / id / idle state: NVIDIA B200, physical GPU 1 (pinned via
  `CUDA_VISIBLE_DEVICES=1`, in-process `cuda:0`); idle before/after
  (`docs/run_log.md` Run 13).
- Workload count and settings: 172 workloads (160 production + 12 grid);
  warmup 10, trials 7, inner iterations 1..4096 calibrated to >= ~1000 us,
  isolated subprocess per workload, timeout 600 s (settings echoed in the
  JSONL provenance record).
- Correctness summary: standalone suite PASS, 0 failing checks (Run 13,
  immediately before the benchmark in the same session); every benchmark row
  passed the harness's poisoned-output comparison.

## Per-Bucket Geomeans (production rows)

| Layout | Size bucket | n | geomean | min | max |
|---|---|---|---|---|---|
| C | small | 24 | 2.4061 | 1.4514 | 3.8497 |
| C | mid | 52 | 3.1375 | 1.6724 | 4.9614 |
| C | large | 20 | 1.1493 | 0.9724 | 1.6290 |
| NC | small | 24 | 2.3233 | 1.8274 | 2.7171 |
| NC | mid | 30 | 2.2820 | 1.3983 | 3.1706 |
| NC | large | 10 | 1.5118 | 1.1502 | 3.6047 |

## Where the Speedup Comes From (roofline-style accounting)

- **Contiguous mid (64K-2M elems, geomean 3.14x)**: the upstream one-pass
  Triton path launches only `B*G = 32` CTAs at `B=1` — under 22% of B200's
  148 SMs. The candidate splits each group across CTAs (vectorized stats with
  a deterministic last-CTA finalize + a division-free apply), filling the
  machine. Occupancy/latency win; both sides move 2 reads + 1 write.
- **Contiguous small (<64K, 2.41x)**: same underfill effect plus 16-byte
  vectorization; one CTA per group remains optimal below
  `GNS_SMALL_MAX = 65536` (re-derived on B200).
- **Channels-last rows (1.51-2.32x per bucket)**: the baseline materializes
  `x.contiguous()` before its kernel — on the NCU probe row the copy alone
  was 121.6 us of the 186 us baseline (uncoalesced NC->C transpose copy at
  ~3.6% DRAM utilization). The candidate reads the channels-last layout
  natively (position-major 16B vectors), computes all 32 groups' statistics
  in one sweep, and writes the contiguous output through padded
  shared-memory tiles — 3 passes instead of 5.
- **Contiguous giant (>2M elems, routed)**: the baseline chunked pipeline
  already runs this forced 2R+1W pattern near achievable bandwidth
  (~5 TB/s-class effective); after three NCU-backed optimization rounds and a
  5-point chunk sweep the split path still measured 0.93-0.96x, so the bucket
  routes to the baseline-equivalent path (`GNS_CONT_FALLBACK_MIN =
  2,000,000`) — `docs/dispatch.md` documents the bounded-attempt trail and
  the active bound (bandwidth-bound; a 1-read-pass algorithm is excluded
  because affine+silu needs the group statistics and giant groups cannot be
  cached on-chip).
- fp32 rows exist only in the correctness grid (never production) and run
  the generic strided kernel with double accumulation.

## Reproduction

```bash
# correctness (both sides, all sections)
CUDA_VISIBLE_DEVICES=<idle B200> python3 bench/correctness.py --device cuda:0 --side both
# workload freeze check (requires this repository's git history; run locally)
python3 bench/gen_workloads.py --check
# full benchmark
CUDA_VISIBLE_DEVICES=<idle B200> python3 bench/benchmark.py --device cuda:0 --out bench/results.jsonl
# summary / gates / per-row table
python3 bench/summarize_results.py bench/results.jsonl --markdown
```

## Per-Row Results (production, definitive run)

Columns: path/regime/matched from the per-row dispatch metadata (captured by
the adapter reporting hook from the same tensors used for timing); per-side
stats are median/mean/std/min/p10/p90 in microseconds; speedup =
baseline_median / candidate_median.

| id | layout | function | path | regime | matched | baseline (us) | candidate (us) | speedup |
|---|---|---|---|---|---|---|---|---|
| hv_apply_1x128x17x256x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 172.06/172.15/1.44/170.82/171.03/173.50 | 172.55/172.89/0.81/171.95/172.14/173.88 | 0.9971 |
| hv_apply_1x128x17x256x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 2760.93/2762.91/11.55/2747.17/2752.97/2778.25 | 765.92/765.23/4.18/758.43/760.96/769.94 | 3.6047 |
| hv_apply_1x128x17x256x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 98.72/99.41/1.86/97.38/97.74/101.52 | 70.92/70.86/0.22/70.41/70.64/71.03 | 1.3919 |
| hv_apply_1x128x17x256x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 272.58/272.66/0.71/271.66/271.94/273.56 | 212.68/212.59/0.72/211.68/211.82/213.33 | 1.2816 |
| hv_apply_1x128x17x96x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 93.62/93.89/2.11/91.08/91.80/96.14 | 82.25/82.16/0.23/81.86/81.87/82.37 | 1.1383 |
| hv_apply_1x128x17x96x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 301.40/301.33/0.49/300.72/300.83/301.91 | 262.05/262.13/1.75/259.08/260.16/263.77 | 1.1502 |
| hv_apply_1x128x17x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.43/98.50/4.11/95.24/96.15/101.83 | 28.95/28.95/0.03/28.92/28.92/28.98 | 3.3658 |
| hv_apply_1x128x17x96x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 111.72/111.38/0.92/110.28/110.41/112.26 | 78.22/78.07/0.51/76.94/77.64/78.40 | 1.4284 |
| hv_apply_1x128x5x256x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 93.68/93.74/1.05/91.85/92.82/94.94 | 67.55/67.37/0.31/66.94/66.96/67.63 | 1.3868 |
| hv_apply_1x128x5x256x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 239.26/239.07/0.37/238.46/238.59/239.38 | 202.21/202.38/0.58/201.73/201.83/203.07 | 1.1832 |
| hv_apply_1x128x5x256x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 96.96/96.84/3.19/93.26/93.60/99.77 | 26.89/26.89/0.03/26.83/26.85/26.91 | 3.6056 |
| hv_apply_1x128x5x256x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 126.54/127.69/14.83/109.80/109.90/144.21 | 64.63/64.65/0.35/64.16/64.28/65.04 | 1.9580 |
| hv_apply_1x128x5x96x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 113.05/122.65/24.53/102.22/104.91/152.73 | 28.98/28.99/0.06/28.91/28.94/29.07 | 3.9006 |
| hv_apply_1x128x5x96x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 109.34/110.10/1.95/108.41/108.61/112.29 | 74.48/74.53/0.22/74.25/74.30/74.80 | 1.4680 |
| hv_apply_1x128x5x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 71.08/71.30/0.79/70.52/70.64/72.06 | 16.75/16.82/0.21/16.62/16.64/17.10 | 4.2437 |
| hv_apply_1x128x5x96x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 100.92/102.44/3.59/100.28/100.40/105.80 | 35.24/35.79/1.58/35.06/35.10/36.94 | 2.8639 |
| hv_apply_1x256x17x256x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 331.54/329.60/3.26/325.42/325.57/332.53 | 329.58/330.10/2.86/326.94/327.03/333.19 | 1.0059 |
| hv_apply_1x256x17x256x80_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 154.32/154.67/1.17/153.25/153.57/156.09 | 156.12/156.14/1.04/154.73/155.09/157.33 | 0.9885 |
| hv_apply_1x256x17x96x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 137.92/138.43/1.72/136.59/136.91/140.55 | 137.94/138.39/1.75/136.59/136.83/140.55 | 0.9999 |
| hv_apply_1x256x17x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.96/96.25/1.46/94.95/95.11/97.61 | 55.84/55.83/0.07/55.74/55.75/55.90 | 1.7184 |
| hv_apply_1x256x3x128x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 93.17/94.18/1.84/92.23/92.59/96.52 | 26.87/26.87/0.01/26.85/26.86/26.89 | 3.4672 |
| hv_apply_1x256x3x128x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 110.38/109.39/3.09/103.83/105.87/112.43 | 56.46/56.49/0.31/56.07/56.18/56.84 | 1.9550 |
| hv_apply_1x256x3x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 54.73/54.77/0.17/54.55/54.63/54.98 | 16.65/16.65/0.02/16.62/16.62/16.67 | 3.2873 |
| hv_apply_1x256x3x128x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 81.27/81.55/0.84/80.53/80.74/82.62 | 25.95/25.97/0.06/25.93/25.93/26.03 | 3.1322 |
| hv_apply_1x256x3x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 66.60/66.65/0.26/66.45/66.46/66.91 | 16.68/16.67/0.03/16.62/16.64/16.70 | 3.9932 |
| hv_apply_1x256x3x48x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 95.52/95.90/1.28/94.73/94.77/97.20 | 30.13/30.16/0.12/30.01/30.06/30.28 | 3.1706 |
| hv_apply_1x256x3x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.31/33.31/0.70/32.31/32.53/34.11 | 22.72/22.67/0.13/22.41/22.51/22.77 | 1.4660 |
| hv_apply_1x256x3x48x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.47/43.82/1.14/42.70/43.02/45.03 | 23.79/23.73/0.13/23.46/23.60/23.81 | 1.8274 |
| hv_apply_1x256x5x256x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 108.63/108.67/0.75/108.03/108.07/109.37 | 110.30/110.19/1.36/108.22/108.40/111.60 | 0.9849 |
| hv_apply_1x256x5x256x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 94.95/96.10/1.97/94.05/94.25/98.35 | 43.65/43.64/0.05/43.58/43.58/43.70 | 2.1754 |
| hv_apply_1x256x5x96x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 94.70/95.22/2.46/92.37/93.40/97.68 | 52.60/52.65/0.30/52.21/52.31/52.99 | 1.8002 |
| hv_apply_1x256x5x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 94.44/94.50/2.21/91.38/91.94/97.09 | 24.84/24.83/0.05/24.73/24.78/24.87 | 3.8023 |
| hv_apply_1x256x9x128x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 99.04/98.79/2.87/95.39/95.85/102.05 | 60.80/60.88/0.52/60.31/60.33/61.54 | 1.6290 |
| hv_apply_1x256x9x128x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 211.79/211.93/0.57/211.19/211.28/212.58 | 169.11/168.90/1.08/167.65/167.79/170.15 | 1.2524 |
| hv_apply_1x256x9x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.43/97.71/1.82/95.57/95.91/99.72 | 24.86/24.86/0.03/24.82/24.84/24.89 | 3.9192 |
| hv_apply_1x256x9x128x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 106.64/107.18/1.10/106.10/106.12/108.43 | 56.43/56.43/0.07/56.35/56.36/56.51 | 1.8898 |
| hv_apply_1x256x9x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 94.81/98.29/5.40/93.36/93.63/104.38 | 26.91/26.90/0.04/26.85/26.86/26.94 | 3.5228 |
| hv_apply_1x256x9x48x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 105.36/105.40/1.51/104.07/104.12/106.68 | 62.02/62.04/0.26/61.72/61.77/62.33 | 1.6988 |
| hv_apply_1x256x9x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 62.71/63.04/0.77/62.40/62.47/63.93 | 16.64/16.63/0.04/16.56/16.59/16.66 | 3.7689 |
| hv_apply_1x256x9x48x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 90.62/90.56/0.27/90.23/90.25/90.87 | 28.91/28.91/0.02/28.88/28.89/28.93 | 3.1340 |
| hv_apply_1x512x2x12x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.29/33.48/0.40/33.10/33.11/33.99 | 9.39/9.47/0.27/9.11/9.23/9.77 | 3.5442 |
| hv_apply_1x512x2x12x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.75/45.09/1.13/43.37/44.00/46.28 | 16.64/16.63/0.02/16.59/16.60/16.65 | 2.6895 |
| hv_apply_1x512x2x12x32_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 32.89/33.21/0.88/32.09/32.48/34.12 | 9.12/9.22/0.23/9.02/9.05/9.54 | 3.6051 |
| hv_apply_1x512x2x12x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.84/44.19/0.90/43.15/43.33/45.38 | 17.69/17.69/0.02/17.65/17.66/17.71 | 2.4779 |
| hv_apply_1x512x2x24x20_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.85/33.74/0.47/33.06/33.20/34.21 | 10.34/10.35/0.03/10.31/10.32/10.38 | 3.2723 |
| hv_apply_1x512x2x24x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.23/43.02/0.73/42.02/42.27/43.71 | 17.69/17.67/0.03/17.62/17.64/17.69 | 2.4441 |
| hv_apply_1x512x2x24x64_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.76/33.77/0.86/32.12/32.98/34.61 | 22.78/22.78/0.02/22.74/22.75/22.80 | 1.4819 |
| hv_apply_1x512x2x24x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.06/47.57/10.18/42.46/42.85/55.13 | 20.73/20.77/0.10/20.64/20.69/20.89 | 2.1251 |
| hv_apply_1x512x2x32x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 32.19/32.09/0.54/31.44/31.49/32.61 | 8.61/8.62/0.15/8.47/8.48/8.78 | 3.7384 |
| hv_apply_1x512x2x32x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 42.79/43.19/0.72/42.31/42.53/43.96 | 20.55/20.53/0.06/20.43/20.47/20.60 | 2.0824 |
| hv_apply_1x512x2x32x32_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.28/33.27/0.23/32.87/33.01/33.47 | 16.61/16.61/0.03/16.58/16.58/16.64 | 2.0031 |
| hv_apply_1x512x2x32x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.31/44.32/0.65/43.55/43.61/45.02 | 18.70/18.70/0.03/18.67/18.67/18.73 | 2.3690 |
| hv_apply_1x512x2x64x20_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.88/33.59/0.65/32.60/32.76/34.15 | 19.07/19.08/0.05/19.01/19.03/19.15 | 1.7768 |
| hv_apply_1x512x2x64x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 47.44/47.49/0.70/46.30/46.76/48.18 | 21.77/21.77/0.03/21.73/21.74/21.80 | 2.1793 |
| hv_apply_1x512x2x64x64_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 58.87/58.85/0.08/58.75/58.76/58.93 | 16.66/16.65/0.04/16.60/16.61/16.69 | 3.5345 |
| hv_apply_1x512x2x64x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 86.39/86.32/0.34/85.86/85.90/86.71 | 27.27/27.30/0.05/27.24/27.25/27.37 | 3.1679 |
| hv_apply_1x512x3x128x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 93.75/94.21/1.35/92.88/92.93/95.89 | 41.54/41.54/0.09/41.43/41.44/41.65 | 2.2572 |
| hv_apply_1x512x3x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 108.03/108.02/0.63/107.40/107.41/108.69 | 21.77/21.78/0.03/21.75/21.76/21.81 | 4.9614 |
| hv_apply_1x512x3x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.74/97.12/2.70/93.82/94.46/99.98 | 22.49/22.43/0.14/22.21/22.25/22.54 | 4.2573 |
| hv_apply_1x512x3x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 41.03/41.01/0.32/40.66/40.69/41.37 | 16.64/16.65/0.03/16.62/16.63/16.70 | 2.4665 |
| hv_apply_1x512x5x12x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 32.72/32.71/0.41/32.15/32.33/33.13 | 8.50/8.56/0.14/8.45/8.45/8.75 | 3.8497 |
| hv_apply_1x512x5x12x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.62/44.50/0.64/43.67/43.71/45.23 | 18.10/18.11/0.08/18.00/18.03/18.22 | 2.4654 |
| hv_apply_1x512x5x12x32_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 32.15/32.50/0.83/31.64/31.89/33.65 | 16.61/16.60/0.01/16.59/16.59/16.62 | 1.9358 |
| hv_apply_1x512x5x12x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.42/44.44/0.52/43.69/43.88/45.04 | 18.68/18.68/0.03/18.63/18.64/18.71 | 2.3782 |
| hv_apply_1x512x5x24x20_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.31/33.35/0.63/32.32/32.81/34.09 | 18.69/18.69/0.04/18.64/18.65/18.73 | 1.7825 |
| hv_apply_1x512x5x24x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 46.31/45.92/1.10/44.53/44.71/47.12 | 18.72/18.72/0.02/18.68/18.69/18.74 | 2.4737 |
| hv_apply_1x512x5x24x64_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 55.16/55.21/0.52/54.59/54.70/55.81 | 16.67/16.73/0.14/16.58/16.60/16.89 | 3.3083 |
| hv_apply_1x512x5x24x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 81.06/81.35/1.11/80.24/80.45/82.59 | 26.88/26.91/0.05/26.84/26.85/26.97 | 3.0152 |
| hv_apply_1x512x5x32x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 34.04/34.03/0.54/33.47/33.48/34.60 | 14.45/14.45/0.01/14.44/14.44/14.46 | 2.3560 |
| hv_apply_1x512x5x32x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.55/43.87/1.03/42.86/42.91/45.05 | 20.71/20.72/0.03/20.68/20.69/20.75 | 2.1024 |
| hv_apply_1x512x5x32x32_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 36.48/36.54/0.32/36.24/36.24/36.92 | 16.61/16.64/0.07/16.54/16.57/16.71 | 2.1958 |
| hv_apply_1x512x5x32x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 52.89/52.92/0.32/52.59/52.64/53.33 | 24.81/24.80/0.03/24.73/24.77/24.83 | 2.1319 |
| hv_apply_1x512x5x64x20_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 44.59/44.61/0.09/44.48/44.51/44.71 | 16.64/16.65/0.06/16.57/16.60/16.70 | 2.6792 |
| hv_apply_1x512x5x64x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 68.21/68.27/0.21/68.09/68.09/68.49 | 26.32/26.27/0.15/26.03/26.10/26.42 | 2.5913 |
| hv_apply_1x512x5x64x64_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 98.94/99.02/1.98/96.01/96.95/101.00 | 25.16/25.12/0.07/24.98/25.03/25.17 | 3.9331 |
| hv_apply_1x512x5x64x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 109.37/109.73/2.92/105.58/107.08/113.25 | 51.78/51.75/0.09/51.57/51.67/51.82 | 2.1125 |
| hv_apply_1x512x9x128x128_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 99.76/99.77/0.32/99.37/99.42/100.17 | 102.01/102.37/1.76/100.28/100.59/104.55 | 0.9779 |
| hv_apply_1x512x9x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 96.74/96.85/1.10/95.08/95.63/98.05 | 39.44/39.49/0.09/39.39/39.41/39.60 | 2.4531 |
| hv_apply_1x512x9x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.73/98.59/2.21/96.21/96.32/101.30 | 47.86/47.87/0.16/47.68/47.69/48.05 | 2.0419 |
| hv_apply_1x512x9x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.19/95.05/1.44/92.92/93.36/96.45 | 22.79/22.78/0.04/22.73/22.74/22.82 | 4.1774 |
| hv_triton_1x128x17x256x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 172.41/173.15/2.67/171.07/171.22/175.48 | 172.66/172.73/0.83/171.68/171.82/173.60 | 0.9986 |
| hv_triton_1x128x17x256x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 2745.38/2747.43/5.64/2741.54/2742.19/2754.90 | 763.06/761.02/6.63/750.93/754.22/768.44 | 3.5979 |
| hv_triton_1x128x17x256x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.01/96.24/0.71/95.24/95.52/97.04 | 70.83/70.77/0.23/70.34/70.50/70.96 | 1.3554 |
| hv_triton_1x128x17x256x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 273.67/273.32/0.71/272.24/272.47/273.94 | 212.43/212.48/0.56/211.75/211.96/213.11 | 1.2883 |
| hv_triton_1x128x17x96x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 134.59/139.42/24.71/110.32/113.86/164.98 | 82.62/82.60/0.45/81.80/82.10/83.04 | 1.6290 |
| hv_triton_1x128x17x96x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 302.06/302.39/0.90/301.50/301.51/303.43 | 262.52/262.28/1.13/260.78/261.09/263.58 | 1.1506 |
| hv_triton_1x128x17x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.83/96.95/1.30/95.00/95.61/98.50 | 29.01/29.00/0.04/28.94/28.95/29.04 | 3.3381 |
| hv_triton_1x128x17x96x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 108.94/109.27/1.12/108.01/108.24/110.67 | 77.91/77.85/0.58/76.80/77.18/78.36 | 1.3983 |
| hv_triton_1x128x5x256x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 95.45/96.28/1.70/94.98/95.07/98.69 | 67.61/67.50/0.30/66.97/67.14/67.78 | 1.4117 |
| hv_triton_1x128x5x256x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 240.16/240.01/0.52/239.19/239.32/240.42 | 202.58/202.53/0.70/201.49/201.75/203.16 | 1.1856 |
| hv_triton_1x128x5x256x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.52/98.34/5.38/92.60/93.03/103.40 | 26.90/26.91/0.04/26.86/26.86/26.95 | 3.6251 |
| hv_triton_1x128x5x256x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 113.80/114.94/3.58/111.39/112.01/119.78 | 64.72/64.62/0.19/64.30/64.38/64.77 | 1.7584 |
| hv_triton_1x128x5x96x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 95.83/95.32/1.55/92.49/93.69/96.68 | 28.92/28.94/0.04/28.89/28.90/28.98 | 3.3131 |
| hv_triton_1x128x5x96x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 115.04/114.79/1.27/113.10/113.46/116.25 | 73.97/74.00/0.43/73.57/73.63/74.53 | 1.5553 |
| hv_triton_1x128x5x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 70.69/70.79/0.31/70.41/70.52/71.14 | 16.64/16.66/0.03/16.62/16.62/16.70 | 4.2473 |
| hv_triton_1x128x5x96x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 100.93/101.02/0.51/100.36/100.47/101.63 | 35.14/35.12/0.12/34.95/34.97/35.24 | 2.8722 |
| hv_triton_1x256x17x256x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 328.87/328.72/3.03/324.86/325.31/332.35 | 329.14/330.16/2.74/327.42/327.58/333.76 | 0.9992 |
| hv_triton_1x256x17x256x80_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 154.28/154.55/1.17/153.44/153.44/155.72 | 155.36/155.70/0.92/154.79/154.85/156.85 | 0.9930 |
| hv_triton_1x256x17x96x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 136.96/136.93/0.24/136.54/136.65/137.18 | 137.24/137.04/0.32/136.60/136.69/137.33 | 0.9979 |
| hv_triton_1x256x17x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 93.32/93.52/1.97/91.57/91.84/95.73 | 55.80/55.78/0.05/55.70/55.72/55.82 | 1.6724 |
| hv_triton_1x256x3x128x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 94.35/94.22/2.47/90.38/91.25/96.94 | 26.87/26.87/0.02/26.84/26.85/26.89 | 3.5110 |
| hv_triton_1x256x3x128x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 104.78/104.95/1.44/102.75/103.60/106.58 | 56.45/56.53/0.24/56.30/56.32/56.84 | 1.8561 |
| hv_triton_1x256x3x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 54.74/54.76/0.10/54.60/54.67/54.88 | 16.68/16.69/0.02/16.66/16.67/16.71 | 3.2814 |
| hv_triton_1x256x3x128x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 80.46/80.62/0.26/80.33/80.39/80.94 | 25.89/25.90/0.03/25.87/25.88/25.94 | 3.1074 |
| hv_triton_1x256x3x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 66.69/66.71/0.27/66.44/66.46/67.02 | 16.66/16.66/0.03/16.62/16.63/16.69 | 4.0040 |
| hv_triton_1x256x3x48x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 94.47/94.74/0.59/94.39/94.39/95.33 | 30.07/30.06/0.10/29.90/29.94/30.16 | 3.1412 |
| hv_triton_1x256x3x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.95/32.70/0.72/31.84/31.93/33.39 | 22.70/22.66/0.14/22.42/22.49/22.79 | 1.4514 |
| hv_triton_1x256x3x48x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.76/45.89/1.05/44.41/44.78/47.01 | 23.81/23.78/0.09/23.59/23.69/23.85 | 1.9220 |
| hv_triton_1x256x5x256x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 108.21/108.16/0.33/107.84/107.86/108.51 | 108.76/109.27/1.55/108.05/108.22/110.86 | 0.9950 |
| hv_triton_1x256x5x256x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.56/96.28/2.47/92.84/93.18/99.02 | 43.70/43.68/0.10/43.49/43.59/43.77 | 2.2097 |
| hv_triton_1x256x5x96x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.98/98.28/2.00/94.97/96.41/100.26 | 52.89/52.74/0.23/52.44/52.45/52.93 | 1.8524 |
| hv_triton_1x256x5x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 92.65/93.36/2.82/90.17/90.27/96.96 | 24.84/24.84/0.03/24.77/24.80/24.86 | 3.7293 |
| hv_triton_1x256x9x128x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.77/97.42/2.31/94.83/95.82/99.46 | 60.94/60.94/0.52/60.16/60.34/61.54 | 1.5878 |
| hv_triton_1x256x9x128x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 211.40/211.50/0.20/211.23/211.29/211.71 | 168.73/168.69/1.06/167.24/167.30/169.68 | 1.2529 |
| hv_triton_1x256x9x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 102.11/102.07/2.02/98.61/99.73/103.92 | 24.87/24.89/0.05/24.82/24.84/24.94 | 4.1051 |
| hv_triton_1x256x9x128x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 108.23/108.08/2.23/106.10/106.10/110.24 | 56.40/56.45/0.19/56.18/56.28/56.69 | 1.9191 |
| hv_triton_1x256x9x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 100.57/100.27/2.20/97.14/98.04/102.96 | 26.90/26.90/0.04/26.86/26.87/26.94 | 3.7387 |
| hv_triton_1x256x9x48x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 106.96/106.98/1.93/104.55/104.75/108.82 | 61.93/61.88/0.19/61.59/61.64/62.05 | 1.7270 |
| hv_triton_1x256x9x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 62.67/62.71/0.32/62.41/62.44/63.12 | 16.66/16.66/0.03/16.62/16.63/16.69 | 3.7618 |
| hv_triton_1x256x9x48x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 90.69/90.89/0.49/90.38/90.43/91.52 | 28.93/28.94/0.04/28.89/28.91/28.97 | 3.1345 |
| hv_triton_1x512x2x12x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 34.09/33.86/1.06/32.51/32.68/35.03 | 9.26/9.35/0.21/9.15/9.15/9.62 | 3.6799 |
| hv_triton_1x512x2x12x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.23/45.14/1.05/43.97/44.06/46.29 | 16.65/16.67/0.10/16.55/16.59/16.77 | 2.7171 |
| hv_triton_1x512x2x12x32_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.69/32.94/0.61/32.18/32.42/33.59 | 8.78/8.80/0.13/8.67/8.68/8.97 | 3.7236 |
| hv_triton_1x512x2x12x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.85/44.70/0.87/43.41/43.58/45.51 | 17.70/17.71/0.04/17.66/17.68/17.74 | 2.5335 |
| hv_triton_1x512x2x24x20_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.85/33.86/0.90/32.32/32.92/34.87 | 10.35/10.35/0.03/10.31/10.32/10.38 | 3.2694 |
| hv_triton_1x512x2x24x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 46.36/46.26/1.25/44.75/44.95/47.70 | 17.70/17.72/0.08/17.66/17.66/17.79 | 2.6192 |
| hv_triton_1x512x2x24x64_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.49/33.83/0.94/32.94/32.99/35.04 | 22.78/22.78/0.02/22.73/22.76/22.80 | 1.4700 |
| hv_triton_1x512x2x24x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 53.37/62.81/15.40/49.04/49.11/79.75 | 21.00/21.55/1.56/20.72/20.74/22.83 | 2.5417 |
| hv_triton_1x512x2x32x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.22/32.27/0.47/31.77/31.85/32.86 | 8.41/8.42/0.15/8.29/8.29/8.62 | 3.8317 |
| hv_triton_1x512x2x32x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.65/45.77/0.93/44.59/45.02/46.60 | 20.60/20.60/0.15/20.31/20.44/20.73 | 2.2161 |
| hv_triton_1x512x2x32x32_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 31.71/32.07/0.71/31.25/31.43/32.83 | 16.62/16.62/0.04/16.57/16.58/16.65 | 1.9079 |
| hv_triton_1x512x2x32x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.14/45.78/0.99/45.01/45.03/47.01 | 18.69/18.70/0.04/18.66/18.67/18.74 | 2.4159 |
| hv_triton_1x512x2x64x20_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.14/33.11/0.23/32.81/32.82/33.34 | 19.03/19.05/0.05/19.02/19.02/19.10 | 1.7411 |
| hv_triton_1x512x2x64x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.46/43.76/0.57/43.18/43.23/44.47 | 21.77/21.76/0.01/21.74/21.75/21.77 | 1.9966 |
| hv_triton_1x512x2x64x64_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 58.79/58.82/0.07/58.75/58.76/58.90 | 16.64/16.66/0.06/16.58/16.61/16.73 | 3.5319 |
| hv_triton_1x512x2x64x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 86.22/86.11/0.39/85.54/85.66/86.51 | 27.37/27.38/0.07/27.30/27.31/27.45 | 3.1498 |
| hv_triton_1x512x3x128x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 95.29/94.98/1.33/93.25/93.33/96.34 | 41.51/41.51/0.05/41.44/41.46/41.57 | 2.2957 |
| hv_triton_1x512x3x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 107.63/107.84/0.63/107.26/107.31/108.57 | 21.78/21.79/0.04/21.72/21.75/21.82 | 4.9408 |
| hv_triton_1x512x3x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 103.48/103.24/5.14/96.06/98.22/107.72 | 22.50/22.50/0.06/22.39/22.44/22.55 | 4.5981 |
| hv_triton_1x512x3x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 40.93/41.16/0.52/40.55/40.63/41.73 | 16.67/16.88/0.60/16.56/16.60/17.33 | 2.4549 |
| hv_triton_1x512x5x12x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.67/32.87/1.16/31.41/31.67/34.35 | 8.62/8.60/0.11/8.43/8.47/8.71 | 3.7895 |
| hv_triton_1x512x5x12x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 42.80/42.96/0.83/42.06/42.13/43.99 | 18.12/18.12/0.16/17.85/17.93/18.29 | 2.3616 |
| hv_triton_1x512x5x12x32_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.14/33.09/0.33/32.45/32.77/33.37 | 16.60/16.60/0.02/16.57/16.58/16.61 | 1.9967 |
| hv_triton_1x512x5x12x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.31/45.09/1.29/43.43/43.64/46.48 | 18.67/18.68/0.03/18.64/18.64/18.72 | 2.4263 |
| hv_triton_1x512x5x24x20_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.24/32.45/0.67/31.65/31.76/33.23 | 18.69/18.68/0.03/18.65/18.65/18.71 | 1.7252 |
| hv_triton_1x512x5x24x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 46.82/47.13/1.85/45.19/45.32/49.30 | 18.72/18.71/0.04/18.65/18.67/18.75 | 2.5010 |
| hv_triton_1x512x5x24x64_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 54.83/54.79/0.10/54.69/54.70/54.90 | 16.65/16.65/0.04/16.59/16.61/16.69 | 3.2926 |
| hv_triton_1x512x5x24x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 80.35/80.74/0.63/80.15/80.15/81.42 | 26.88/26.87/0.03/26.80/26.84/26.90 | 2.9893 |
| hv_triton_1x512x5x32x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 34.06/33.90/0.64/32.98/33.12/34.57 | 14.44/14.45/0.02/14.42/14.43/14.47 | 2.3588 |
| hv_triton_1x512x5x32x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.28/45.66/1.06/44.28/44.82/46.74 | 20.72/20.71/0.04/20.63/20.66/20.76 | 2.1856 |
| hv_triton_1x512x5x32x32_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 36.55/36.66/0.22/36.44/36.45/36.90 | 16.60/16.62/0.04/16.57/16.59/16.65 | 2.2018 |
| hv_triton_1x512x5x32x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 52.96/53.14/0.30/52.83/52.86/53.47 | 24.82/24.82/0.02/24.79/24.80/24.84 | 2.1336 |
| hv_triton_1x512x5x64x20_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 44.74/44.76/0.18/44.58/44.59/44.99 | 16.68/16.66/0.05/16.57/16.59/16.71 | 2.6825 |
| hv_triton_1x512x5x64x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 68.32/68.32/0.21/68.00/68.12/68.53 | 26.26/26.25/0.10/26.05/26.16/26.35 | 2.6019 |
| hv_triton_1x512x5x64x64_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.75/96.55/2.03/93.64/94.11/98.44 | 25.27/25.26/0.08/25.14/25.16/25.33 | 3.8287 |
| hv_triton_1x512x5x64x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 104.91/105.17/2.06/102.98/103.08/107.33 | 51.70/51.67/0.10/51.47/51.58/51.74 | 2.0294 |
| hv_triton_1x512x9x128x128_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 99.86/100.64/1.67/99.32/99.51/102.46 | 102.70/103.69/1.61/102.34/102.50/105.96 | 0.9724 |
| hv_triton_1x512x9x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 94.52/94.28/1.00/92.25/93.19/95.05 | 39.49/39.50/0.09/39.33/39.41/39.58 | 2.3937 |
| hv_triton_1x512x9x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.07/96.72/1.42/94.32/94.97/98.16 | 47.99/47.93/0.18/47.71/47.73/48.11 | 2.0226 |
| hv_triton_1x512x9x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 99.29/100.53/3.14/97.19/97.61/104.70 | 22.85/22.85/0.06/22.75/22.78/22.91 | 4.3447 |

Non-production regression-grid rows (12, contract shapes x dtypes) all PASSED in-benchmark correctness; their timings and dispatch metadata are in `bench/results.jsonl` but excluded from the headline by design.
