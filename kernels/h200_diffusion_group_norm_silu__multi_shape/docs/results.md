# Final Results — h200_diffusion_group_norm_silu__multi_shape

**Headline (frozen 48-row production set, equal-weight geomean): 1.3961**
(arithmetic mean 1.4808, min 0.9662, max 3.8642; sum-of-medians wall
3489 us -> 2875 us = 1.2135x). 57/57 workloads PASSED; correctness suite
210/210 green before timing (production grid, contract regression grid at
both eps values, wrapper path incl. all LTX diagnostics, edge layouts,
poison/grad-gate/Triton-authenticity methodology checks).

- Run: ion8-h200 (NVIDIA H200, `REMOTE_GPU_ID=3`, idle before/after — see
  results.jsonl provenance), container `sglang_bbuf`, torch 2.11.0+cu130,
  CUDA 13.0, triton 3.6.0, tvm-ffi 0.1.9.
- Command: `CUDA_VISIBLE_DEVICES=3 python3 bench/benchmark.py --device cuda:0
  --out bench/results.jsonl` (frozen template policy: 7 trials, warmup 10,
  inner-loop to ~1000 us, deterministic interleaved A/B, isolated
  subprocesses).
- Baseline: upstream sglang main `133254086b` Triton kernels, copied locally
  (docs/baseline_source.md). Candidate source: solution/ at the PR commit.
- This is the second of two back-to-back full runs (run A geomean 1.3972 /
  min 0.9252, run B = this run 1.3961 / min 0.9662): the headline is stable
  to +-0.1%; individual host-bound rows swing +-3-7% between processes. Both
  runs are retained in docs/run_log.md; this run is the promotion record.

## Per-regime summary (dispatch table in docs/dispatch.md)

| route | n | geomean | min | max |
|---|---:|---:|---:|---:|
| cuda one-pass (small groups) | 9 | 1.5904 | 1.1230 | 1.8569 |
| cuda chunked 3-kernel (large) | 20 | 1.7996 | 1.2070 | 3.8642 |
| cuda giant 2-kernel | 7 | 1.0272 | 0.9898 | 1.0891 |
| baseline-fallback (giant, Triton-clean) | 9 | 0.9937 | 0.9662 | 1.0030 |
| baseline-fallback (small crossover) | 3 | 0.9857 | 0.9774 | 0.9904 |

The 12 fallback rows execute the IDENTICAL copied Triton kernels on both
sides of the comparison (the candidate dispatcher routes to the local
baseline per the promotion decision DEC-6); their 0.97-1.00 readings measure
the dispatcher's host-side routing tax on host-bound rows, not device
regression — the A/A harness validation (geomean 1.0037 over 8 spread rows)
bounds the glue itself at ~0.99-1.00, and the one row below the 0.97 floor
(`1x256x5x96x256`, 0.9662; 0.948/0.958/0.966 across three runs) is a 61 us
host-bound row paying ~2-3% routing tax on device-identical work.

## Roofline conclusion

- Largest production row `[1,256,17,256,256]` (group_size 8.9M, 570 MB
  fp16): traffic floor = 2 reads + 1 write = 1.71 GB. Baseline Triton
  chunked: ~440 us = 3.89 TB/s ~= 81% of the 4.8 TB/s H200 peak. Candidate
  giant pipeline at its best measured ~457 us (apply kernel ~85% DRAM, stats
  kernel ~68% with the fused finalize) — within ~4% of the baseline and ~78%
  of peak; the row routes to the baseline fallback (spatial % 8192 == 0)
  whose reading is parity by construction.
- The candidate's structural wins: small groups (one CTA per group, two
  in-kernel passes — up to 1.86x where launch overhead dominates the
  baseline), large groups (persistent chunked 3-kernel pipeline — up to
  3.86x), and giants whose spatial extent straddles the baseline's
  8192-element chunk (the two-segment vectorized giant apply keeps full
  streams where Triton drops to per-element affine: 1.03-1.09x).
- Named bound for the all-CUDA giant gap (NCU, profile/ncu_giant_v0): the
  original ported apply kernel sat at 52 regs -> 4 CTAs/SM -> 44% occupancy
  / 41% DRAM; rebuilding it register-lean (32 regs = the H200 100%-occupancy
  boundary, exact one-task-per-CTA grids, hoisted single-channel fast loop)
  lifted the giant bucket from 0.756 to 0.94-0.99 geomean across bounded
  attempts v1-v7; the residual 3-6% on Triton-clean-stream shapes is the
  stats kernel's block-reduce overhead per chunk plus per-process variance,
  and is routed around (not shipped) per DEC-6.

## LTX upsampler diagnostics (production=false, wrapper path)

| diagnostic | base med (us) | cand med (us) | speedup |
|---|---:|---:|---:|
| ltx 1x1024x16x8x12 bf16 | 28.66 | 27.81 | 1.0305 |
| ltx 1x1024x16x8x12 fp32 | 29.41 | 29.36 | 1.0017 |
| ltx 1x1024x16x16x24 bf16 | 87.43 | 28.56 | 3.0614 |
| ltx 1x1024x16x16x24 fp32 | 147.84 | 32.23 | 4.5867 |
| ltx 1x1024x16x32x48 bf16 | 71.37 | 57.89 | 1.2328 |

## Per-shape production table (48 rows, group_size ascending)

