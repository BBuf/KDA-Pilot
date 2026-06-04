# NCU Report: select01 v2 vs Triton baseline (prod07 shape)

- Run: `profile/select01_v2/` — harness `harness/profile_select01.py`, report `reports/full.ncu-rep` (synced under `$REMOTE_KDA_DIR/kernel/profile/select01_v2/reports/`).
- Host/GPU: ion-h200-8, container `sglang_bbuf`, GPU 3 (idle: 0% / 0 MiB before run), CC 9.0 (H200), `ncu --set full --target-processes all`, 8 invocations per kernel profiled.
- Shape: B=1, L=8424, C=3072, bf16, int32 index, weight=bias=None (exact captured prod07 row).
- Build: candidate compiled with `KDA_LINEINFO=1` (profiling-only `-lineinfo`; benchmark builds keep default flags).

## Side-by-side (averages over 8 invocations)

| metric | Triton baseline `_fused_layernorm_..._select01_kernel` | native v2 `fused_ln_select01` |
|---|---|---|
| grid x block | (8424,1,1) x (128,1,1) | (8424,1,1) x (128,1,1) |
| Duration | **43.47 us** | **48.86 us** |
| DRAM Throughput (SOL) | 61.8% | 54.9% |
| Compute (SM) Throughput | 60.8% | 47.2% |
| L2 Throughput | 79.6% | 71.3% |
| Executed IPC (active) | 2.60 | 2.07 |
| Executed instructions | 20.45M | 18.11M |
| Elapsed cycles | 64,701 | 72,887 |
| **Average DRAM Active Cycles** | **84,042** | **84,048** |

## Diagnosis (dimensions: memory / latency-hiding)

The decisive pair is DRAM Active Cycles vs Elapsed Cycles: both kernels keep
DRAM busy for the SAME absolute number of cycles (~84.0k — identical bytes
moved, no waste on either side), but the native kernel stretches them over
12.7% more elapsed cycles. The gap is therefore NOT extra traffic and NOT an
instruction-count problem (native executes 11% FEWER instructions) — it is
un-overlapped memory latency: bubbles where no loads are in flight.

Structural cause in v2: the kernel ordered [load x tile] -> [block-reduction
barrier] -> per-iteration [load scale -> load shift -> fma -> store out ->
load gate -> store gate]. Everything after the barrier issues at most a couple
of loads per thread before stalling on them, so the memory pipeline drains at
the barrier and refills slowly three times. The Triton baseline issues its
whole BLOCK_N=4096 tile per phase, keeping far more loads in flight (higher
IPC 2.60 and DRAM 61.8%).

## Design change adopted (v3)

The modulation selection depends only on `index[b, l]` — available before the
reduction. v3 hoists the gate copy-through (load+store) and the selected
scale/shift tile loads into the x-load loop ABOVE the barrier, holding
scale/shift in fp32 registers; the post-barrier epilogue becomes pure
register compute + the out stores. Cost: ~64 extra fp32 registers/thread
(occupancy tradeoff measured by the v3 benchmark).

## Verdict

- Active bound: DRAM bandwidth with a latency-hiding defect in v2 (memory
  busy-cycle parity proves the traffic is minimal).
- Next edit: barrier hoist (implemented as cuda-flat-v3). If v3 still trails,
  the remaining lever is occupancy (drop the shift prefetch to halve register
  cost) — decided by measurement, not speculation.
