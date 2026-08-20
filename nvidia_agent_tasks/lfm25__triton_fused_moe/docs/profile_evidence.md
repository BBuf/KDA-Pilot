# Profile evidence: Triton fused MoE (LFM2.5-8B-A1B + GLM-4.7-Flash)

## `workloads.json` (model: `LiquidAI/LFM2.5-8B-A1B`)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `triton_fused_moe_gemm` | 427506 | 1138 | 11 |

Representative shapes (largest / smallest kept row per op):

- `triton_fused_moe_gemm` hottest: A[1, 2048]:bfloat16, B[32, 3584, 2048]:bfloat16, C[4, 3584]:bfloat16, topk_weights[1, 4]:float32, topk_ids[1, 4]:int32, sorted_token_ids[64]:int32
  - another operating point: A[16384, 2048]:bfloat16, B[32, 3584, 2048]:bfloat16, C[65536, 3584]:bfloat16, topk_weights[16384, 4]:float32, topk_ids[16384, 4]:int32, sorted_token_ids[67615]:int32


Call counts are real traffic only: every call observed before a capture-group
label was active (start-up, CUDA-graph capture, autotune) is kept separately in
the `warmup_only_shapes` section of the source manifest and never enters a
workload row. See `../docs/workload_capture.md`.

**Cross-check:** 50.5% of serving GPU time on LFM2.5 and 30.4% on GLM-4.7-Flash in the earlier
sweep. In this capture the Triton MoE GEMM fired **427,506** times across 9 operating points on
LFM2.5 and **223,652** times on GLM-4.7-Flash, so both shape families are live.

Expert weights are metadata-only in the payload (too large to ship) - their shape/dtype/scale
layout is recorded. The activation and routing side is real, which is where the distribution
matters: real routing is skewed and that changes tile occupancy.

## Second shape family: GLM-4.7-Flash

`bench/workloads_glm47_flash.json` carries the same kernel from a different expert
geometry, captured in the GLM-4.7-Flash run (its serving command and GSM8K accuracy
of 0.820 are recorded in `bench/workloads_glm47_flash.json`; the GLM-4.7-Flash
attention task that shared this capture is no longer part of the set):

| | LFM2.5-8B-A1B | GLM-4.7-Flash |
| --- | --- | --- |
| real calls | 427,506 | 571,044 |
| distinct signatures | 1,138 | 420 |
| experts / top-k | 32 / top-4 | 65 / top-5 |
| activation width | 1792, 2048 | 1536, 2048 |
| expert weight block | `[32, 2048 or 3584, ...]` | `[65, 2048 or 3072, ...]` |
| token counts seen | 1, 2, 4, 8, 16, 32, 64, 128 ... 16384 | 1, 2, 5, 10, 16, 32, 80 ... 16384 |

Two families matter here because the routing distribution, not just the GEMM shape,
drives tile occupancy: `sorted_token_ids` reaches 67,615 on LFM2.5 and 86,078 on
GLM-4.7-Flash, and `expert_ids` 1,057 vs 1,345 padded blocks. A candidate that only
tunes one geometry will regress the other.
