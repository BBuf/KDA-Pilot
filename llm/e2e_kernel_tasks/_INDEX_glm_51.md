# glm_51 — e2e kernel task selection

- Model: `zai-org/GLM-5.1-FP8` (tp=8)
- Cookbook cmd: `sglang serve --model-path zai-org/GLM-5.1-FP8 --tp 8 --tool-call-parser glm47 --reasoning-parser glm45`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `glm_51__sglang_deep_gemm_fp8_fp8_bf16_nt` | quant_gemm | linear_gemm | 20.6% | random_low | yes |
| `glm_51__fp8_bmm` | quant_gemm | fp8_bmm | 19.0% | random_mid | role |
| `glm_51__attention` | attention | attention | 3.8% | sharegpt_mid | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 36.7%
- void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMM (quant_gemm, comm): up to 3.6%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 2.8%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 2.7%
- bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8 (quant_gemm, fused_moe_trtllm): up to 2.1%
