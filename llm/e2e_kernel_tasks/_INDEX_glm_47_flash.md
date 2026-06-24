# glm_47_flash — e2e kernel task selection

- Model: `zai-org/GLM-4.7-Flash` (tp=1)
- Cookbook cmd: `sglang serve --model-path zai-org/GLM-4.7-Flash --tp 1 --attention-backend triton --reasoning-parser glm45 --tool-call-parser glm47`
- Kept: max GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `glm_47_flash__sglang_unified_attention_with_output` | other | attention | 75.3% | sharegpt_mid | yes |
| `glm_47_flash__sglang_inplace_fused_experts` | moe | fused_moe_triton | 30.4% | random_mid | yes |
| `glm_47_flash__linear_gemm` | quant_gemm | linear_gemm | 15.6% | random_low | role |

## Dropped < 3.0%

- fused_add_rmsnorm: 2.8%

## Excluded (comm / trtllm fused-MoE)

