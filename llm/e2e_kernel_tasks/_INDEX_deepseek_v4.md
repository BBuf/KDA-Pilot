# deepseek_v4 — e2e kernel task selection

- Model: `deepseek-ai/DeepSeek-V4-Flash` (tp=4)
- Cookbook cmd: `sglang serve --model-path deepseek-ai/DeepSeek-V4-Flash --tp 4 --moe-runner-backend flashinfer_mxfp4 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `deepseek_v4__sglang_deep_gemm_fp8_fp8_bf16_nt` | quant_gemm | linear_gemm | 15.9% | random_mid | yes |
| `deepseek_v4__mhc_post_tilelang_kernel` | other | mhc_post_tilelang_kernel | 4.2% | random_mid | role |
| `deepseek_v4__sgl_kernel_sparse_decode_fwd` | quant_gemm | attention | 4.1% | sharegpt_mid | yes |

## Dropped < 3.0%

- fp8_bmm: 2.7%

## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 47.2%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 36.2%
- mhc_post_tilelang_kernel (other, comm): up to 33.0%
- bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x8x512u (quant_gemm, comm): up to 2.2%
