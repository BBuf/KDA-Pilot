# `norm_tanh_mul_add_kernel` (anchor candidate) Profiling Report

**Kernel:** `norm_tanh_mul_add_kernel<false>` (single) / `norm_tanh_mul_add_kernel<true>` (dual), bf16, rms
**Target GPU:** NVIDIA H200 (132 SM, CC 9.0, ~4.8 TB/s HBM3e peak)
**Nsight Compute:** 2025.3.1.0 (container `sglang_bbuf`, ion8-h200, GPU 0, idle)
**Compile flags:** SGLang `load_jit` defaults (`-std=c++20 -O3 --expt-relaxed-constexpr` + arch define) **+ `-lineinfo`** (profile build only, separate module name) — no `--use_fast_math`
**Profile date:** 2026-06-04
**Run directory:** `profile/ncu_anchor_r2/`

---

## 0. Profiling setup

- Harness: `harness/profile_harness.py` — Python driver that builds the task-local
  `src/norm_tanh_mul_add_candidate.cuh` through `sglang.jit_kernel.utils.load_jit`
  with `-lineinfo` (module `kda_h200_norm_tanh_mul_add_profile`, so the production
  build cache is untouched), warms up 5 calls, then issues 30 launches per entry.
- Workloads: the captured production shape `x=[1,4096,3840]` bf16 / rms / eps=1e-5
  (S=4128 is byte-equivalent ±0.8%); weight-only affine, `scale=[D]` view, full shift.
- Dispatch paths: `single` → grid 4096 × block 480; `dual` → same geometry, 2 outputs.
- Collection: `--set full` and `--set source --section SourceCounters`, each with
  `--launch-skip 10 --launch-count 3` (steady-state instances; 3 instances per report,
  metric spread < 1%).

```
CUDA_VISIBLE_DEVICES=0 ncu --set full --target-processes all \
  -k regex:norm_tanh_mul_add --launch-skip 10 --launch-count 3 \
  -o profile/ncu_anchor_r2/reports/full_<entry> -f \
  python profile/ncu_anchor_r2/harness/profile_harness.py <entry> 30
```

### Artifacts

```
profile/ncu_anchor_r2/
├── REPORT.md                ← this file
├── harness/profile_harness.py
├── reports/{full,source}_{single,dual}.ncu-rep
└── analysis/{parse_reports.py, metrics.csv, stalls.csv}
```

Metric-name caveat: `dram__throughput.avg.pct_of_peak_sustained_elapsed` and
`dram__bytes.sum` return None through `ncu_report` on this build; DRAM traffic is
taken from `dram__bytes_read.sum` + `dram__bytes_write.sum`, and the memory headline
from `gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed`.

---

## 1. Headline numbers (median of 3 steady-state instances)

| metric | single | dual |
|---|---|---|
| kernel duration (NCU) | **33.9–34.2 µs** | **50.0–50.1 µs** |
| grid × block | 4096 × 480 | 4096 × 480 |
| registers/thread | 32 | **40** |
| occupancy limit (regs) | 4 CTAs/SM | **3 CTAs/SM** |
| theoretical max warps | 93.75 % | **70.3 %** |
| achieved warps active | 81.5 % | 65.5 % |
| issue active | 77.9 % | 76.7–77.1 % |
| SM throughput | 70–72 % | 72.2–72.6 % |
| compute-memory throughput | **50.2 %** | **51.0 %** |
| DRAM read + write | 62.9 + 18.7 MB | 63.0 + 43.1 MB |
| achieved DRAM BW (actual bytes) | ~2.41 TB/s | ~2.12 TB/s |
| L2 (lts) hit rate | 34.7 % | 44.0 % |
| pipe ALU / XU / FMA / LSU | 52 / **38.6** / 36.4 / 13.7 % | 55.6 / 29.3 / 34.4 / 15.9 % |

Top warp stalls (warps per issue, `analysis/stalls.csv`):

| rank | single | dual |
|---|---|---|
| 1 | **long_scoreboard 5.0** | **not_selected 3.9** |
| 2 | not_selected 4.4 | **barrier 2.7** |
| 3 | barrier 2.5 | long_scoreboard 2.0 |
| 4 | — | math_pipe_throttle 1.3 |

---

## 2. Six-dimension walk

