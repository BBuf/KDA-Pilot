# Implementation Draft & Optimization Log — b200_diffusion_rotary_embedding__multi_shape

Living notes for the RLCR loop. Prior-art, design decisions, and per-direction
keep/reject records go here (alongside `solutions.jsonl`).

## Recovered Contract (K / R / W)

- **K (kernel semantics)** — two out-of-place SGLang diffusion RoPE entry points:
  - `apply_rotary_embedding(x, cos, sin, interleaved=False)` — adjacent-pair `(2i,2i+1)` rotation, fp32 math then cast to x dtype. `o1 = x1*cos - x2*sin` (`tl.fma(-x2,sin,x1*cos)`), `o2 = x2*cos + x1*sin`. cos/sin are `[tokens, head_dim/2]` fp32 in the captured signature. (`sglang/jit_kernel/diffusion/triton/rotary.py`)
  - `apply_ltx2_split_rotary_emb(x, cos, sin)` — split-half rotation; `out_first = round_bf16(x_first*cos) - x_second*sin`, `out_second = round_bf16(x_second*cos) + x_first*sin`. The `x*cos` term is rounded to bf16 BEFORE the fp32 sin add (matches PyTorch `addcmul_`). cos/sin are `(B,H,S,half)` bf16, **structured non-contiguous** (inner half contiguous; head stride=half; seq stride=H*half). (`sglang/jit_kernel/diffusion/triton/ltx2_rotary.py`)
- **R (oracle)** — the SGLang diffusion Triton baselines above + a PyTorch FP32 cross-check, dynamic BF16-aware tolerance. `test_rope.py` targets a *different* function (`apply_rope_inplace`, LLM q/k RoPE) — style guidance only. (See `README.md`.)
- **W (workload)** — exactly the 11 unique captured signatures in `docs/captured_shapes_b200.jsonl` (1 standard + 10 LTX-2). Do not broaden. The two hunyuanvideo JSONL rows are computationally identical (differ only in a B=1 outer batch stride) → 11 unique (DEC-1).

## Candidate cuda-v1 (current)

Native CUDA, built+exported through SGLang `jit_kernel`/tvm-ffi (no `torch.utils.cpp_extension`, no `--use_fast_math`), workspace-owned `src/csrc/rotary_embedding.cuh` built in place via an absolute `load_jit(cuda_files=[...])` path.

- Standard kernel: one block per token row; cos/sin row staged in shared memory and reused across heads; adjacent pair loaded/stored as a packed 2-element vector (`packed_t<DType>`); fp32 `fmaf` matching the baseline.
- LTX-2 kernel: one block per `(batch, token)` row; cos/sin indexed via the passed strides (handles the structured non-contiguous layout); `round_bf16(x*cos)` before the fp32 sin add for bit-exactness; templated on `half_dim ∈ {32,64}`.
- Dispatcher (`src/wrapper.py`): routes only the captured signature families to CUDA; everything else falls back to the baseline object captured at import (recursion-safe after a public-symbol swap). PDL OFF for v1 (validated separately).

## Optimization Directions (ranked; to be confirmed with B200 evidence)

1. Vectorize LTX-2 loads/stores (wider packed access across `j`) — both ops are memory-bound; coalesced wide access is the primary lever. (risk: low; attacks DRAM throughput)
2. Standard: confirm cos/sin shared-mem reuse pays off; tune block/grid (token-tiling) for the 27030×24×128 shape. (risk: low)
3. LTX-2-small `S=126`: launch/occupancy/tail-bound — consider fewer CTAs doing more rows each. (risk: med; only if NCU confirms launch bound)
4. PDL A/B per shape (kept only if it wins; the qknorm pilot showed it can hurt). (risk: low)
5. Per-bucket dispatch/specialization only if NCU shows different tradeoffs per bucket.

## Optimization Log (Round 0) — search DAG in solutions.jsonl

