# Capture provenance

| field | value |
| --- | --- |
| model | `/scratch/models/lfm25` |
| serving args | `--trust-remote-code --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 1 |
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
| `random_1k1k_cc1` | shapes | 11:45:36 | - | 59.42 |
| `random_1k1k_cc16` | shapes | 11:46:34 | - | 620.60 |
| `random_1k1k_cc256` | shapes | 11:47:27 | - | 4551.77 |
| `random_4k512_cc8` | shapes | 11:48:12 | - | 349.37 |
| `sharegpt_cc32` | shapes | 11:48:50 | - | 647.79 |
| `gsm8k_5shot_cc1` | shapes | 11:49:35 | 1.000 | - |
| `gsm8k_5shot_cc32` | shapes | 11:49:51 | 0.484 | - |
| `gsm8k_16shot_cc16` | shapes | 11:50:19 | 0.875 | - |
| `gsm8k_accuracy_200` | shapes | 11:50:40 | 0.365 | - |
| `gsm8k_5shot_cc1` | tensors | 11:58:30 | 1.000 | - |
| `gsm8k_16shot_cc16` | tensors | 11:58:45 | 0.875 | - |
| `random_1k1k_cc16` | tensors | 11:59:01 | - | 620.60 |

Real GSM8K accuracy on the very run these shapes came from is the sanity check
that the capture is from a correctly serving model. `bench/workloads.json` carries
the per-signature real-traffic call counts; `../../docs/workload_capture.md`
explains the selection rule and the two capture-only modifiers.
