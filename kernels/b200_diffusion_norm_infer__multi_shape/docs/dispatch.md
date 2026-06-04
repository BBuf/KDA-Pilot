# Dispatch table — b200_diffusion_norm_infer__multi_shape

Final per-bucket routing for the six production shapes. The dispatcher
(`src/register.py`) routes a shape to the native CUDA kernel iff it matches the
explicit allowlist + input validation; everything else falls back to the SGLang
Triton baseline.

**ROUND-2 UPDATE (2026-06-04, ion-b200 GPU 1, sglang `edb1b3f8f`, fresh tvm-ffi
JIT, host loaded on other GPUs / selected GPU idle):** the large-S RMS bucket is
REOPENED through its recorded re-open condition and PROMOTED to
`RmsNormTiledKernel<128,32,bf16>` with `scheduling=1` (persistent whole-wave
grid) — see "Round-2 large-S reopen" below. LN and small/mid RMS routing
unchanged and re-verified unregressed. The LN optimization gate stayed CLOSED
this round: round-2 achieved BW on `[8640,5120]` was ~59% of peak under host
load (round-1: ~67%), no new NCU signal, and the LN hot path carries no
custom-op delta (parity lane 1.00–1.01×) — protect the promoted kernel, no
edits. Round-2 geomean (outcome): **1.358× wall / 1.389× kernel-event**
(`cand-0013-dispatch-v4`, the final mask-fixed kernel; 297/297 correctness with
`KDA_REQUIRE_CUDA=1` incl. odd-tail rows; the pre-fix run `cand-0011` measured
1.360×/1.395× — the tail-safety fix is performance-neutral on the even
production shapes).
Round-1 numbers are kept below for lineage; absolute µs across rounds are NOT
comparable (different host-load conditions; interleaved ratios remain valid).

Round-1 record: measured on idle NVIDIA B200 (interleaved A/B, cand-0004-dispatch;
sglang 0b65588c, CUDA 13.0.88, torch 2.11.0+cu130). Speedups are baseline/candidate
median (wall-clock primary; kernel-event in parens). Geomean (outcome): 1.29× wall /
1.33× kernel. Evidence: `benchmark.csv`, `solutions.jsonl::cand-0004-dispatch`,
`profile/ac_e_r5/REPORT.md`, `profile/rms_largeS_r4/REPORT.md`.

## Support predicates (`src/register.py`)
- **LN → CUDA** iff: `fp32`, 2-D, contiguous, `is_rms_norm=False`, `(M,N) ∈ _SUPPORTED_LN`, and weight+bias non-None, contiguous, `shape==(N,)`, same device+dtype; `out` is None or `shape==x.shape` + same device/dtype + contiguous.
- **RMS → CUDA** iff: `bf16`, exactly 2-D, contiguous, `(S,D) ∈ _SUPPORTED_RMS` (i.e. `D==128` and `S ∈ {1320,4096,16384, 648720, 650040}` for production + regression-small), and `w` non-None, contiguous, `shape==(D,)`, same device+dtype. Within the CUDA route: `S ≥ 100000` → tiled kernel (R=32, persistent); smaller → one-warp-per-row kernel.
- **Everything else → SGLang baseline fallback** (fp16/bf16 LN, `is_rms_norm=True`, N/S/D outside the table, non-contiguous, wrong device/dtype/shape, higher-rank, invalid `out`). Verified by `tests/test_correctness.py::test_fallback_routing` (15 cases, re-passed after the round-2 routing change).

## Per-shape decision

