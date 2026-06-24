# deepseek_math_v2 — e2e kernel task selection

- Model: `deepseek-ai/DeepSeek-Math-V2` (tp=8)
- Cookbook cmd: `sglang serve --model-path deepseek-ai/DeepSeek-Math-V2 --tp 8 --ep 8 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `deepseek_math_v2__sglang_deep_gemm_fp8_fp8_bf16_nt` | quant_gemm | linear_gemm | 26.1% | random_low | yes |
| `deepseek_math_v2__fp8_bmm` | quant_gemm | fp8_bmm | 24.7% | random_high | role |
| `deepseek_math_v2__sglang_unified_attention_with_output` | gemm | attention | 11.8% | sharegpt_low | yes |
| `deepseek_math_v2__void_anonymous_namespace_fast_ha` | other | void_anonymous_namespace_fast_ha | 3.8% | sharegpt_mid | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 22.5%
- bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x (quant_gemm, fused_moe_trtllm): up to 7.2%
- void moe::dev::activation::activationDeepSeekKernel<moe (moe, fused_moe_trtllm): up to 4.8%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64 (quant_gemm, fused_moe_trtllm): up to 3.9%
