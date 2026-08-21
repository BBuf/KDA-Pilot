# Capture provenance

## `bench/workloads.json`

| field | value |
| --- | --- |
| model | LiquidAI/LFM2.5-8B-A1B |
| serving args | `--trust-remote-code --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 1 |
| SGLang commit | `43226af` |
| torch / triton / transformers | 2.13.0+cu130 / 3.7.1 / 5.12.1 |
| GPU | NVIDIA B300 SXM6 AC |

### Capture-only modifiers

- --disable-cuda-graph (python-level ops are invisible inside a captured graph)
- tensors phase adds --disable-radix-cache (radix cache rewrites mamba/state pool rows outside the kernel call and breaks the state chain; shapes phase keeps radix ON so prefix-hit-driven chunk lengths stay realistic)

### Operating points walked

| group | phase | started (UTC) | GSM8K accuracy | output tok/s | mean TTFT |
| --- | --- | --- | ---: | ---: | ---: |
| `random_1k1k_cc1` | shapes | 11:45:36 | - | 59.42 | 78.67 |
| `random_1k1k_cc16` | shapes | 11:46:34 | - | 620.60 | 91.58 |
| `random_1k1k_cc256` | shapes | 11:47:27 | - | 4551.77 | 587.70 |
| `random_4k512_cc8` | shapes | 11:48:12 | - | 349.37 | 116.95 |
| `sharegpt_cc32` | shapes | 11:48:50 | - | 647.79 | 165.67 |
| `gsm8k_5shot_cc1` | shapes | 11:49:35 | 1.000 | - | - |
| `gsm8k_5shot_cc32` | shapes | 11:49:51 | 0.484 | - | - |
| `gsm8k_16shot_cc16` | shapes | 11:50:19 | 0.875 | - | - |
| `gsm8k_accuracy_200` | shapes | 11:50:40 | 0.365 | - | - |
| `gsm8k_5shot_cc1` | tensors | 11:58:30 | 1.000 | - | - |
| `gsm8k_16shot_cc16` | tensors | 11:58:45 | 0.875 | - | - |
| `random_1k1k_cc16` | tensors | 11:59:01 | - | 620.60 | 91.58 |

Workload sources:

- sglang.bench_serving --dataset-name random (cookbook operating points)
- sglang.bench_serving --dataset-name sharegpt
- benchmark/gsm8k/bench_sglang.py (real GSM8K, 2/5/16-shot, incl. a 200-question accuracy run)

## `bench/workloads_glm47_flash.json`

| field | value |
| --- | --- |
| model | zai-org/GLM-4.7-Flash |
| serving args | `--trust-remote-code --reasoning-parser glm45 --tool-call-parser glm47 --attention-backend triton --tp 1` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 4 |
| SGLang commit | `43226af` |
| torch / triton / transformers | 2.13.0+cu130 / 3.7.1 / 5.12.1 |
| GPU | NVIDIA B300 SXM6 AC |

### Capture-only modifiers

- --disable-cuda-graph (python-level ops are invisible inside a captured graph)
- tensors phase adds --disable-radix-cache (radix cache rewrites mamba/state pool rows outside the kernel call and breaks the state chain; shapes phase keeps radix ON so prefix-hit-driven chunk lengths stay realistic)

### Operating points walked

| group | command | GSM8K accuracy | output tok/s |
| --- | --- | ---: | ---: |
| `gsm8k_5shot_cc1` | `benchmark/gsm8k/bench_sglang.py --num-questions 4 --num-shots 5 --parallel 1` | 1.000 | - |
| `gsm8k_16shot_cc16` | `benchmark/gsm8k/bench_sglang.py --num-questions 16 --num-shots 16 --parallel 16` | 1.000 | - |
| `gsm8k_5shot_cc32` | `benchmark/gsm8k/bench_sglang.py --num-questions 32 --num-shots 5 --parallel 32` | 0.781 | - |
| `random_1k256_cc16` | `sglang.bench_serving --dataset-name random --random-input-len 1024 --random-output-len 256 --num-prompts 32 --max-concurrency 16` | - | 30.40 |

Every row in this file comes from one of these four groups; the accuracy column is the GSM8K score of the very run the tensors were taken from.
