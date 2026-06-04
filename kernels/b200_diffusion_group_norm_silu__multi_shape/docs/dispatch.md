# Candidate Dispatch — `b200_diffusion_group_norm_silu__multi_shape`

The candidate exposes ONE ABI (`group_norm_silu(x, weight, bias, num_groups,
eps, out)`) and selects internally. Selection happens at two levels:

1. `solution/binding.py::select_path` (Python): `cuda_kernel` vs
   `baseline_fallback` (the copied upstream Triton implementation — the
   baseline-equivalent path sanctioned by the no-regression ruling DEC-3).
2. `solution/kernel.cu::select_regime_impl` (C++): which CUDA regime runs a
   `cuda_kernel` row. Crossovers are env-tunable (`GNS_SMALL_MAX`,
   `GNS_CHUNK`, `GNS_CONT_FALLBACK_MIN`) and were re-derived empirically on
   B200 (not inherited from the Triton 2^18 or H200 thresholds).

## Buckets (production workload mix: fp16, G=32, B=1)

| Bucket condition | Path / regime | Evidence (iter3 subset + run-4 full A/B, GPU 1, ion-b200) | Why |
|---|---|---|---|
| contiguous, group_size <= 65536 (`GNS_SMALL_MAX`) | `cont_small`: one CTA/group, 16B-vectorized two-pass | C small bucket geomean 2.53x (n=24, min 1.41, max 4.59) | small groups are launch/latency-bound; vectorized one-pass with 32 CTAs suffices and avoids split-path scratch traffic |
| contiguous, 65536 < group_size <= 2,000,000 (`GNS_CONT_FALLBACK_MIN`) | `cont_split`: split-group stats (last-CTA finalize, generation counters) + division-free apply | C mid bucket geomean 2.44x (n=52, min 1.32, max 3.93); largest passing row (128,17,96,256)=1.67M at 1.14x | the upstream one-pass path launches only B*G=32 CTAs at B=1 — severe underfill on 148 SMs; splitting groups across CTAs fills the machine |
| contiguous, group_size > 2,000,000 | `baseline_fallback` (copied upstream Triton chunked pipeline) | failing rows before routing: 2.36M 0.948 / 2.62M 0.931 / 3.34M 0.941-0.945 / 4.45M 0.941-0.952 / 8.91M 0.957-0.961 | see "Giant contiguous bucket" below |
| channels-last(-3d), cpg >= 4, C <= 1024, G <= 32 | `nchw_last`: native position-major reads, all-group tile stats, smem-staged transposed writes | NC small 1.48x..2.37x; NC mid/large 1.06x..1.83x after fixes (worst NC row 1.06x) | skips the baseline's full `x.contiguous()` materialization (the copy alone was 121.6us of the 186us baseline on the probe row) |
| anything else (fp32 rows, cpg < 4, unaligned, 2-D token case) | `generic` CUDA regime (strided two-pass; fp32 accumulates in double) | grid + stress rows green at contract tolerances | correctness safety net; fp32 rows are correctness-only, never production |

## Giant Contiguous Bucket — bounded attempts before routing (all NCU-backed)

Row class: contiguous fp16, group_size >= ~2.4M (e.g., `(1,256,17,256,256)`,
0.57 GB tensor). Baseline chunked pipeline measured ~5 TB/s-class effective
on these rows — already near memory-bound-optimal.

Attempts (profile runs in `profile/r1_losers/`, summarized in
`analysis/metrics.csv`):

1. Chunk-constant affine in `gns_split_apply_kernel` — NCU showed the apply
   instruction-throughput-bound (SM 84% busy, DRAM 14%) due to a per-vector
   int64 division; hoisting affine to a chunk constant cut apply 527→471 us
   (NCU clock-locked scale).
2. Baseline-class exp (`__expf`, the same SFU exp2 class the upstream
   tl.sigmoid lowers to; per-call intrinsic, no fast-math flags) in the
   16-bit regimes — subset gate band moved 0.87-0.91 → 0.91-0.97.
3. Persistent grow-only scratch + generation counters (no per-call
   mallocAsync/memset/freeAsync) — band moved to 0.93-0.96. (This change also
   eliminated bimodal multi-hundred-microsecond swings caused by the default
   mempool's zero release threshold; twin-row agreement restored.)
4. `GNS_CHUNK` sweep on the losing rows: 8192→0.845, 16384→0.88-0.96 (best),
   32768→0.863, 65536→0.809, 131072→0.754. 16384 is locally optimal;
   direction excludes chunk sizing as the fix.

Residual gap after all attempts: 4-7% on 9 rows. Active bound: the baseline
chunked pipeline already saturates the achievable DRAM bandwidth for this
2-read+1-write pattern, and the split path's stats-side win (~60us NCU) does
not cover its apply-side instruction overhead plus the second full pass
timing at these sizes. Per ruling DEC-3 (no production row < 0.97x; route
losing buckets), contiguous rows above `GNS_CONT_FALLBACK_MIN = 2,000,000`
elements take the baseline-equivalent path; their measured ratio is ~1.00 by
construction (A/A gate: 1.0005 geomean) and they are counted and reported in
the per-row results table like every other row.

Deferred (would need new evidence to justify): cluster/DSMEM cooperative
single-kernel stats+apply, PDL — NCU shows the bucket is bandwidth-bound, not
launch/sync-bound, so neither addresses the active bound. A one-read-pass
algorithm is information-theoretically excluded here: the affine+silu output
cannot be produced before the group statistics are known, and a giant group
(4.7+ MB per group) cannot be cached on-chip, so both sides are forced into
the same 2-read+1-write pattern.

## Measured Residual on Routed Giant Rows (order-debt artifact)

Routed rows execute the IDENTICAL implementation on both benchmark sides (the
candidate resolves to the copied baseline callable), so a real regression is
impossible by construction; the residual sub-1.0 readings on this row class
are a measurement artifact, characterized as follows (2026-06-05, GPU 1):

- Direct steady-state interleaved probe on `(1,512,9,128,128)` fp16
  (300 back-to-back calls per side, repeated 3x): baseline 95.6 us vs
  candidate 96.0 us — delta 0.21-0.37 us (~0.4%), i.e. true ratio ~0.997.
  The candidate's Python dispatch (~3 us `select_path`) fully overlaps with
  GPU execution in the pipelined regime.
- In-harness, rows with ~75-150 MB outputs (vs ~126 MB L2) show ~3-8% debt on
  whichever side runs SECOND within a trial (dirty-L2 writeback from the
  first side's output). The template randomizes the A/B order per trial with
  a per-workload-id seed; the MEDIAN therefore jumps between the two order
  classes with the majority draw. Evidence: twin rows with identical tensors
  and identical code read 0.9594 vs 0.9810 in the same 21-trial run
  (`bench/results_marginal21.jsonl`); the same id flips between ~0.93 and
  ~0.96 across runs while its twin reads ~0.98-1.00.
- Per the no-regression ruling (DEC-3 / AC-5.2: residual regressions must be
  explained with evidence), these readings are reported as-is in the per-row
  table and explained by this section; the controlled interleaved probe and
  the identical-code-path argument bound the true per-row ratio at ~0.997.
