# Implementation Draft: h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape

Written before any optimized-kernel code. Companion to `prompt.md`,
`interface.md`, `docs/baseline_source.md`, and the Humanize plan at
`.humanize/kernel-agent/refined-plan.md` (untracked).

## Recovered Contract (summary)

- `fused_norm_tanh_mul_add(x, weight?, bias?, scale, shift, norm_type, eps=1e-5) -> y`:
  `y = norm(x) * tanh(scale) + shift`.
- `fused_norm_tanh_mul_add_norm_scale(... weight2?, bias2?, scale2, ...) -> (y, y2)`:
  `y2 = norm2(y) * (1 + scale2)`, where the second norm consumes the
  dtype-quantized `y` (the kernel stores `y` to the output element type in
  registers before the second reduction).
- Both ops are `@torch.library.custom_op("sglang::...")` with fake registration —
  the shipped integration must preserve that.
- `scale`/`shift`/`scale2` must be 3-D `[1|B, 1|S, D]` (validate_3d runs before
  the BSFD broadcast helper); 1-D/2-D/4-D sister-family layouts raise ValueError.
- Domain: `D % 256 == 0`, `D <= 8192`, dtype in {fp16, bf16, fp32}; outputs
  allocated via `torch.empty_like`; current-stream launch.
- Production workload (verbatim, `docs/captured_shapes_h200.jsonl`): bf16, rms,
  eps=1e-5, D=3840, `weight=[D]`, `bias=None`, `scale(/scale2)=[1,1,D]`,
  `shift=[B,S,D]`, `x=[1,4096,3840]` and `[1,4128,3840]`, both entry points.

## Baseline Structure (CuTe-DSL, vendored under `baseline/`)

- Grid `[B*S]` row-CTAs; block `D//256 * 32` threads → D=3840: 15 warps / 480
  threads; each thread owns one 8-element 128-bit vector chunk.
- FP32 accumulation; warp shuffle reduce + cross-warp smem reduce
  (`baseline/common/reduce.py`); `rsqrt(acc/D + eps)`.
- Per-row loads: x row, weight, (bias), scale row-slice, shift row-slice; tanh
  computed PER ROW on the scale slice even when scale is `[1,1,D]`
  (row-invariant) — every CTA redundantly loads + tanh's the same D values.
- Dual variant: second reduction over the quantized y registers, then
  `* w2 * (1 + scale2)`, two full-size stores (y, y2).

## Roofline Pre-Estimates (H200, HBM3e ~4.8 TB/s peak)

Per call, bf16, D=3840:

| Entry | Streams (full-size) | Bytes @ S=4096 | Ideal time @ ~3.8 TB/s eff. |
|---|---|---|---|
| single | read x, read shift, write y (~3 × B·S·D × 2B) | ~94.4 MB | ~25 µs |
| dual | + write y2 (~4 ×) | ~125.8 MB | ~33 µs |

`[D]`-sized tensors (weight, scale row) are negligible (~7.7 KB each) but the
baseline re-reads scale and recomputes tanh per row-CTA: 4096 CTAs × 3840
tanh+loads — worth checking as a non-bandwidth bound (SFU throughput / issue
pressure). H200 = sm90: 132 SMs; 4096 CTAs × 480 threads → ~4 CTAs/SM resident
(1920/2048 threads, 93.75% occupancy cap by thread count).

## Ranked Candidate Directions

1. **Faithful CUDA port of the CuTe structure** (first candidate, clean
   device-delta attribution): row-per-CTA, 480 threads, bf16x8 vector loads,
   FP32 warp+smem reduction, identical math order. Expectation: parity or
   slight win; establishes the attribution anchor. Risk: low.
2. **Row-invariant operand exploitation** (attacks the redundant per-row
   `tanh(scale)` + weight loads in the production signatures): stage
   `weight[D]` and `tanh(scale[1,1,D])` in shared memory once per CTA and
   process MULTIPLE ROWS per CTA (rows-per-CTA 2–8), amortizing the staging
   and the tanh; `shift` stays streamed. Expectation: removes ~D tanh + 2·D
   loads per extra row; helps if the baseline is not purely DRAM-bound.
   Risk: medium (occupancy/smem tradeoff: 2 × 3840 × 4B fp32 staging = 30 KB
   per CTA — fits 228 KB/SM smem at 4 CTAs/SM; may prefer bf16 staging 15 KB).
