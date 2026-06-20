# b200_tilert_fused_moe
Target GPU: NVIDIA B200 (sm_100).
## Problem — THE #2 decode cost (36.5%), the make-or-break lever
DeepSeek-V3.2 MoE decode, matching TileRT `FusedMoe`. sigmoid + noaux_tc group-limited
routing (n_group=8, topk_group=4) selects top-8 of 256 experts (+1 shared); FP4 experts.
```
scores = sigmoid(x @ gate); choice = scores + e_score_bias
group-limited top-k (top-2/group summed -> top-4 groups -> top-8 experts); norm; *2.5
out = sum_k w_k * down_k(silu(gate_k(x)) * up_k(x)) + shared(x)
```
Shapes (decode): x[1,7168] bf16; gate[256,7168]; bias[256] f32; experts up/gate/down (FP4,
moe_inter=2048); -> out[1,7168] bf16.
## TileRT reference
FusedMoe = **22.4µs/call avg, 36.5% of decode** (profiler), FP4 experts. Key finding
(../../../TileRT_讨论材料.md §17): bf16 grouped GEMM = 157µs/58% HBM at M=1 (too slow);
**must use fused FP4 + M=1-specialized kernel** (deep_gemm fp8_fp4_mega_moe) to hit 22µs.
This is the single op that decides whether the engine reaches TileRT-class tok/s.
## Design levers to exploit (see ../../docs/tilert_design_levers.md)
- **L5 FP4 bandwidth** (§16/§20): MXFP4 expert up/gate weights → ~4× less HBM. A bf16
  grouped GEMM caps ~58% HBM at 157µs (M=1); FP4 + M=1-specialized kernel is the only path to 22µs.
- **L3 weight-read-once + occupancy=1 persistent grid** (§4): stream the 8 selected
  experts' FP4 weights once via TMA into the resident CTA.
- **L2 no-GMEM intermediates** (§13.3): keep up/gate products on-chip through SiLU and the down-proj.
- **L1 tile overlap** (§4/§13): Prefetcher TMA + Consumer HMMA + mbarrier double-buffer.

## Shapes (decode + MTP)
FusedMoe SASS kSeqLen = {1,2,4}, KeComputeType = 5(fp4)/7(fp8). Workloads
`bench/workloads.json` cover N∈{1,2,4} × {fp4,fp8}. The compute core (up/gate/silu,
routing) is validated standalone via `harness/tilert_oracle.py` cases
`rmsnorm_up_gate_silu` (3.4e-2 fp8) + `rmsnorm_expert_proj` (1e-7); the full 256-expert
FP4 pack is not a 1-call standalone module (see ORACLE_RESULTS.md).

## Goal
CUDA MoE-decode kernel matching the baseline output and ≤ ~22µs on N∈{1,2,4}. Lever:
FP4 block-scaled MMA + fused up/gate/silu/down + M=1 decode specialization (not generic
grouped GEMM). TileRT target latency = in-graph profiler 22.4µs (the fused full-MoE op
is not isolatable per-call; see docs/benchmark_method.md).
