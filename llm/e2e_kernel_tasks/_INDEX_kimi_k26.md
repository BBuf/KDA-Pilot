# kimi_k26 — e2e kernel task selection

- Model: `moonshotai/Kimi-K2.6` (tp=8)
- Cookbook cmd: `sglang serve --model-path moonshotai/Kimi-K2.6 --tp 8 --reasoning-parser kimi_k2 --tool-call-parser kimi_k2`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `kimi_k26__sgl_kernel_dsv3_fused_a_gemm` | quant_gemm | linear_gemm | 39.0% | random_low | yes |
| `kimi_k26__fp8_bmm` | quant_gemm | fp8_bmm | 21.0% | random_high | role |

## Dropped < 3.0%

- attention: 2.7%

## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 37.3%
- bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128 (quant_gemm, comm): up to 4.0%
