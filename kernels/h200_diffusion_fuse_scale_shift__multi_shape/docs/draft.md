# Implementation Draft: candidate directions (evidence-ranked)

Status: living document for the optimization loop. Workload = the 15 rows of
`docs/captured_shapes_h200.jsonl`. Baseline numbers = `benchmark.csv`
tag `baseline-frozen-r0` (ion-h200-8, GPU 3, idle, valid=True).

## Measured baseline (frozen) and implied bandwidth

H200 HBM3e peak ~4.8 TB/s; realistic streaming ceiling ~4.3 TB/s (~90%).

| row | shape | device median | bytes/call | implied BW | bound (per evidence) |
|---|---|---|---|---|---|
| prod00 firered rowwise | 8424x3072 bf16 | 42.7 us | 155 MB | 3.64 TB/s | memory BW, mild headroom |
| prod01/03 hunyuan rowwise | 27030/27085x3072 | 125.5 us | 498 MB | 3.97 TB/s | memory BW, small headroom |
| prod02/05/06/10/11 tiny | 19..195x3072 | ~32.6 us (= host gap) | 0.35..3.6 MB | n/a | Triton HOST submit floor ~31 us; true kernel ~us |
| prod04 qwen | 4096x3072 | 36.0 us | 75.5 MB | 2.10 TB/s | half launch-tail / undersized grid |
| prod07 select01 | 8424x3072 | 47.9 us | 155 MB | 3.24 TB/s | memory BW, real headroom |
| prod08 residual | 8424x3072 | 81.0 us | 311 MB | 3.84 TB/s | memory BW, mild headroom |
| prod09 per-token | 8424x3072 (4 tensors) | 54.0 us | 207 MB | 3.84 TB/s | memory BW, mild headroom |
| prod12/13 wan 5120 | 37044/37800x5120 | 373/381 us | 1.14/1.16 GB | **3.05 TB/s** | memory BW, LARGE headroom |
| prod14 wan NC | 18144x3072, fp32 NC scale | 141.5 us | 557 MB | 3.94 TB/s | memory BW, modest headroom (correction r1: the original 446 MB figure omitted the bf16 per-token shift read) |

Note on tiny rows: `device_ev` brackets the stream timeline, so for
host-bound shapes it measures the submit gap, not kernel duration. The
`amort_wall` columns in benchmark.csv isolate pure host submit (~30 us for
Triton). True tiny-kernel device time will come from NCU when needed.

## Ranked directions

### D1 — Family A flat vectorized elementwise kernel (HIGH benefit, LOW risk) [first]
Flat 1-D grid-stride kernel over `B*L*C` in 16-byte packets (8x bf16/fp16 or
4x fp32), templated on a scale/shift layout class resolved by the wrapper:
ROWWISE (scale[b,c] / scale[c]), PER_TOKEN (row-strided pointers, covers the
NC fp32 scale whose inner dim stays stride-1/coalesced), FRAME4D
(frame = l / frame_seqlen), SCALAR. Mixed dtype: load fp32 scale as 4x fp32
packets, compute fp32, store x-dtype. `scale_constant` as runtime fp32 (0/1).
- Attacks: wan rows 3.05 -> ~4.1+ TB/s (~1.3x device), prod00/04/09 (1.1-1.3x),
  NC row 3.15 -> ~4.0 (~1.25x).
- Tiny rows: device-parity (both ~us); the candidate's win there is the
  tvm-ffi submit path vs Triton's ~31 us Python+JIT dispatch — measured
  honestly in sync_wall/amort_wall and decomposed; the shipping-path verdict
  comes from the in-tree drop-in (plan AC-9).
- Risk: low (no reduction, no smem). Sources: KernelWiki
  technique-vectorized-loads, pattern-memory-bound; qknorm_rope.cuh
  AlignedVector pattern.

### D2 — Family B one-CTA-per-row LN + select01 (+residual) (HIGH benefit, MED risk)
One CTA per row (B*L rows, C=3072 production), vectorized loads, fp32
two-pass mean/centered-variance block reduction (matches baseline numerics),
mean/rstd via smem broadcast, per-row index scalar selects modulation row
pointers, epilogue `x_hat*(1+scale)+shift` fp32, gate copy-through in native
dtype; optional weight/bias via template flags; residual variant computes
fp32 `residual_out = residual + residual_gate*x`, stores rounded copy, runs
LN on the UNROUNDED fp32 values (baseline semantics).
- Attacks: select01 3.24 -> ~4.0 TB/s (~1.2x device); residual 3.84 -> ~4.2 (~1.1x).
- Risk: medium (reduction correctness vs 1e-5 fp32 tolerance; multi-output).

### D3 — Tiny-shape launch configs (MED benefit, LOW risk; mostly host-side)
Single-wave minimal-grid config for L<=256 rows; the device side is ~us either
way. Benefit shows in sync_wall/amort (host submit ~31 us -> ~5-10 us local
ABI). Claim ONLY with device/host decomposition; production-relevance decided
by the in-tree drop-in, not the thin harness (lesson from the qknorm pilot).

### D4 — PDL (programmatic dependent launch) (UNKNOWN benefit; try late)
`enable_pdl` is one launcher flag in the tvm-ffi path. It HURT isolated-launch
latency in the qknorm pilot — try after D1/D2 land, keep only if this task's
benchmark improves.

### D5 — 4D per-frame perf specialization: REJECTED for perf (kept for correctness)
No production row uses the 4D layout; the generic FRAME4D template path covers
the regression grid. No perf iterations.

### Rejected outright (with reasons)
- tcgen05 / TMEM / MMA paths: Blackwell-only features and these kernels have
  no matmul; H200 is SM90 (plan Allowed Choices).
- Shared-memory staging for Family A: pure streaming op, zero data reuse.
- Persistent/cluster (DSMEM) schemes: no inter-CTA reuse; launch overhead is
  host-bound, not wave-bound.

## Loop context refresh (per-iteration ledger, plan AC-8)

- r0 (this entry): KernelWiki consulted — pr-sglang-14717 (upstream origin of
  this kernel family; motivation was fusing GPU bubbles),
  technique-vectorized-loads, pattern-memory-bound. ncu-report-skill SKILL.md
  read (mandatory profile pattern noted; B200 metric-name caveats apply on
  H200 = SM90, use classic names or enumerate). Baseline evidence above makes
  D1 unambiguous as the first edit; NCU deferred until the first candidate
  measurement is in (profile only when a result is not understood or would
  change the next edit).
- iter v1 (D1+D2 first cut): no new KernelWiki query (direction fixed by the
  r0 ranking); result — Family A wins everywhere (wan 1.42x at the ceiling),
  Family B device regression 0.771x/0.887x. Cause hypothesis from code
  reading (idle half-block + double reduction) -> v2 without profiling.
- iter v2: no new query; single-pass stats + 128-thread blocks recovered to
  0.895x/0.991x but the residual select01 gap was NOT explained by code
  reading -> mandatory NCU trigger. Profile run profile/select01_v2 (full
  set, baseline + candidate side-by-side).
- iter v3: edit driven by the NCU diagnosis (latency bubbles, identical DRAM
  active cycles). Register-prefetch variant REGRESSED (occupancy) — rejected
  with evidence; lesson recorded in .humanize/bitlesson.md.
- iter v4 (final): gate-only hoist per the occupancy lesson; 0.954x/0.982x
  device, +12-13% end-to-end; bounded-iteration budget for D2 (3 focused
  iterations) spent — closure per the stop rule. No further KernelWiki query
  needed: the NCU evidence fully localized the remaining 5% (reduction-barrier
  latency inherent to the LN family at this shape).