| Cand | Change | Correctness | Geomean | Key per-shape | Decision |
|---|---|---|---|---|---|
| cuda-v1 | standard packed bf16x2 + shared cos/sin; LTX-2 scalar strided loads | bit-exact 11/11 | 0.954× | ltx2-large 0.61–0.73× (scalar loads BW-inefficient) | reject (large regressed) |
| cuda-v2 | 128-bit vectorized loads/stores both kernels | bit-exact 11/11 | 1.351× | standard 1.54×, ltx2-large-half64 1.00× (BW ceiling) | keep |
| cuda-v3 | standard drops shared-mem `__syncthreads`; vectorized fp32 cos/sin (L2) | bit-exact 11/11 | 1.349× | standard 1.76× (DRAM SOL 48→59%) | keep |
| **cuda-v4** | LTX-2 block size matched to per-row work (half32→128 threads) | bit-exact 11/11 | **1.383×** | standard 1.80×, ltx2-small/med 1.66–1.71×, occ 73.6→86% | **promote** |

## Prior Art / Lever Analysis (Codex `analyze`, gpt-5.5:high)
Independent review concurred with the active-bound diagnosis and "promote, no blocker". Levers ranked:
1. Multi-row-per-CTA / warp-density — **applied in cuda-v4** (block-size match; the top lever).
2. Cache-policy / read-only tuning — modest, fragile; not pursued (diminishing returns past 128-bit BW).
3. Grid ordering for standard cos/sin L2 reuse — already adjacent (heads contiguous per token).
4. 256-bit loads — low benefit once 128-bit saturates BW; alignment/register risk; not pursued.
5. `__launch_bounds__` — low value; occupancy already healthy.
6. Persistent kernel / TMA / clusters — **rejected**: streaming elementwise RoPE with little reuse; those are for tiled/reused workloads (KernelWiki memory-bound guidance agrees).
7. Fusion with producer/consumer — only path beyond the BW ceiling, but changes API/scope; out of bounds for a standalone-kernel task.

Conclusion: each bucket is at/near its active bound; cuda-v4 exceeds the prior-run hypothesis (1.3676×) at 1.3834× and wins every shape. No further standalone-kernel lever has a favorable benefit/risk ratio.

## Open Decisions (defaults applied; see refined-plan DEC-1..3)
- DEC-1: geomean over 11 unique signatures.
- DEC-2: leave `prompt.md` oracle text; correction documented here + README.
- DEC-3: kernel-folder artifacts during the loop; SGLang-tree placement only at export.

---

# Continuation Run (k09, 2026-06-04) — revalidation + bounded headroom attempts

Plan: `.humanize/kernel-agent/refined-plan.md` (continuation per DEC-1..DEC-6).
Optimization gate for replacing `cuda-v4`: per-shape no-regression within
noise band = max(3%, cross-run spread), 2-of-3 idle-gated paired runs, plus a
beyond-noise win on >=1 targeted bucket.

## Environment re-pin (2026-06-04, AC-2)

- Host `ion-b200` (`innomatrix-us-adc-smb200-0003`), container `sglang_bbuf`, GPU 1 (NVIDIA B200, idle-gated), driver 580.126.20.
- SGLang checkout `/sgl-workspace/sglang` @ `edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7` (version `0.0.0.dev1+gedb1b3f8f`) — **rewound vs the 2026-06-01 pin** `0b65588c…` (`0.5.12.dev472`): the old pin is NOT an ancestor of the current HEAD.
- torch 2.11.0+cu130, triton 3.6.0, nvcc cuda_13.0 (V13.0.48 build 36424714), tvm_ffi 0.1.9.
- Remote workspace: `/home/sglang-omni/bbuf/kda_runs/b200_diffusion_rotary_embedding__multi_shape/2026-06-04_17-45-46/kernel`.

## Revalidation results (cuda-v4, unchanged sources)

- Correctness: `KDA_RUN_CORRECTNESS=1 pytest tests/test_correctness.py` → 4 passed
  (11/11 signatures vs current baseline + FP32 cross-check, register metadata,
  fallback-exactly-once spy, dispatch predicates).
