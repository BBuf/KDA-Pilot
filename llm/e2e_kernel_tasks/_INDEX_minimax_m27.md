# minimax_m27 — e2e kernel task selection

- Model: `MiniMaxAI/MiniMax-M2.7` (tp=8)
- Cookbook cmd: `sglang serve --model-path MiniMaxAI/MiniMax-M2.7 --tp 8 --ep 8 --tool-call-parser minimax-m2 --reasoning-parser minimax-append-think`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `minimax_m27__fused_moe_triton` | moe | fused_moe_triton | 32.5% | random_high | role |
| `minimax_m27__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 12.6% | sharegpt_low | role |
| `minimax_m27__linear_gemm` | gemm | linear_gemm | 12.5% | random_mid | role |
| `minimax_m27__sglang_unified_attention_with_output` | attention | attention | 5.4% | sharegpt_high | yes |
| `minimax_m27__per_token_group_quant` | quant_gemm | per_token_group_quant | 4.8% | sharegpt_low | role |
| `minimax_m27__rmsnorm` | norm | rmsnorm | 3.9% | random_low | role |
| `minimax_m27__moe_align_block_size` | moe | moe_align_block_size | 3.6% | sharegpt_low | role |

## Dropped < 3.0%

- void_moe_sum_reduce_warp_per_tok: 2.1%

## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 17.2%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 10.9%
