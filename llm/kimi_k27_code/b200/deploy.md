# Kimi-K2.7-Code / B200 deployment & workflow capture

- **Model:** `moonshotai/Kimi-K2.7-Code`
- **Cookbook source:** `https://docs.sglang.io/cookbook/autoregressive/Moonshotai/Kimi-K2.7-Code.md`
- **Current status:** waiting for a clean 8-GPU B200 window.

## Serve

```bash
sglang serve \
  --model-path moonshotai/Kimi-K2.7-Code \
  --tp 8 \
  --reasoning-parser kimi_k2 \
  --tool-call-parser kimi_k2 \
  --trust-remote-code \
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
- Delete only `moonshotai/Kimi-K2.7-Code` weights/cache/locks after completion.
