# ring_25_1t — e2e kernel task selection

- Model: `inclusionAI/Ring-2.5-1T` (tp=8)
- Cookbook cmd: `sglang serve --model-path inclusionAI/Ring-2.5-1T --tp 8 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `ring_25_1t__sglang_inplace_fused_experts` | moe | fused_moe_triton | 32.3% | random_high | yes |
| `ring_25_1t__sgl_kernel_fp8_scaled_mm` | gemm | linear_gemm | 17.7% | random_high | yes |
| `ring_25_1t__void_at_native_unrolled_elementw` | memory_bound | void_at_native_unrolled_elementw | 5.0% | random_high | role |
| `ring_25_1t__sgl_kernel_sgl_per_token_quant_fp8` | quant_gemm | quant_fp8 | 4.4% | random_high | yes |
| `ring_25_1t__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 3.6% | random_high | role |
| `ring_25_1t__void_moe_sum_reduce_warp_per_tok` | moe | void_moe_sum_reduce_warp_per_tok | 3.3% | random_high | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 31.4%
- kernel_cutlass_kernel_flashinfernormkernelsfused_add_rm (gemm, comm): up to 27.8%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 16.0%
- void at::native::unrolled_elementwise_kernel<at::native (memory_bound, comm): up to 4.0%