3. **`tanh(scale)` precompute pre-launch** (DEC-5, allowed with evidence):
   tiny kernel writes `tanh(scale)` to a temp `[D]` buffer; main kernel reads
   it. Alternative to (2) when rows-per-CTA hurts occupancy. Must win in the
   interleaved A/B including launch + alloc cost; must stay graph-safe.
4. **Threads-per-row / vectors-per-thread tuning**: 480×1 vs 240×2 vs 160×3
   vs 120×4 chunks; fewer threads → fewer cross-warp reduction steps, more
   ILP per thread; affects occupancy granularity (480 threads/CTA is awkward:
   2048/480 → 4 CTAs; 240 threads → 8 CTAs/SM). Risk: low, mechanical sweep.
5. **Dual-variant register residency** (port baseline behavior, then improve
   scheduling): ensure y is normed from registers (baseline already does) and
   try splitting the two stores to overlap reduction latency; check whether
   one fused kernel beats two simpler kernels.
6. **Optional PDL** (`cudaTriggerProgrammaticLaunchCompletion` /
   `enable_pdl`-style): validate on the real benchmark; the qknorm pilot
   showed PDL can HURT isolated-launch latency — keep only on a measured win.
7. **Considered and rejected up front**: tcgen05/TMEM (SM100-only, no matmul
   here); TMA bulk copies (row-wise streaming with LDG.128 already saturates;
   revisit only if NCU shows L2/DRAM inefficiency); `--use_fast_math`
   (forbidden — diverges from SGLang numerics).

Stopping rule: a direction gets a bounded number of focused iterations; keep /
revise / reject with benchmark + (when surprising) NCU evidence; everything
logged in `solutions.jsonl` with parent links.

## Prior Art (reviewed 2026-06-04, KernelWiki @ faed56ce)

