# mistral_medium35 — e2e kernel task selection

- Model: `mistralai/Mistral-Medium-3.5-128B` (tp=2)
- Cookbook cmd: `sglang serve --model-path mistralai/Mistral-Medium-3.5-128B --tp 2 --reasoning-parser mistral --tool-call-parser mistral`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `mistral_medium35__sgl_kernel_fp8_scaled_mm` | gemm | linear_gemm | 63.5% | sharegpt_mid | yes |
| `mistral_medium35__attention` | attention | attention | 9.7% | random_high | role |
| `mistral_medium35__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 6.5% | random_mid | role |
| `mistral_medium35__quant_fp8` | quant_gemm | quant_fp8 | 3.5% | random_low | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- _ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUnivers (gemm, comm): up to 55.4%
- kernel_cutlass_kernel_flashinfernormkernelsfused_add_rm (gemm, comm): up to 17.6%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 17.0%
