# qwen3_coder — e2e kernel task selection

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` (tp=8)
- Cookbook cmd: `sglang serve --model-path Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --tp 8 --ep 8 --tool-call-parser qwen3_coder`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `qwen3_coder__fp8_bmm` | quant_gemm | fp8_bmm | 34.0% | random_high | role |
| `qwen3_coder__linear_gemm` | quant_gemm | linear_gemm | 18.1% | random_low | role |
| `qwen3_coder__per_token_group_quant` | quant_gemm | per_token_group_quant | 17.2% | random_low | role |
| `qwen3_coder__sglang_unified_attention_with_output` | attention | attention | 6.8% | sharegpt_high | yes |

## Dropped < 3.0%

- fused_add_rmsnorm: 3.0%

## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 22.6%
- ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelA (comm, comm): up to 16.3%
- void moe::dev::activation::activationDeepSeekKernel<moe (moe, fused_moe_trtllm): up to 10.6%
- bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x (quant_gemm, fused_moe_trtllm): up to 10.4%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64 (quant_gemm, fused_moe_trtllm): up to 5.1%
- void moe::dev::finalize::finalizeKernel<moe::dev::final (moe, fused_moe_trtllm): up to 2.6%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 2.4%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 2.2%
- void moe::dev::routing::routingCustom::routingIndicesBl (moe, fused_moe_trtllm): up to 2.2%
