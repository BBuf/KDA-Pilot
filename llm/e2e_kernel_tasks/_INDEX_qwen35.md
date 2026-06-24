# qwen35 — e2e kernel task selection

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` (tp=4)
- Cookbook cmd: `sglang serve --model-path nvidia/Qwen3.5-397B-A17B-NVFP4 --tp 4 --reasoning-parser qwen3 --tool-call-parser qwen3_coder`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `qwen35__linear_gemm` | quant_gemm | linear_gemm | 40.7% | sharegpt_low | role |
| `qwen35__fp8_bmm` | quant_gemm | fp8_bmm | 16.0% | random_mid | role |
| `qwen35__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 3.3% | random_high | role |

## Dropped < 3.0%

- rmsnorm: 2.6%

## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 41.7%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 6.1%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 3.4%
- bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x128x25 (quant_gemm, comm): up to 2.8%
