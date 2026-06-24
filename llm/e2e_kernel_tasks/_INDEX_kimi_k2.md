# kimi_k2 — e2e kernel task selection

- Model: `moonshotai/Kimi-K2-Instruct` (tp=8)
- Cookbook cmd: `sglang serve --model-path moonshotai/Kimi-K2-Instruct --tp 8 --tool-call-parser kimi_k2`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `kimi_k2__fp8_bmm` | quant_gemm | fp8_bmm | 38.5% | sharegpt_high | role |
| `kimi_k2__sglang_deep_gemm_fp8_fp8_bf16_nt` | quant_gemm | linear_gemm | 23.1% | sharegpt_low | yes |
| `kimi_k2__per_token_group_quant` | quant_gemm | per_token_group_quant | 12.6% | random_low | role |
| `kimi_k2__sglang_unified_attention_with_output` | attention | attention | 9.5% | sharegpt_high | yes |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 11.1%
- bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x (quant_gemm, fused_moe_trtllm): up to 11.0%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64 (quant_gemm, fused_moe_trtllm): up to 7.4%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64 (quant_gemm, fused_moe_trtllm): up to 6.4%
- bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x (quant_gemm, fused_moe_trtllm): up to 6.2%
- void moe::dev::routing::routingCustom::routingIndicesBl (moe, fused_moe_trtllm): up to 3.6%
- void moe::dev::finalize::finalizeKernel<moe::dev::final (moe, fused_moe_trtllm): up to 2.9%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 2.5%
- void moe::dev::activation::activationDeepSeekKernel<moe (moe, fused_moe_trtllm): up to 2.3%
- kernel_cutlass_kernel_flashinfernormkernelsfused_add_rm (gemm, fused_moe_trtllm): up to 2.1%
