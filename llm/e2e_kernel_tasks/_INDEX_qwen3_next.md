# qwen3_next — e2e kernel task selection

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct` (tp=8)
- Cookbook cmd: `sglang serve --model-path Qwen/Qwen3-Next-80B-A3B-Instruct --tp 8`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `qwen3_next__linear_gemm` | quant_gemm | linear_gemm | 44.3% | sharegpt_low | role |
| `qwen3_next__rmsnorm` | gemm | rmsnorm | 6.8% | random_mid | role |
| `qwen3_next__fp8_bmm` | other | fp8_bmm | 5.9% | random_high | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 44.3%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 6.8%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 2.3%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 2.1%
