# deepseek_r1_fp4 — e2e kernel task selection

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2` (tp=8)
- Cookbook cmd: `sglang serve --model-path nvidia/DeepSeek-R1-0528-FP4-v2 --tp 8 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `deepseek_r1_fp4__sgl_kernel_dsv3_fused_a_gemm` | quant_gemm | linear_gemm | 42.4% | random_high | yes |
| `deepseek_r1_fp4__sglang_flashinfer_dsv3_router_gemm` | gemm | attention | 19.1% | sharegpt_low | yes |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void flashinfer::trtllm_allreduce_fusion::allreduce_fus (comm, comm): up to 34.5%
- _ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUnivers (quant_gemm, comm): up to 3.6%
- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 2.3%
