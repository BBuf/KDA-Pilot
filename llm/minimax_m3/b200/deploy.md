# MiniMax-M3 / B200 deployment & workflow capture

- **Model:** `MiniMaxAI/MiniMax-M3-MXFP8` for the B200-friendly command path.
- **Cookbook source:** `https://docs.sglang.io/cookbook/autoregressive/MiniMax/MiniMax-M3.md`
- **Runtime note:** The live cookbook says MiniMax-M3 support is in SGLang PR
  `#27944`. For B200 it recommends `lmsysorg/sglang:dev-minimax-m3`.
- **Current status:** waiting for a clean 8-GPU B200 window. Do not run on a
  shared or partially occupied node.

## Serve

The live cookbook B200 MXFP8 path is a single TP8 server.

```bash
CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 sglang serve \
  --trust-remote-code \
  --model-path MiniMaxAI/MiniMax-M3-MXFP8 \
  --reasoning-parser auto \
  --tool-call-parser auto \
  --tp 8 \
  --attention-backend fa4 \
  --page-size 128 \
  --moe-runner-backend deep_gemm \
  --chunked-prefill-size 8192 \
  --mem-fraction-static 0.65 \
  --host 0.0.0.0 \
  --port 30000
```

## Benchmark Matrix

Run both datasets against the server endpoint:

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
- Save raw profiler traces under `profile/`.
- Save the filtered kernel inventory under `docs/kernel_workflow.md` and
  `docs/kernel_workflow.csv`.
- Include only SGLang-relevant optimized kernels whose GPU kernel-time share is
  greater than `2%`, with shape/meta provenance from profiler CPU op shapes.
- Delete only `MiniMaxAI/MiniMax-M3-MXFP8` weights/cache/locks after the folder
  is complete.
