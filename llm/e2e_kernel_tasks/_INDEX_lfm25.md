# lfm25 — e2e kernel task selection

- Model: `LiquidAI/LFM2.5-8B-A1B` (tp=1)
- Cookbook cmd: `sglang serve --model-path LiquidAI/LFM2.5-8B-A1B --tp 1 --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2`
- Threshold: kept kernels with max GPU-time share `>= 3.0%` (non-comm, non-fused-MoE)

## Kept tasks (e2e-impactful)

| task | category | max % GPU | peak scenario | clean op |
|---|---|---:|---|---|
| `lfm25__sglang_inplace_fused_experts` | moe | 50.5% | random_mid | yes |
| `lfm25__linear_gemm` | quant_gemm | 19.0% | random_low | role |
| `lfm25__rmsnorm` | gemm | 5.2% | random_low | role |
| `lfm25__sgl_kernel_moe_align_block_size` | moe | 5.1% | random_low | yes |
| `lfm25__sglang_run_activation_inplace` | other | 4.4% | random_high | yes |

## Dropped: below 3.0% (not worth e2e)

- role:attention_prefill: 2.5%

## Excluded: comm / fused-MoE (not single-kernel optimizable)

