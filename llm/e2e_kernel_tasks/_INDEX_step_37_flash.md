# step_37_flash — e2e kernel task selection

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4` (tp=8)
- Cookbook cmd: `sglang serve --model-path stepfun-ai/Step-3.7-Flash-NVFP4 --tp 8 --ep 8 --moe-runner-backend flashinfer_trtllm --kv-cache-dtype fp8_e4m3`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `step_37_flash__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 32.1% | random_low | role |
| `step_37_flash__linear_gemm` | gemm | linear_gemm | 12.9% | random_mid | role |
| `step_37_flash__fp8_bmm` | quant_gemm | fp8_bmm | 3.6% | random_high | role |

## Dropped < 3.0%

- void_moe_top_k_256_float_const_b: 2.9%

## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 38.6%
- kernel_cutlass_kernel_flashinfernormkernelsfused_add_rm (gemm, comm): up to 33.9%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 33.3%
