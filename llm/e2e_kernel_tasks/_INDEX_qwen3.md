# qwen3 — e2e kernel task selection

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507` (tp=8)
- Cookbook cmd: `sglang serve --model-path Qwen/Qwen3-235B-A22B-Instruct-2507 --tp 8`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `qwen3__fp8_bmm` | other | fp8_bmm | 32.0% | random_mid | role |
| `qwen3__linear_gemm` | quant_gemm | linear_gemm | 28.8% | sharegpt_low | role |
| `qwen3__sglang_unified_attention_with_output` | attention | attention | 7.8% | sharegpt_high | yes |
| `qwen3__void_cublas_lt_split_kreduce_ker` | gemm | void_cublas_lt_split_kreduce_ker | 5.4% | random_low | role |
| `qwen3__rmsnorm` | norm | rmsnorm | 3.9% | random_mid | role |

## Dropped < 3.0%

- rope: 2.4%

## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 20.9%
- ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelA (comm, comm): up to 17.8%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 4.5%
- void moe::dev::finalize::finalizeKernel<moe::dev::final (moe, fused_moe_trtllm): up to 4.3%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 4.1%
- void moe::dev::routing::routingCustom::routingIndicesBl (moe, fused_moe_trtllm): up to 2.9%