1. **SM occupancy & launch geometry** — 4096 CTAs over 132 SMs (7.8 / 10.3 waves).
   Single: thread-limited 4 CTAs/SM (480×4=1920/2048), 93.75 % cap, 81.5 % achieved.
   Dual: **register-limited** — 40 regs/thread → 3 CTAs/SM → 70.3 % cap, 65.5 %
   achieved. The dual cap is the clearest structural lever found.
2. **Thread-block balance / tail** — uniform row work, grid >> SMs, partial-wave tail
   ≤ 1/8 of a wave; per-instance duration spread < 1 %. Not a factor.
3. **Stall breakdown** — single: long_scoreboard dominates (5.0/issue — global-load
   latency on x/shift streams), barrier 2.5 from the 3-sync block reduction. Dual:
   not_selected 3.9 (issue-saturated) + barrier 2.7 (TWO reductions) lead;
   long_scoreboard halves (the second pass reuses registers, no new big loads).
4. **Tensor core utilization** — n/a (no MMA); scalar pipes: ALU 52–56 % and XU
   (tanh) 38.6 % on single are the busiest — real compute-pipe pressure, math
   visible as math_pipe_throttle 1.3 on dual.
5. **SM utilization timeline** — issue_active ~78 % both entries, steady across the
   launch (no warmup/tail shape in the 3 sampled instances).
6. **Memory pattern & cache** — fully coalesced 128-bit accesses (uint4); actual DRAM
   traffic is BELOW the fused-logical model (single 81.6 vs 94.4 MB; dual 106 vs
   125.8 MB) because L2 retains part of the write-back + row-invariant vectors
   (L2 hit 35–44 %). At 50 % memory throughput the kernel is NOT bandwidth-saturated.

## 3. Diagnosis (playbook match)

- **single = memory-LATENCY-bound with compute-pipe pressure.** Evidence:
  `gpu__compute_memory_throughput` ~50 % (well under saturation) while
  `long_scoreboard` dominates the stall mix at 5.0 warps/issue and ALU/XU pipes run
  at 52/38.6 % — warps park on x/shift loads, and when data lands the epilogue's
  ALU+XU instruction stream (tanhf per element per row + bf16↔fp32 conversions)
  slows the drain. This also explains the wave-1 result: fewer/larger CTAs cut the
  number of in-flight loads (less latency hiding) and pre-staged operands serialized
  ahead of the reduction — both made latency WORSE, not better.
- **dual = issue/barrier-bound under a register-occupancy cap.** Evidence:
  not_selected 3.9 + barrier 2.7 lead; 40 regs/thread caps occupancy at 70.3 %
  (3 CTAs/SM); memory at 51 %.

## 4. Ranked recommendations (next optimization wave)

1. **Dual: cap registers to restore 4 CTAs/SM** — e.g. `__launch_bounds__` with a
   min-blocks hint (target ≤32 regs/thread like the single instantiation). Expected:
   occupancy 70.3→93.75 % cap; attacks not_selected + barrier hiding. Risk: spills —
   verify with the interleaved A/B + a re-profile.
2. **Single: eliminate per-row tanh via the pre-launch tanh(scale) buffer (DEC-5,
   draft direction 3).** XU is 38.6 % busy purely on tanhf over a row-invariant [D]
   vector recomputed 4096 times (~15.7 M tanhf per call vs 3840 needed). A tiny
   precompute kernel + main-kernel load of pre-tanh'd scale removes ~all XU work
   and shortens the post-load drain. Must win the interleaved A/B including the
   extra launch + temp alloc; CUDA-graph-safe.
3. **Both: cheaper block reduction** — the 3-`__syncthreads` reduction contributes
   barrier 2.5–2.7; a 2-sync variant (no leading barrier needed for the first
   reduction; warp 0 broadcast via shuffle + single smem slot) trims barrier cost,
   most valuable for dual (two reductions).
4. NOT recommended (evidence): rows-per-CTA batching, fewer-threads/more-vectors,
   pre-reduction operand staging — all measured slower (wave-1 sweep,
   `solutions.jsonl: task9-wave1-sweep`).

## 5. Bound statement for the ledger

At the captured production shapes the anchor candidate is **not DRAM-bandwidth-bound**
(50–51 % memory throughput): single is memory-latency-bound (long_scoreboard 5.0)
with secondary ALU/XU pipe pressure; dual is issue/barrier-bound under a 40-register
occupancy cap. Headroom toward the ~25/33 µs bandwidth-ideal exists but is gated on
latency hiding and instruction-stream slimming, not on bytes.

---

# FINAL ADDENDUM — this profile is the FINAL-CANDIDATE evidence (AC-5)

