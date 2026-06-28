# Round-2 results — b200_diffusion_norm_infer__multi_shape

Continuation on the promoted round-1 state (PR #23). Environment: `ion-b200`
(= `ion-b200`), container `sglang_bbuf`, GPU 1 (idle;
host otherwise loaded: other GPUs 53–97%), sglang `edb1b3f8f` (baseline files
drift-checked byte-identical to round-1 pin `0b65588c1`), CUDA 13.0,
torch 2.11.0+cu130, driver 580.126.20, fresh per-round `TVM_FFI_CACHE_DIR`.

## Outcome

| Shape | dtype | route (round 2, final v4 kernel) | wall | kernel-event |
|---|---|---|---|---|
| helios `[8640,5120]` | fp32 LN | CUDA float4 LN (unchanged) | 1.200× | 1.238× |
| hunyuanvideo `[1320,128]` | bf16 RMS | CUDA warp-per-row (unchanged) | 1.654× | 1.703× |
| zimage `[4096,128]` | bf16 RMS | CUDA warp-per-row (unchanged) | 1.661× | 1.697× |
| zimage `[16384,128]` | bf16 RMS | CUDA warp-per-row (unchanged) | 1.665× | 1.686× |
| hunyuanvideo `[648720,128]` | bf16 RMS | **CUDA tiled R=32 persistent (NEW)** | **1.071×** | **1.094×** |
| hunyuanvideo `[650040,128]` | bf16 RMS | **CUDA tiled R=32 persistent (NEW)** | **1.088×** | **1.097×** |
| **geomean (6 shapes, outcome metric)** | | | **1.358×** | **1.389×** |

vs installed SGLang baseline, interleaved per-iteration A/B, median of 100 iters
after 25 warmup, `benchmark.csv::cand-0013-dispatch-v4` — the final kernel state
after the segmented reduction gained half-warp shuffle masks (odd-tail safety;
performance-neutral on the even production shapes; the pre-fix run `cand-0011`
measured 1.360×/1.395×). Round-1 geomean was 1.29×/1.33× with the two huge
shapes at fallback parity. Production-mix steady-state smoke through the public
wrapper (S648720×2+S1320+S650040 per step, ×30): **1.0716×** per step. The
pinned-lane promote evidence is `cand-0010*` (two CI-gated runs) re-confirmed
post-fix by `cand-0013-tile-v4-maskfix` (CI95 lower bounds 1.086–1.134).

## Roofline / bound closure per bucket

- **fp32 LN `[8640,5120]`** (353.9 MB logical bytes): candidate 73.9 µs
  kernel-event ≈ 4.79 TB/s ≈ ~60% of peak under loaded-host conditions
  (round-1: ~67% on the same hardware under lighter load). Named bound:
  memory-bandwidth, ceiling set by host-load conditions. Gate to reopen stayed
  CLOSED — no new exploitable signal; kernel protected.
- **bf16 RMS small/mid `[1320/4096/16384,128]`**: launch/occupancy-bound
  (round-1 NCU: occ 15–76%, launch-dominated at these row counts); round-2
  ratios 1.64–1.70× unregressed. No new work (evidence unchanged).
- **bf16 RMS huge `[648720/650040,128]`** (332.8 MB logical): tiled winner
  72.3–72.9 µs kernel-event live ≈ 3.97 TB/s; NCU isolation at live clocks
  ~55.5 µs ≈ 67% DRAM with long-scoreboard 8% and occupancy at its 46.8%
  configuration ceiling. Named bound: mixed memory-bandwidth/issue, with the
  production-regime ceiling set by dirty-L2 write-back contention
  (`profile/tile_r32_r2/REPORT.md`). The Triton baseline is faster in
  cache-flushed isolation (46–49 µs; 78–82% DRAM) but collapses to 83–85 µs in
  the back-to-back steady state that diffusion denoise actually runs —
  the steady-state interleaved lane is the promotion arbiter.

## Decisions of record

1. Large-S reopen executed per the round-1 re-open condition; PROMOTE with
   conditions (all pre-dispatch conditions met; see `docs/dispatch.md`).
2. LN gate CLOSED (round-2 measured bound + no new signal + design review
   concurrence).
3. Small/mid RMS untouched, re-verified.
4. Pinned `baseline/` lane created (DEC-2: new-artifacts-only layout); parity
   6/6 bitwise vs installed sglang; custom-op host-layer delta quantified
   separately (LN ~1.00×, RMS small 1.14–1.16×, RMS huge 1.05–1.06×) so host
   effects can never masquerade as device wins.
5. kda_kernels overlay promotion remains out of scope this round (DEC-3).

## Evidence index

- `benchmark.csv`: `cand-0007-rebaseline` (round-2 truth), `baseline-parity-r2`
  (pinned-lane parity), `cand-0008/0009/0010(+rep2)` (bounded tile iterations
  with bootstrap CIs), `cand-0011-dispatch-tiled` + `cand-0011-mix-smoke`
  (pre-fix shipped routing), `cand-0013-tile-v4-maskfix` +
  `cand-0013-dispatch-v4` (final mask-fixed kernel), plus per-candidate
  `provenance_addendum` rows.
- `solutions.jsonl`: `cand-0007` … `cand-0014` (parent-linked into the round-1
  DAG; `cand-0012` superseded by `cand-0014-arbiter-rerun-v4`).
- `profile/tile_r32_r2/`: full + source NCU of the winner, baseline comparison,
  parsed `analysis/metrics.csv`, six-dimension `REPORT.md`.
- `docs/dispatch.md`: round-2 routing table + promote package + residual risks.
- `docs/baseline_source.md`: pinned-copy lineage.
- In-SGLang export refresh: `docs/sglang_jit_export.md` round-2 section —
  arbiter re-run with the v4 kernel (`cand-0014-arbiter-rerun-v4`): oracle
  288/288, shipping geomean 1.3722×/1.3946×; per-entry symmetry (RMS
  custom-op-body, LN public-function — the wrapped LN entry has no custom-op
  registration on its hot path).
