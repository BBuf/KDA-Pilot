# Results: h200_diffusion_fuse_scale_shift__multi_shape (final candidate cuda-flat-v5)

Environment: ion-h200-8, container `sglang_bbuf`, GPU 3 (NVIDIA H200, idle
verified before AND after every run; all quoted rows `valid=True`), torch
2.11.0+cu130, triton 3.6.0 (baseline), CUDA candidate built via
`sglang.jit_kernel.utils.load_jit` with default jit_kernel flags (no
`--use_fast_math`), PDL off. Baseline = vendored Triton copy, proven
bit-identical to live SGLang (21/21 cases; docs/baseline_source.md).

## Correctness (gates the numbers below)

- Full grid: **2428/2428 pass** (15 production rows verbatim + canonical
  regression grid incl. large-offset LayerNorm cases that reject
  uncentered-variance failures + negative parity incl. the
  fp32-x/bf16-modulation decline), routes 2418 native / 10 fallback (the 10 =
  negative suite). CI subset 300/300. Fixed oracle tolerances AND the dynamic
  quantization-noise cross-check, NaN/Inf guards. Reports:
  `bench/reports/remote_r0/correctness_full_native_r5.json`.

## Headline (geometric mean of per-shape median-latency speedups, ALL 15 rows)

| metric | geomean | meaning |
|---|---|---|
| sync_wall | **1.2878x** | end-to-end callable latency (host submit + device + sync) |
| device_ev | **1.2238x** | CUDA-event device-side view |
| amort_wall | **1.2911x** | back-to-back submission (host overhead view) |

Per the plan decisions these are OUTCOME metrics (no pass/fail multiplier);
the per-bucket bound analysis below is the completion evidence. Per-shape
table: docs/dispatch.md; raw rows: benchmark.csv (tag `cuda-flat-v5`,
evidence JSON under bench/reports/remote_r0/).

## Device-vs-host decomposition (plan-mandated, per claimed win)

- Large rows (>= 4096 tokens): the win is DEVICE-side — sync and device
  deltas match (e.g. prod13: sync -122.7 us vs device -112.8 us; prod12/13
  device 1.42x). Host contribution ~10 us/call on both sides.
