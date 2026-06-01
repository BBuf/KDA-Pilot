# NCU REPORT — h200_diffusion_qknorm_rope candidate (round 0)

Run: `profile/round0_ncu/` · GPU: NVIDIA H200 (SM90, 132 SMs, HBM3e ~4.8 TB/s boost),
idle GPU 7 · container `sglang_omni_bbuf_kda` · candidate `src=00a0686e2e29c665`
(2-heads-per-warp float4 path, 256 thr/block, 32 regs/thread, theoretical occ 100%).
Profiles: `reports/full_{large_h24,large_h30,tiny}.ncu-rep` (`ncu --set full`,
isolated steady-state launch via `harness/prof_entry.py`, kernel built with `-lineinfo`).

## Speed-of-Light + occupancy (base clock)

| Bucket (T×H) | Dur µs | DRAM % | L2 % | L1/TEX % | SM(compute) % | Achieved occ % | Eligible warps/sched | Issue slots % | Top rule Est. |
|---|---|---|---|---|---|---|---|---|---|
| large_h24 8424×24 | 72.61 | 51.46 | 64.87 | 43.26 | 66.51 | 84.76 | 3.09 | 70.65 | 20.33% |
| large_h30 4128×30 | 46.18 | 44.81 | 61.52 | 43.35 | 64.27 | 81.20 | — | — | 19.49% |
| tiny 47×24 | 4.03 | 3.08 | 8.98 | 7.09 | 8.01 | 13.27 | 0.18 | 15.46 | 85.63% |

Warp state — large_h24: Warp cycles/issued instr 19.35, of which **~47% (9.1 cyc) is
long-scoreboard** (global-load dependency) stall; issued IPC 2.83. tiny: No-Eligible
85.63%, 0.18 eligible warps/sched, waves/SM 0.13, grid 141 blocks.

## Diagnosis (active bound per bucket)

- **large_h24 / large_h30 — memory-latency-bound (global-load), not HBM-saturated.**
  DRAM is only 45–51% of base-clock peak while L2 (62–65%), SM/LSU throughput (64–67%)
  and issue-slot busy (71%) are higher, and the dominant stall is long-scoreboard
  (~47% of warp cycles = waiting on q/k global loads). Occupancy is already healthy
  (81–85%, 3.09 eligible warps/sched). At boost clock the candidate sustains ~56–62%
  of HBM3e peak by the analytical roofline (`docs/perf_analysis.md`). This is the
  expected regime for an in-place read-modify-write whose dominant traffic is the
  q/k bytes (≈207 MB for 8424×24) — that traffic is irreducible for the op.
- **tiny — launch / SM-underfill bound.** 13% achieved occupancy, 0.18 eligible
  warps/scheduler, grid 141 blocks for 132 SMs (waves/SM 0.13); the isolated kernel is
  4.03 µs while the wall-clock benchmark is ~14 µs (launch overhead dominates). Not
  improvable by kernel-body tuning.

## Recommendations (ranked, evidence-backed)

1. **Keep the 2-heads-per-warp path as the universal kernel.** Dispatcher A/B
   (`bench_variants.py`) shows 2-head is **1.20–1.21× faster than 1-head** on all
   large shapes and ties on tiny — a single kernel is optimal across all 9 captured
   shapes (see `docs/dispatch.md`).
2. **(Future, bounded) Shared-memory cos/sin staging.** cos/sin (float32, 512 B/token)
   is reloaded ~`num_qk_heads/2`×/token (≈24× for H=24); staging it once per token-group
   in shared memory would cut redundant L2 reads + LSU *instruction* pressure (helps the
   ~66% SM-throughput / issue-slot dimension). Expected upside is bounded: cos/sin is
   ~2% of moved bytes and L2-resident, and the long-scoreboard stall is q/k-load
   dominated, so the latency dimension changes little. Codex (task10) estimates
   single-digit–low-teens %; my read is the lower end. Risk: smem sync / bank conflicts /
   indexing complexity. Worth one focused RLCR iteration only if a clear large-shape gain
   appears without hurting tiny.
3. Other levers are weak: vector width already 16 B, occupancy already 81–85%, large
   shapes not underfilled.

## Conclusion (completion bar)

- **large_h24 / large_h30: near the attainable bound** for this kernel class. The op is
  memory-latency-bound on the irreducible q/k traffic; the candidate is well-tuned on all
  first-order levers and wins 1.167–1.183× over the SGLang baseline. The one remaining
  lever (cos/sin staging) has bounded, q/k-latency-limited upside and is recorded as a
  ranked future direction rather than chased to hit a number (per the completion bar).
- **tiny: near-bound / no-go for kernel tuning** — launch/underfill-bound; the ~1.13–1.17×
  win comes from lower launch overhead (DEC-2: accept evidence-backed near-baseline).
- Headline: geomean **~1.11×** over the SGLang baseline across the 9 captured shapes
  (run-to-run ~1.09–1.13; 3 committed runs 1.0965/1.1258/1.0883; outcome metric, not a
  threshold). The all-9 geomean is noisy — the launch-bound tiny shapes dominate it — while the
  large shapes (the bandwidth-bound ones this report analyzes) are stable at ~1.14–1.16×.

> NCU collection provenance (exact command + GPU-7 before/after idleness) is recorded in
> `profile/round0_ncu/gpu_state.md`. The 2-head production kernel is byte-identical across the
> round-0 and round-1 source hashes, so these metrics remain valid for the current candidate.
