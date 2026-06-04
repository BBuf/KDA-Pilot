# Continuation Draft — h200_diffusion_rotary_embedding__multi_shape (round 2 of the KDA loop)

Status: continuation from promoted candidate `native_cuda_v2_vectorized` (ledger `s4`,
kernel-pilot `fe769ccb6`/`be7bb20f1` lineage, promoted to `kda_kernels` in PR #20).
This draft is written BEFORE any kernel source edit in this round, per the workspace rule.

## Context refresh (what changed since s4)

- The task prompt's benchmark rules were tightened after s4 landed: benchmark the
  SHIPPING integration symmetrically (identical wrapper/dispatch on both sides, only the
  device kernel differs), preserve every production requirement of the public entry
  points, and decompose every speedup into DEVICE vs HOST.
- Verified from `profile/ncu_v2_20260602_065439/analysis/metrics.csv`: the worst bucket
  `ltx2__B1_S6144_H32_half64__bf16` is device-parity — kernel-vs-kernel (CUDA events)
  1.004x (40.30µs vs 40.16µs) while wall-clock shows 1.123x. The wall win on that bucket
  is host-path (Triton launch machinery vs tvm-ffi), not the device kernel.
- Verified in the current SGLang checkout (HEAD `0689ba84b8`, rotary files byte-identical
  to pin `6965fe0ee`): `apply_rotary_embedding` and `apply_ltx2_split_rotary_emb` are
  plain Python functions — NO `@register_custom_op` / torch.library registration. The
  custom-op preservation clause is therefore N/A for this task; the host-path win drops
  nothing production-required. It must still be REPORTED as host, not kernel.
- The prior `benchmark.py` times baseline and candidate sequentially (all baseline reps,
  then all candidate reps). The tightened rules require a same-process interleaved A/B
  cross-check; the harness is upgraded this round (legacy mode preserved for
  comparability with the 1.2955x headline).

## K/R/W recovery

- K (kernel semantics + callsite contract): standard adjacent-pair RoPE
  `apply_rotary_embedding(x, cos, sin, interleaved=False) -> new Tensor`, x
  `(B,T,H,D)`/`(T,H,D)` bf16, cos/sin `(T, D/2)` fp32; LTX-2 split-half
  `apply_ltx2_split_rotary_emb(x, cos, sin) -> new Tensor`, x `(B,S,H*2*half)` bf16,
  cos/sin `(B,H,S,half)` bf16 possibly non-contiguous (last dim stride 1). Functional:
  never mutate inputs. Fallback chain CUDA -> captured SGLang baseline -> fp32 reference,
  non-recursive (baselines captured at import).
- R (oracle + tolerance): pinned SGLang diffusion Triton baselines (rotary.py sha1
  `81fb5ffeaf387903c45da1b62accce5b1e275039`, ltx2_rotary.py
  `3408d9084b4cc9e92cbd3dbd584fa7ec5f8d5d4b`, == pin `6965fe0ee`), cross-checked vs the
  fp32 references in `src/reference.py` that reproduce baseline rounding (standard fp32
  FMA + round-on-store; LTX-2 `(x*cos)->bf16` intermediate). Pass = `atol=rtol=1e-2` AND
  dynamic bf16-noise bound (err <= 3x ref noise, RMS and max), NaN/Inf-free, CUDA route
  asserted on all 6 production cases. On remote drift from the pin: re-pin, record
  old/new hashes, re-measure baseline first.
- W (workload + methodology): exactly the 6 deduplicated captured shapes from
  `docs/captured_shapes_h200.jsonl` (1 hunyuanvideo standard + 5 LTX-2). Median latency
  with warmup 25 / iters 100, stats median/mean/std/min/p10/p90, allocation included on
  both paths, register module cached. Headline = geomean of per-shape median speedups —
  an OUTCOME metric, not pass/fail.

## Current candidate design (s4, unchanged so far)

- `standard_rope_kernel`: one 256-thread block per token; cos/sin row staged to shared
  memory once per token and reused across all 24 heads; 128-bit bf16 vectors
  (`AlignedVector<bf16x2,4>`); shift/mask indexing (D power of 2); fp32 FMA,
  round-on-store. Grid 27030, smem 512B, nvec=384 per block (1.5 vec iterations/thread —
  threads 128..255 idle in the second sweep).
- `ltx2_split_rope_kernel`: one 256-thread block per (b,s); per thread one 8-wide vec
  group: loads xf/xs (first/second half) + cos/sin via stride arithmetic (last dim
  contiguous, so 8-thread groups per head are coalesced 16B accesses); preserves the
  baseline's `(x*cos)->bf16` intermediate rounding. half=64: nvec=256 (full block);
  half=32: nvec=128 (half the block idle).

## Prior NCU evidence anchors (ncu_v2_20260602_065439)

| case | kernel µs (NCU) | DRAM% | SM% | L2 hit | occ | regs | ideal µs | % roofline |
|---|---|---|---|---|---|---|---|---|
| std B1_T27030_H24_D128 | 90.56 | 74.95 | 37.52 | 48.07 | 81.35 | 28 | ~72 | ~80 |
| ltx2 S6144 half64 | 34.62 | 79.49 | 42.29 | 34.08 | 80.99 | 32 | ~31 | ~90 |

Kernel-vs-kernel (CUDA events, all 6): std 1.374x; ltx2 1.459/1.399/1.314/1.286x; worst
ltx2 S6144 half64 1.004x. Wall-clock: 1.492/1.423/1.306/1.263/1.202/1.123x, geomean
1.2955x.

## KernelWiki / ncu-report-skill context for this iteration

- `technique-vectorized-loads` (wiki/techniques/vectorized-loads.md): for memory-bound
  kernels, differentiated L1 cache policies — `L1::no_allocate` (or `__ldcs`) for
  streamed-once data and `L1::evict_last` for reused data — gave 1.44x in a GPU Mode
  NVFP4 GEMV case (39µs -> 27µs); 256-bit `ld.global.v4.u64` is available when more
  bytes/instruction help; `-maxrregcount` occupancy budgeting (our regs 28/32 are already
  low — not a lever here). This grounds direction D1.
- No rope-specific kernel pages exist in KernelWiki (`--tag rope --type kernel` returns
  nothing); the memory-bound pattern + vectorized-loads technique pages are the relevant
  prior art. FlashInfer rope PRs were already mined in the prior round (s3 lineage).
- ncu-report-skill: one `profile/<run>/` dir per run with harness/reports/analysis +
  REPORT.md; `--set full` + `--set source --section SourceCounters`; sm90 metric-name
  caveats analogous to the documented sm100 ones — enumerate `action.metric_names()`
  when a metric returns None.

## Ranked optimization directions (bounded: <=2 focused iterations each)

- D1 — standard bucket cache-policy + launch-shape (expected benefit: close part of the
  90.56µs vs ~72µs gap, i.e. up to ~1.1x device on this bucket; risk: low; bottleneck:
  DRAM 75% / L2-hit 48% with pure-streaming x/out, plus intra-block tail from
  nvec=384 vs 256 threads):
  1. Streaming hints on x/out (`__ldcs`/`__stcs` or `L1::no_allocate`-class policies via
     the sgl_kernel vec helpers if expressible; otherwise inline PTX kept minimal) while
     cos/sin stay default/`__ldg`.
  2. Launch-shape variant: 128 threads/block (3 uniform vec sweeps) or restructured
     mapping so all threads stay active (remove the half-active second sweep);
     `__launch_bounds__` pin; optional 2-vec-per-thread (256-bit-equivalent) variant.
- D2 — ltx2 S6144 half64 gather diagnosis (expected benefit: <=1.12x theoretical, likely
  ~1.0-1.05x; risk: medium that it is already at bound; bottleneck: 79.5% DRAM, L2-hit
  34%, non-contiguous 4D cos/sin): first re-measure under the symmetric harness + NCU
  SourceCounters sectors/request on cos/sin loads; only if gathers are provably wasteful,
  try thread-remap or a small per-(s-block) cos/sin smem tile; else record near-bound and
  apply DEC-3 to the dispatch entry (the wall win is host-path; keep CUDA route only if
  the wall-fair win reproduces under the symmetric interleaved harness).
- D3 (optional) — PDL validation try (`enable_pdl` arch-gated like the SGLang baseline
  templates): keep only on a measured win on THIS task's benchmark (the b200 qknorm pilot
  showed PDL hurting isolated-launch latency).

Deprioritized by prior evidence: persistent/grid-stride for large buckets (grids of
6k-27k uniform CTAs already saturate), cp.async/TMA (elementwise, nothing to overlap),
pure occupancy tuning (81% occ, 28-32 regs), the four smaller ltx2 buckets (device-fair
1.29-1.46x already and small absolute times).

## Round exit conditions

Either (a) a device-fair win beyond noise on at least one bucket, correct 6/6, with NCU
explaining the gain, dispatch/ledgers/export refreshed; or (b) an evidence-backed
near-attainable-bound no-go: refreshed symmetric+interleaved benchmark + decomposition
table, bounded attempts recorded with reject reasons, roofline summary per representative
bucket. Do NOT iterate past near-bound evidence to chase a number.
