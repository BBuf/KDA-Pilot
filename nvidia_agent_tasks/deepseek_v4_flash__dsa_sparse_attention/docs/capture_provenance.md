# Capture provenance

## `bench/workloads.json`

| field | value |
| --- | --- |
| model | deepseek-ai/DeepSeek-V4-Flash |
| serving args | `--tp 4 --trust-remote-code --moe-runner-backend flashinfer_mxfp4 --mem-fraction-static 0.85` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 0,1,2,3 |
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
| `gsm8k_5shot_cc32` | `benchmark/gsm8k/bench_sglang.py --num-questions 32 --num-shots 5 --parallel 32` | 1.000 | - |
| `random_1k256_cc16` | `sglang.bench_serving --dataset-name random --random-input-len 1024 --random-output-len 256 --num-prompts 32 --max-concurrency 16` | - | 63.01 |

Every row in this file comes from one of these four groups; the accuracy column is the GSM8K score of the very run the tensors were taken from.

## `bench/workloads_mhc.json`

| field | value |
| --- | --- |
| model | deepseek-ai/DeepSeek-V4-Flash |
| serving args | `--tp 4 --trust-remote-code --moe-runner-backend flashinfer_mxfp4 --mem-fraction-static 0.85` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 0,1,2,3 |
| SGLang commit | `43226af` |
| torch / triton / transformers | 2.13.0+cu130 / 3.7.1 / 5.12.1 |
| GPU | NVIDIA B300 SXM6 AC |

### Capture-only modifiers

- --disable-cuda-graph (python-level ops are invisible inside a captured graph)
- tensors phase adds --disable-radix-cache (radix cache rewrites mamba/state pool rows outside the kernel call and breaks the state chain; shapes phase keeps radix ON so prefix-hit-driven chunk lengths stay realistic)

### Operating points walked

| group | phase | started (UTC) | GSM8K accuracy | output tok/s | mean TTFT |
| --- | --- | --- | ---: | ---: | ---: |
| `random_1k1k_cc1` | shapes | 12:27:20 | - | 13.18 | 966.40 |
| `random_1k1k_cc16` | shapes | 12:30:21 | - | 134.20 | 1886.30 |
| `random_1k1k_cc256` | shapes | 12:33:45 | - | 576.57 | 6483.08 |
| `random_4k512_cc8` | shapes | 12:37:49 | - | 67.98 | 2076.73 |
| `sharegpt_cc32` | shapes | 12:39:58 | - | 101.36 | 3332.57 |
| `gsm8k_5shot_cc1` | shapes | 12:42:46 | 1.000 | - | - |
| `gsm8k_5shot_cc32` | shapes | 12:43:24 | 0.984 | - | - |
| `gsm8k_16shot_cc16` | shapes | 12:45:13 | 1.000 | - | - |
| `gsm8k_accuracy_200` | shapes | 12:46:35 | 0.980 | - | - |

Workload sources:

- sglang.bench_serving --dataset-name random (cookbook operating points)
- sglang.bench_serving --dataset-name sharegpt
- benchmark/gsm8k/bench_sglang.py (real GSM8K, 2/5/16-shot, incl. a 200-question accuracy run)
