# ernie45 — e2e kernel task selection

- Model: `baidu/ERNIE-4.5-21B-A3B-PT` (tp=1)
- Cookbook cmd: `sglang serve --model-path baidu/ERNIE-4.5-21B-A3B-PT --tp 1`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `ernie45__fused_moe_triton` | moe | fused_moe_triton | 65.0% | random_high | role |
| `ernie45__linear_gemm` | quant_gemm | linear_gemm | 29.1% | sharegpt_low | role |
| `ernie45__sglang_unified_attention_with_output` | attention | attention | 8.0% | random_high | yes |
| `ernie45__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 4.5% | sharegpt_low | role |

## Dropped < 3.0%

- rope: 2.4%
- rmsnorm: 2.2%
- moe_align_block_size: 2.2%

## Excluded (comm / trtllm fused-MoE)