| Production shape | dtype | owner (kernel) | baseline µs | candidate µs | speedup (wall / kernel) | active bound | decision |
|---|---|---|---|---|---|---|---|
| helios `[8640,5120]` | fp32 LN | **CUDA** `LayerNormInferKernel<fp32_t>` (float4, parallel reduce) | 82.96 | 71.10 | **1.17× / 1.19×** | memory-bandwidth (~66% peak; `ac_e_r5/reports/ln.ncu-rep`) | **PROMOTE** |
| hunyuanvideo `[1320,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | 33.36 | 20.37 | **1.64× / 1.70×** | launch/occupancy (occ 15%; `ac_e_r5/reports/rms1320.ncu-rep`) | **PROMOTE** |
| zimage `[4096,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | 32.87 | 20.16 | **1.63× / 1.71×** | launch/occupancy (occ 40%; `ac_e_r5/reports/rms4096.ncu-rep`) | **PROMOTE** |
| zimage `[16384,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | 33.45 | 21.88 | **1.53× / 1.66×** | launch/occupancy (partial wave, occ 76%; `ac_e_r5/reports/rms16384.ncu-rep`) | **PROMOTE** |
| hunyuanvideo `[648720,128]` | bf16 RMS | **SGLang baseline (fallback)** | 77.00 | 78.24 (CUDA, not used) | ~1.0× (fallback) | memory-latency + occupancy | **NO-GO → fallback** |
| hunyuanvideo `[650040,128]` | bf16 RMS | **SGLang baseline (fallback)** | 76.72 | 78.47 (CUDA, not used) | ~1.0× (fallback) | memory-latency + occupancy | **NO-GO → fallback** |

## Large-RMS round-1 no-go package (superseded in round 2; kept for lineage)
- **Correctness:** the CUDA RMS kernel is correct at large S (validated rounds 0-3, and kUnroll variants in round 4).
- **Attempts:** one-warp-per-row (kUnroll=1) and the MLP grid-stride variant (kUnroll=2/4/8). Best (kUnroll=4) ~77 µs vs baseline ~71 µs (interleaved, idle B200).
- **Benchmark:** ~0.84-0.92× across runs; not parity-or-better at any tried config.
- **NCU/roofline:** `profile/rms_largeS_r4/REPORT.md` + `profile/ac_e_r5/` — not bandwidth-saturated (~4.3-4.7 TB/s, ~55-59% peak); kUnroll=1 is memory-latency bound (long-scoreboard 56%, occ 77%), kUnroll=4 trades occupancy (41%) for MLP. Neither warp-per-row variant matches the baseline's 16-row tile.
- **Named active bound:** memory-load latency vs occupancy trade-off intrinsic to the warp-per-row family for `D=128` huge-S streaming RMS.
- **Round-1 decision:** fall back to the SGLang Triton baseline (faster) → parity, no production regression. Re-open only if a tile-based CUDA RMS (multi-row-per-block, shared load pipeline) is implemented and beats the baseline.

## Round-2 large-S reopen → PROMOTE (tiled multi-row kernel)

The recorded re-open condition was met. Bounded exploration (3 iterations,
ordered by the round-2 design review):

| iteration | config | wall vs pinned baseline | kernel-event vs pinned | verdict |
|---|---|---|---|---|
| 1 (`cand-0008`) | R=16, one CTA/tile, register-direct | 0.747×/0.762× | 0.763×/0.771× | rejected (launch/drain dominates; no MLP) |
| 2 (`cand-0009`) | R=16, persistent grid | 0.960×/0.967× | 0.989×/0.988× | rejected (single load in flight/thread) |
| 3 (`cand-0010`) | **R=32, persistent** (two row-pairs/warp, both pair loads in flight) | **1.105×/1.110×** (rep2 1.100×/1.099×) | **1.151×/1.161×** (rep2 1.141×/1.142×) | **PROMOTE** |

- **Promotion lane (the arbiter):** live steady-state interleaved A/B vs the
  PINNED Triton baseline (`baseline/`, bitwise-parity-validated, custom-op layer
  stripped symmetrically), two independent runs, paired-bootstrap CI95 lower
  bounds 1.094–1.152 on every (shape × metric-kind) — gate was lower bound > 1.02.
  Harness preserved at `bench/large_s_tile_ab.py`.
- **NCU cross-check + the context-dependence finding**
  (`profile/tile_r32_r2/REPORT.md`): the intended kernel was profiled (grid
  592×256, 56 regs, occupancy 46.8% ≈ its config ceiling, long-scoreboard 8% —
  the latency problem that killed the warp-per-row family is solved). NOTE the
  ranking inverts by context: in cache-flushed/serialized NCU isolation the
  Triton baseline is faster (46–49 µs live-clocks vs tiled 55–56 µs; DRAM 78–82%
  vs 67%); in back-to-back steady state each launch inherits the predecessor's
  ~126 MB dirty-L2 write-back debt and the bandwidth-hungry baseline collapses
  to ~83–85 µs while the issue-limited persistent tile holds ~72 µs. Diffusion
  denoise pipelines run this op hundreds of times amid attention/GEMM write
  traffic — the dirty-L2 steady state IS the production regime, so the
  steady-state lane is the promotion arbiter (round-2 verdict:
  PROMOTE_WITH_CONDITIONS, all pre-dispatch conditions met; in-SGLang symmetric
  drop-in arbiter at the export step).
- **Production regression gate:** 272/272 correctness (full grid + tile suite +
  15 fallback cases, `KDA_REQUIRE_CUDA=1`); six-shape production benchmark
  `cand-0011-dispatch-tiled` — no promoted bucket regressed; production-mix
  steady-state smoke through the public wrapper (S648720×2 + S1320 + S650040
  per step ×30): **1.0716×** per step. A true HunyuanVideo end-to-end smoke was
  substituted by this mix smoke because the model weights are not cached on the
  box (the capture protocol deletes them); revisit only if reviewers require it.
- **Residual risks (recorded):** context sensitivity (a workload with clean-L2
  isolation semantics would favor the Triton baseline); win valid only for the
  two large-S buckets (no broader allowlist claims); future Triton/driver/clock
  changes can shift the isolation/steady-state gap; custom-op symmetry must be
  re-verified at export.

## Per-shape decision (round 2)

| Production shape | dtype | owner (kernel) | speedup vs installed baseline (wall / kernel) | active bound | decision |
|---|---|---|---|---|---|
| helios `[8640,5120]` | fp32 LN | **CUDA** `LayerNormInferKernel<fp32_t>` | **1.200× / 1.238×** | memory-BW (~59% peak under load; LN gate CLOSED — no new headroom signal) | **KEEP (round-1 promote)** |
| hunyuanvideo `[1320,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | **1.654× / 1.703×** | launch/occupancy | **KEEP** |
| zimage `[4096,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | **1.661× / 1.697×** | launch/occupancy | **KEEP** |
| zimage `[16384,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | **1.665× / 1.686×** | launch/occupancy | **KEEP** |
| hunyuanvideo `[648720,128]` | bf16 RMS | **CUDA** `RmsNormTiledKernel<128,32,bf16_t>` sched=1, half-warp masks (v4) | **1.071× / 1.094×** (was ~0.98× fallback) | mixed BW/issue; robust to dirty-L2 steady state | **PROMOTE (round 2)** |
| hunyuanvideo `[650040,128]` | bf16 RMS | **CUDA** `RmsNormTiledKernel<128,32,bf16_t>` sched=1, half-warp masks (v4) | **1.088× / 1.097×** (was ~0.98× fallback) | mixed BW/issue; robust to dirty-L2 steady state | **PROMOTE (round 2)** |

## Summary
6/6 production shapes better-than-baseline: **6 CUDA routes** (round-1's 4 + the
round-2 tiled large-S pair, v4 tail-safe). Round-2 final geomean **1.358× wall /
1.389× kernel-event** (`cand-0013-dispatch-v4`) reported as an outcome, not a
pass/fail threshold (per the prompt). Per-shape numbers above are the v4
final-state run; the pinned-lane promote evidence (CI-gated, two runs) is under
`cand-0010*` and re-confirmed post-fix under `cand-0013-tile-v4-maskfix`.
