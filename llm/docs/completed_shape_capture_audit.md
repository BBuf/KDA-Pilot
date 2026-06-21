# Completed Shape Capture Audit

This audit checks for shape-capture illusions in the completed B200 LLM sweep.
Only external-id-bound non-empty shape samples are considered strong enough
to seed optimization task definitions.

| Model slug | Problem scenes | Weak rows | Empty rows | Notes |
|---|---|---:|---:|---|
| `deepseek_math_v2` | sharegpt_low: weak/empty only | 15 | 22 | empty-shape rows excluded |
| `deepseek_r1_fp4` | none | 26 | 0 | weak fallback rows excluded |
| `deepseek_v3` | none | 9 | 0 | weak fallback rows excluded |
| `deepseek_v31` | none | 11 | 0 | weak fallback rows excluded |
| `deepseek_v32` | sharegpt_low: weak/empty only | 29 | 16 | empty-shape rows excluded |
| `deepseek_v4` | none | 9 | 0 | weak fallback rows excluded |
| `ernie45` | random_low: weak/empty only | 20 | 11 | empty-shape rows excluded |
| `gemma4` | none | 34 | 0 | weak fallback rows excluded |
| `glm_47_flash` | random_low: weak/empty only | 13 | 3 | empty-shape rows excluded |
| `glm_5` | sharegpt_low: weak/empty only | 39 | 11 | empty-shape rows excluded |
| `glm_51` | none | 10 | 0 | weak fallback rows excluded |
| `glm_52` | sharegpt_mid: weak/empty only, sharegpt_high: weak/empty only | 43 | 0 | weak fallback rows excluded |
| `gpt_oss_120b` | sharegpt_low: weak/empty only | 23 | 20 | empty-shape rows excluded |
| `hunyuan3_preview` | none | 13 | 0 | weak fallback rows excluded |
| `inclusion_ring26` | none | 12 | 0 | weak fallback rows excluded |
| `intern_s2_preview` | none | 9 | 0 | weak fallback rows excluded |
| `kimi_k2` | sharegpt_low: weak/empty only | 43 | 0 | weak fallback rows excluded |
| `kimi_k25` | none | 26 | 0 | weak fallback rows excluded |
| `kimi_k26` | none | 27 | 0 | weak fallback rows excluded |
| `kimi_k27_code` | none | 26 | 0 | weak fallback rows excluded |
| `kimi_linear` | random_mid: zero row | 14 | 0 | weak fallback rows excluded |
| `laguna_m1` | none | 22 | 0 | weak fallback rows excluded |
| `lfm25` | none | 15 | 0 | weak fallback rows excluded |
| `ling_26` | none | 11 | 0 | weak fallback rows excluded |
| `llada_21_flash` | random_mid: weak/empty only, random_high: weak/empty only, sharegpt_low: weak/empty only, sharegpt_mid: weak/empty only, sharegpt_high: weak/empty only | 41 | 0 | weak fallback rows excluded |
| `llada_21_mini` | random_mid: weak/empty only, random_high: weak/empty only, sharegpt_low: weak/empty only, sharegpt_mid: weak/empty only, sharegpt_high: weak/empty only | 47 | 0 | weak fallback rows excluded |
| `mimo_v2_flash` | none | 0 | 0 | all retained rows have promoted shapes |
| `minimax_m2` | none | 8 | 0 | weak fallback rows excluded |
| `minimax_m25` | sharegpt_low: weak/empty only | 11 | 9 | empty-shape rows excluded |
| `minimax_m27` | none | 14 | 5 | empty-shape rows excluded |
| `minimax_m3` | sharegpt_low: weak/empty only | 12 | 18 | empty-shape rows excluded |
| `mistral_small4` | none | 39 | 0 | weak fallback rows excluded |
| `nemotron3_nano` | random_low: weak/empty only | 37 | 0 | weak fallback rows excluded |
| `nemotron3_super` | none | 24 | 0 | weak fallback rows excluded |
| `nemotron3_ultra` | none | 32 | 0 | weak fallback rows excluded |
| `poolside_laguna_xs2` | sharegpt_low: weak/empty only | 14 | 4 | empty-shape rows excluded |
| `qwen3` | none | 54 | 0 | weak fallback rows excluded |
| `qwen35` | none | 21 | 0 | weak fallback rows excluded |
| `qwen36` | none | 18 | 0 | weak fallback rows excluded |
| `qwen3_coder` | none | 32 | 0 | weak fallback rows excluded |
| `qwen3_coder_next` | none | 28 | 0 | weak fallback rows excluded |
| `qwen3_next` | none | 10 | 0 | weak fallback rows excluded |
| `ring_25_1t` | none | 11 | 0 | weak fallback rows excluded |
| `step35_flash` | none | 12 | 0 | weak fallback rows excluded |
| `step_37_flash` | none | 8 | 0 | weak fallback rows excluded |
