# Capture provenance

| field | value |
| --- | --- |
| model | `/scratch/models/dsv4_flash` |
| serving args | `--tp 4 --trust-remote-code --moe-runner-backend flashinfer_mxfp4 --mem-fraction-static 0.85` |
| host | light-face-hides-fin-03-1 (RadixArk devbox b300-diffusion-kernel-opt) |
| GPUs used | 4,5,6,7 |
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
| `random_1k1k_cc1` | shapes | 12:27:20 | - | 13.18 |
| `random_1k1k_cc16` | shapes | 12:30:21 | - | 134.20 |
| `random_1k1k_cc256` | shapes | 12:33:45 | - | 576.57 |
| `random_4k512_cc8` | shapes | 12:37:49 | - | 67.98 |
| `sharegpt_cc32` | shapes | 12:39:58 | - | 101.36 |
| `gsm8k_5shot_cc1` | shapes | 12:42:46 | 1.000 | - |
| `gsm8k_5shot_cc32` | shapes | 12:43:24 | 0.984 | - |
| `gsm8k_16shot_cc16` | shapes | 12:45:13 | 1.000 | - |
| `gsm8k_accuracy_200` | shapes | 12:46:35 | 0.980 | - |

Real GSM8K accuracy on the very run these shapes came from is the sanity check
that the capture is from a correctly serving model. `bench/workloads.json` carries
the per-signature real-traffic call counts; `../docs/workload_capture.md`
explains the selection rule and the two capture-only modifiers.
