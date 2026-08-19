# Capture provenance

## `bench/workloads.json`

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

## `bench/workloads_qwen3_next_secondary.json`

| field | value |
| --- | --- |
| model | Qwen/Qwen3-Next-80B-A3B-Instruct |
| serving args | `--trust-remote-code --attention-backend triton --tp 8` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 0,1,2,3,4,5,6,7 |
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
| `gsm8k_5shot_cc32` | `benchmark/gsm8k/bench_sglang.py --num-questions 32 --num-shots 5 --parallel 32` | 0.969 | - |
| `random_1k256_cc16` | `sglang.bench_serving --dataset-name random --random-input-len 1024 --random-output-len 256 --num-prompts 32 --max-concurrency 16` | - | 25.21 |

Every row in this file comes from one of these four groups; the accuracy column is the GSM8K score of the very run the tensors were taken from.
