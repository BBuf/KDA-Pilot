# Results: h200_diffusion_fuse_scale_shift__multi_shape (final candidate cuda-flat-v4)

Environment: ion-h200-8, container `sglang_bbuf`, GPU 3 (NVIDIA H200, idle
verified before AND after every run; all quoted rows `valid=True`), torch
2.11.0+cu130, triton 3.6.0 (baseline), CUDA candidate built via
`sglang.jit_kernel.utils.load_jit` with default jit_kernel flags (no
`--use_fast_math`), PDL off. Baseline = vendored Triton copy, proven
bit-identical to live SGLang (21/21 cases; docs/baseline_source.md).

## Correctness (gates the numbers below)

- Full grid: **2424/2424 pass** (15 production rows verbatim + canonical
  regression grid + negative parity), routes 2415 native / 9 fallback (the 9 =
  negative suite). CI subset 296/296. Fixed oracle tolerances AND the dynamic
  quantization-noise cross-check, NaN/Inf guards. Reports:
  `bench/reports/remote_r0/correctness_full_native_r4.json`.

## Headline (geometric mean of per-shape median-latency speedups, ALL 15 rows)

| metric | geomean | meaning |
|---|---|---|
| sync_wall | **1.2874x** | end-to-end callable latency (host submit + device + sync) |
| device_ev | **1.2274x** | CUDA-event device-side view |
| amort_wall | **1.2951x** | back-to-back submission (host overhead view) |

Per the plan decisions these are OUTCOME metrics (no pass/fail multiplier);
the per-bucket bound analysis below is the completion evidence. Per-shape
table: docs/dispatch.md; raw rows: benchmark.csv (tag `cuda-flat-v4`,
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
- Family B rows: device 0.954x/0.982x vs sync 1.122x/1.131x — host saving
  exceeds the small device deficit (see bound analysis).

## Roofline / bound analysis per bucket

H200 HBM3e peak 4.8 TB/s; realistic streaming ceiling ~4.3-4.4 TB/s (~90%).

| bucket | rows | bytes/call | baseline BW | candidate BW | active bound, conclusion |
|---|---|---|---|---|---|
| large video C=5120 (wan i2v/t2v) | prod12/13 | 1.14/1.16 GB | 3.05 TB/s | **4.33 TB/s** | memory bandwidth; candidate AT the achievable ceiling (~90% peak) — target-complete |
| large 3072 rowwise (hunyuan) | prod01/03 | 498 MB | 3.97 | 4.21 | memory bandwidth; within ~3% of ceiling — target-complete |
| 8424-token rows (firered/qwen-edit per-token) | prod00/09 | 155/207 MB | 3.68/3.87 | 3.83/4.02 | memory bandwidth + wave-quantization tail (25k blocks = ~15 waves; tail ~7% explains the gap to 4.2-4.3) — accepted |
| NC fp32-scale (wan-ti2v) | prod14 | 446 MB | 3.15 | 3.38 | memory bandwidth with reduced DRAM page locality (fp32 scale rows are 12 KB reads at 73.7 KB strides); adjusted ceiling est. ~3.6-3.8 -> candidate ~90% of it — accepted |
| mid (qwen 4096x3072) | prod04 | 75.5 MB | 1.96 | 2.89 | launch tail dominates at this size; candidate halves it (1.48x device) — accepted |
| tiny (19..195 tokens) | prod02/05/06/10/11 | 0.3..3.6 MB | n/a | n/a | HOST submit floor (Triton ~31 us vs ~21 us); device ~us both sides — bound is the host path, decided finally by the in-tree test |
| LN select01 | prod07 | 155 MB | 3.44 | 3.28 | memory bandwidth throttled by the row reduction barrier (NCU: DRAM active cycles IDENTICAL ~84.0k both kernels; the residual gap is un-overlapped latency). Candidate at 95% of Triton device after the gate-copy hoist (v2 0.895 -> v4 0.954); 3 bounded iterations spent (v3 register-prefetch variant REGRESSED to 0.685x and was rejected — occupancy loss > overlap gain). Known 5% device gap, +12% end-to-end — documented tradeoff, kept native (DEC-1 fallback reserved pending the in-tree verdict) |
| LN residual | prod08 | 311 MB | 3.85 | 3.79 | same family; 0.982x device (~parity), +13% end-to-end — accepted |

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
**cuda-flat-v4 (KEPT: gate-only hoist)**.

## Caveats / deferred

- The promotion arbiter is the post-loop in-SGLang in-tree drop-in
  (oracle test + smoke benchmark through the unchanged public ops); these
  local numbers are the device-fair evidence feeding it.
- PDL untested-by-default (off); prior pilot evidence says it hurts isolated
  launches. KDA_PDL=1 exists for a follow-up experiment.
