# Completed LLM Model Task Index

- Generated at: `2026-06-21T00:45:47Z`
- Completed model folders audited: `45`
- Promoted task candidates: `465`
- Strong rows: `1005`
- Weak fallback rows not promoted: `972`
- Empty-shape rows not promoted: `119`

## Category Counts

| Category | Task candidates |
|---|---:|
| `attention` | 19 |
| `comm` | 80 |
| `gemm` | 85 |
| `memory_bound` | 8 |
| `moe` | 48 |
| `moe_comm` | 2 |
| `norm` | 9 |
| `other` | 34 |
| `quant_gemm` | 180 |

## Models

| Model slug | Model | Tasks | Strong rows | Weak rows | Empty rows | Scene caveats |
|---|---|---:|---:|---:|---:|---|
| `deepseek_math_v2` | `deepseek-ai/DeepSeek-Math-V2` | 7 | 9 | 15 | 22 | weak/empty only: `sharegpt_low` |
| `deepseek_r1_fp4` | `nvidia/DeepSeek-R1-0528-FP4-v2` | 11 | 26 | 26 | 0 | none |
| `deepseek_v3` | `deepseek-ai/DeepSeek-V3` | 13 | 29 | 9 | 0 | none |
| `deepseek_v31` | `deepseek-ai/DeepSeek-V3.1` | 10 | 25 | 11 | 0 | none |
| `deepseek_v32` | `nvidia/DeepSeek-V3.2-NVFP4` | 13 | 18 | 29 | 16 | weak/empty only: `sharegpt_low` |
| `deepseek_v4` | `deepseek-ai/DeepSeek-V4-Flash` | 3 | 11 | 9 | 0 | none |
| `ernie45` | `baidu/ERNIE-4.5-21B-A3B-PT` | 2 | 5 | 20 | 11 | weak/empty only: `random_low` |
| `gemma4` | `google/gemma-4-26B-A4B-it` | 9 | 17 | 34 | 0 | none |
| `glm_47_flash` | `zai-org/GLM-4.7-Flash` | 2 | 5 | 13 | 3 | weak/empty only: `random_low` |
| `glm_5` | `nvidia/GLM-5-NVFP4` | 8 | 13 | 39 | 11 | weak/empty only: `sharegpt_low` |
| `glm_51` | `zai-org/GLM-5.1-FP8` | 9 | 21 | 10 | 0 | none |
| `glm_52` | `zai-org/GLM-5.2-FP8` | 5 | 7 | 43 | 0 | weak/empty only: `sharegpt_mid`, `sharegpt_high` |
| `gpt_oss_120b` | `openai/gpt-oss-120b` | 22 | 27 | 23 | 20 | weak/empty only: `sharegpt_low` |
| `hunyuan3_preview` | `tencent/Hy3-preview` | 9 | 18 | 13 | 0 | none |
| `inclusion_ring26` | `inclusionAI/Ring-2.6-1T` | 9 | 30 | 12 | 0 | none |
| `intern_s2_preview` | `internLM/Intern-S2-Preview` | 7 | 20 | 9 | 0 | none |
| `kimi_k2` | `moonshotai/Kimi-K2-Instruct` | 12 | 16 | 43 | 0 | weak/empty only: `sharegpt_low` |
| `kimi_k25` | `moonshotai/Kimi-K2.5` | 8 | 20 | 26 | 0 | none |
| `kimi_k26` | `moonshotai/Kimi-K2.6` | 8 | 20 | 27 | 0 | none |
| `kimi_k27_code` | `moonshotai/Kimi-K2.7-Code` | 9 | 20 | 26 | 0 | none |
| `kimi_linear` | `moonshotai/Kimi-Linear-48B-A3B-Instruct` | 8 | 18 | 14 | 0 | zero rows: `random_mid` |
| `laguna_m1` | `poolside/Laguna-M.1-NVFP4` | 15 | 29 | 22 | 0 | none |
| `lfm25` | `LiquidAI/LFM2.5-8B-A1B` | 6 | 20 | 15 | 0 | none |
| `ling_26` | `inclusionAI/Ling-2.6-flash` | 8 | 20 | 11 | 0 | none |
| `llada_21_flash` | `inclusionAI/LLaDA2.1-flash` | 7 | 7 | 41 | 0 | weak/empty only: `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `llada_21_mini` | `inclusionAI/LLaDA2.1-mini` | 7 | 7 | 47 | 0 | weak/empty only: `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `mimo_v2_flash` | `XiaomiMiMo/MiMo-V2-Flash` | 2 | 7 | 0 | 0 | none |
| `minimax_m2` | `MiniMaxAI/MiniMax-M2` | 15 | 43 | 8 | 0 | none |
| `minimax_m25` | `MiniMaxAI/MiniMax-M2.5` | 17 | 39 | 11 | 9 | weak/empty only: `sharegpt_low` |
| `minimax_m27` | `MiniMaxAI/MiniMax-M2.7` | 16 | 40 | 14 | 5 | none |
| `minimax_m3` | `MiniMaxAI/MiniMax-M3-MXFP8` | 8 | 16 | 12 | 18 | weak/empty only: `sharegpt_low` |
| `mistral_small4` | `mistralai/Mistral-Small-4-119B-2603` | 14 | 29 | 39 | 0 | none |
| `nemotron3_nano` | `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` | 10 | 27 | 37 | 0 | weak/empty only: `random_low` |
| `nemotron3_super` | `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` | 15 | 43 | 24 | 0 | none |
| `nemotron3_ultra` | `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` | 14 | 27 | 32 | 0 | none |
| `poolside_laguna_xs2` | `poolside/Laguna-XS.2-FP8` | 21 | 37 | 14 | 4 | weak/empty only: `sharegpt_low` |
| `qwen3` | `Qwen/Qwen3-235B-A22B-Instruct-2507` | 15 | 26 | 54 | 0 | none |
| `qwen35` | `nvidia/Qwen3.5-397B-A17B-NVFP4` | 12 | 29 | 21 | 0 | none |
| `qwen36` | `Qwen/Qwen3.6-35B-A3B-FP8` | 13 | 28 | 18 | 0 | none |
| `qwen3_coder` | `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` | 22 | 38 | 32 | 0 | none |
| `qwen3_coder_next` | `Qwen/Qwen3-Coder-Next` | 10 | 26 | 28 | 0 | none |
| `qwen3_next` | `Qwen/Qwen3-Next-80B-A3B-Instruct` | 7 | 22 | 10 | 0 | none |
| `ring_25_1t` | `inclusionAI/Ring-2.5-1T` | 12 | 29 | 11 | 0 | none |
| `step35_flash` | `stepfun-ai/Step-3.5-Flash` | 6 | 24 | 12 | 0 | none |
| `step_37_flash` | `stepfun-ai/Step-3.7-Flash-NVFP4` | 9 | 17 | 8 | 0 | none |
