# NCU + Roofline Report — normv5 candidate vs SGLang baseline

- Host: `ion8-h200` (`ion-h200-8`), container `sglang_bbuf`, GPU id 7 (NVIDIA H200), idle.
- Tool: Nsight Compute 2025.3.1.0. SGLang `c47f0e7cd`, torch 2.11.0+cu130.
- Method: targeted `--metrics` on the post-warmup launch (`--launch-skip 5 --launch-count 1`),
  Python entrypoint `harness/profile_entry.py`. CSVs + logs in `analysis/`.
- H200 HBM3e peak ~4.8 TB/s. `dram__throughput...pct_of_peak_sustained_elapsed` is the
  fraction of that peak achieved (the active-bound indicator for these kernels).

## Per-bucket bound table (kernel-only)

| Bucket | which | dur (us) | DRAM % | SM % | occ % | grid | active bound |
|---|---|---|---|---|---|---|---|
| LN fp32 [8640,5120] | baseline | 85.8 | 79.73 | 46.9 | 46.4 | 8640 | HBM bandwidth |
| LN fp32 [8640,5120] | candidate | 85.6 | **79.83** | 22.1 | 58.7 | 8640 | HBM bandwidth |
| RMS huge [648720,128] | baseline | 76.8 | 83.15 | 41.4 | 92.9 | 40545 | HBM bandwidth |
| RMS huge [648720,128] | candidate | 83.1 | **77.54** | 40.9 | 94.2 | 1056 | HBM bandwidth |
| RMS small [4096,128] | baseline | 3.0 | 7.44 | 8.7 | 21.7 | 512 | launch / dispatch |
| RMS small [4096,128] | candidate | 3.3 | 6.79 | 9.7 | 22.2 | 256 | launch / dispatch |

## Diagnosis per bucket (six-dimension walk → dominant signal)

### LN fp32 N=5120 (helios)
- Memory: candidate 79.83% DRAM ≈ baseline 79.73% → **at the HBM bandwidth bound**.
  Compute (SM) 22%, so not compute-bound. Occupancy 58.7% (higher than baseline's
  46.4%) is sufficient to saturate; pushing it further would not raise DRAM% (already
  at the ~80% practical ceiling for this streaming + 2-reduction access pattern).
- Exact-`N=5120` tiling (no masked over-read) gives a marginally faster kernel
  (85.6 vs 85.8 us); the 1.067x wall win comes from the leaner launch.
- Diagnosis: **bandwidth-bound, near attainable limit.** No further kernel lever
  expected to matter. Promote at parity+.

### RMS huge bf16 D=128 (hunyuanvideo M~650k)
- Memory: candidate 77.54% DRAM vs baseline 83.15% → both **HBM bandwidth bound**;
  the candidate kernel sits ~7% (of peak) below the baseline's achieved bandwidth,
  i.e. ~93% of what Triton's 16-row-tile / 40545-block kernel extracts.
- The 2-rows-per-warp 128-bit redesign lifted this from 70.65% (64-bit warp-per-row)
  to 77.54%. Occupancy is already 94% — the residual gap is the per-warp
  load→warp-reduce→store dependency vs the baseline's wider multi-row tiles, not
  occupancy. Closing the last ~5.6% would need a deeper tiling rewrite with
  diminishing return (baseline already ~83% of peak).
- Wall-clock is parity+ (1.04-1.046x) because the candidate launches 1056 blocks
  (lean) vs the baseline's 40545.
- Diagnosis: **bandwidth-bound; candidate near (not at) the kernel bound, wall parity+.**
  Per the user-confirmed policy, promote at documented parity+.

### RMS small bf16 D=128 (1320 / 4096 / 16384)
- The kernel runs in ~3 us at <8% DRAM and ~22% occupancy → **not memory-bound**;
  the row count is too small to fill the machine. End-to-end latency is dominated by
  host launch/dispatch (baseline ~31 us wall for a ~3 us kernel; the SGLang
  `register_custom_op` + Triton launch path adds ~28 us).
- Diagnosis: **launch/dispatch-bound.** The lever is the lean native callable, not
  the kernel. Candidate integrated path 14.93 us (dispatcher guard overhead 2.57 us)
  vs baseline 31.5 us → ~1.9-2.1x. No ~5 us fixed Python tax (AC-9 satisfied).

## Conclusion
- 3 HBM-bandwidth-bound shapes (helios LN + 2 huge RMS): parity-to-parity+ with the
  baseline at/near the HBM bound; geomean lever here is the leaner launch, not kernel
  bandwidth (which is at the bound for LN and ~93% of baseline for huge RMS).
- 3 launch/dispatch-bound shapes (small RMS): ~1.9x from the lean tvm-ffi dispatch.
- Overall geomean 1.4223x. No shape regresses (all ≥1.04x). The one residual kernel
  gap (huge RMS 77.5% vs 83% DRAM) is documented; further closing it is low-yield
  given the baseline is itself only ~83% of peak.
