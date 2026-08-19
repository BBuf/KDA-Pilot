# Capture provenance

| field | value |
| --- | --- |
| model | moonshotai/Kimi-K3 |
| serving args | `--trust-remote-code --tp-size 8 --mem-fraction-static 0.85 --reasoning-parser kimi_k3 --tool-call-parser kimi_k3` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 0-7 (TP8) |
| SGLang commit | `43226af` |
| torch / triton / transformers | 2.13.0+cu130 / 3.7.1 / 5.12.1 |
| GPU | NVIDIA B300 SXM6 |

### Capture-only modifiers

- --disable-cuda-graph (python-level ops are invisible inside a captured graph)
- tensors phase adds --disable-radix-cache (radix rewrites mamba/KDA state pool rows outside the kernel call and breaks the state chain)

### Operating points walked

| group | phase | started (UTC) | GSM8K accuracy | output tok/s | mean TTFT |
| --- | --- | --- | ---: | ---: | ---: |
| `gsm8k_5shot_cc1` | tensors | - | 1.000 | - | - |
| `gsm8k_16shot_cc16` | tensors | - | 1.000 | - | - |
| `gsm8k_5shot_cc32` | tensors | - | 1.000 | - | - |

Workload sources:

- benchmark/gsm8k/bench_sglang.py (real GSM8K, 5-shot serial / 16-shot 16-way / 5-shot 32-way)
- sglang.bench_serving random 1024/256 cc16 for the profiled GPU-time share
