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
