# devstral2 — e2e kernel task selection

- Model: `mistralai/Devstral-2-123B-Instruct-2512` (tp=8)
- Cookbook cmd: `sglang serve --model-path mistralai/Devstral-2-123B-Instruct-2512 --tp 8 --reasoning-parser mistral --tool-call-parser mistral`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `devstral2__linear_gemm` | gemm | linear_gemm | 38.5% | sharegpt_low | role |
| `devstral2__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 10.6% | random_low | role |
| `devstral2__sglang_unified_attention_with_output` | attention | attention | 10.5% | sharegpt_high | yes |
| `devstral2__rmsnorm` | norm | rmsnorm | 8.5% | sharegpt_mid | role |
| `devstral2__quant_fp8` | quant_gemm | quant_fp8 | 6.6% | random_low | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelA (comm, comm): up to 32.4%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 21.0%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 9.7%