| Source | Relevance | Kept? |
|---|---|---|
| `pr-sglang-18762` (Z-Image norm fusion — THIS kernel's upstream PR) | origin of both entry points + zimage callsites; its dedicated test file no longer exists at the pinned commit (tests were reorganized under `tests/diffusion/`), confirming the harness-adaptation approach | kept (contract + callsite reference) |
| `pr-sglang-14717` (gated residual layernorm scale-shift fusion) | foundations of `common/norm_fusion.py` + `common/reduce.py` reduction patterns this kernel reuses; sister test structure source | kept (harness structure + reduction reference) |
| `pr-sglang-19059` (fused_qknorm_rope JIT kernel) | the jit_kernel csrc + `load_jit`/`make_cpp_args`/`cache_once` export pattern to mirror (`csrc/elementwise/fused_qknorm_rope.cuh`) | kept (build/export pattern) |
| `pr-flashinfer-2233` (CuTe-DSL RMSNorm + FP4 quant fusion) | independent CuTe-DSL rmsnorm fusion data points | noted (no direct port) |
| `pr-flashinfer-3008` (PDL for rmsnorm CuTe-DSL kernels) | PDL-on-norm-kernel precedent → informs direction 6 | noted (validate-on-task rule stands) |
| KernelWiki `--tag modulation` | no such tag; no additional modulation-specific pages found | n/a |
| Sibling `kernels/h200_diffusion_norm_infer__multi_shape` | `abtest.py`, `benchmark.py --lock`, `validate_install.py`, `docs/baseline_locked.json` admissible-benchmark patterns | kept (harness upgrade template) |
| Sibling `kernels/b200_diffusion_qknorm_rope__multi_shape/src` | lazy `register.py` + `EXPORTS` wrapper pattern; qknorm PDL lesson | kept (register pattern) |

## Harness / Benchmark Plan

- `tests/test_correctness.py`: fp32 tanh oracle; 4 production cases (bench=True)
  + sister-structure regression blocks (96 cases; `KDA_EXHAUSTIVE=1` → 484);
  NaN/Inf validator; dynamic tolerance (cand err ≤ 2× baseline err + 1e-6);
  rejection-contract tests (non-3-D layouts, bad D); sensitivity tests that
  prove the tolerances catch `(1+scale)` math and tanh-on-scale2 mutations.
- `tests/test_baseline_parity.py`: vendored baseline ≡ sglang package
  (torch.equal) on the 4 captured signatures at the pinned commit.
- `benchmark.py` upgrade (next round): CUDA-event + wall-clock timing,
  interleaved same-process A/B, device/host decomposition, GPU-state capture,
  `--lock` baseline freeze following the norm_infer sibling.

## Remote Execution Notes

- Hosts: ion8-h200 primary, ion9-h200 backup; container `sglang_bbuf`; pick an
  idle GPU (no compute procs, no meaningful memory), export `REMOTE_GPU_ID`.
- Task workspace: `/home/sglang-omni/bbuf/kda_runs/h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape/<session>`.
- GPU state recorded before/after every run; results valid only on idle cards.

## Open Questions Carried Into Implementation

- Whether the baseline is DRAM-bound or tanh/issue-bound at D=3840 row-CTAs —
  decides direction 2 vs 3 priority (first A/B + NCU will tell).
- tvm-ffi optional-tensor pattern for `bias=None` in the candidate launcher
  (production fast path needs weight-present/bias-absent only; fallback covers
  the rest) — resolve while porting (task7).

## Round-1 Status Update (2026-06-04)

- Direction 1 (faithful CUDA port) LANDED as candidate-v1: geomean 1.47x
  sequential / 1.36x alternating-interleaved vs the re-locked exact-signature
  baseline; device-only 1.42-1.66x; candidate 2.2-2.7 TB/s vs baseline
  1.43-1.64 TB/s. Same row-per-CTA/480-thread structure — the win comes from
  the leaner native epilogue and lower per-call overhead under symmetric
  custom-op layers.
- Next ranked directions (task9): rows-per-CTA batching + smem staging of
  weight/tanh(scale) (directions 2/4), tanh precompute (direction 3) — single
  still at 40.8us GPU vs ~25us bandwidth-bound ideal (~1.6x residual), dual at
  46.9-47.5us vs ~33us (~1.4x residual). NCU profile when the next edit is
  non-obvious.
- Harness lesson: production signature is weight-only (bias=None); the
  bias-tensor lock overestimated baseline GPU time by ~5% (69.2 -> 65.98us).

## Round-2 Status Update (2026-06-04)

- AC-3 verification closed: default-eps arities (6/9) normalized; dispatch
  unified in dispatch_decision() with branch-contract tests; 16B-alignment +
  grid-limit gates (task8 review); misaligned views fall back AND surface the
  baseline's own ValueError (CuTe assumed_align=32 rejects them upstream too).
- task8 design review integrated; reporting convention: interleaved A/B is the
  primary local number; ab_run1 rows (jit-cache bug) invalidated.
- Direction 2/4 wave-1 sweep REJECTED with evidence: rows-per-CTA (r2/r4),
  fewer-threads (v3/v5), and upfront operand staging ALL lose vs the anchor
  (best non-anchor: v1r2 at 1.18x interleaved vs anchor 1.33x). The anchor's
  load-AFTER-reduce ordering overlaps operand loads with reduction latency;
  pre-staging serializes them. Fewer/larger CTAs reduce memory-level
  parallelism on 4096-row grids. Anchor re-confirmed: 1.4463x/1.3253x.
- Next (round 3): task10 NCU on the anchor (REQUIRED before mechanism claims;
  decides direction 3 tanh-precompute vs occupancy levers vs accept-near-bound),
  then task11 roofline/completion docs, task12 audit, task13 export.
- task10 NCU (profile/ncu_anchor_r2/REPORT.md): NOT DRAM-bound (50-51% mem).
  single = memory-latency-bound (long_scoreboard 5.0/issue) + XU 38.6% (per-row
  tanhf); dual = issue/barrier-bound under 40-reg cap (3 CTAs/SM, 70.3% max
  warps). Wave-2 ranking (evidence-backed): (1) dual launch_bounds reg cap;
  (2) single tanh-precompute buffer (DEC-5); (3) 2-sync block reduction.
