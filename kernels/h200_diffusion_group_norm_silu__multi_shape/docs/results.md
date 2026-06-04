# Final Results — h200_diffusion_group_norm_silu__multi_shape

**Headline (frozen 48-row production set, equal-weight geomean): 1.4787**
(arithmetic mean 1.5621, min 0.9464, max 3.9220; sum-of-medians wall
3434 us -> 2812 us = 1.2212x). 57/57 workloads PASSED; correctness suite
**210/210** green before timing. **Every timed row executes solution-owned
CUDA kernels** — the candidate contains no baseline routing of any kind.

- Run: ion8-h200 (NVIDIA H200, `REMOTE_GPU_ID=3`, idle before/after — see
  results.jsonl provenance), container `sglang_bbuf`, torch 2.11.0+cu130,
  CUDA 13.0, triton 3.6.0, tvm-ffi 0.1.9.
- Command: `CUDA_VISIBLE_DEVICES=3 python3 bench/benchmark.py --device cuda:0
  --out bench/results.jsonl` (frozen template policy: 7 trials, warmup 10,
  inner-loop to ~1000 us, deterministic interleaved A/B, isolated
  subprocesses, preallocated outputs on BOTH sides).
- Baseline: upstream sglang main `133254086b` Triton kernels, copied locally
  and driven through destination-passing local wrappers (replicating the
  copied launcher bodies verbatim; verified bit-identical to the
  allocate-and-return entries). A/A under this exact contract: 0.9990.
- Cross-run context: an equivalent run with the generic giant route on the
  clean class measured headline 1.5010 (docs/run_log.md); full-run headlines
  sit in a ±1.5% band run-to-run, and the route change affects only the
  10-row clean class. This run is the promotion record because its code is
  the shipped configuration.

## Per-regime summary (all solution-owned CUDA; dispatch in docs/dispatch.md)

| route | n | geomean | min | max |
|---|---:|---:|---:|---:|
| cuda one-pass, 256-thread blocks (gs < 32K) | 7 | 1.6408 | 1.2873 | 1.7951 |
| cuda one-pass, 1024-thread blocks (32K <= gs < 64K) | 5 | 1.7380 | 1.6878 | 1.7799 |
| cuda chunked 3-kernel (large) | 20 | 1.8391 | 1.1787 | 3.9220 |
| cuda giant 2-kernel (straddle shapes) | 6 | 1.1030 | 1.0562 | 1.2094 |
| cuda clean-giant 2-kernel (spatial % 8192 == 0) | 10 | 0.9776 | 0.9464 | 1.0824 |

## AC-5 per-row floor: explicit no-go record

The immutable acceptance criterion requires geomean > 1.0 (met: 1.4787) AND
no production row below 0.97x. **The floor is NOT met: 6 rows sit in
[0.9464, 0.9690]**, all in the clean-giant class (giants whose per-channel
spatial extent is a multiple of 8192, where the copied baseline's chunked
Triton kernels run straddle-free with a hoisted-affine apply at their
measured best, ~81-85% of H200 peak HBM).

This class absorbed **twelve measured candidate variants** across the rounds
(occupancy fix to the 32-reg full-occupancy boundary, exact grids, fused
deterministic last-block finalize, per-shape zero-straddle tiles, streaming
`__ldcs`/`__stcs` hints, ILP split accumulators, tile sweeps 8K/16K/32K,
grid-stride and wave-model rejections, and finally the review-prescribed
dedicated clean pipeline — branch-free hoisted-affine apply with
channel-aligned tiles — at both the prescribed 8192 tile, which regressed to
0.89-0.94, and the proven per-shape divisor tile, which matched but did not
beat the generic route). Every structurally distinct implementation lands in
the same 0.94-0.97 band with ±2-4% run-to-run swing; both implementations
sit near the same memory roofline, and the residual 3-5% on this class did
not close.

**User ruling (DEC-7, 2026-06-05, recorded in the goal tracker evolution
log): the 0.97 per-row floor is formally waived for this documented class —
the bound is accepted and the pure all-CUDA candidate promotes at the
1.4787 headline.** The waiver is class-scoped and evidence-bound: it covers
exactly the giants with spatial % 8192 == 0, on the strength of the
12-variant attempt history and the shared-roofline analysis above. All other
rows remain subject to the unrevised floor (and meet it).

## Roofline conclusion

- Largest production row `[1,256,17,256,256]` (group_size 8.9M, 570 MB fp16):
  traffic floor = 2 reads + 1 write = 1.71 GB. Baseline ~441 us = 3.88 TB/s
  ~= 81% of the 4.8 TB/s peak; candidate ~461 us = 3.71 TB/s ~= 77%
  (clean stats ~68-72% DRAM, clean apply ~85%).
- Candidate structural wins: small groups 1.29-1.80x (one CTA per group;
  1024-thread blocks for the crossover band where 32 resident CTAs starve
  the part); large groups up to 3.92x (persistent chunked pipeline);
  straddle giants 1.06-1.21x (two-segment vectorized tiles where the
  baseline drops to per-element affine).

## LTX upsampler diagnostics (production=false, wrapper path)

bf16 8x12: 1.731 | fp32 8x12: 1.842 | bf16 16x24: 3.093 | fp32 16x24: 4.894 |
bf16 32x48: 1.149 — plus wrapper-path production spot checks 0.96-1.90
matching their direct-entry rows.

## Per-shape production table (48 rows, group_size ascending)

