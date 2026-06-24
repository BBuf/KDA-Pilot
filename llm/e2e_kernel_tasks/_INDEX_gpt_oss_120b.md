# gpt_oss_120b — e2e kernel task selection

- Model: `openai/gpt-oss-120b` (tp=8)
- Cookbook cmd: `sglang serve --model-path openai/gpt-oss-120b --tp 8`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `gpt_oss_120b__linear_gemm` | quant_gemm | linear_gemm | 29.8% | sharegpt_low | role |
| `gpt_oss_120b__fp8_bmm` | quant_gemm | fp8_bmm | 15.8% | random_mid | role |
| `gpt_oss_120b__sglang_unified_attention_with_output` | attention | attention | 8.4% | sharegpt_low | yes |
| `gpt_oss_120b__rmsnorm` | norm | rmsnorm | 7.0% | random_mid | role |

## Dropped < 3.0%

- rope: 2.4%

## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 27.7%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 11.9%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 3.5%
- void moe::dev::finalize::finalizeKernel<moe::dev::final (moe, fused_moe_trtllm): up to 3.0%
- void moe::dev::routing::routingCustom::routingIndicesCl (moe, fused_moe_trtllm): up to 2.9%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 2.8%
- void moe::dev::routing::routingCustom::routingIndicesBl (moe, fused_moe_trtllm): up to 2.6%
