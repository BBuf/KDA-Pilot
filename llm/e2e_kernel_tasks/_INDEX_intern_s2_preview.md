# intern_s2_preview — e2e kernel task selection

- Model: `internlm/Intern-S2-Preview` (tp=8)
- Cookbook cmd: `sglang serve --model-path internlm/Intern-S2-Preview --tp 8 --reasoning-parser qwen3 --tool-call-parser qwen3_coder`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `intern_s2_preview__linear_gemm` | quant_gemm | linear_gemm | 42.0% | random_low | role |
| `intern_s2_preview__fp8_bmm` | other | fp8_bmm | 9.0% | random_high | role |

## Dropped < 3.0%

- fused_add_rmsnorm: 2.2%

## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 39.9%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 2.8%
- bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128_s5_et128 (other, comm): up to 2.3%
