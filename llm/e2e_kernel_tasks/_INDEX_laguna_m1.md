# laguna_m1 — e2e kernel task selection

- Model: `poolside/Laguna-M.1-NVFP4` (tp=8)
- Cookbook cmd: `sglang serve --model-path poolside/Laguna-M.1-NVFP4 --tp 8 --trust-remote-code --reasoning-parser poolside_v1 --tool-call-parser poolside_v1`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `laguna_m1__linear_gemm` | quant_gemm | linear_gemm | 36.6% | random_high | role |
| `laguna_m1__sglang_unified_attention_with_output` | gemm | attention | 8.0% | random_low | yes |
| `laguna_m1__compute_expert_blockscale_offset` | moe | compute_expert_blockscale_offset | 5.7% | random_low | role |
| `laguna_m1__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 5.5% | sharegpt_low | role |
| `laguna_m1__void_apply_shuffle_mul_sum_kerne` | other | void_apply_shuffle_mul_sum_kerne | 3.9% | random_low | role |

## Dropped < 3.0%

- void_cublas_lt_split_kreduce_ker: 2.8%
- rmsnorm: 2.7%
- activation: 2.6%

## Excluded (comm / trtllm fused-MoE)

- ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelA (comm, comm): up to 11.7%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 8.4%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 7.0%
