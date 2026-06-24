# deepseek_v3 — e2e kernel task selection

- Model: `deepseek-ai/DeepSeek-V3` (tp=8)
- Cookbook cmd: `sglang serve --model-path deepseek-ai/DeepSeek-V3 --tp 8 --speculative-algorithm EAGLE`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `deepseek_v3__linear_gemm` | quant_gemm | linear_gemm | 19.7% | random_low | role |
| `deepseek_v3__sglang_flashinfer_dsv3_router_gemm` | gemm | attention | 16.4% | sharegpt_low | yes |
| `deepseek_v3__fp8_bmm` | quant_gemm | fp8_bmm | 7.4% | random_mid | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 35.0%
- bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x (quant_gemm, fused_moe_trtllm): up to 11.2%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64 (quant_gemm, fused_moe_trtllm): up to 5.2%
- bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x (quant_gemm, fused_moe_trtllm): up to 4.5%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64 (quant_gemm, fused_moe_trtllm): up to 3.8%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8 (quant_gemm, fused_moe_trtllm): up to 2.5%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 2.1%
- bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_ (quant_gemm, fused_moe_trtllm): up to 2.0%
