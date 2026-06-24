# ling_26 — e2e kernel task selection

- Model: `inclusionAI/Ling-2.6-flash` (tp=4)
- Cookbook cmd: `sglang serve --model-path inclusionAI/Ling-2.6-flash --tp 4 --trust-remote-code`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `ling_26__sglang_inplace_fused_experts` | moe | fused_moe_triton | 32.3% | random_mid | yes |
| `ling_26__fused_add_rmsnorm` | gemm | fused_add_rmsnorm | 18.0% | random_high | role |
| `ling_26__linear_gemm` | gemm | linear_gemm | 12.1% | random_mid | role |

## Dropped < 3.0%


## Excluded (comm / trtllm fused-MoE)

- void (anonymous namespace)::all_reduce_one_shot_push_ke (comm, comm): up to 33.9%
- kernel_cutlass_kernel_flashinfernormkernelsfused_add_rm (gemm, comm): up to 29.9%
- void (anonymous namespace)::all_reduce_two_shot_kernel< (comm, comm): up to 18.5%
