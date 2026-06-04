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
