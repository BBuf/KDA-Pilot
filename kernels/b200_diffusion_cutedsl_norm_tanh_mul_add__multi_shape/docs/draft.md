# Implementation Draft — ranked optimization directions

Task: native CUDA candidate for `fused_norm_tanh_mul_add` / `fused_norm_tanh_mul_add_norm_scale`
on B200, vs the CuTe-DSL baseline (copied under `baseline/`, lineage in `docs/baseline_source.md`).

## Workload + bound context (drives the ranking)

Production shapes (all of them): x `[1, S, 3840]` bf16, S ∈ {4096, 4128}, rms, bias=None,
scale/scale2 `[1,1,3840]`, shift `[1,S,3840]` (residual). Both entry points.

Bytes per call at S=4096 (bf16, D=3840; weight/scale D-vectors ≈ 7.5 KB each, negligible):

| Variant | Reads | Writes | Total | Floor @ ~7 TB/s effective |
|---|---|---|---|---|
| v1 (`y` only) | x 31.5 MB + shift 31.5 MB | y 31.5 MB | ≈ 94.4 MB | ≈ 13.5 µs |
| v2 (`y`,`y2`) | x + shift | y + y2 | ≈ 125.8 MB | ≈ 18.0 µs |

B200 peak ≈ 8 TB/s HBM3e (148 SMs). Arithmetic intensity is far below the roofline knee →
memory-bandwidth-bound. KernelWiki `pattern-memory-bound` priorities apply: maximize
bandwidth, reduce registers, differentiate cache policies, do NOT optimize compute paths
that latency-hides anyway (`wiki/patterns/memory-bound.md`).

Baseline device facts (from `baseline/norm_tanh_mul_add_norm_scale.py`): one CTA per row,
grid `[B*S]` (4096–4128 CTAs ≈ 27.7 waves on 148 SMs at 1 CTA/SM... actually 480-thread CTAs
→ up to 4 concurrent CTAs/SM, ≈ 7 waves), `D/8 = 480` threads, bf16x8 128-bit copies,
fp32 reductions, norm result rounded to I/O dtype before modulation, second norm consumes
the rounded `y` held in registers, per-row re-evaluation of `tanh(scale)` even though
production scale is `[1,1,D]` (row-invariant).

## Ranked directions

| # | Direction | Expected benefit | Risk | Attacks |
|---|---|---|---|---|
| R0 | Faithful native CUDA port: CTA/row, 480 thr, bf16x8 128-bit LDG/STG, warp-shuffle + smem CTA reduction, exact `tanhf` (fp32), same rounding points as baseline, single kernel per variant | Correctness anchor + measurable starting point; expect ≈ parity | Low | — |
| R1 | Hoist row-invariant `tanh(scale)` (and `(1+scale2)`): when scale is `[1,1,D]`/`[B,1,D]`, compute tanh once per CTA (registers), reuse across rows (pairs with R2); for CTA/row kernels it still removes redundant per-thread tanh re-eval only when K>1 — at K=1 each CTA does one row anyway, so the win materializes via R2 | Removes (B*S−1)×D redundant SFU/FMA work (~15.7 M tanh → 3.8 K); real win only if NCU shows math pipe pressure or latency exposure | Low | SFU/issue pressure |
| R2 | Multi-row CTA: template K rows/CTA, K ∈ {2,4,8}; weight/`tanh(scale)`/weight2/`scale2` loaded+computed once, x/shift streamed per row; grid 4096/K | Amortizes invariant loads + tanh; fewer CTA launches; better L2 locality for weight/scale | Medium: register pressure (Kx live state? no — stream rows sequentially, state is invariant vectors only), tail rows (4128 = 4096+32, any K∈{2,4,8} divides 4128? 4128/2=2064 ✓, /4=1032 ✓, /8=516 ✓ — clean; still keep a guard loop) | Invariant-load redundancy, wave quantization |
| R3 | Cache-policy + width tuning: `ld.global.nc`/`L1::no_allocate` (streaming) for x/shift and `st.global` streaming hints for y/y2; `L1::evict_last` (or default) for weight/scale; optionally 256-bit loads (`ld.global.v4.u64`) to halve load instruction count | Direct bandwidth-utilization lever per KernelWiki `technique-vectorized-loads`; keeps reused D-vectors hot in L1/L2 | Low-medium (PTX inline; measure, policies can backfire) | DRAM/L2 efficiency |
| R4 | Launch-config tuning for D=3840: threads/CTA ∈ {240(×16/thr), 480(×8/thr), 960(×4/thr)}, `-maxrregcount` budget, occupancy vs ILP | Cheap sweep; picks the best occupancy point; B200 SM = 2048 thr → 480×4 = 1920 (94%) vs 960×2 = 1920 vs 240×8 = 1920 — equal occupancy ceilings, different ILP/reduction width tradeoffs | Low | Occupancy/latency hiding |
| R5 | PDL A/B (`cudaTriggerProgrammaticLaunchCompletion` / launch attribute): OPTIONAL, default OFF | Could hide launch latency in back-to-back denoise steps | Known risk: hurt isolated-launch latency in the qknorm pilot; only keep if it wins on this benchmark | Launch overhead |

