# minimax_m2 — e2e kernel task selection

- Model: `MiniMaxAI/MiniMax-M2` (tp=4)
- Cookbook cmd: `sglang serve --model-path MiniMaxAI/MiniMax-M2 --tp 4 --reasoning-parser minimax-append-think --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `minimax_m2__fused_moe_triton` | moe | fused_moe_triton | 48.1% | random_high | role |
| `minimax_m2__linear_gemm` | quant_gemm | linear_gemm | 25.5% | random_low | role |
| `minimax_m2__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 6.2% | random_low | role |
| `minimax_m2__sglang_unified_attention_with_output` | attention | attention | 5.7% | sharegpt_high | yes |
| `minimax_m2__per_token_group_quant` | quant_gemm | per_token_group_quant | 4.7% | random_low | role |

## Dropped < 3.0%

- void_moe_sum_reduce_kernel_warp: 2.8%
- rmsnorm: 2.8%

## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 7.5%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 3.5%
