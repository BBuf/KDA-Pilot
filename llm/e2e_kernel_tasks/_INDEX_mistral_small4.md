# mistral_small4 — e2e kernel task selection

- Model: `mistralai/Mistral-Small-4-119B-2603` (tp=1)
- Cookbook cmd: `sglang serve --model-path mistralai/Mistral-Small-4-119B-2603 --tp 1 --reasoning-parser mistral --tool-call-parser mistral`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `mistral_small4__fp8_bmm` | other | fp8_bmm | 42.3% | random_high | role |
| `mistral_small4__sgl_kernel_fp8_scaled_mm` | gemm | linear_gemm | 28.4% | sharegpt_low | yes |
| `mistral_small4__attention` | attention | attention | 8.3% | sharegpt_mid | role |
| `mistral_small4__quant_fp8` | quant_gemm | quant_fp8 | 7.1% | sharegpt_low | role |
| `mistral_small4__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 3.8% | sharegpt_low | role |

## Dropped < 3.0%

- attention_mla: 2.4%

## Excluded (comm / trtllm fused-MoE)

- bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x8x256u2_s6_et1 (other, fused_moe_trtllm): up to 24.8%
- bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x64x256u2_s5_et (other, fused_moe_trtllm): up to 15.9%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x256u2_s6_et128x8_m128 (other, fused_moe_trtllm): up to 13.7%
- bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x64x256_s5_et12 (other, fused_moe_trtllm): up to 11.0%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s8_et128x64_m2 (other, fused_moe_trtllm): up to 9.1%
- bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x8x256_s6_et128 (other, fused_moe_trtllm): up to 7.0%
- bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x32x256u2_s5_et (other, fused_moe_trtllm): up to 5.8%
- _static_quant_fp8 (quant_gemm, fused_moe_trtllm): up to 3.1%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x256u2_s5_et128x32_m1 (other, fused_moe_trtllm): up to 3.0%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128_s8_et128x64_m256 (other, fused_moe_trtllm): up to 3.0%
- kernel_cutlass_kernel_flashinfernormkernelsfused_add_rm (gemm, fused_moe_trtllm): up to 3.0%
- void moe::dev::finalize::finalizeKernel<moe::dev::final (moe, fused_moe_trtllm): up to 2.5%
