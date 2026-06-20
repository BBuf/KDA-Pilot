# b200_tilert_head_proj_gemm

Target GPU: NVIDIA B200 (sm_100).

## Problem
Implement the DeepSeek-V3.2 **LM-head projection** as a CUDA kernel matching
TileRT's fused `HeadProjExecutorImpl` on the decode shapes.

Math (correctness baseline, `baseline/head_proj.py`):
```
logits[V] = hidden[K] @ W[V, K]^T          # row-major lm_head weight
```
Shapes (per TP shard, vocab split across 8 GPUs):
- hidden: [seq, K=7168] bf16,  seq ∈ {1,2,3,4} (decode / MTP draft widths)
- W (lm_head shard): [V=16160, K=7168] bf16   (vocab_size 129280 / 8)
- logits: [seq, V=16160] fp32

This is **bandwidth-bound**: it reads ~235MB of weights per token; the kernel
quality = how close to HBM roofline you get for small seq.

## TileRT reference (the target to match)
From profiling the real `libtilert_dsv32.so` op on B200 (see
`docs/tilert_reference.md`):
- kernel `HeadProjExecutorImpl<DefaultSchedule, 4, 40960, 1, 1, 3=bf16>`
- grid (148,1,1) × block (384,1,1) — persistent, 1 CTA/SM, 256 consumer + 128 prefetcher
- **39.2 µs, 78.4% of HBM peak (6.0 TB/s), 235 MB read**

TileRT stores the weight in a "native bf16 warp gemv" swizzle:
`[V,K] -> reshape(V/16,16,K/1024,1024).transpose(1,2).reshape(V/16*K/1024,16,1024)`
(16-row × 1024-K tiles for coalesced warp reads). Your candidate may use any
layout — only the **output logits** must match the baseline; pick a layout that
maximizes coalesced HBM throughput.

## Goal
A CUDA kernel that matches the baseline output (rtol per
`../../docs/tilert_correctness_contract.md`) and reaches TileRT's ~39µs / ~78%
HBM on seq ∈ {1,2,4}. Reference levers (TileRT design): persistent grid
occupancy=1, warp-specialized TMA double-buffer streaming the weight once,
warpgroup HMMA. A generic tiled GEMM caps ~58% HBM here (see
`../../../TileRT_讨论材料.md` §17); reaching 78% needs the dedicated
vectorized/warp-spec GEMV.

## Design levers to exploit (see ../../docs/tilert_design_levers.md)
- **L1 tile overlap** (§4/§13): Prefetcher TMA-streams the weight while Consumer warps
  run warpgroup HMMA; mbarrier double-buffer overlaps tile t+1 load with tile t MMA.
- **L2 no-GMEM intermediates** (§13.3): normalized hidden stays on-chip.
- **L3 weight-read-once + occupancy=1 persistent grid** (§4): 148 CTAs × 384 thr,
  1 CTA/SM (~168 reg), weight streamed once. Generic tiled GEMM caps ~58% HBM at
  decode M≈1 (§17); reaching 78% needs the vectorized warp-spec GEMV over the 16×1024 swizzle.

## Milestone
1. `baseline/head_proj.py` — correct PyTorch reference (validated by
   `../../harness/tilert_oracle.py case_head_proj`, rel ~5e-3 vs the real op).
2. `solution/kernel.cu` — candidate CUDA kernel, same ABI.
3. `bench/` — workloads.json (decode 1/2/4 + prefill 8/16), correctness.py, adapter.py.
4. Match TileRT latency (≥3× ncu median, see config.toml `[reference]`); record in `docs/results.md`.
