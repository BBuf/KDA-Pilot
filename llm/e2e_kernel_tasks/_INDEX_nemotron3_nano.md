# nemotron3_nano — e2e kernel task selection

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (tp=1)
- Cookbook cmd: `python3 -m sglang.launch_server --model-path nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 --trust-remote-code --max-running-requests 1024`
- Threshold: kept kernels with max GPU-time share `>= 3.0%` (non-comm, non-fused-MoE)

## Kept tasks (e2e-impactful)

| task | category | max % GPU | peak scenario | clean op |
|---|---|---:|---|---|
| `nemotron3_nano__sglang_nemotron_mamba2_with_output` | other | 55.8% | sharegpt_mid | yes |
| `nemotron3_nano__linear_gemm` | gemm | 26.7% | sharegpt_low | role |
| `nemotron3_nano__sglang_flashinfer_bmm_fp8` | gemm | 20.7% | random_mid | yes |
| `nemotron3_nano__sglang_unified_attention_with_output` | quant_gemm | 6.1% | sharegpt_mid | yes |
| `nemotron3_nano__fused_add_rmsnorm` | gemm | 4.4% | sharegpt_low | role |
| `nemotron3_nano__static_quant_fp8` | quant_gemm | 4.1% | sharegpt_low | role |

## Dropped: below 3.0% (not worth e2e)

- role:attention_prefill: 2.2%

## Excluded: comm / fused-MoE (not single-kernel optimizable)

- void moe::dev::finalize::finalizeKernel<moe::dev:: (moe, comm_or_fused_moe): up to 2.9%
- void moe::dev::routing::routingCustom::routingIndi (moe, comm_or_fused_moe): up to 2.7%
