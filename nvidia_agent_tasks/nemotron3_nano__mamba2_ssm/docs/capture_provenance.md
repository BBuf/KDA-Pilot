# Capture provenance

| field | value |
| --- | --- |
| model | `/scratch/models/nemotron3_nano` |
| serving args | `--trust-remote-code --max-running-requests 1024` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 0 |
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
| `random_1k1k_cc1` | shapes | 11:45:36 | - | 25.60 |
| `random_1k1k_cc16` | shapes | 11:47:18 | - | 249.34 |
| `random_1k1k_cc256` | shapes | 11:49:09 | - | 2490.11 |
| `random_4k512_cc8` | shapes | 11:50:20 | - | 145.48 |
| `sharegpt_cc32` | shapes | 11:51:31 | - | 261.17 |
| `gsm8k_5shot_cc1` | shapes | 11:52:48 | 0.333 | - |
| `gsm8k_5shot_cc32` | shapes | 11:53:29 | 0.344 | - |
| `gsm8k_16shot_cc16` | shapes | 11:54:38 | 0.688 | - |
| `gsm8k_accuracy_200` | shapes | 11:55:27 | 0.310 | - |
| `gsm8k_5shot_cc1` | tensors | 12:03:48 | 0.333 | - |
| `gsm8k_16shot_cc16` | tensors | 12:04:45 | 0.688 | - |
| `random_1k1k_cc16` | tensors | 12:05:18 | - | 249.34 |

Real GSM8K accuracy on the very run these shapes came from is the sanity check
that the capture is from a correctly serving model. `bench/workloads.json` carries
the per-signature real-traffic call counts; `../docs/workload_capture.md`
explains the selection rule and the two capture-only modifiers.
