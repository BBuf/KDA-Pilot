# Capture provenance

## `bench/workloads.json`

| field | value |
| --- | --- |
| model | moonshotai/Kimi-K3 |
| serving args | `--trust-remote-code --tp-size 8 --mem-fraction-static 0.85 --reasoning-parser kimi_k3 --tool-call-parser kimi_k3` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 0,1,2,3,4,5,6,7 |
| SGLang commit | `43226af` |
| torch / triton / transformers | 2.13.0+cu130 / 3.7.1 / 5.12.1 |
| GPU | NVIDIA B300 SXM6 AC |

### Capture-only modifiers

- --disable-cuda-graph (python-level ops are invisible inside a captured graph)
- tensors phase adds --disable-radix-cache (radix cache rewrites mamba/state pool rows outside the kernel call and breaks the state chain; shapes phase keeps radix ON so prefix-hit-driven chunk lengths stay realistic)

### Operating points walked

| group | phase | started (UTC) | GSM8K accuracy | output tok/s | mean TTFT |
| --- | --- | --- | ---: | ---: | ---: |

Workload sources:

- sglang.bench_serving --dataset-name random (cookbook operating points)
- sglang.bench_serving --dataset-name sharegpt
- benchmark/gsm8k/bench_sglang.py (real GSM8K, 2/5/16-shot, incl. a 200-question accuracy run)

## `bench/workloads_kda_chunk_prefill.json`

| field | value |
| --- | --- |
| model | moonshotai/Kimi-K3 |
| serving args | `--trust-remote-code --tp-size 8 --mem-fraction-static 0.85 --reasoning-parser kimi_k3 --tool-call-parser kimi_k3` |
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
| `gsm8k_5shot_cc32` | `benchmark/gsm8k/bench_sglang.py --num-questions 32 --num-shots 5 --parallel 32` | 1.000 | - |
| `random_1k256_cc16` | `sglang.bench_serving --dataset-name random --random-input-len 1024 --random-output-len 256 --num-prompts 32 --max-concurrency 16` | - | 89.81 |

Every row in this file comes from one of these four groups; the accuracy column is the GSM8K score of the very run the tensors were taken from.
