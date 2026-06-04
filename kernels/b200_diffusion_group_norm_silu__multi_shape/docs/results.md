# Results — `b200_diffusion_group_norm_silu__multi_shape`

## Headline (frozen harness, definitive run 2026-06-05, post review-fix kernel)

- Equal-weight geometric mean speedup over all **160 production rows**:
  **2.2794x** (arithmetic mean 2.4815x, secondary metric).
- 172/172 workloads PASSED in-benchmark correctness
  (`required_matched_ratio = 1.0`); the standalone correctness suite
  (`bench/correctness.py --side both`, all sections including the
  review-round regression rows: channels-last `cpg=6` routing and
  non-default-stream execution) passed with 0 failing checks immediately
  before this run in the same configuration (`docs/run_log.md` Run 14).
- Command as executed (chained after correctness in the same detached remote
  session): `CUDA_VISIBLE_DEVICES=1 python3 bench/benchmark.py --device
  cuda:0 --out bench/results_r3.jsonl`; output copied byte-identically to the
  tracked canonical evidence file `bench/results.jsonl`. Workloads frozen
  (`bench/gen_workloads.py --check` green the same day, sha256
  `1255972107562ab14e9b04c3e433a9a5334b169eadf43e6b0f50f1cf7c46eeb8`).
- Environment: ion-b200 / container `sglang_bbuf`, NVIDIA B200 (GPU 1, pinned
  via `CUDA_VISIBLE_DEVICES=1`; idle before/after — embedded provenance block
  in `bench/results.jsonl`), Python 3.12.3, torch 2.11.0+cu130, CUDA 13.0,
  triton 3.6.0, tvm-ffi 0.1.9.
- Baseline: copied upstream SGLang Triton implementation @ `main`
  `133254086bf1f5b887c8c99d311719102d58a7eb` (see `docs/baseline_source.md`).
- Candidate source (exact content measured): `solution/kernel.cu` sha256
  `2fd730bfebb1d6df0928b48570e05540aec8a2583ab53c2b3ad17bc0ccab5e89`,
  `solution/binding.py` sha256
  `4c5587507d622fea57c31a8314d120cbeb9df7b768895a4bee32ddacab0a458a`.

## Promotion Gates (verbatim from `python3 bench/summarize_results.py bench/results.jsonl`; exit code 0)

```
headline geomean (production, equal weight): 2.2794
arithmetic mean (secondary): 2.4815
gate geomean>1.0: PASS
gate no row <0.97: PASS (explained residual: 2 baseline-equivalent row(s) below floor)
  explained-residual: hv_apply_1x512x9x128x128_C speedup=0.9166 path=baseline_fallback regime=baseline_fallback (identical code both sides; see docs/dispatch.md)
  explained-residual: hv_triton_1x512x9x128x128_C speedup=0.9570 path=baseline_fallback regime=baseline_fallback (identical code both sides; see docs/dispatch.md)
```

- This run drew the unlucky per-trial order pattern on the
  `(1,512,9,128,128)` contiguous pair and reports the machine-checked
  **explained-residual pass**: both below-floor readings are ROUTED rows
  executing the IDENTICAL baseline callable (`candidate_path =
  baseline_fallback`, `matched_status = baseline_equivalent`) — a real
  regression is impossible by construction. The readings are the
  characterized dirty-L2 order-debt measurement artifact on this row class:
  the same pair read 0.9724/0.9779 (above floor) in the immediately
  preceding run of identical code paths, the direct steady-state interleaved
  probe measures 0.997, and the identical-code twin read 0.9810 in the
  21-trial order-balanced run. Full characterization and raw evidence:
  `docs/dispatch.md` ("Measured Residual on Routed Giant Rows"),
  `bench/results_marginal21.jsonl`, `bench/results_routed.jsonl`.
- The exit code IS the promotion verdict: 0 only when no benchmark row
  failed AND geomean > 1.0 AND every below-floor production row is
  `baseline_equivalent`; a below-floor row on an optimized path exits
  nonzero (`bench/summarize_results.py --self-test` covers all scenarios).

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
  (`docs/run_log.md` Run 14).
- Workload count and settings: 172 workloads (160 production + 12 grid);
  warmup 10, trials 7, inner iterations 1..4096 calibrated to >= ~1000 us,
  isolated subprocess per workload, timeout 600 s (settings echoed in the
  JSONL provenance record).
- Correctness summary: standalone suite PASS, 0 failing checks (Run 14,
  immediately before the benchmark in the same session); every benchmark row
  passed the harness's poisoned-output comparison.

## Per-Bucket Geomeans (production rows)

