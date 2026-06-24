# gemma4 — e2e kernel task selection

- Model: `google/gemma-4-26B-A4B-it` (tp=1)
- Cookbook cmd: `sglang serve --model-path google/gemma-4-26B-A4B-it --reasoning-parser gemma4 --tool-call-parser gemma4`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `gemma4__sglang_inplace_fused_experts` | moe | fused_moe_triton | 50.8% | random_high | yes |
| `gemma4__linear_gemm` | quant_gemm | linear_gemm | 29.0% | sharegpt_low | role |
| `gemma4__rmsnorm` | gemm | rmsnorm | 18.9% | sharegpt_low | role |
| `gemma4__attention` | attention | attention | 12.0% | random_high | role |

## Dropped < 3.0%

- fused_add_rmsnorm: 2.2%
- activation: 2.2%

## Excluded (comm / trtllm fused-MoE)

