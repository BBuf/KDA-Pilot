# NCU bound report — large-S RMS (S=650040, D=128, bf16)

Run: round 4, ion-b200 / NVIDIA B200, sglang 0b65588c, CUDA 13.0.88.
Kernel profiled: `rmsnorm_onepass_kernel<128,1,bf16_t>` (cand-0002 one-warp-per-row).
Full report (binary): `<REMOTE_KDA_DIR>/profile/rms_largeS_r4/reports/full_cand0002.ncu-rep`
(profiled via `ncu --set full -k regex:rmsnorm_onepass -s 1 -c 1` through the python JIT entrypoint;
a standalone `-lineinfo` harness is deferred to the formal task11 round).

## Key metrics
| metric | value |
|---|---|
| DRAM Throughput | 38.5% (2.56 TB/s) |
| Memory Throughput | 46.8% |
| Compute (SM) Throughput | 62.9% |
| Achieved Occupancy | 77.0% (49.3 active warps/SM) |
| Dominant stall | long scoreboard ~55.6% of 18.4 avg cycles/warp (global-load latency) |

## Active bound (interpretation)
NOT DRAM-bandwidth bound (38% DRAM, 47% mem). The limiter is the mix of
memory-load latency (long-scoreboard stalls) and SM issue/compute (63%, the
highest meter): the one-warp-per-row structure does a load -> warp-shuffle
reduce -> rsqrt -> store per row with limited row-to-row overlap.

## Optimization attempts (task10)
- kUnroll=2/4 MLP (issue several rows' loads before reducing): improved the kernel
  vs kUnroll=1 (~105us -> ~77us best, interleaved) but REGRESSED occupancy/TLP and
  still measured ~0.84-0.92x vs the Triton baseline (interleaved, idle GPU).
- kUnroll=8: worse (too few warps).
- Conclusion: the warp-per-row family cannot match the SGLang Triton 16-row tile
  for this huge bandwidth-streaming regime.

## Decision: NO-GO -> baseline fallback (parity)
Large-S RMS (648720, 650040) is removed from the CUDA allowlist; the dispatcher
falls back to the SGLang Triton baseline (= parity, no production regression).
No-go package: correctness (56/56), attempts (kUnroll 1/2/4/8), benchmark
(~0.84-0.92x interleaved), NCU (above), named bound (memory-latency + SM-issue;
warp-per-row inferior to 16-row tile).
