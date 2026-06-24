# kimi_linear — e2e kernel task selection

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct` (tp=4)
- Cookbook cmd: `sglang serve --model-path moonshotai/Kimi-Linear-48B-A3B-Instruct --tp 4 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `kimi_linear__sglang_inplace_fused_experts` | moe | fused_moe_triton | 26.4% | sharegpt_high | yes |
| `kimi_linear__rmsnorm` | norm | rmsnorm | 26.0% | sharegpt_low | role |
| `kimi_linear__linear_gemm` | quant_gemm | linear_gemm | 16.5% | random_low | role |
| `kimi_linear__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 5.6% | random_low | role |
| `kimi_linear__activation` | other | activation | 3.4% | random_low | role |

## Dropped < 3.0%

- attention: 2.8%
- void_moe_sum_reduce_warp_per_tok: 2.5%
- causal_conv1d: 2.3%

## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 50.3%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 3.1%
- nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT (quant_gemm, comm): up to 2.7%
