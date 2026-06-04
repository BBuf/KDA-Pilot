# NCU + roofline — candidate v3 (native_cuda_v3_streamcache): streaming-cache hints, near-bound on the big buckets, honest kernel-vs-kernel decomposition

Run: 2026-06-04, ion-h200-8 GPU 0 (idle 0%/0MiB before and after), `sglang_bbuf`,
SGLang `84e110831` (rotary files sha1 == pinned oracle `6965fe0ee`), torch 2.11.0+cu130,
triton 3.6.0. Candidate source `src/csrc/rotary_embedding.cuh` (v3: v2 + `__ldcs`/`__stcs`
streaming-cache accesses on all read-once/write-once global streams; built with
`-lineinfo` only added via `KDA_PROFILE=1`; no `--use_fast_math`). Collection commands in
`harness/ncu_cmd.txt`; raw `.ncu-rep` under `reports/` (kept out of the PR); parsed dump
in `analysis/metrics_raw.csv`, curated table in `analysis/metrics.csv`.

## What was measured

1. `--set full` + `--set source` on the candidate for the three decision buckets:
   the standard hunyuanvideo bucket and both `ltx2 S6144` buckets.
2. `gpu__time_duration.sum`-only passes for BOTH sides on all six buckets — the
   kernel-vs-kernel arbiter that CUDA events cannot provide for the small LTX-2
   buckets (Triton's kernel there is shorter than its own per-launch host cost, so
   even pipelined event timing keeps starvation gaps on the baseline side).

## Candidate v3 state (full sets, clock-controlled)

| case | kernel µs | DRAM% | SM% | L2 hit | occ | regs | achieved | active bound |
|---|---|---|---|---|---|---|---|---|
| std B1_T27030_H24_D128 | 89.41 | 74.4 | 38.4 | 48.1 | 81.5 | 29 | ~3.87 TB/s (~81% peak; ideal ~72µs) | **memory bandwidth** |
| ltx2 S6144 half64 | 35.94 | 76.2 | 42.0 | 34.0 | 81.0 | 32 | ~4.20 TB/s (~88% peak; ideal ~31µs) | **memory bandwidth** |
| ltx2 S6144 half32 | 18.72 | 63.2 | 39.3 | 34.5 | 68.1 | 32 | ~4.03 TB/s (~84% peak; ideal ~15.7µs) | memory bandwidth (occ-limited tail: half=32 leaves half the 256-thread block idle) |

L1 hit ~0% on the streamed kernels is by design (`.cs` evict-first on one-shot data).

## Kernel-vs-kernel truth (NCU duration, same method both sides)

| case | Triton steady µs | cand v3 µs | ratio | reading |
|---|---|---|---|---|
| std | 153.5 | 89.41 | **1.72×** | real kernel win |
| ltx2 S6144 h64 | 35.2 | 35.94 | 0.98× | **kernel parity** (slightly slower under NCU); the 1.17× wall win is host-path |
| ltx2 S6144 h32 | 19.5 | 18.72 | 1.04× | small real kernel win |
| ltx2 S1536 h64 | 10.65 | 11.49 | 0.93× | Triton kernel faster; wall win (1.24×) is host-path |
| ltx2 S1536 h32 | 6.62 | 7.81 | 0.85× | Triton kernel faster; wall win (1.28×) is host-path |
| ltx2 S126 h32 | 2.70 | 3.58 | 0.75× | Triton kernel faster; wall win (1.35×) is host-path |

Cross-method note: free-clock CUDA-event ratios (benchmark.csv) agree in direction for
the big buckets (std 1.46×, S6144h64 1.02×, S6144h32 1.13×) and are starvation-inflated
for the small buckets (~1.5× artifacts) — NCU rows above are the arbiter there.

## Six analysis dimensions (decision buckets)

- Compute: SM 38–42% — never the limiter.
- Memory: DRAM 74–76% on the two big buckets at 81–88% of analytical roofline; the
  remaining gap is address/sector overhead on the strided cos/sin path and L2 write-back
  behavior, not wasted gathers (at ~4.2 TB/s achieved there is no room for a "provably
  wasteful" gather — the DEC-3-related question is settled: no gather rewrite justified).
- Occupancy: 81% on std/h64 (healthy); 68% on h32 because half=32 activates only 128 of
  256 threads per block — a known shape property; the bucket still beats Triton
  kernel-only and is host-dominated at the wall level.
- Latency hiding: streaming `.cs` accesses + 8-wide vectors keep enough requests in
  flight; no scoreboard pathology in the source counters.
- Launch overhead: the dominant *wall* factor for every bucket except std/S6144h64 —
  Triton's host launch path costs ~19–34µs vs the tvm-ffi wrapper's ~7–20µs residual
  (benchmark.csv decomposition columns).
- Tail effect: `S126` runs 126 blocks on 132 SMs (undersubscribed by design of the
  one-block-per-(b,s) mapping) — the kernel-only deficit (2.70µs vs 3.58µs) lives here;
  it is invisible at the wall level (host-dominated bucket).

## v3 vs v2 (what the streaming hints bought)

- std: NCU 90.56 → 89.41µs; free-clock events 93.04 → 89.49µs (device-fair 1.40× → 1.46×).
- ltx2 S6144 h32: events 21.52 → 20.56µs (device-fair 1.086× → 1.128×); NCU 18.72 vs
  Triton 19.5 — the hints turned event-parity into a small real win.
- ltx2 S6144 h64: unchanged within noise (events 39.81 → 39.59µs; NCU 35.94 vs prior-round
  34.62 on a different day/GPU). Parity stands.
- Small buckets: unchanged within noise (host-dominated either way).
- Rejected on evidence: 384-thread launch shape for std (event device-fair 1.46× → 1.41×;
  occupancy 93.75% < 100% hurts this DRAM-bound kernel more than sweep uniformity helps).

## Diagnosis playbook match + verdict

Pattern: memory-bandwidth-bound elementwise kernels at 81–88% of roofline with
differentiated cache policy already applied → remaining levers (L2 policy windows,
256-bit accesses, persistent CTAs) are each worth ≲5% and risk regressions; the
prompt's near-bound stop rule applies. The small-bucket kernel-only deficit is a
launch-grid undersubscription issue (queued as future work: split heads across blocks
when `S < 2×SMs`), not a memory-efficiency issue — and those buckets are host-bound at
the wall, where the shipped path already wins 1.24–1.35×.

**Verdict: near-attainable-bound for the buckets that matter; stop optimizing.**
Shipping outcome (symmetric interleaved, free clocks): wall geomean **1.2977×**
(legacy-mode headline 1.2775×), device geomean 1.3379× (diagnostic only — small-bucket
device numbers are starvation-inflated; per-bucket kernel truth is the NCU table above).
