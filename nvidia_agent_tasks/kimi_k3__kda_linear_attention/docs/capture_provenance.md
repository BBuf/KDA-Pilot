# Capture provenance

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