| workload | route | base med (us) | cand med (us) | speedup |
|---|---|---:|---:|---:|
| 1x512x2x12x10 | cuda one-pass | 25.06 | 13.58 | 1.8456 |
| 1x512x5x12x10 | cuda one-pass | 25.04 | 13.49 | 1.8569 |
| 1x512x2x32x10 | cuda one-pass | 24.44 | 13.50 | 1.8100 |
| 1x512x2x12x32 | cuda one-pass | 25.57 | 13.89 | 1.8403 |
| 1x512x2x24x20 | cuda one-pass | 25.00 | 13.77 | 1.8155 |
| 1x512x5x32x10 | cuda one-pass | 24.94 | 15.95 | 1.5633 |
| 1x512x5x12x32 | cuda one-pass | 24.66 | 17.97 | 1.3720 |
| 1x512x2x32x32 | cuda one-pass | 24.71 | 18.94 | 1.3043 |
| 1x512x5x24x20 | cuda one-pass | 24.63 | 21.93 | 1.1230 |
| 1x512x2x64x20 | baseline-fallback (small) | 24.36 | 24.92 | 0.9774 |
| 1x256x3x48x40 | baseline-fallback (small) | 24.81 | 25.06 | 0.9904 |
| 1x512x2x24x64 | baseline-fallback (small) | 25.14 | 25.41 | 0.9895 |
| 1x512x5x32x32 | cuda chunked 3-kernel | 33.47 | 27.57 | 1.2137 |
| 1x512x3x48x40 | cuda chunked 3-kernel | 38.94 | 28.06 | 1.3880 |
| 1x512x5x64x20 | cuda chunked 3-kernel | 42.63 | 27.65 | 1.5417 |
| 1x256x3x128x40 | cuda chunked 3-kernel | 52.04 | 27.61 | 1.8845 |
| 1x512x5x24x64 | cuda chunked 3-kernel | 51.83 | 28.13 | 1.8424 |
| 1x512x2x64x64 | cuda chunked 3-kernel | 55.59 | 27.94 | 1.9897 |
| 1x256x9x48x40 | cuda chunked 3-kernel | 58.79 | 27.48 | 2.1394 |
| 1x256x3x48x128 | cuda chunked 3-kernel | 63.34 | 27.79 | 2.2795 |
| 1x128x5x96x80 | cuda chunked 3-kernel | 67.24 | 27.68 | 2.4294 |
| 1x512x3x128x40 | cuda chunked 3-kernel | 107.36 | 27.78 | 3.8642 |
| 1x512x9x48x40 | cuda chunked 3-kernel | 61.19 | 28.70 | 2.1320 |
| 1x512x3x48x128 | cuda chunked 3-kernel | 62.33 | 29.80 | 2.0914 |
| 1x256x5x96x80 | cuda chunked 3-kernel | 60.89 | 30.03 | 2.0276 |
| 1x512x5x64x64 | cuda chunked 3-kernel | 61.24 | 31.70 | 1.9316 |
| 1x256x9x128x40 | cuda chunked 3-kernel | 61.89 | 37.13 | 1.6667 |
| 1x256x3x128x128 | cuda chunked 3-kernel | 61.08 | 37.61 | 1.6242 |
| 1x128x5x256x80 | cuda chunked 3-kernel | 61.83 | 39.82 | 1.5526 |
| 1x256x9x48x128 | cuda chunked 3-kernel | 59.95 | 42.54 | 1.4094 |
| 1x128x5x96x256 | cuda chunked 3-kernel | 59.57 | 48.12 | 1.2379 |
| 1x128x17x96x80 | cuda chunked 3-kernel | 60.63 | 50.23 | 1.2070 |
| 1x512x9x128x40 | cuda giant 2-kernel | 61.78 | 56.72 | 1.0891 |
| 1x512x3x128x128 | cuda giant 2-kernel | 61.26 | 58.69 | 1.0437 |
| 1x256x5x256x80 | cuda giant 2-kernel | 62.87 | 60.23 | 1.0439 |
| 1x512x9x48x128 | cuda giant 2-kernel | 65.55 | 64.07 | 1.0231 |
| 1x256x5x96x256 | baseline-fallback (giant) | 61.09 | 63.23 | 0.9662 |
| 1x256x17x96x80 | cuda giant 2-kernel | 72.65 | 73.39 | 0.9898 |
| 1x256x9x128x128 | baseline-fallback (giant) | 71.78 | 72.47 | 0.9905 |
| 1x128x5x256x256 | baseline-fallback (giant) | 79.03 | 78.95 | 1.0011 |
| 1x128x17x256x80 | cuda giant 2-kernel | 92.13 | 92.89 | 0.9918 |
| 1x128x17x96x256 | baseline-fallback (giant) | 96.40 | 96.61 | 0.9978 |
| 1x512x9x128x128 | baseline-fallback (giant) | 131.57 | 131.76 | 0.9985 |
| 1x256x5x256x256 | baseline-fallback (giant) | 143.75 | 143.32 | 1.0030 |
| 1x256x17x256x80 | cuda giant 2-kernel | 168.37 | 166.34 | 1.0122 |
| 1x256x17x96x256 | baseline-fallback (giant) | 175.80 | 176.42 | 0.9965 |
| 1x128x17x256x256 | baseline-fallback (giant) | 227.29 | 228.04 | 0.9967 |
| 1x256x17x256x256 | baseline-fallback (giant) | 437.22 | 440.09 | 0.9935 |


Raw per-trial samples, provenance (GPU state before/after, versions, settings) live in `bench/results.jsonl` (kept local + remote; excluded from the PR per the artifact policy — this table is the committed record).