| Layout | Size bucket | n | geomean | min | max |
|---|---|---|---|---|---|
| C | small | 24 | 2.4004 | 1.4319 | 3.8075 |
| C | mid | 52 | 3.1166 | 1.7119 | 4.9445 |
| C | large | 20 | 1.1306 | 0.9166 | 1.6020 |
| NC | small | 24 | 2.3395 | 1.8348 | 2.8285 |
| NC | mid | 30 | 2.2796 | 1.4142 | 3.1685 |
| NC | large | 10 | 1.5103 | 1.1457 | 3.6001 |

## Where the Speedup Comes From (roofline-style accounting)

- **Contiguous mid (64K-2M elems, geomean ~3.1x)**: the upstream one-pass
  Triton path launches only `B*G = 32` CTAs at `B=1` — under 22% of B200's
  148 SMs. The candidate splits each group across CTAs (vectorized stats with
  a deterministic last-CTA finalize + a division-free apply), filling the
  machine. Occupancy/latency win; both sides move 2 reads + 1 write.
- **Contiguous small (<64K, ~2.4x)**: same underfill effect plus 16-byte
  vectorization; one CTA per group remains optimal below
  `GNS_SMALL_MAX = 65536` (re-derived on B200).
- **Channels-last rows (~1.5-2.3x per bucket)**: the baseline materializes
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
# summary / gates / per-row table — the EXIT CODE is the promotion verdict:
# 0 only when no benchmark row failed AND geomean > 1.0 AND every below-floor
# production row is baseline_equivalent (explained residual); nonzero otherwise
python3 bench/summarize_results.py bench/results.jsonl --markdown
# gate exit-code semantics self-check (synthetic strict-pass /
# explained-residual / unexplained-fail / low-geomean / failed-row scenarios)
python3 bench/summarize_results.py --self-test
```

## Per-Row Results (production, definitive run)

Columns: path/regime/matched from the per-row dispatch metadata (captured by
the adapter reporting hook from the same tensors used for timing); per-side
stats are median/mean/std/min/p10/p90 in microseconds; speedup =
baseline_median / candidate_median.

| id | layout | function | path | regime | matched | baseline (us) | candidate (us) | speedup |
|---|---|---|---|---|---|---|---|---|
| hv_apply_1x128x17x256x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 172.08/172.60/1.28/171.45/171.54/174.00 | 173.43/173.50/1.28/172.33/172.38/175.11 | 0.9922 |
| hv_apply_1x128x17x256x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 2754.21/2754.85/4.29/2750.18/2750.31/2760.24 | 766.46/764.81/3.56/760.24/761.01/768.22 | 3.5934 |
| hv_apply_1x128x17x256x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 100.64/100.67/2.02/97.53/98.34/102.68 | 70.90/71.05/0.52/70.46/70.62/71.63 | 1.4194 |
| hv_apply_1x128x17x256x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 274.46/274.28/0.62/273.68/273.69/274.85 | 213.30/213.09/0.89/211.73/211.99/213.84 | 1.2867 |
| hv_apply_1x128x17x96x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.51/98.46/3.53/93.76/94.69/102.24 | 82.45/82.24/0.39/81.59/81.77/82.57 | 1.1826 |
| hv_apply_1x128x17x96x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 302.31/302.58/0.92/301.87/301.92/303.50 | 263.86/263.61/1.33/261.66/262.24/265.08 | 1.1457 |
| hv_apply_1x128x17x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.52/96.20/3.34/92.14/92.56/100.37 | 28.95/28.97/0.06/28.91/28.92/29.05 | 3.3001 |
| hv_apply_1x128x17x96x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 110.15/110.36/1.78/108.53/108.57/112.76 | 77.84/77.78/0.55/76.67/77.25/78.24 | 1.4150 |
| hv_apply_1x128x5x256x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 98.36/99.49/2.93/96.64/96.69/102.82 | 67.61/67.83/0.45/67.43/67.50/68.29 | 1.4549 |
| hv_apply_1x128x5x256x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 238.86/238.85/0.42/238.24/238.37/239.28 | 202.82/202.49/0.96/201.10/201.30/203.42 | 1.1777 |
| hv_apply_1x128x5x256x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 96.80/97.44/3.82/92.51/93.48/102.16 | 26.90/26.91/0.04/26.88/26.88/26.97 | 3.5984 |
| hv_apply_1x128x5x256x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 109.77/109.76/1.34/108.09/108.29/111.42 | 64.72/64.59/0.30/64.11/64.25/64.88 | 1.6959 |
| hv_apply_1x128x5x96x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 93.36/94.51/3.58/91.10/91.24/99.43 | 28.96/28.95/0.03/28.89/28.91/28.98 | 3.2232 |
| hv_apply_1x128x5x96x256_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 109.90/110.41/3.03/107.12/107.53/113.67 | 74.40/74.39/0.40/73.81/73.88/74.79 | 1.4771 |
| hv_apply_1x128x5x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 70.57/70.95/0.75/70.29/70.36/72.01 | 16.67/16.70/0.08/16.63/16.64/16.79 | 4.2320 |
| hv_apply_1x128x5x96x80_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 100.76/100.78/0.28/100.38/100.48/101.08 | 35.13/35.17/0.26/34.83/34.93/35.49 | 2.8681 |
| hv_apply_1x256x17x256x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 331.06/329.86/2.97/325.78/326.28/332.54 | 329.26/329.46/2.37/326.98/327.23/332.09 | 1.0054 |
| hv_apply_1x256x17x256x80_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 155.15/154.49/1.11/153.06/153.14/155.48 | 155.72/156.37/2.06/155.14/155.22/157.97 | 0.9963 |
| hv_apply_1x256x17x96x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 137.47/137.75/0.95/136.24/136.85/138.84 | 137.46/137.59/0.57/136.85/137.03/138.19 | 1.0001 |
| hv_apply_1x256x17x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.71/96.22/2.19/94.21/94.28/98.43 | 55.79/55.82/0.09/55.74/55.76/55.92 | 1.7156 |
| hv_apply_1x256x3x128x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.38/94.72/1.91/92.25/92.68/96.63 | 26.89/26.88/0.03/26.83/26.85/26.91 | 3.5468 |
| hv_apply_1x256x3x128x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 108.48/109.32/4.08/105.68/105.84/113.69 | 56.62/56.49/0.22/56.18/56.20/56.67 | 1.9158 |
| hv_apply_1x256x3x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 55.31/55.26/0.20/54.98/55.05/55.47 | 17.13/17.03/0.28/16.67/16.74/17.29 | 3.2295 |
| hv_apply_1x256x3x128x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 80.96/81.14/0.65/80.61/80.63/81.77 | 25.92/25.93/0.04/25.88/25.88/25.98 | 3.1231 |
| hv_apply_1x256x3x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 66.48/66.72/0.41/66.38/66.41/67.23 | 16.65/16.64/0.02/16.61/16.62/16.66 | 3.9938 |
| hv_apply_1x256x3x48x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 95.47/95.61/0.75/94.74/94.93/96.39 | 30.13/30.12/0.06/30.02/30.05/30.18 | 3.1685 |
| hv_apply_1x256x3x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 34.36/34.68/1.85/33.38/33.43/36.29 | 22.77/22.69/0.15/22.45/22.47/22.80 | 1.5087 |
| hv_apply_1x256x3x48x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.60/43.95/0.93/42.88/43.09/45.13 | 23.76/23.74/0.13/23.47/23.62/23.84 | 1.8348 |
| hv_apply_1x256x5x256x256_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 108.67/108.55/0.34/107.99/108.08/108.83 | 109.06/109.38/1.40/108.21/108.30/110.82 | 0.9964 |
| hv_apply_1x256x5x256x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.39/96.97/2.40/94.17/94.24/99.17 | 43.72/43.72/0.11/43.58/43.62/43.83 | 2.2275 |
| hv_apply_1x256x5x96x256_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.10/95.97/1.85/94.66/94.68/98.41 | 52.88/52.75/0.32/52.25/52.34/53.03 | 1.7986 |
| hv_apply_1x256x5x96x80_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 93.63/93.82/2.76/90.53/90.96/96.73 | 24.84/24.84/0.06/24.75/24.79/24.91 | 3.7689 |
| hv_apply_1x256x9x128x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.44/95.14/2.35/92.16/92.61/97.91 | 60.73/60.85/0.50/60.20/60.37/61.47 | 1.5716 |
| hv_apply_1x256x9x128x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 212.09/211.87/0.52/211.05/211.15/212.32 | 168.82/168.94/0.76/168.10/168.32/169.73 | 1.2563 |
| hv_apply_1x256x9x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 96.07/97.06/2.53/95.08/95.09/100.01 | 24.88/24.88/0.03/24.84/24.85/24.91 | 3.8620 |
| hv_apply_1x256x9x128x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 106.78/107.88/3.01/104.86/105.16/111.85 | 56.59/56.56/0.26/56.29/56.31/56.86 | 1.8869 |
| hv_apply_1x256x9x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 95.42/95.78/2.00/93.37/94.02/97.77 | 26.92/26.92/0.03/26.88/26.89/26.95 | 3.5453 |
| hv_apply_1x256x9x48x128_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 113.90/114.72/2.38/111.93/112.11/117.23 | 62.10/62.07/0.20/61.79/61.83/62.29 | 1.8342 |
| hv_apply_1x256x9x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 63.12/63.11/0.40/62.53/62.70/63.52 | 16.65/16.64/0.04/16.58/16.59/16.68 | 3.7900 |
| hv_apply_1x256x9x48x40_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 90.83/90.81/0.50/90.16/90.26/91.38 | 28.94/28.95/0.02/28.93/28.94/28.97 | 3.1380 |
| hv_apply_1x512x2x12x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.65/33.56/0.57/32.84/32.98/34.10 | 9.08/9.09/0.11/8.93/8.98/9.22 | 3.7057 |
| hv_apply_1x512x2x12x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 47.04/46.87/1.48/44.54/45.21/48.30 | 16.63/16.63/0.02/16.59/16.61/16.66 | 2.8285 |
| hv_apply_1x512x2x12x32_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 33.13/33.03/0.64/31.97/32.42/33.62 | 8.71/8.70/0.11/8.52/8.57/8.81 | 3.8022 |
| hv_apply_1x512x2x12x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 46.92/46.71/2.23/43.62/44.66/48.87 | 17.72/17.74/0.09/17.69/17.69/17.82 | 2.6482 |
| hv_apply_1x512x2x24x20_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 34.18/34.56/1.09/33.51/33.54/35.81 | 10.20/10.22/0.14/10.04/10.10/10.38 | 3.3492 |
| hv_apply_1x512x2x24x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.44/44.51/0.98/43.20/43.46/45.52 | 17.67/17.67/0.03/17.62/17.64/17.71 | 2.5154 |
| hv_apply_1x512x2x24x64_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 32.60/32.96/0.71/32.41/32.46/33.83 | 22.76/22.77/0.04/22.71/22.73/22.81 | 1.4319 |
| hv_apply_1x512x2x24x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.92/44.99/1.07/43.34/43.86/46.20 | 20.74/20.75/0.07/20.65/20.68/20.83 | 2.1659 |
| hv_apply_1x512x2x32x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 34.58/34.40/0.87/33.02/33.30/35.26 | 9.80/9.81/0.17/9.60/9.64/9.99 | 3.5295 |
| hv_apply_1x512x2x32x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.41/45.85/1.53/44.87/44.88/47.17 | 20.58/20.60/0.06/20.52/20.54/20.68 | 2.2062 |
| hv_apply_1x512x2x32x32_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 34.63/34.45/0.82/33.48/33.52/35.36 | 16.62/16.64/0.08/16.57/16.59/16.71 | 2.0836 |
| hv_apply_1x512x2x32x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 46.27/46.65/1.76/44.02/44.63/48.38 | 18.70/18.72/0.04/18.67/18.69/18.78 | 2.4742 |
| hv_apply_1x512x2x64x20_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 34.10/34.25/0.50/33.70/33.76/34.85 | 19.07/19.06/0.06/18.98/18.99/19.11 | 1.7883 |
| hv_apply_1x512x2x64x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.83/46.25/1.32/44.70/44.96/47.69 | 21.77/21.77/0.03/21.74/21.74/21.81 | 2.1049 |
| hv_apply_1x512x2x64x64_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 58.88/58.89/0.10/58.75/58.78/59.00 | 16.67/16.67/0.05/16.60/16.61/16.72 | 3.5312 |
| hv_apply_1x512x2x64x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 85.86/85.96/0.46/85.46/85.52/86.55 | 27.37/27.38/0.11/27.24/27.27/27.50 | 3.1371 |
| hv_apply_1x512x3x128x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 96.99/98.07/2.18/96.54/96.59/101.06 | 41.60/41.62/0.12/41.46/41.49/41.75 | 2.3312 |
| hv_apply_1x512x3x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 107.94/108.15/0.68/107.53/107.54/109.11 | 21.83/21.85/0.05/21.81/21.81/21.89 | 4.9436 |
| hv_apply_1x512x3x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.79/98.35/2.77/95.58/95.86/102.09 | 22.47/22.46/0.17/22.19/22.23/22.62 | 4.3519 |
| hv_apply_1x512x3x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 41.18/41.16/0.26/40.72/40.90/41.41 | 16.65/16.67/0.04/16.63/16.63/16.72 | 2.4725 |
| hv_apply_1x512x5x12x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 42.51/43.42/8.80/32.56/33.13/54.41 | 11.17/11.13/1.50/9.38/9.41/12.91 | 3.8075 |
| hv_apply_1x512x5x12x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 46.00/46.18/0.98/44.70/45.09/47.26 | 18.19/18.25/0.22/18.02/18.03/18.49 | 2.5284 |
| hv_apply_1x512x5x12x32_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 34.80/34.77/0.58/33.82/34.21/35.24 | 16.65/16.65/0.03/16.62/16.63/16.68 | 2.0902 |
| hv_apply_1x512x5x12x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.51/45.88/0.75/45.08/45.14/46.78 | 18.69/18.69/0.04/18.63/18.64/18.72 | 2.4351 |
| hv_apply_1x512x5x24x20_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 32.90/33.11/0.71/32.46/32.48/33.89 | 18.67/18.68/0.04/18.64/18.64/18.73 | 1.7621 |
| hv_apply_1x512x5x24x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 47.46/47.35/1.14/45.31/46.19/48.44 | 18.74/18.73/0.04/18.65/18.68/18.77 | 2.5328 |
| hv_apply_1x512x5x24x64_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 54.75/54.84/0.16/54.70/54.71/55.01 | 16.67/16.66/0.04/16.57/16.61/16.70 | 3.2854 |
| hv_apply_1x512x5x24x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 80.58/80.63/0.30/80.12/80.36/80.94 | 26.88/26.88/0.02/26.85/26.86/26.90 | 2.9977 |
| hv_apply_1x512x5x32x10_C | C | apply_group_norm_silu | cuda_kernel | cont_small | optimized | 32.47/32.57/0.56/31.96/32.04/33.26 | 14.44/14.44/0.01/14.42/14.43/14.45 | 2.2489 |
| hv_apply_1x512x5x32x10_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.00/45.02/0.41/44.37/44.54/45.50 | 20.73/20.73/0.03/20.70/20.71/20.76 | 2.1708 |
| hv_apply_1x512x5x32x32_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 38.74/38.57/0.63/37.62/37.80/39.15 | 16.70/16.76/0.16/16.56/16.60/16.93 | 2.3200 |
| hv_apply_1x512x5x32x32_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 51.99/52.15/0.35/51.84/51.87/52.64 | 24.75/24.74/0.02/24.71/24.71/24.76 | 2.1009 |
| hv_apply_1x512x5x64x20_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 44.79/44.87/0.37/44.51/44.61/45.21 | 16.69/16.68/0.06/16.58/16.62/16.75 | 2.6844 |
| hv_apply_1x512x5x64x20_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 68.92/68.81/0.64/67.76/68.05/69.49 | 26.14/26.16/0.15/26.05/26.05/26.31 | 2.6370 |
| hv_apply_1x512x5x64x64_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.09/96.50/1.23/94.97/94.99/97.70 | 25.20/25.22/0.10/25.08/25.12/25.32 | 3.8522 |
| hv_apply_1x512x5x64x64_NC | NC | apply_group_norm_silu | cuda_kernel | nchw_last | optimized | 108.12/108.13/3.16/102.67/104.91/111.25 | 51.80/51.79/0.11/51.58/51.69/51.87 | 2.0874 |
| hv_apply_1x512x9x128x128_C | C | apply_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 100.93/101.09/0.88/100.03/100.14/102.17 | 110.12/109.85/1.98/107.20/107.94/111.88 | 0.9166 |
| hv_apply_1x512x9x128x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.13/97.30/1.65/95.09/95.81/98.80 | 39.55/39.53/0.07/39.44/39.44/39.60 | 2.4557 |
| hv_apply_1x512x9x48x128_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.18/96.78/1.39/94.29/95.16/98.04 | 47.81/47.82/0.13/47.63/47.71/47.93 | 2.0326 |
| hv_apply_1x512x9x48x40_C | C | apply_group_norm_silu | cuda_kernel | cont_split | optimized | 97.14/96.92/3.03/93.46/94.11/100.15 | 22.81/22.81/0.05/22.74/22.74/22.85 | 4.2594 |
| hv_triton_1x128x17x256x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 172.72/173.76/2.48/171.50/171.73/176.80 | 174.40/174.34/1.93/171.70/172.26/176.41 | 0.9903 |
| hv_triton_1x128x17x256x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 2759.81/2764.57/13.71/2754.30/2755.96/2776.35 | 766.59/767.10/6.29/758.19/759.97/774.64 | 3.6001 |
| hv_triton_1x128x17x256x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 95.53/95.35/1.83/93.02/93.26/97.41 | 71.03/70.96/0.26/70.45/70.66/71.16 | 1.3450 |
| hv_triton_1x128x17x256x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 273.85/274.14/0.52/273.62/273.68/274.75 | 212.97/212.80/0.63/211.52/212.16/213.26 | 1.2859 |
| hv_triton_1x128x17x96x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 95.45/95.37/0.91/93.75/94.35/96.26 | 82.11/82.29/0.39/81.88/81.94/82.75 | 1.1624 |
| hv_triton_1x128x17x96x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 302.71/302.67/0.76/301.91/301.95/303.44 | 262.37/262.63/1.29/260.71/261.16/263.91 | 1.1538 |
| hv_triton_1x128x17x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.13/97.31/4.21/92.31/93.44/102.12 | 29.02/29.40/1.01/28.92/28.93/30.16 | 3.3476 |
| hv_triton_1x128x17x96x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 110.47/110.72/1.96/108.65/109.05/112.88 | 78.11/77.97/0.55/76.88/77.40/78.37 | 1.4142 |
| hv_triton_1x128x5x256x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.07/96.62/1.62/93.68/94.80/98.27 | 67.46/67.53/0.24/67.20/67.30/67.80 | 1.4390 |
| hv_triton_1x128x5x256x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 239.38/239.42/0.49/238.70/238.89/239.99 | 202.41/202.23/0.36/201.82/201.84/202.58 | 1.1827 |
| hv_triton_1x128x5x256x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 91.10/93.08/3.28/89.69/90.34/97.39 | 26.91/26.91/0.03/26.85/26.88/26.94 | 3.3858 |
| hv_triton_1x128x5x256x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 112.30/113.11/2.91/109.77/110.64/116.48 | 64.55/64.53/0.24/64.20/64.29/64.74 | 1.7398 |
| hv_triton_1x128x5x96x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 93.73/93.66/2.66/89.87/90.47/96.69 | 28.95/28.95/0.03/28.91/28.92/28.97 | 3.2372 |
| hv_triton_1x128x5x96x256_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 110.95/110.35/1.45/107.71/108.64/111.63 | 74.49/74.10/0.67/73.08/73.36/74.70 | 1.4896 |
| hv_triton_1x128x5x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 70.64/70.69/0.16/70.57/70.57/70.90 | 16.67/16.68/0.05/16.59/16.63/16.74 | 4.2379 |
| hv_triton_1x128x5x96x80_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 100.50/100.72/0.51/100.25/100.34/101.25 | 35.07/35.13/0.12/35.01/35.02/35.26 | 2.8659 |
| hv_triton_1x256x17x256x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 327.42/328.27/2.66/325.24/325.60/331.61 | 327.45/330.27/3.93/327.06/327.12/335.22 | 0.9999 |
| hv_triton_1x256x17x256x80_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 155.04/155.27/0.73/154.30/154.56/156.18 | 156.05/156.45/1.55/154.64/154.94/158.15 | 0.9935 |
| hv_triton_1x256x17x96x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 137.53/137.63/1.24/135.95/136.44/139.00 | 137.68/137.45/0.80/136.33/136.40/138.19 | 0.9989 |
| hv_triton_1x256x17x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 95.63/95.59/1.58/93.87/94.11/97.16 | 55.86/55.87/0.09/55.74/55.77/55.98 | 1.7119 |
| hv_triton_1x256x3x128x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 93.12/93.64/1.17/92.57/92.76/94.94 | 26.87/26.86/0.01/26.85/26.85/26.87 | 3.4658 |
| hv_triton_1x256x3x128x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 110.17/110.28/2.96/107.08/107.61/113.95 | 56.53/56.59/0.23/56.29/56.39/56.84 | 1.9490 |
| hv_triton_1x256x3x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 54.74/54.82/0.23/54.59/54.61/55.07 | 16.73/16.72/0.05/16.63/16.67/16.77 | 3.2716 |
| hv_triton_1x256x3x128x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 81.70/81.76/0.49/80.90/81.31/82.21 | 25.91/25.95/0.10/25.86/25.87/26.05 | 3.1528 |
| hv_triton_1x256x3x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 66.50/66.53/0.21/66.20/66.32/66.77 | 16.63/16.65/0.05/16.59/16.60/16.70 | 3.9983 |
| hv_triton_1x256x3x48x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 94.55/94.83/0.56/94.38/94.41/95.42 | 30.13/30.15/0.12/30.04/30.06/30.25 | 3.1382 |
| hv_triton_1x256x3x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.92/32.82/0.68/31.85/31.98/33.50 | 22.69/22.63/0.16/22.37/22.42/22.76 | 1.4511 |
| hv_triton_1x256x3x48x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.82/43.94/0.72/42.86/43.27/44.65 | 23.81/23.78/0.10/23.57/23.69/23.85 | 1.8401 |
| hv_triton_1x256x5x256x256_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 108.38/108.33/0.35/107.86/107.91/108.70 | 109.83/110.07/1.58/108.38/108.78/111.63 | 0.9868 |
| hv_triton_1x256x5x256x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 95.15/95.71/1.81/93.73/94.00/97.61 | 43.69/43.69/0.10/43.51/43.58/43.80 | 2.1775 |
| hv_triton_1x256x5x96x256_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 94.59/94.11/1.18/92.37/92.82/95.32 | 52.66/52.61/0.36/52.15/52.24/52.98 | 1.7962 |
| hv_triton_1x256x5x96x80_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.09/96.30/2.37/92.71/93.58/98.70 | 24.86/24.86/0.04/24.80/24.81/24.90 | 3.8653 |
| hv_triton_1x256x9x128x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.60/97.83/1.44/96.33/96.72/99.16 | 60.93/60.89/0.55/60.29/60.34/61.55 | 1.6020 |
| hv_triton_1x256x9x128x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 211.40/211.48/0.62/210.85/210.89/212.25 | 169.52/169.46/0.42/168.84/169.05/169.89 | 1.2471 |
| hv_triton_1x256x9x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.18/95.89/1.99/92.44/93.54/97.67 | 24.88/24.87/0.04/24.79/24.83/24.90 | 3.8664 |
| hv_triton_1x256x9x128x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 109.16/110.88/4.64/106.48/107.50/116.21 | 56.66/56.67/0.21/56.38/56.43/56.89 | 1.9266 |
| hv_triton_1x256x9x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 100.98/101.79/1.85/100.12/100.27/103.91 | 26.92/26.92/0.04/26.87/26.88/26.97 | 3.7518 |
| hv_triton_1x256x9x48x128_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 109.32/109.66/1.57/107.48/108.00/111.39 | 62.03/62.07/0.23/61.86/61.89/62.31 | 1.7625 |
| hv_triton_1x256x9x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 63.30/63.23/0.56/62.41/62.57/63.83 | 16.70/16.69/0.04/16.63/16.64/16.74 | 3.7912 |
| hv_triton_1x256x9x48x40_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 90.87/90.91/0.36/90.45/90.61/91.26 | 28.92/28.92/0.04/28.87/28.88/28.96 | 3.1421 |
| hv_triton_1x512x2x12x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.00/32.98/0.47/32.29/32.41/33.44 | 9.07/9.12/0.19/8.92/8.96/9.31 | 3.6402 |
| hv_triton_1x512x2x12x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.72/45.23/1.23/42.92/43.93/46.28 | 16.63/16.64/0.04/16.59/16.60/16.69 | 2.7497 |
| hv_triton_1x512x2x12x32_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.80/33.42/0.92/32.03/32.44/34.35 | 9.47/9.55/0.31/9.28/9.30/9.93 | 3.5692 |
| hv_triton_1x512x2x12x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.61/46.21/1.57/44.68/44.85/48.26 | 17.68/17.69/0.03/17.66/17.66/17.72 | 2.5790 |
| hv_triton_1x512x2x24x20_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.05/33.00/1.08/31.54/31.80/34.06 | 10.36/10.35/0.04/10.27/10.31/10.39 | 3.1902 |
| hv_triton_1x512x2x24x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.13/44.38/1.48/42.31/43.03/46.30 | 17.69/17.68/0.02/17.67/17.67/17.70 | 2.4946 |
| hv_triton_1x512x2x24x64_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 34.45/34.50/0.60/33.34/33.96/35.09 | 22.79/22.79/0.01/22.77/22.78/22.80 | 1.5116 |
| hv_triton_1x512x2x24x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.93/46.39/1.87/44.52/44.68/48.62 | 20.74/20.75/0.06/20.69/20.70/20.81 | 2.2142 |
| hv_triton_1x512x2x32x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.53/33.04/0.83/32.22/32.29/34.06 | 9.39/9.51/0.26/9.25/9.26/9.82 | 3.4632 |
| hv_triton_1x512x2x32x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.55/45.83/0.93/44.57/44.92/46.95 | 20.69/20.64/0.13/20.35/20.50/20.72 | 2.2016 |
| hv_triton_1x512x2x32x32_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.95/34.12/0.55/33.36/33.58/34.70 | 16.64/16.64/0.03/16.61/16.62/16.67 | 2.0408 |
| hv_triton_1x512x2x32x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 46.33/46.62/1.24/45.31/45.34/48.17 | 18.73/18.71/0.04/18.66/18.66/18.76 | 2.4737 |
| hv_triton_1x512x2x64x20_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.39/33.27/0.60/32.54/32.58/33.86 | 19.08/19.06/0.06/18.97/19.00/19.13 | 1.7498 |
| hv_triton_1x512x2x64x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.12/45.13/0.97/43.69/43.94/46.10 | 21.78/21.78/0.02/21.76/21.77/21.81 | 2.0713 |
| hv_triton_1x512x2x64x64_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 58.91/58.91/0.11/58.72/58.78/59.04 | 16.61/16.63/0.06/16.58/16.59/16.70 | 3.5474 |
| hv_triton_1x512x2x64x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 85.93/86.06/0.32/85.68/85.79/86.47 | 27.45/27.43/0.11/27.25/27.29/27.54 | 3.1302 |
| hv_triton_1x512x3x128x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.35/97.83/0.95/97.06/97.10/99.20 | 41.59/41.58/0.08/41.45/41.48/41.65 | 2.3405 |
| hv_triton_1x512x3x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 107.68/107.73/0.24/107.42/107.49/108.05 | 21.78/21.78/0.04/21.74/21.74/21.84 | 4.9445 |
| hv_triton_1x512x3x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 93.13/94.04/2.17/91.67/91.76/96.68 | 22.48/22.48/0.12/22.30/22.33/22.61 | 4.1423 |
| hv_triton_1x512x3x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 40.86/40.91/0.29/40.55/40.62/41.23 | 16.64/16.64/0.04/16.58/16.60/16.68 | 2.4547 |
| hv_triton_1x512x5x12x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 32.31/32.66/0.77/31.76/31.94/33.53 | 9.76/9.65/0.34/9.23/9.26/10.00 | 3.3111 |
| hv_triton_1x512x5x12x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 43.78/43.85/0.88/42.72/43.09/44.78 | 18.15/18.15/0.21/17.81/17.96/18.33 | 2.4121 |
| hv_triton_1x512x5x12x32_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.82/34.14/0.87/33.30/33.47/35.29 | 16.61/16.62/0.03/16.57/16.59/16.65 | 2.0355 |
| hv_triton_1x512x5x12x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 44.81/44.62/0.71/43.51/43.69/45.31 | 18.71/18.72/0.04/18.67/18.69/18.76 | 2.3953 |
| hv_triton_1x512x5x24x20_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.69/33.76/0.89/32.71/33.01/34.60 | 18.69/18.69/0.03/18.65/18.65/18.73 | 1.8027 |
| hv_triton_1x512x5x24x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.33/45.55/0.95/44.23/44.46/46.59 | 18.72/18.72/0.03/18.70/18.70/18.75 | 2.4220 |
| hv_triton_1x512x5x24x64_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 54.81/54.87/0.16/54.73/54.73/55.09 | 16.63/16.64/0.04/16.60/16.61/16.68 | 3.2966 |
| hv_triton_1x512x5x24x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 80.58/80.73/0.50/80.30/80.31/81.38 | 26.90/27.99/2.89/26.80/26.83/30.01 | 2.9953 |
| hv_triton_1x512x5x32x10_C | C | triton_group_norm_silu | cuda_kernel | cont_small | optimized | 33.50/33.39/0.52/32.53/32.74/33.88 | 14.45/14.45/0.01/14.44/14.44/14.45 | 2.3188 |
| hv_triton_1x512x5x32x10_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 45.24/45.53/0.95/44.43/44.57/46.72 | 20.73/20.74/0.05/20.67/20.69/20.79 | 2.1819 |
| hv_triton_1x512x5x32x32_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 36.58/36.72/0.60/36.24/36.33/37.26 | 16.63/16.64/0.05/16.57/16.59/16.69 | 2.1991 |
| hv_triton_1x512x5x32x32_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 52.86/52.99/0.30/52.76/52.76/53.28 | 24.83/24.84/0.02/24.81/24.81/24.86 | 2.1288 |
| hv_triton_1x512x5x64x20_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 44.76/44.83/0.12/44.69/44.72/44.97 | 16.66/16.64/0.05/16.55/16.58/16.68 | 2.6875 |
| hv_triton_1x512x5x64x20_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 68.60/68.46/0.38/67.96/68.05/68.86 | 26.28/26.25/0.12/26.09/26.12/26.37 | 2.6100 |
| hv_triton_1x512x5x64x64_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 97.49/98.38/2.15/95.69/96.41/100.67 | 25.23/25.22/0.06/25.14/25.15/25.28 | 3.8639 |
| hv_triton_1x512x5x64x64_NC | NC | triton_group_norm_silu | cuda_kernel | nchw_last | optimized | 109.81/110.43/3.89/106.27/106.30/115.41 | 51.71/51.69/0.10/51.55/51.59/51.81 | 2.1237 |
| hv_triton_1x512x9x128x128_C | C | triton_group_norm_silu | baseline_fallback | baseline_fallback | baseline_equivalent | 99.70/100.65/1.66/99.46/99.46/102.44 | 104.19/104.11/2.19/100.58/101.75/106.70 | 0.9570 |
| hv_triton_1x512x9x128x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.23/96.56/1.37/94.74/95.47/97.81 | 39.50/39.50/0.10/39.32/39.40/39.59 | 2.4362 |
| hv_triton_1x512x9x48x128_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 94.56/95.94/2.76/92.64/93.52/99.54 | 47.90/47.89/0.20/47.60/47.68/48.09 | 1.9741 |
| hv_triton_1x512x9x48x40_C | C | triton_group_norm_silu | cuda_kernel | cont_split | optimized | 96.74/96.81/2.64/93.68/94.19/100.19 | 22.84/22.85/0.07/22.78/22.80/22.91 | 4.2354 |

Non-production regression-grid rows (12, contract shapes x dtypes) all PASSED in-benchmark correctness; their timings and dispatch metadata are in `bench/results.jsonl` but excluded from the headline by design.