- Tiny rows (19..195 tokens): the win is HOST-side — the true kernels are
  ~2-4 us on both sides; the Triton path pays a measured ~31 us/call Python +
  JIT-dispatch submit floor vs ~21 us through the dispatcher + tvm-ffi call
  (amort_wall isolates this). Claimed honestly as integration-path savings,
  NOT a device win; no production-required layer is dropped (the dispatcher
  sits under the same public callable, and the post-loop in-tree test keeps
  SGLang's own registration).
- Family B rows: device 0.933x/0.979x vs sync 1.114x/1.138x (v5,
  centered-variance build) — host saving exceeds the small device deficit
  (see bound analysis).

## Roofline / bound analysis per bucket

H200 HBM3e peak 4.8 TB/s; realistic streaming ceiling ~4.3-4.4 TB/s (~90%).

| bucket | rows | bytes/call | baseline BW | candidate BW | active bound, conclusion |
|---|---|---|---|---|---|
| large video C=5120 (wan i2v/t2v) | prod12/13 | 1.14/1.16 GB | 3.05 TB/s | **4.33 TB/s** | memory bandwidth; candidate AT the achievable ceiling (~90% peak) — target-complete |
| large 3072 rowwise (hunyuan) | prod01/03 | 498 MB | 3.97 | 4.21 | memory bandwidth; within ~3% of ceiling — target-complete |
| 8424-token rows (firered/qwen-edit per-token) | prod00/09 | 155/207 MB | 3.68/3.87 | 3.83/4.02 | memory bandwidth + wave-quantization tail (25k blocks = ~15 waves; tail ~7% explains the gap to 4.2-4.3) — accepted |
| NC fp32-scale (wan-ti2v) | prod14 | 557 MB (x 111.5 + fp32 NC scale 223 + bf16 shift 111.5 reads, y 111.5 write) | 3.94 | **4.22** | memory bandwidth; candidate within ~2% of the ~4.3 TB/s streaming ceiling — target-complete (the strided fp32 scale rows, 12 KB reads at 73.7 KB strides, cost nothing material) |
| mid (qwen 4096x3072) | prod04 | 75.5 MB | 1.96 | 2.89 | launch tail dominates at this size; candidate halves it (1.48x device) — accepted |
| tiny (19..195 tokens) | prod02/05/06/10/11 | 0.3..3.6 MB | n/a | n/a | HOST submit floor (Triton ~31 us vs ~21 us); device ~us both sides — bound is the host path, decided finally by the in-tree test |
| LN select01 | prod07 | 155 MB | 3.44 | 3.21 | memory bandwidth throttled by the row reduction barriers (NCU: DRAM active cycles IDENTICAL ~84.0k both kernels; the gap is un-overlapped latency). v5 carries the review-mandated CENTERED two-pass variance (the single-pass form catastrophically cancels on large-offset rows), costing one extra block reduction: device 0.933x vs Triton (v4's single-pass build measured 0.954x); end-to-end +11% and the shipping path absorbs the cost entirely (1.139x sync via the CustomOp callsite). Iteration history: v2 0.895 -> v3 0.685 (register prefetch, rejected on occupancy evidence) -> v4 gate-copy hoist -> v5 centered numerics. Known ~7% bare-device gap, documented tradeoff for baseline-faithful numerics; kept native on shipping-path evidence |
| LN residual | prod08 | 311 MB | 3.85 | 3.77 | same family; 0.979x device (~parity), +14% end-to-end — accepted |

NCU evidence: `profile/select01_v2/REPORT.md` (full side-by-side: duration
43.5 vs 48.9 us at v2, DRAM SOL 61.8% vs 54.9%, IPC 2.60 vs 2.07, identical
DRAM active cycles — diagnosis: latency-hiding defect, not traffic), raw
report under `$REMOTE_KDA_DIR/kernel/profile/select01_v2/reports/full.ncu-rep`.
Elementwise buckets were NOT NCU-profiled: the wan rows sit at the streaming
ceiling (cause and result both evident from the roofline arithmetic), and the
tail/locality explanations follow from block-count arithmetic — justified
skip per the profiling policy.

## Candidate lineage (solutions.jsonl)

baseline-triton (frozen, bit-identical) -> baseline-frozen-r0 (15-row
baseline) -> cuda-flat-v1 (first native: Family A wins everywhere, Family B
regression) -> cuda-flat-v2 (single-pass LN stats + runtime block size) ->
cuda-flat-v3 (REJECTED: modulation register prefetch, occupancy loss) ->
cuda-flat-v4 (gate-only hoist) -> **cuda-flat-v5 (KEPT: review-mandated
centered two-pass variance — baseline-faithful numerics on ill-conditioned
rows — plus the dtype-width dispatch gate)**.

## Promotion arbiter: in-tree SGLang drop-in (EXECUTED — see docs/sglang_jit_export.md)

The candidate was placed in-tree (task-owned sglang worktree at 84e1108312b5:
`.cuh` under `jit_kernel/csrc/diffusion/`, wrapper module via `load_jit` with
the relative csrc path, 18 inserted lines routing the UNCHANGED public Triton
functions through `try_native_*` with their original bodies as fallback; the
CustomOp/torch.compile layer untouched) and validated on idle GPU 3:

- Oracle: SGLang's `test_qwen_image_modulation.py` **288/288 passed** with
  native ON under the unchanged public ops.
- Routing 15/15 native; parity 15/15 within oracle tolerances; fp64/NC-x/CPU
  fallback checks reach the original Triton body with identical behavior.
- **FINAL shipping-path geomean (identical public wrapper/dispatch/
  registration on both sides, only the device path toggles; the two
  registered select01 rows measured THROUGH the CustomOp layer — their
  production callsite; run r3 with the centered-variance build):
  sync_wall 1.2643x, stream-span device_ev 1.3433x — all rows positive
  (min 1.1258x), CustomOp-layer rows at 1.139x/1.154x sync (they are
  0.933x/0.979x on the bare-kernel device view).** PERF_FALLBACK stays empty
  (DEC-1 unused). Oracle 288/288 with the centered build; CustomOp-layer
  parity 2/2. Earlier runs for lineage: r1 (direct-only) 1.2513x/1.3269x,
  r2 (CustomOp-inclusive, single-pass build) 1.2496x/1.3233x.

The local-loop geomeans above (1.2874x/1.2274x/1.2951x) remain the
device-fair RLCR evidence; the promotion claim is the shipping-path table in
docs/sglang_jit_export.md.

## Caveats

- PDL off by default (prior pilot evidence says it hurts isolated launches);
  `SGLANG_SCALE_SHIFT_KDA_PDL=1` / `KDA_PDL=1` exist for follow-up
  experiments.
- The in-tree harness carries per-call event records inside the timed region
  (~15 us, identical on both sides) — absolute numbers shift, ratios do not.
