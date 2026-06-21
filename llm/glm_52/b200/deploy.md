# GLM-5.2 / B200 deployment & workflow capture

- **Model:** `zai-org/GLM-5.2-FP8`
- **Cookbook source:** `https://docs.sglang.io/cookbook/autoregressive/GLM/GLM-5.2.md`
- **Selected command:** B200 / default / FP8 / balanced / single node from the
  live command panel.
- **Current status:** waiting for a clean 8-GPU B200 window.

## Serve

```bash
sglang serve \
  --model-path zai-org/GLM-5.2-FP8 \
  --tp 8 \
  --dp 8 \
  --enable-dp-attention \
  --moe-a2a-backend deepep \
  --speculative-algorithm EAGLE \
  --speculative-num-steps 1 \
  --speculative-eagle-topk 1 \
  --speculative-num-draft-tokens 2 \
  --mem-fraction-static 0.85 \
  --cuda-graph-max-bs 128 \
  --chunked-prefill-size 32768 \
  --max-running-requests 80 \
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
- Delete only `zai-org/GLM-5.2-FP8` weights/cache/locks after completion.
