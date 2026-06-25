# glm_45 — e2e kernel task selection

- Model: `zai-org/GLM-4.5-FP8` (tp=8)
- Cookbook cmd: `sglang serve --model-path zai-org/GLM-4.5-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `glm_45__fused_moe_triton` | moe | fused_moe_triton | 34.9% | random_high | role |
| `glm_45__attention` | gemm | attention | 9.1% | sharegpt_low | role |
| `glm_45__linear_gemm` | gemm | linear_gemm | 7.1% | random_low | role |
| `glm_45__quant_fp8` | quant_gemm | quant_fp8 | 6.4% | random_low | role |
| `glm_45__void_at_native_sbtopk_gather_top` | moe | void_at_native_sbtopk_gather_top | 5.9% | random_mid | role |
| `glm_45__rmsnorm` | norm | rmsnorm | 3.5% | sharegpt_mid | role |
| `glm_45__void_moe_sum_reduce_warp_per_tok` | moe | void_moe_sum_reduce_warp_per_tok | 3.3% | random_mid | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 18.8%
- ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelA (comm, comm): up to 16.4%