**Status:** After this profile, all NCU-ranked wave-2 levers were implemented and
measured (`logs/wave2_sweep.log`, `logs/wave2_dtp_pipeline.log`): the dual
`__launch_bounds__` register cap was performance-neutral on device (0.999x), the
2-sync reduction was neutral-to-negative (0.996x), and the tanh-precompute buffer —
the only device-level winner (+2.2 % dual) — LOST at the shipping wrapper layer
(interleaved geomean 1.3122x vs the same-session anchor control 1.3314x; the
per-call fp32 buffer allocation + extra launch exceed the ~1 µs device gain).
Combined with the wave-1 tiling rejections, the search is exhausted within the
plan's bounded-iteration policy and **the anchor profiled in this report IS the
final promoted candidate** (`solutions.jsonl: final-candidate-decision`). Per the
round-3 review instruction, this addendum upgrades the report to final AC-5
evidence rather than re-profiling an identical kernel.

## Final roofline table (captured production buckets)

Conventions: *modeled logical* = fused-logical bytes (`benchmark.py:_bytes_moved`);
*actual* = NCU `dram__bytes_read + dram__bytes_write` (L2 retains part of the
working set; H200 L2 = 50 MB). TWO timing conventions appear side by side and are
NOT interchangeable: "NCU kernel time" = clock-controlled kernel-only duration from
the profiler; "device speedup (events)" = CUDA-event medians around the public
custom-op call from `benchmark.py` (includes launch overhead within the event
window) — the speedup column compares like-with-like (events vs events). The
S=4128 bucket scales bytes by +0.78 % with event-level times within 1 % of S=4096
(`benchmark.csv`), so its roofline position is identical.

| bucket | modeled logical bytes | actual DRAM bytes | NCU kernel time | BW (actual) | BW (logical) | % of 4.8 TB/s peak (actual) | locked baseline GPU | device speedup (events) | active bound |
|---|---|---|---|---|---|---|---|---|---|
| single S=4096 | 94.40 MB | 81.6 MB | 33.9 µs | 2.41 TB/s | 2.79 TB/s | 50 % | 65.98 µs | 1.57–1.62x | memory latency (long_scoreboard 5.0/issue) + ALU 52 %/XU 38.6 % |
| single S=4128 | 95.14 MB | ≈82 MB | ≈34 µs (events ±1 %) | ≈2.41 TB/s | ≈2.79 TB/s | 50 % | 65.98 µs | 1.58–1.61x | same |
| dual S=4096 | 125.86 MB | 106.1 MB | 50.1 µs | 2.12 TB/s | 2.51 TB/s | 44 % | 77.79 µs | 1.60–1.64x | issue/barrier under 40-reg occupancy cap (3 CTAs/SM, 70.3 % max warps) |
| dual S=4128 | 126.84 MB | ≈107 MB | ≈50 µs (events ±1 %) | ≈2.12 TB/s | ≈2.51 TB/s | 44 % | 77.66 µs | 1.61–1.63x | same |

Locked CuTe-DSL baseline reference points (same convention, from
`docs/baseline_locked.json`): single 65.98 µs GPU → 1.43 TB/s logical; dual
77.7 µs → 1.62 TB/s logical. The candidate moves both entries from ~30–40 % to
~52–58 % of peak logical bandwidth.

## Promotion reasoning (completion bar)

1. **Correctness**: 14/14 H200 suite (oracle + dynamic bounds + dispatch contract +
   fallback bitwise equality), 844-case exhaustive grid, baseline parity.
2. **Performance**: interleaved geomean over all 4 captured shapes 1.3253–1.3621x
   (3 independent sessions: ab_run2, run10, r3-anchor-control), sequential
   1.4463–1.4695x, device-only 1.38–1.66x — symmetric custom-op layers throughout.
3. **Near-bound evidence**: the remaining gap to the bandwidth ideal (~25/33 µs) is
   attributable to memory latency + issue structure, NOT unexploited bandwidth;
   13 variants across two waves (tiling, occupancy, XU-elimination, barrier
   reduction) all fail to beat the anchor at the shipping layer — the anchor sits
   at the practical operating point for this dataflow on H200 within the plan's
   bounded search. Further pursuit of the latency bound (e.g. async-copy double
   buffering across rows) would change the dataflow class and is out of the
   bounded-iteration budget; recorded as the no-go basis for further search,
   while the candidate itself is promoted on its measured win.
