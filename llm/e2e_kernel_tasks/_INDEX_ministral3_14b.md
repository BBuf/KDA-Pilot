# ministral3_14b — e2e kernel task selection

- Model: `mistralai/Ministral-3-14B-Instruct-2512` (tp=1)
- Cookbook cmd: `sglang serve --model-path mistralai/Ministral-3-14B-Instruct-2512 --tp 1 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `ministral3_14b__sgl_kernel_fp8_scaled_mm` | gemm | linear_gemm | 69.4% | random_mid | yes |
| `ministral3_14b__attention` | attention | attention | 18.5% | sharegpt_high | role |
| `ministral3_14b__quant_fp8` | quant_gemm | quant_fp8 | 6.7% | random_low | role |
| `ministral3_14b__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 5.7% | random_low | role |
| `ministral3_14b__sglang_run_activation_inplace` | other | activation | 5.3% | random_mid | yes |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