| workload | route | base med (us) | cand med (us) | speedup |
|---|---|---:|---:|---:|
| 1x512x2x12x10 | cuda one-pass (256 thr) | 21.83 | 12.52 | 1.7438 |
| 1x512x5x12x10 | cuda one-pass (256 thr) | 21.38 | 12.29 | 1.7388 |
| 1x512x2x32x10 | cuda one-pass (256 thr) | 21.63 | 12.31 | 1.7566 |
| 1x512x2x12x32 | cuda one-pass (256 thr) | 22.23 | 12.39 | 1.7951 |
| 1x512x2x24x20 | cuda one-pass (256 thr) | 21.74 | 12.20 | 1.7811 |
| 1x512x5x32x10 | cuda one-pass (256 thr) | 21.66 | 14.83 | 1.4608 |
| 1x512x5x12x32 | cuda one-pass (256 thr) | 21.68 | 16.85 | 1.2873 |
| 1x512x2x32x32 | cuda one-pass (1024 thr) | 21.28 | 11.96 | 1.7799 |
| 1x512x5x24x20 | cuda one-pass (1024 thr) | 21.80 | 12.36 | 1.7633 |
| 1x512x2x64x20 | cuda one-pass (1024 thr) | 21.45 | 12.28 | 1.7470 |
| 1x256x3x48x40 | cuda one-pass (1024 thr) | 21.48 | 12.54 | 1.7137 |
| 1x512x2x24x64 | cuda one-pass (1024 thr) | 22.10 | 13.09 | 1.6878 |
| 1x512x5x32x32 | cuda chunked 3-kernel | 33.46 | 26.79 | 1.2490 |
| 1x512x3x48x40 | cuda chunked 3-kernel | 38.80 | 26.61 | 1.4580 |
| 1x512x5x64x20 | cuda chunked 3-kernel | 42.76 | 26.59 | 1.6083 |
| 1x256x3x128x40 | cuda chunked 3-kernel | 51.76 | 26.64 | 1.9430 |
| 1x512x5x24x64 | cuda chunked 3-kernel | 52.02 | 26.58 | 1.9567 |
| 1x512x2x64x64 | cuda chunked 3-kernel | 55.30 | 26.68 | 2.0732 |
| 1x256x9x48x40 | cuda chunked 3-kernel | 58.71 | 26.47 | 2.2184 |
| 1x256x3x48x128 | cuda chunked 3-kernel | 63.33 | 27.10 | 2.3371 |
| 1x128x5x96x80 | cuda chunked 3-kernel | 66.77 | 25.86 | 2.5824 |
| 1x512x3x128x40 | cuda chunked 3-kernel | 103.75 | 26.45 | 3.9220 |
| 1x512x9x48x40 | cuda chunked 3-kernel | 58.70 | 27.32 | 2.1491 |
| 1x512x3x48x128 | cuda chunked 3-kernel | 59.06 | 28.15 | 2.0983 |
| 1x256x5x96x80 | cuda chunked 3-kernel | 58.92 | 28.50 | 2.0677 |
| 1x512x5x64x64 | cuda chunked 3-kernel | 58.60 | 30.02 | 1.9522 |
| 1x256x9x128x40 | cuda chunked 3-kernel | 58.03 | 35.29 | 1.6442 |
| 1x256x3x128x128 | cuda chunked 3-kernel | 58.66 | 36.04 | 1.6280 |
| 1x128x5x256x80 | cuda chunked 3-kernel | 59.35 | 38.20 | 1.5537 |
| 1x256x9x48x128 | cuda chunked 3-kernel | 58.62 | 40.95 | 1.4315 |
| 1x128x5x96x256 | cuda chunked 3-kernel | 59.09 | 46.69 | 1.2654 |
| 1x128x17x96x80 | cuda chunked 3-kernel | 57.89 | 49.11 | 1.1787 |
| 1x512x9x128x40 | cuda giant 2-kernel | 61.90 | 51.18 | 1.2094 |
| 1x512x3x128x128 | cuda clean-giant | 59.03 | 54.53 | 1.0824 |
| 1x256x5x256x80 | cuda giant 2-kernel | 60.32 | 55.08 | 1.0950 |
| 1x512x9x48x128 | cuda giant 2-kernel | 65.09 | 57.88 | 1.1246 |
| 1x256x5x96x256 | cuda clean-giant | 64.75 | 64.12 | 1.0098 |
| 1x256x17x96x80 | cuda giant 2-kernel | 72.85 | 68.46 | 1.0642 |
| 1x256x9x128x128 | cuda clean-giant | 73.06 | 76.66 | 0.9531 |
| 1x128x5x256x256 | cuda clean-giant | 79.77 | 81.95 | 0.9734 |
| 1x128x17x256x80 | cuda giant 2-kernel | 92.39 | 85.90 | 1.0756 |
| 1x128x17x96x256 | cuda clean-giant | 96.77 | 99.87 | 0.9690 |
| 1x512x9x128x128 | cuda clean-giant | 132.18 | 137.18 | 0.9636 |
| 1x256x5x256x256 | cuda clean-giant | 144.67 | 148.66 | 0.9731 |
| 1x256x17x256x80 | cuda giant 2-kernel | 169.53 | 160.51 | 1.0562 |
| 1x256x17x96x256 | cuda clean-giant | 176.93 | 186.94 | 0.9464 |
| 1x128x17x256x256 | cuda clean-giant | 228.44 | 239.20 | 0.9550 |
| 1x256x17x256x256 | cuda clean-giant | 442.06 | 461.94 | 0.9570 |

Raw per-trial samples and provenance live in `bench/results.jsonl` (local + remote; excluded from the PR per the artifact policy).
