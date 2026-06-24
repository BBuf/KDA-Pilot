# deepseek_v31 — e2e kernel task selection

- Model: `deepseek-ai/DeepSeek-V3.1` (tp=8)
- Cookbook cmd: `sglang serve --model-path deepseek-ai/DeepSeek-V3.1 --tp 8 --speculative-algorithm EAGLE --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `deepseek_v31__linear_gemm` | quant_gemm | linear_gemm | 19.2% | random_low | role |
| `deepseek_v31__sglang_flashinfer_dsv3_router_gemm` | gemm | attention | 16.8% | sharegpt_low | yes |
| `deepseek_v31__fp8_bmm` | quant_gemm | fp8_bmm | 12.1% | sharegpt_mid | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 35.3%
- bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x (quant_gemm, fused_moe_trtllm): up to 11.7%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64 (quant_gemm, fused_moe_trtllm): up to 6.7%
- bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x (quant_gemm, fused_moe_trtllm): up to 4.2%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64 (quant_gemm, fused_moe_trtllm): up to 3.6%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 2.9%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8 (quant_gemm, fused_moe_trtllm): up to 2.2%
