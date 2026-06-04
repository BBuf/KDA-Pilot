# NCU Report: r0v1 — nss-b1-s176400-d5120-bf16-s11D.bf16 (candidate v1)

- Case: `nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06` (mova-720p,
  largest captured row count), candidate kernel `norm_scale_shift_kernel`
  (single-pass-variance build, vec32, block=D/16=320), `-lineinfo` profiling
  build, ion-b200 GPU0 (idle before/after), `ncu --set full`, 3 instances.
- Note: ncu locks clocks to base — durations here (≈1181us) are not comparable
  to the boost-clock benchmark numbers (733us); ratios and SOL percentages are.

## Six analysis dimensions

1. Occupancy: 56.4% warps-active (block 320, regs 40 → 5 CTAs/SM theoretical
   78%; barrier serialization between reduction phases costs the rest).
   Waves/SM ≈ 298 → no tail effect at this scale.
2. Compute/memory balance: **sm_SOL 65.8% > mem_SOL 45.4%** — the kernel is
   issue/compute-pressured, not purely DRAM-limited, despite being a
   memcpy-class op. dram traffic 1.81+1.76 GB matches the 4 B/elem model.
3. Stalls: long_scoreboard only 3.26 (memory latency well hidden);
   not_selected 2.76 + math_pipe_throttle 1.25 corroborate issue pressure.
4. Tensor core: n/a (no MMA).
5. Timeline: flat across instances (1181.5/1181.2/1181.2us) — stable.
6. Memory: read+write ≈ symmetric; no over-fetch (bytes match model, so
   broadcast scale/shift rows stay L2-resident as designed).

## Diagnosis (playbook match)

"High SM SOL on a bandwidth-class kernel" → per-element instruction count is
the limiter at the margin: per-element float<->bf16 conversions, the rounding
round-trip, epilogue FMAs, plus reduction shuffles — all on top of only 4 B of
traffic per element. At boost clocks the benchmark still reaches 4.87 TB/s
(~61% of peak), 1.45x over the CuTe baseline (3.36 TB/s).

## Resulting design change

- None for this bucket in v2 (already the best-performing bucket). Queued
  lever for a later bounded round: packed bf16x2 conversions
  (`__bfloat1622float2` / `__float22bfloat162_rn`) to cut convert-instruction
  count; revisit only if the two-pass-variance flip (v2, contract fix)
  measurably hurts this bucket.
