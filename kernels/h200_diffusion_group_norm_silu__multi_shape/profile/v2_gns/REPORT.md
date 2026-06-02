# NCU Report — v2 large-path (3-stage) GroupNorm+SiLU

- Run: `profile/v2_gns/` (harness `harness/prof2.py`, metrics `reports/large_metrics.csv`)
- Host/GPU: ion8-h200, GPU 7 (NVIDIA H200), idle. CUDA_VISIBLE_DEVICES=7, no_grad.
- Shape: `[1,512,9,128,128]` fp16, num_groups=32, eps=1e-6 (gs=2,359,296 -> LARGE path). 151 MB.
- Benchmark context: this shape LOSES at 0.667x (cand 190µs vs baseline 127µs).
- Kernels profiled: gns_stats_kernel, gns_finalize_kernel, gns_apply_kernel (3 instances each).

## Key metrics (aggregate; apply/stats dominate)
| metric | value | reading |
|---|---|---|
| sm__throughput.avg.pct_of_peak | 66.5% | high compute utilization |
| dram__throughput.avg.pct_of_peak | 31.2% | LOW — memory under-utilized |
| sm__warps_active (achieved occupancy) | 39.8% | low (~40%) |
| launch__registers_per_thread | 52 | moderate-high -> caps occupancy |
| launch__waves_per_multiprocessor | 1 | single wave |
| grid_size | 528-1056 (=bps*132) | persistent grid |

## Six-dimension walk
- compute: HIGH (sm 66%) — the apply kernel is compute-leaning.
- memory: LOW (dram 31%) — NOT bandwidth-bound, so the gap vs baseline is not a BW wall.
- occupancy: LOW (~40%, 52 regs, 1 wave) — limited latency hiding.
- latency-hiding: weak (low occupancy + 1 wave).
- launch-overhead: small (3 launches, but kernels are ~100-190µs).
- tail-effect: 1 wave -> the persistent grid covers the SMs ~once.

## Diagnosis
The large path is COMPUTE / OCCUPANCY-bound, not BW-bound (dram only 31%). The Triton
baseline beats it here by being more compute-efficient (higher effective BW ~4000 GB/s).
Likely costs in my apply kernel:
1. Per-vector int64 DIVISION `(i0)/spatial` and `(i0+7)/spatial` for channel indexing.
   For these large shapes `spatial` >> chunk (8192), so a whole chunk lies in ONE channel,
   yet I still do int64 divs per vector. int64 div is ~tens of cycles, not pipelined.
2. 52 regs/thread caps occupancy at ~40% -> poor latency hiding -> dram only 31%.
3. sigmoid = z/(1+exp(-z)) per element (exp + fp32 div).

## Next edit (v3, ranked)
1. Hoist channel indexing to chunk granularity: compute `c = (group_base_off)/spatial` ONCE
   per chunk when `chunk_start/spatial == (chunk_end-1)/spatial` (true for large spatial),
   eliminating per-vector int64 divs (matches the baseline scalar-affine idea). EXPECT the
   biggest win on the giants.
2. `__launch_bounds__(256, N)` to cap registers -> raise occupancy -> lift dram% -> faster.
3. Re-profile; if dram% rises toward the baseline's effective ~84% of peak, the giants close.
Then re-benchmark; if the giants still lose after tuning, dispatch them to the baseline
(parity) — the small/medium 1.2-2.7x wins already give geomean 1.31x.
