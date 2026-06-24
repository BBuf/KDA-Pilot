# glm_5 — e2e kernel task selection

- Model: `nvidia/GLM-5-NVFP4` (tp=4)
- Cookbook cmd: `sglang serve --model-path nvidia/GLM-5-NVFP4 --tp 4 --quantization modelopt_fp4 --kv-cache-dtype fp8_e4m3`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `glm_5__linear_gemm` | quant_gemm | linear_gemm | 33.9% | sharegpt_low | role |
| `glm_5__fp8_bmm` | quant_gemm | fp8_bmm | 19.5% | random_mid | role |
| `glm_5__sglang_flashinfer_fp4_quantize` | attention | attention | 13.1% | sharegpt_high | yes |
| `glm_5__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 4.1% | random_high | role |
| `glm_5__void_anonymous_namespace_fast_ha` | other | void_anonymous_namespace_fast_ha | 3.7% | sharegpt_high | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 19.4%
- ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelA (comm, comm): up to 14.7%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 4.9%
