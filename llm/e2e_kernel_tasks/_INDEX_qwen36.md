# qwen36 — e2e kernel task selection

- Model: `Qwen/Qwen3.6-35B-A3B-FP8` (tp=1)
- Cookbook cmd: `sglang serve --model-path Qwen/Qwen3.6-35B-A3B-FP8 --reasoning-parser qwen3 --tool-call-parser qwen3_coder --speculative-algorithm EAGLE --speculative-num-steps 3 --speculative-eagle-topk 1`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `qwen36__sglang_deep_gemm_fp8_fp8_bf16_nt` | quant_gemm | linear_gemm | 26.3% | sharegpt_low | yes |
| `qwen36__fp8_bmm` | quant_gemm | fp8_bmm | 15.9% | random_mid | role |
| `qwen36__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 3.5% | sharegpt_low | role |

## Dropped < 3.0%

- fused_qkvzba_split_reshape_cat_c: 2.0%

## Excluded (comm / trtllm fused-MoE)

- bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x (quant_gemm, fused_moe_trtllm): up to 12.8%
- bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x (quant_gemm, fused_moe_trtllm): up to 11.8%
- bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_ (quant_gemm, fused_moe_trtllm): up to 10.8%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8 (quant_gemm, fused_moe_trtllm): up to 7.8%
- void moe::dev::activation::activationDeepSeekKernel<moe (moe, fused_moe_trtllm): up to 6.9%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64 (quant_gemm, fused_moe_trtllm): up to 6.1%
- bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x (quant_gemm, fused_moe_trtllm): up to 3.1%
- void moe::dev::finalize::finalizeKernel<moe::dev::final (moe, fused_moe_trtllm): up to 2.6%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 2.1%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64 (quant_gemm, fused_moe_trtllm): up to 2.1%
- void moe::dev::routing::routingCustom::routingIndicesBl (moe, fused_moe_trtllm): up to 2.0%
