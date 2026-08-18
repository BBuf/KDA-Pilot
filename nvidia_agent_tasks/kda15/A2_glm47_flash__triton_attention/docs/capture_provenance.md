# Capture provenance

| field | value |
| --- | --- |
| model | `/scratch/models/glm47_flash` |
| serving args | `--trust-remote-code --reasoning-parser glm45 --tool-call-parser glm47 --attention-backend triton --tp 1` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 2 |
| SGLang commit | `43226af` |
| torch / triton / transformers | 2.13.0+cu130 / 3.7.1 / 5.12.1 |
| GPU | NVIDIA B300 SXM6 AC |

## Capture-only modifiers

- --disable-cuda-graph (python-level ops are invisible inside a captured graph)
- tensors phase adds --disable-radix-cache (radix cache rewrites mamba/state pool rows outside the kernel call and breaks the state chain; shapes phase keeps radix ON so prefix-hit-driven chunk lengths stay realistic)

## Workload sources

- sglang.bench_serving --dataset-name random (cookbook operating points)
- sglang.bench_serving --dataset-name sharegpt
- benchmark/gsm8k/bench_sglang.py (real GSM8K, 2/5/16-shot, incl. a 200-question accuracy run)

## Capture matrix actually walked

| group | phase | started (UTC) | GSM8K accuracy | throughput / TTFT |
| --- | --- | --- | --- | --- |
| `random_1k1k_cc1` | shapes | 11:45:36 | - | 5.51 |
| `random_1k1k_cc16` | shapes | 11:52:32 | - | - |
| `sharegpt_cc32` | short | 12:15:14 | - | 8.56 |
| `gsm8k_5shot_cc1` | short | 12:30:41 | 1.000 | - |
| `gsm8k_5shot_cc32` | short | 12:34:09 | 0.750 | - |
| `gsm8k_16shot_cc16` | short | 12:39:30 | 1.000 | - |
| `gsm8k_accuracy_100` | short | 12:43:50 | 0.820 | - |

Real GSM8K accuracy on the very run these shapes came from is the sanity check
that the capture is from a correctly serving model. `bench/workloads.json` carries
the per-signature real-traffic call counts; `../../docs/workload_capture.md`
explains the selection rule and the two capture-only modifiers.
