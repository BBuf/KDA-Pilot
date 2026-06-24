# minimax_m25 — e2e kernel task selection

- Model: `MiniMaxAI/MiniMax-M2.5` (tp=8)
- Cookbook cmd: `sglang serve --model-path MiniMaxAI/MiniMax-M2.5 --tp 8 --ep 8 --reasoning-parser minimax-append-think`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `minimax_m25__fused_moe_triton` | moe | fused_moe_triton | 31.7% | random_high | role |
| `minimax_m25__linear_gemm` | quant_gemm | linear_gemm | 22.5% | sharegpt_low | role |
| `minimax_m25__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 10.8% | random_low | role |
| `minimax_m25__sglang_unified_attention_with_output` | attention | attention | 5.2% | sharegpt_high | yes |
| `minimax_m25__per_token_group_quant` | quant_gemm | per_token_group_quant | 4.2% | sharegpt_low | role |
| `minimax_m25__void_moe_sum_reduce_kernel_warp` | moe | void_moe_sum_reduce_kernel_warp | 3.3% | random_mid | role |
| `minimax_m25__moe_align_block_size` | moe | moe_align_block_size | 3.1% | sharegpt_low | role |
| `minimax_m25__rmsnorm` | norm | rmsnorm | 3.0% | sharegpt_mid | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 13.9%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 9.6%