- Benchmark: 3 idle-gated `benchmark.py --warmup 50 --iters 300 --candidate cuda-v4`
  runs appended to `benchmark.csv` (lines 43-84). Geomeans 3.1747 / 3.0772 / 3.1321x.
- cuda-v4 medians match the 2026-06-01 evidence (61.86us standard; 92.54us
  half64-large; 49.57us half32-large; 21-23us small class, 7-8% cross-run spread).

## BASELINE SHIFT (must accompany any geomean claim from this run)

The current container baseline is SLOWER than the 2026-06-01 baseline on large
LTX-2 shapes (e.g. `1x24576x2048`: 59.6 -> 414.1us; `2x6144x2048`: 43.3 -> 209.4us).
Cause: the 2026-06-01 pin `0b65588c` was a branch carrying **PR #24732
"[codex] Optimize LTX2 split rotary kernel"** (BLOCK_HEADS<=16 multi-head
programs, num_warps scaled) — absent from the current HEAD `edb1b3f8f`, whose
`_ltx2_split_rotary_kernel` runs one tiny program per (token, head) with
num_warps=1 (last touched by PR #24411). The standard `rotary.py` baseline is
identical in both environments (110us). cuda-v4 is unaffected (device kernel
unchanged, medians stable), so the inflated geomean (~3.1x vs ~1.45x) reflects
the baseline environment change, NOT a candidate improvement. The continuation
gate is therefore evaluated **vs cuda-v4**, and the final report must quote
both baselines explicitly.

## Fresh continuation reference (median us, 3 runs: r1/r2/r3)

| shape | base r1/r2/r3 | cuda-v4 r1/r2/r3 | spd (med) | cand spread |
|---|---|---|---|---|
| standard 1x27030x24x128 | 109.97/110.82/110.85 | 61.86/61.86/61.86 | 1.792x | 0.00% |
| ltx2 1x1536x4096 h64 | 39.36/40.64/39.42 | 21.22/22.69/21.92 | 1.799x | 6.94% |
| ltx2 1x126x2048 h32 | 31.87/33.06/32.83 | 21.18/22.72/21.79 | 1.507x | 7.25% |
| ltx2 1x1536x2048 h32 | 39.30/41.23/39.46 | 20.99/22.66/21.50 | 1.835x | 7.93% |
| ltx2 1x6144x4096 h64 | 108.83/108.90/108.93 | 27.14/29.18/28.91 | 3.766x | 7.55% |
| ltx2 1x6144x2048 h32 | 106.94/107.01/107.01 | 21.55/23.20/22.22 | 4.815x | 7.65% |
| ltx2 2x6144x4096 h64 | 209.31/209.34/209.38 | 49.54/49.54/49.63 | 4.226x | 0.19% |
| ltx2 2x126x2048 h32 | 31.84/33.23/32.38 | 21.15/22.82/21.57 | 1.501x | 7.87% |
| ltx2 2x6144x2048 h32 | 209.38/209.38/209.38 | 27.87/30.08/28.13 | 7.444x | 7.92% |
| ltx2 1x24576x4096 h64 | 414.08/414.14/414.11 | 92.54/92.54/92.58 | 4.475x | 0.03% |
| ltx2 1x24576x2048 h32 | 414.05/414.11/414.14 | 49.57/49.57/49.62 | 8.354x | 0.10% |

## Ranked continuation directions (AC-3; evidence = profile/ncu-v2/REPORT.md + src/csrc/rotary_embedding.cuh + fresh reference above)

KernelWiki consult (2026-06-04): `--tag rope --architecture sm100` -> no RoPE-specific SM100 pages;
`technique-vectorized-loads` (wiki/techniques/vectorized-loads.md) is the relevant prior art:
128/256-bit loads + differentiated L1 cache policies for streaming data on B200 (8TB/s).
ncu-report-skill consult: existing ncu-v2 SOL map reused for ranking (kernels unchanged since);
fresh NCU only after a candidate result needs explanation (AC-6).

Noise bands for the gate (max(3%, cross-run spread)): standard 3%; large LTX-2 3%; small/medium LTX-2 ~8%.

| # | Bucket | Direction | Expected benefit | Risk | Evidence basis |
|---|---|---|---|---|---|
| D1 | LTX-2 large-half32 | Multi-row CTA for kHalf=32: 2 rows/block x 128 thr = 256-thr blocks (half64-identical occupancy/MLP); half64 template path untouched | 74.9% -> ~85% DRAM SOL; 49.6 -> ~44us (+10-12%) | LOW (same math, bit-exact; predicate/grid change only) | half64 sibling hits 85.3% SOL with 256-thr blocks; half32 has half the in-flight loads (waves 10.4 vs 20.8) |
| D2 | standard | Instruction diet, math unchanged: hoist cos/sin vector loads out of the per-head loop (each thread's pair-segment is invariant across its 1.5 passes); try 192-thr blocks (384 vec/row = 2 full passes, no idle half-pass) | fewer LSU ops + no idle pass; 61.9 -> ~56-58us (+5-10%) | LOW (bit-exact preserved) | ncu-v2: compute 62.1%/DRAM 59.1% (issue-balanced); current code re-loads cos+sin per vector and idles 50% of lanes in pass 2 |
| D3 | standard | bf16-packed math under the tolerance contract (DEC-2): PRMT even/odd split + bf16x2 FMA pipeline, drop per-element cvt fp32<->bf16 | if still compute-leaning after D2: -> ~52-54us (additional +5-8%) | MEDIUM (precision must pass dynamic tolerance; bit-exactness lost; PRMT complexity) | compute SOL 62% with fp32 math + cvt per element; B200 bf16x2 SIMD halves FMA issue + removes cvt |
| D4 | LTX-2 small | Host dispatch-cost shave: memoize predicate result keyed on full (shape,stride,dtype,device) tuple; full decomposition per the device-vs-host rule; fallback/predicate tests must stay green | small-shape median -5..15%; must beat ~8% noise band 2-of-3 runs | MEDIUM (dispatch-correctness risk; host-layer change needs decomposition evidence) | small class is launch/wrapper-floor bound (0.05 waves/SM; 21-23us flat); kernel itself is a minor fraction |
| D5 | LTX-2 large-half32 | 256-bit (32B) accesses + L1 no-allocate/evict-first streaming hints — only if D1 lands <80% SOL and NCU shows LSU/L1 pressure | +2-5% conditional | MEDIUM-LOW | KernelWiki technique-vectorized-loads; all streams are single-use (no reuse) |
| — | LTX-2 large-half64 | No work: no-go stands (85.3% DRAM SOL, HBM ceiling, parity baseline) | — | — | ncu-v2 REPORT.md; kernel unchanged |
| — | LTX-2 small (device side) | No kernel work beyond D4: launch floor; cannot add work to fixed shapes | — | — | ncu-v2 dimension 5 (launch-overhead) |

Execution: cuda-v5 = D1 + D2 (disjoint kernels: ltx2<32> launcher + standard kernel; half64 path byte-identical).
cuda-v6 = D3 (only if post-v5 NCU still shows compute/issue pressure on standard).
cuda-v7 = D4 (single bounded attempt, decomposition required). D5 only on D1 underperformance.
PDL re-trial: WAIVED this round — prior A/B showed PDL hurting isolated-launch latency on this exact task (docs above); no new evidence to revisit.

## Codex triage review integration (2026-06-04, gpt-5.5:high)

Codex reviewed the D1-D5 ranking (full text in the loop workspace). Verdicts applied:
- **D1 re-ranked: bounded experiment, uncertain payoff** (was: top win). Codex: half32 already
  runs 86% achieved occupancy; 2 rows/CTA keeps the same resident-thread count (2048/SM either
  way), so the half64-SOL analogy does not justify a 10-12% claim. The 74.9%->85% SOL projection
  is withdrawn; D1 is attempted because it halves block-scheduling events and improves tail
  behavior at zero numeric risk, with revert-on-regression per bucket.
- **D1 exact mapping (per Codex)**: `num_blocks=(total_rows+1)/2`, `local_row=threadIdx.x/tpr`,
  `lane=threadIdx.x%tpr`, per-thread row guard (odd tail), per-row recompute of b/s/cos/sin bases.
- **D2 confirmed correct** (pass-invariance holds for any blockDim multiple of kVecPerHead=16);
  extended with a {128,192,256} block-size sweep (hoisted cos/sin) before any D3 work.
- **D3 tightened**: MEDIUM-HIGH risk; only after post-D2 NCU still shows compute/issue pressure;
  fp32 cos/sin loads remain, so the gain estimate is reduced.
- **D4 DROPPED from the gate-eligible ranking**: predicate memoization is host-layer work; any
  win must be decomposed against a memoized-cuda-v4 control and cannot satisfy the "targeted
  bucket kernel win" gate. Parked as queued host-integration follow-up, out of this round's gate.
- **D5 unchanged** (conditional on NCU LSU/L1-pressure evidence; 256-bit vectors may reduce lane
  count and hurt parallelism).
- PDL waiver and half64 no-go endorsed.

Execution after integration: cuda-v5 = D2 (hoist + swept block size) + D1 (2-rows/CTA, kHalf=32
only, half64 path byte-identical), evaluated per-bucket vs cuda-v4 with the noise-band gate;
revert whichever component regresses its bucket.

## Continuation outcomes per bucket (gate vs cuda-v4; full data: benchmark.csv 2026-06-04 + profile/ncu-v3/REPORT.md)

| Bucket | Direction(s) tried | Outcome |
|---|---|---|
| standard | D2 (cuda-v6: cos/sin register hoist + full-pass 128-thr blocks; B200 sweep {64..256}); D5-class MLP probe (cuda-v7 double-buffer) | **WIN: cuda-v6 1.0709-1.0718x over cuda-v4 (3-of-3 beyond 3% band), 61.86 -> 57.7us.** v7 rejected (zero movement) -> kernel DRAM-queue-paced at ~75% of peak; D3 no-go by evidence (compute SOL 47%, not the limiter) |
| LTX-2 large-half32 | D1 (cuda-v5 two-rows-per-CTA) | NO-GO: D1 = 1.0006x on target (Codex residency argument experimentally confirmed); fresh NCU 76.1% DRAM SOL, clean coalescing, no LSU/sector rule fired -> D5 evidence bar not met; bound = DRAM bandwidth at layout granularity |
| LTX-2 small | (D1 side effect measured; D4 ruled gate-ineligible by Codex review) | NO-GO: launch/latency floor; v5 grid-halving regressed 1x126x2048 by 12% (hypersensitive to launch shape); device-side floor confirmed |
| LTX-2 large-half64 | none (kernel byte-identical) | NO-GO stands (ncu-v2: 85.3% DRAM SOL, HBM ceiling) |

Gate verdict: **cuda-v6 PASSES the hard no-regression gate.** Authoritative gate evidence = the
THREE provenance-complete idle-gated paired sessions of 2026-06-04 ~11:0x-11:17 UTC
(`benchmark.csv` rows `cuda-v6_vs_cuda-v4` whose `cmd='…'` includes the literal
`--compare-src ../v4_src --compare-label cuda-v4`; v4 snapshot `f4c8b844044f`):
standard 1.0703/1.0709/1.0709x (3-of-3 beyond the 3% band); no shape regresses beyond its noise
band in 2-of-3 runs (worst single-run ratio 0.9723 on `1x6144x4096 h64`, one run only, within
its ~7.6% band; the 24576-row and `2x6144x4096` shapes are literal 1.0000x in all 3 sessions).
Fresh pair geomeans 1.0049/1.0050/1.0018x. (An earlier 3-session set with the same verdict —
1.0038/1.0061/1.0066x — predates the command-provenance fix in `benchmark.py` and remains in
the CSV as corroborating history only.) Outcome metric vs the CURRENT SGLang baseline
(edb1b3f8f): geomean 3.1043-3.1965x across all six sessions — read with the BASELINE SHIFT note
above (the ltx2 Triton baseline on this checkout lacks PR #24732 and is 2-8x slower at scale
than the 2026-06-01 pinned baseline; cuda-v6's device kernels are the same speed in both
environments). Like-for-like vs the 2026-06-01 environment: standard 110.8/57.7 = 1.92x (was
1.80x), LTX-2 buckets unchanged -> environment-adjusted geomean = old geomean x geomean(fresh
pair geomeans) = 1.4505 x 1.0039 = **1.456 -> headline ~1.46x**.

## Gate-review corrections (Codex independent review, 2026-06-04)

Codex verified the gate verdict and bound conclusions, and required five corrections — all applied:

1. **cuda-v5 / cuda-v7 evidence provenance.** The cuda-v5 paired-run CSV rows were LOST: the
   full-folder re-sync that uploaded the v6 sources recreated the remote workspace and overwrote
   the remote `benchmark.csv` before those rows were pulled back. cuda-v7 was timed only by the
   sweep harness (by design, no CSV rows). Their `solutions.jsonl` evidence pointers are corrected
   by an appended correction entry; the v5 paired-run log (as printed by `benchmark.py`) is
   preserved verbatim below. The v5/v7 rows are REJECTED candidates — no promotion claim rests on
   them; the shipping evidence (cuda-v4 revalidation + cuda-v6 gate runs) is fully CSV-backed.

   cuda-v5 paired run log (run 1 of 1, idle-gated true/true, GPU 1, 2026-06-04):
   `standard 61.86->57.78us 1.0706x | 1x1536x4096h64 0.9930x | 1x126x2048h32 23.33->26.45us 0.8820x |
   1x1536x2048h32 1.0000x | 1x6144x4096h64 0.9989x | 1x6144x2048h32 0.9923x | 2x6144x4096h64 1.0000x |
   2x126x2048h32 0.9943x | 2x6144x2048h32 1.0017x | 1x24576x4096h64 0.9997x | 1x24576x2048h32 1.0006x |
   GEOMEAN_VS_CUDA-V4 0.9930x`
   cuda-v7 sweep log: `57.73/57.74/57.76us` (3 runs, 300 iters each) vs cuda-v6 57.7us. Correctness
   4/4 passed for both v5 and v7 before their rejection (pytest run per iteration; v6's final raw
   log is in `docs/logs/correctness_cuda_v6_20260604.log`).

2. **Like-for-like estimate corrected to ~1.46x** (was ~1.49x, bad composition). Arithmetic:
   environment-adjusted geomean = old-environment geomean x paired geomean(v6/v4) =
   1.4505 x (1.0038..1.0066) = **1.456-1.460**; using the old-run spread (1.4417-1.4633) the
   cross-run combination range is ~1.447-1.473. Headline like-for-like: **~1.46x**.

3. **Large-shape parity phrasing**: "large shapes remain within <=0.6% paired delta; the
   24576-row shapes are exact parity to the displayed precision" (worst observed paired slowdown
   across ALL shapes/runs: +1.198% on 1x1536x4096 half64, within its ~8% band).

4. **LTX-2 "byte-identical" -> "functionally unchanged"**, now diff-backed:
   `docs/logs/v4_to_v6_rotary_cuh.diff` (78-line diff vs the v4 snapshot `f4c8b844044f`) shows all
   code deltas live in the standard kernel/launcher; the only LTX-2 delta is a 3-line comment
   (no kernel-body or launch-config change). Paired runs confirm behavioral parity.

5. **Final correctness re-run recorded raw**: `docs/logs/correctness_cuda_v6_20260604.log` —
   4 passed; per-shape `pair_diff=0.000e+00` on 11/11 (cuda-v6 BIT-EXACT vs the SGLang baseline;
   `cand_err == base_err` exactly on every signature).

Queued (non-blocking, next cycle): stale `static_assert` message in `StandardRotaryKernel`
mentions a removed "shared cos/sin cache" — comment-only cleanup deferred to avoid churning the
gate-evidence source hash (`317e2fab7ade`).

## Round-1 corrections (Codex round-0 RLCR review, 2026-06-04)

All four REQUIRED items applied:
1. `benchmark.py` `cmdstr` now records `--compare-src/--compare-label`; the hard-gate evidence was
   re-collected as three fresh idle-gated paired sessions (rows of 2026-06-04 ~11:0x-11:17 UTC,
   full command provenance) — gate verdict unchanged (see the updated verdict paragraph above).
2. `kda_install_validate.py` gained parent/worker `nvidia-smi` idle gating with before/after
   states embedded in the JSON; the replacement run shows `idle_gated: true`, installed-path
   standard 57.71us == direct wrapper (no host tax), oracle bit-exact 11/11.
3. The stale `~1.49x` like-for-like paragraph was replaced in place with the corrected
   composition (1.4505 x 1.0039 = 1.456 -> ~1.46x).
4. b200 KDA metadata unified: `__init__.py` / `KDA_EXPORTS.json` / `KDA_STATUS.md` all carry the
   same kp commit and the same annotated speedup string (verified by script + grep). Stale-string
   sweep across docs/prompt.md/interface.md/solutions.jsonl/kda_kernels: zero occurrences of
   `1.49x` (outside correction notes), `ec7b6459`, or bare `1.0038x`/`1.0018x` (the only
   remaining `1.0018x` is the legitimate fresh pair-geomean citation in the verdict paragraph).

## Round-2 correction (Codex round-1 RLCR review, 2026-06-04)

Gap from the round-1 review: the active "Continuation re-export" statement in
`docs/sglang_jit_export.md` cited the interim kp commit stamp from the first re-export pass,
contradicting the unified b200 metadata commit `afb416adff0765da3bf610826631b6d5704d5381`.
Fixed in round 2: that statement now cites only the canonical commit (and names all three
unified surfaces). The round-2 sweep note that documented this fix was itself internally
inconsistent (it claimed zero occurrences of strings it contained); this round-3 rewrite
replaces it with the two-scope validation below, whose stated counts were verified against an
actual re-run AFTER this note reached its final form.

Sweep pattern and full surface list (the pattern literals appear in this file ONLY on the next
line; the two superseded commit short-hashes inside the command self-match, which is accounted
for in scope B):

    grep -RnE "1\.49x|ec7b6459|ea349b784|1\.0038x" docs prompt.md interface.md solutions.jsonl ../../kda_kernels/diffusion/rotary_embedding

**Scope A — active surfaces** (everything above EXCEPT this correction log `docs/draft.md` and
the append-only `solutions.jsonl` history rows; i.e. `docs/sglang_jit_export.md`, `docs/logs/`,
all other `docs/` files, `prompt.md`, `interface.md`, and the kda_kernels rotary_embedding
package): **0 matches**. Neither superseded commit short-hash, nor the rejected like-for-like
estimate, nor a bare unqualified pair-geomean value appears on any active surface; every active
claim reads ~1.46x (1.4505 x 1.0039 composition) and cites only the canonical commit.

**Scope B — full sweep including the correction log and append-only history**:
- `docs/draft.md` — 7 pattern occurrences on 4 lines, all correction-log self-references:
  - line 210 (round-0 gate-review corrections, item 2): the rejected like-for-like estimate
    literal, in "corrected to ~1.46x (was ~…)" prose.
  - line 241 (round-1 corrections, item 3): prose describing the replaced estimate.
  - line 246 (round-1 corrections, item 4): the round-1 sweep-pattern documentation line — the
    estimate literal, the OLDER superseded commit short-hash, and the bare pair-geomean literal.
  - line 264 (the single command line above in THIS note): the two superseded commit
    short-hashes, which self-match inside the documented pattern.
- `solutions.jsonl` — 2 occurrences (lines 15 and 16): the append-only correction rows
  `evidence-correction-v5-v7` and `evidence-refresh-round1`, each containing the rejected
  estimate literal inside its correction prose.
- Every other swept surface (`docs/sglang_jit_export.md`, `docs/logs/`, the remaining `docs/`
  files, `prompt.md`, `interface.md`, `kda_kernels/diffusion/rotary_embedding`): **0 occurrences**.
- Totals: **9 occurrences on 6 lines**; the superseded commit short-hashes appear ONLY on lines
  246 and 264 of this correction log and nowhere else in the entire sweep surface.
All scope-B matches are, by construction, one of: (i) correction-log prose describing what was
corrected (the round-0/round-1 notes in this file), (ii) the single command line above (the two
commit short-hashes self-match), or (iii) the two append-only `solutions.jsonl` correction rows,
which the evidence policy forbids rewriting. None is an active claim.

## OFFICIAL BASELINE: sglang main (post-loop re-measurement, 2026-06-04)

Per user direction, the PR-facing performance comparison uses **sglang MAIN as the baseline**,
not the container's rolled-back checkout. Method: task-owned worktree of sglang at
`origin/main` = `8933ec877235e24fd994246c6f8db225a4cb2823` (which CONTAINS PR #24732's fast
BLOCK_HEADS LTX-2 Triton kernel); `benchmark.py --sglang-path ../sglang_main/python` resolves
`import sglang` (baseline kernels + jit build stack) from that worktree, so the recorded command
alone pins the baseline source. Correctness re-run against the main baseline first: 4 passed
(11/11 signatures, bit-exact pair_diff=0; main's kernel math is identical, only its launch
blocking differs from the rolled-back checkout).

Three idle-gated sessions (idle_before/idle_after true; benchmark.csv rows with
`--sglang-path` in the cmd field; GPU 1, B200):

| shape | main base (med of 3) | cuda-v6 (med of 3) | speedup |
|---|---|---|---|
| standard 1x27030x24x128 | 110.69 | 57.73 | 1.917x |
| ltx2 1x1536x4096 h64 | 36.02 | 21.63 | 1.665x |
| ltx2 1x126x2048 h32 | 35.49 | 21.50 | 1.650x |
| ltx2 1x1536x2048 h32 | 35.58 | 21.41 | 1.662x |
| ltx2 1x6144x4096 h64 | 42.45 | 28.03 | 1.514x |
| ltx2 1x6144x2048 h32 | 36.24 | 21.66 | 1.673x |
| ltx2 2x6144x4096 h64 | 49.57 | 49.54 | 1.001x |
| ltx2 2x126x2048 h32 | 35.30 | 21.38 | 1.651x |
| ltx2 2x6144x2048 h32 | 42.38 | 27.90 | 1.519x |
| ltx2 1x24576x4096 h64 | 92.54 | 92.54 | 1.000x |
| ltx2 1x24576x2048 h32 | 59.81 | 49.54 | 1.207x |

**Geomean vs sglang main: 1.4660x** (per-shape medians; session geomeans 1.4325/1.4640/1.4740x).
This MEASURES what the round-1 like-for-like composition estimated (~1.46x) and supersedes both
the estimate and the container-baseline geomean (3.1x, kept only as documented context for the
BASELINE SHIFT note above). The main baseline's per-shape numbers match the 2026-06-01 pinned
environment closely (e.g. 24576-h32 59.81 vs 59.6us), confirming main == the fast baseline.

v4-pair legs inside these sessions: standard 1.0709-1.0721x (consistent with the gate set);
one launch-bound outlier in session 1 (126-row h32 pair ratio 0.79, 1-of-3 sessions, the v6/v4
code paths are byte-identical there -> environmental noise; the authoritative gate evidence
remains the dedicated provenance-complete set, where the 2-of-3 rule holds on every shape).
