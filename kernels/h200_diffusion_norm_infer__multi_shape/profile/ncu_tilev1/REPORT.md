# NCU Report — tilev1 (multi-row tiled RMSNorm) vs SGLang Triton baseline

## Summary

The continuation-round question was whether a CUDA kernel can match the Triton
one-pass RMSNorm baseline's device time on the huge streaming shapes
([648720,128] bf16), where the prior persistent warp kernel (normv5) regressed
~9% at device level (83.1us @ 77.54% DRAM vs 76.8us @ 83.15%, profile/ncu_normv2).

**Answer: yes — exact device parity at the HBM bound.** The 8x128-tile kernel
(`rms_norm_tile<128,8,128,0,0,bf16>`, one tile per CTA, grid = ceil(M/8)) and
the Triton baseline measure an IDENTICAL single-launch duration of 77,664 ns on
the same GPU in the same session, with the candidate at 82.67% DRAM-of-peak vs
the baseline's 82.17%. The prior kernel's deficit was its capped persistent
grid (1056 blocks, 4.8 waves/SM) starving memory-level parallelism; the tile
kernel restores it (81,090 blocks, 38.4 waves/SM).

## Setup

- Host `ion8-h200` (ion-h200-8), container `sglang_bbuf`, GPU 0 (NVIDIA H200,
  idle-gated 0util/0MB/0 apps before, clean after), CUDA_VISIBLE_DEVICES=0,
  REMOTE_GPU_ID=0. ncu 2025.3.1.0, sglang editable @ 84e1108312,
  torch 2.11.0+cu130, triton 3.6.0.
- Harness: `harness/profile_entry.py` (5 warmup launches + 1 profiled;
  `--launch-skip 5 --launch-count 1`), `harness/run_ncu.sh` (targeted metric
  set; CSV parser filters the `==PROF==` preamble ncu prints to stdout).
- Profiled through the real dispatcher path (`src/norm_dispatch.py`), kernels
  built via SGLang jit_kernel/tvm-ffi `load_jit`, flags matching SGLang (no
  `--use_fast_math`). LN was not re-profiled: `layer_norm_n5120.cuh` is
  byte-unchanged from the `profile/ncu_normv2` run (79.83% DRAM == baseline
  79.73%, at the HBM bound).

## Measurements (analysis/*.csv)

| run | kernel | grid | waves/SM | gpu time | DRAM % peak | SM % | warps active % | dram bytes |
|---|---|---|---|---|---|---|---|---|
| rms_huge_cand | `rms_norm_tile<128,8,128>` | 81,090 | 38.39 | **77,664 ns** | **82.67** | 57.98 | 82.57 | 308.9 MB |
| rms_huge_base | `_rms_norm_tiled_onepass` | 40,545 | 19.20 | **77,664 ns** | **82.17** | 41.06 | 93.10 | 306.8 MB |
| rms_small_cand | `rms_norm_tile<128,8,128>` | 512 | 0.24 | 3,168 ns | 7.01 | 8.95 | 21.73 | 1.05 MB |
| rms_small_base | `_rms_norm_tiled_onepass` | 512 | 0.24 | 3,104 ns | 7.09 | 8.32 | 21.89 | 1.05 MB |

Prior-round reference (profile/ncu_normv2): warp kernel (normv5) on the same
huge shape: 83.1 us @ 77.54% DRAM, 1056 blocks; baseline then: 76.8 us @ 83.15%.

## Analysis dimensions

- **Memory**: huge shape is DRAM-bandwidth-bound on both legs (82.2–82.7% of
  peak sustained, ≈3.95–3.98 TB/s of the 4.8 TB/s HBM3e peak). The candidate
  moves +2.1 MB more DRAM traffic (per-CTA weight re-reads that miss L2 across
  81k CTAs) yet sustains slightly higher throughput — immaterial at this bound.
- **Occupancy / waves**: candidate 38.4 waves/SM of small CTAs (128 thr) vs
  baseline 19.2 waves (256-thr programs); both far above the latency-hiding
  threshold; warps-active 82.6% vs 93.1% — neither is the limiter.
- **Compute**: SM throughput 58.0% (cand) vs 41.1% (base) — well under the
  memory pressure; not the limiter.
- **Launch/tail**: 81k tiny CTAs amortize cleanly at 38 waves; no tail effect
  at this depth (the prior 1056-block persistent grid was the pathological
  case — too FEW CTAs, not too many).
- **Latency-hiding**: the prior normv2 diagnosis (capped grid-stride starving
  MLP) is confirmed by the fix: restoring a Triton-like CTA count lifted DRAM
  from 77.54% to 82.67%.
- **Small shape** ([4096,128]): both kernels ~3.1 us, <8% DRAM, 0.24 waves —
  launch/dispatch-bound; the wall delta on these shapes is entirely host-side
  (launcher path), as the symmetric benchmark's decomposition shows.

## Diagnosis → decision

- Matched playbook pattern: memory-bound streaming kernel limited by
  memory-level parallelism (CTA count), not by per-thread efficiency.
- Decision: the huge-RMS bucket ships the tile kernel — device parity (equal
  duration, equal-or-better DRAM%) plus the leaner host path. No fallback-by-M
  needed; the same kernel also wins every smaller captured shape, so the
  dispatcher routes ALL supported RMS shapes to it (single-kernel family).
- Residual headroom: both implementations sit at ~82–83% of peak DRAM — the
  practical HBM bound for this access pattern on H200; pushing further is not
  defensible (baseline itself caps there).

## Artifacts

- `analysis/rms_{huge,small}_{cand,base}.csv` + `.log` (raw targeted-metric CSVs)
- `harness/profile_entry.py`, `harness/run_ncu.sh` (reproduction; run inside
  the container from the synced workdir)
