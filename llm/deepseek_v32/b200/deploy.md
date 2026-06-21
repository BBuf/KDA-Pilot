# DeepSeek-V3.2 / B200 deployment & workflow capture

- **Model:** `nvidia/DeepSeek-V3.2-NVFP4`
- **Cookbook source:** `https://docs.sglang.io/cookbook/autoregressive/DeepSeek/DeepSeek-V3_2.md`
- **Selected command:** NVIDIA H200/B200 NVFP4 command from the DeepSeek-V3.2
  page.
- **Current status:** waiting for 4 idle B200 GPUs on the same node.

## Serve

```bash
python -m sglang.launch_server \
  --model nvidia/DeepSeek-V3.2-NVFP4 \
  --tp 4 \
  --quantization modelopt_fp4 \
  --moe-runner-backend flashinfer_trtllm \
  --tool-call-parser deepseekv32 \
  --reasoning-parser deepseek-v3 \
  --host 0.0.0.0 \
  --port 30000
```

## Benchmark Matrix

Use both required datasets:

| Label | Dataset | num_prompts | max_concurrency |
|---|---|---:|---:|
| random_low | random 1000/1000 | 10 | 1 |
| random_mid | random 1000/1000 | 300 | 32 |
| random_high | random 1000/1000 | 500 | 100 |
| sharegpt_low | ShareGPT | 10 | 1 |
| sharegpt_mid | ShareGPT | 300 | 32 |
| sharegpt_high | ShareGPT | 500 | 100 |

## Deliverables

- Save bench logs under `bench/`.
- Save profiler traces under `profile/`.
- Save `>2%` SGLang optimized-kernel shape/meta inventory under `docs/`.
- Delete only `nvidia/DeepSeek-V3.2-NVFP4` weights/cache/locks after completion.
