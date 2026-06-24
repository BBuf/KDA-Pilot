# nemotron3_super — e2e kernel task selection

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` (tp=4)
- Cookbook cmd: `sglang serve --model-path nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 --tp 4 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `nemotron3_super__sglang_nemotron_mamba2_with_output` | other | mamba2_ssm | 27.3% | random_high | yes |
| `nemotron3_super__linear_gemm` | quant_gemm | linear_gemm | 18.8% | random_low | role |
| `nemotron3_super__fp8_bmm` | other | fp8_bmm | 18.0% | random_high | role |
| `nemotron3_super__rmsnorm` | norm | rmsnorm | 8.8% | random_low | role |
| `nemotron3_super__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 3.6% | random_low | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 35.6%
- ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelA (comm, comm): up to 10.4%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 6.9%
- bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et1 (other, comm): up to 5.8%
- void moe::dev::routing::routingCustom::routingIndicesBl (moe, fused_moe_trtllm): up to 3.0%
- void moe::dev::finalize::finalizeKernel<moe::dev::final (moe, fused_moe_trtllm): up to 2.5%
- void moe::dev::finalize::finalizeKernelVecLoad<moe::dev (moe, fused_moe_trtllm): up to 2.2%
