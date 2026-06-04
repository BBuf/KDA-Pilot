# Dispatch Policy — solution/binding.py + solution/kernel.cu

The shipped candidate is an all-CUDA dispatcher: every regime, production or
otherwise, runs solution-owned kernels. No baseline routing exists in the
candidate (the round-0 fallback experiment was removed per the round-0
review; see the attempt history below for what was measured).

| # | condition (group_size gs, spatial s) | route | rationale (final-run evidence) |
|---|---|---|---|
| 1 | gs < 32,768 | CUDA one-pass, 256-thread blocks (one CTA per group, two in-kernel passes) | launch-overhead-dominated; geomean 1.71, up to 1.88 |
| 2 | 32,768 <= gs < 65,536 | CUDA one-pass, 1024-thread blocks | with only num_groups resident CTAs, per-SM memory parallelism limits throughput; 4x wider blocks quadruple outstanding loads: 0.90 -> 1.69-1.90 on the crossover rows |
| 3 | 65,536 <= gs < 700,000 | CUDA chunked 3-kernel (stats -> finalize -> apply, 8192-elem tiles, persistent occupancy grid) | geomean 1.87, up to 4.02 |
| 4 | gs >= 700,000 (and s >= 16,384) | CUDA giant 2-kernel: register-lean exact-grid stats with fused last-block finalize + two-segment vectorized apply; per-shape zero-straddle tiles; `__ldcs`/`__stcs` streaming hints; ILP split accumulators | wins 0.99-1.17 where the baseline straddles its 8192 chunk; 0.94-0.97 on the straddle-free class (documented bound in docs/results.md) |

Notes:

- Unsupported layouts (non-contiguous, misaligned base) normalize to fresh
  aligned tensors and run the same CUDA kernels (correctness-only path; no
  production row hits it).
- fp16/bf16/fp32 all dispatch identically (kernels instantiate all three).
- Tunables: `GNS_SMALL_LARGE_THRESH` (65,536), `GNS_GIANT_THRESH` (700,000),
  giant tiles `GNS_GIANT_CHUNK` (16,384 target; per-shape zero-straddle
  divisor) / `GNS_GIANT_STATS_CHUNK` (0 = follow apply tile); the
  256->1024-thread one-pass boundary is `kSmallWideThreshold` (32,768) in
  solution/kernel.cu.

## Bounded giant-bucket attempt history (NCU-driven)

| variant | change | giant/near-giant evidence |
|---|---|---|
| v0 (port) | prior-round chunked 3-kernel on giants | 0.78 (0.63-0.93) |
| v1 | dedicated giant kernels: __launch_bounds__(256,8) (52->32 regs, 44%->82% occupancy), exact grids, 16K tiles | 0.82 (scalar straddle loop regressed straddle-heavy shapes) |
| v2 | two-segment vectorized straddle handling | 0.963 |
| v3 | fused last-block finalize (2 launches) + per-shape zero-straddle tiles | 0.990 |
| v4 | 32K tiles (env sweep) | 0.968 (tail waves on mid shapes) |
| v5 | grid-stride loops + wave-multiple grids | 0.891 (loop state pushed regs over the 32-reg cliff) |
| v6 | wave-cost-minimizing tile picker | 0.939 (model underweights per-task overhead) |
| v7 | independent 32K stats tile | 0.977 (no robust win) |
| r1-a | `__ldcs`/`__stcs` streaming hints (stats loads; apply loads+stores) | straddle giants 1.04-1.14; clean-stream class 0.946-0.984 |
| r1-b | 32K stats tile re-probe under streaming hints | 0.947 on the clean class (rejected) |
| r1-c | ILP split accumulators in stats (FADD-chain break), regs kept <= 32 | clean class unchanged (0.94-0.97) — bound declared |

Crossover-band history: round-0 measured the chunked pipeline (0.90 via
3-launch overhead at ~25 us) and a 2-launch one-channel-per-tile config
(0.90-0.93) before the 1024-thread one-pass variant landed 1.64-1.85.
