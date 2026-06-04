# Dispatch Policy — solution/binding.py

The shipped candidate is a five-regime dispatcher over solution-owned CUDA
kernels plus a rule-based local-baseline fallback (promotion decision DEC-6;
all rules are signature-independent and env-tunable for future rounds).

| # | condition (group_size gs, spatial s) | route | rationale (final-run evidence) |
|---|---|---|---|
| 1 | gs < 40,960 | CUDA one-pass (one CTA per group, two in-kernel passes) | launch-overhead-dominated; geomean 1.59, up to 1.86 |
| 2 | 40,960 <= gs < 65,536 | local baseline Triton | one-CTA-per-group starves (32 CTAs) just under the crossover, and the 3-launch chunked path loses ~10% to launch overhead at ~25 us (measured both ways); fallback reads 0.977-0.990 = routing tax on device-identical work |
| 3 | 65,536 <= gs < 700,000 | CUDA chunked 3-kernel (stats -> finalize -> apply, 8192-elem chunks, persistent grid) | geomean 1.80, up to 3.86 |
| 4 | gs >= 700,000 and s % 8192 != 0 (and s >= 16,384) | CUDA giant 2-kernel (register-lean exact-grid stats with fused last-block finalize + two-segment vectorized apply, zero-straddle per-shape tiles) | Triton straddles its 8192 chunk here and drops to per-element affine; candidate keeps full vector streams: 0.99-1.09, geomean 1.03 |
| 5 | gs >= 900,000 and s % 8192 == 0 | local baseline Triton | baseline runs straddle-free at ~81-85% of peak HBM; best bounded all-CUDA attempt trailed by 3-6% (apply ~85% DRAM, stats ~68%; NCU-named bound = stats block-reduce overhead per chunk); fallback reads 0.966-1.003 = routing tax |

Notes:

- Rows with 700,000 <= gs < 900,000 and s % 8192 == 0 stay on the CUDA giant
  path (rule 4 precedence; measured 1.06-1.10 there — e.g. `1x512x3x128x128`).
- Unsupported layouts (non-contiguous, misaligned base) normalize to fresh
  aligned tensors and run the same CUDA kernels (correctness-only path; no
  production row hits it).
- fp16/bf16/fp32 all dispatch identically (kernels instantiate all three).
- Thresholds: `GNS_SMALL_LARGE_THRESH` (65,536), `GNS_GIANT_THRESH`
  (700,000), `GNS_FALLBACK_SMALL_LO` (40,960), `GNS_FALLBACK_GIANT_LO`
  (900,000), giant tiles `GNS_GIANT_CHUNK` (16,384 target; per-shape
  zero-straddle divisor) / `GNS_GIANT_STATS_CHUNK` (0 = follow apply tile).

## Bounded giant-bucket attempt history (NCU-driven, profile/ncu_giant_v0)

| variant | change | 16-row giant/near-giant geomean |
|---|---|---|
| v0 (port) | prior-round chunked 3-kernel on giants | 0.78 (0.63-0.93) |
| v1 | dedicated giant kernels: __launch_bounds__(256,8) (52->32 regs, 44%->82% occupancy), exact grids, 16K tiles | 0.82 (regressed straddle-heavy shapes: scalar straddle loop) |
| v2 | two-segment vectorized straddle handling | 0.963 |
| v3 | fused last-block finalize (2 launches) + per-shape zero-straddle tiles | **0.990** (best) |
| v4 | 32K tiles (env sweep) | 0.968 (tail waves on mid shapes) |
| v5 | grid-stride loops + wave-multiple grids | 0.891 (loop state pushed regs over the 32-reg cliff) |
| v6 | wave-cost-minimizing tile picker | 0.939 (model underweights per-task overhead) |
| v7 | independent 32K stats tile | 0.977 (no robust win; reverted to v3 config) |

v3 shipped for rule-4 shapes; rule-5 shapes route to the baseline per DEC-6.