Not pursued (and why): tcgen05/TMEM/cluster TMA multicast — no matmul, working set per row
(7.5 KB) far below smem limits, plain LDG already saturates; persistent grid-stride kernel —
equivalent to R2 with K=S/grid, considered inside R2's sweep; separate tanh-precompute kernel —
only if NCU shows SFU dominance that R1/R2 cannot absorb (extra launch likely nets negative
at 13–18 µs total).

## Order of execution

R0 → benchmark + NCU → R2 (with R1 folded in, K sweep) → R3 → R4 → (R5 only as isolated A/B).
Each step: correctness grid → symmetric interleaved benchmark vs frozen baseline →
keep/revise/reject with `solutions.jsonl` lineage; NCU whenever a result deviates from the
bytes-model prediction in either direction.

## KernelWiki references consulted (recorded per AC-7 / exploration policy)

- `pattern-memory-bound` (`wiki/patterns/memory-bound.md`) — optimization priorities for memory-bound kernels; "profile FIRST"; B200 8 TB/s speed-of-light framing.
- `technique-vectorized-loads` (`wiki/techniques/vectorized-loads.md`) — 128/256-bit loads, per-access cache policies, `-maxrregcount`; sm100-relevant.
- `pr-flashinfer-3157` — DiT LayerNorm fusions for WAN (`include/flashinfer/norm/fused_dit_layernorm.cuh`): closest upstream family precedent (cuda-cpp, sm100); useful for kernel structure cross-checks.
- `pr-flashinfer-718` — FusedAddRMSNorm smem pressure when d is large (we stay register-resident; smem only for the warp-partials array).
- Queries run (2026-06-04): "fused rmsnorm layernorm modulation elementwise memory bound kernel sm100"; `--symptom memory-bound`; "vectorized 128-bit loads rows per CTA elementwise norm diffusion".

## Dispatcher gates (fast path; everything else → `baseline/` fallback)

CUDA device + dtype ∈ {bf16, fp16, fp32} + `norm_type` ∈ {layer, rms} + x/scale/shift(scale2)
3-D with last-dim stride 1 and shapes `[1|B, 1|S, D]` + weight/bias ∈ {None, `[D]` contiguous} +
`D % 256 == 0 && D <= 8192` + 16-byte-aligned base pointers (128-bit path). Non-3-D
scale/shift layouts (modes `1, D, 1D, BD, BF1D`) are REJECTED by the public contract
(`validate_3d` upstream) — candidate reproduces the same ValueError behavior.

## Addendum (post-baseline-freeze evidence, round 0)

Frozen baseline (CUDA-event interleaved, B200 GPU0, commit 3957e12df): v1 73.1/72.0 µs,
v2 86.4/88.4 µs (S=4096/4128); wall-synced 82-112 µs. NCU `--set basic` on v1 S=4096
(profile/baseline_r0_sol/): duration **43.3 µs**, Compute(SM) **67-68%**, DRAM **24%**,
grid 4096 × 480 thr, 32 regs, occupancy 80.6%.

Evidence-driven re-ranking:
1. The baseline is COMPUTE-bound (not memory-bound as assumed a priori): R1 (hoist
   row-invariant `tanh(scale)`) is now the top lever, expected to flip the kernel to
   memory-bound; combined with R2 (multi-row CTA) the device floor ~13.5/18 µs becomes
   reachable (potential ~2.5-3x device win).
2. Timing-methodology caveat: event-bracketed baseline time (73 µs) > NCU kernel time
   (43 µs) — the CuTe tvm-ffi host path serializes inside the event bracket. Device-only
   claims use NCU kernel durations; end-to-end claims use the wall-synced numbers; both
   are reported and decomposed.
