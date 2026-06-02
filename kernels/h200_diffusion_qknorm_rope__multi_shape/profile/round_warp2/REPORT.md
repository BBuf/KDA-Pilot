# NCU REPORT — fused_qknorm_rope_warp2 (H200 / sm_90, bf16)

Run env: ion8-h200 GPU7 (idle), container `sglang_omni_bbuf_kda`, ncu 2025.3.1.0, candidate built
via SGLang load_jit with `-lineinfo` (KDA_LINEINFO=1). Raw reports (on REMOTE_KDA_DIR):
`profile/round_warp2_large/reports/full.ncu-rep`, `profile/round_warp2_tiny/reports/full.ncu-rep`.
`--set full`, one profiled launch of `fused_qknorm_rope_warp2` (2 warmups skipped).

## Summary

| Shape | Duration | DRAM % | Compute(SM) % | SM Busy % | Achieved Occ % (theo) | Dominant stall | Bound |
|---|---|---|---|---|---|---|---|
| qwen_t4096 (large) | 39.33 µs | 39.6 | 58.1 | 62.2 | 72.7 (75) | long-scoreboard 58.2% | memory-latency |
| qwen_t19 (tiny) | 4.13 µs | 1.25 | 3.30 | 15.0 | 12.4 (75) | n/a (0.07 waves/SM) | launch/underfill |

Registers/thread = 38 → theoretical occupancy capped at 75% (Block Limit Registers = 6). L2 hit 49.9%
(large).

## Diagnosis (six dimensions)
- **Compute**: not compute-bound (58% SM throughput large; 3% tiny). No tensor cores (elementwise).
- **Memory**: large shape DRAM only 39.6% of peak → NOT bandwidth-saturated. ~103 MB q/k read+write.
- **Occupancy**: large 72.7% (register-limited, 38 reg/thread); tiny 12.4% (only 57 blocks / 0.07 waves).
- **Latency-hiding**: large shape dominated by long-scoreboard (58.2% of 18.2 avg stall cycles) =
  waiting on global memory loads → **memory-latency-bound**.
- **Launch overhead**: tiny shape is launch/underfill-bound — device work 4.13 µs but the GPU is nearly
  empty; end-to-end ~8.5 µs is launch/dispatch dominated.
- **Tail effect**: large shape Waves Per SM = 1 (single wave; minimal tail). Tiny: 0.07 (pure underfill).

## Playbook match + design change
- Large = memory-latency-bound (long-scoreboard dominant, DRAM < 50% peak). The 2-heads-per-warp
  float4 path (vs the one-head baseline) raises useful memory work per issued warp instruction (one
  128-bit load/store per lane) and halves launched warps → better memory-level parallelism / latency
  hiding. Measured: module 1.07–1.08× on large shapes (>5% no-go bar cleared). Near the attainable
  bound for this irreducible-traffic elementwise kernel.
- Tiny = launch/underfill-bound → kernel no-go; addressed end-to-end by lean dispatch (wrapper ~1.10×).

## Ranked future direction (not pursued — outcome-metric stop)
Lower register pressure (process the 8 elements in two float4 halves) to raise occupancy above 75% and
hide more latency — bounded upside, risks complexity/correctness. Not pursued: the candidate already
clears the win bar and the bound is latency, not throughput.
