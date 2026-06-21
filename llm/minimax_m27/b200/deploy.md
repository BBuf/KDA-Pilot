# MiniMax-M2.7 B200 Deployment And Shape Capture

- Model: `MiniMaxAI/MiniMax-M2.7`
- Cookbook page: `MiniMax/MiniMax-M2.7.md`
- Platform: NVIDIA B200 x8
- Final run status: completed + cleaned
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`

## Serve

The successful run used the live cookbook B200 command shape: TP8 + EP8 with
MiniMax parsers and `mem-fraction-static=0.85`.

```bash
sglang serve \
  --model-path MiniMaxAI/MiniMax-M2.7 \
  --tp-size 8 \
  --ep-size 8 \
  --tool-call-parser minimax-m2 \
  --reasoning-parser minimax-append-think \
  --trust-remote-code \
  --mem-fraction-static 0.85 \
  --host 0.0.0.0 \
  --port 30000
```

The captured run was launched through `llm/scripts/run_serving_kernel_profile.sh`
from `profile_config.sh`, which starts per-workload torch profiling through the
server profiler endpoint.

## Benchmark Matrix

Each workload used the standard B200 text-only serving sweep:

| Workload | Dataset | Max concurrency | Num prompts |
|---|---|---:|---:|
| `random_low` | random 1000/1000 | 1 | 10 |
| `random_mid` | random 1000/1000 | 32 | 300 |
| `random_high` | random 1000/1000 | 100 | 500 |
| `sharegpt_low` | ShareGPT | 1 | 10 |
| `sharegpt_mid` | ShareGPT | 32 | 300 |
| `sharegpt_high` | ShareGPT | 100 | 500 |

## Shape Artifacts

- Parsed kernel shape rows live under `docs/kernel_shapes_*.{json,md,tsv}`.
- Promoted task candidates live in `docs/kernel_task_index.{json,md}` and
  `kernels/*/prompt.md`.
- Raw torch profiler traces are intentionally not committed.

Final row counts:

```text
random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high
= 11/10/9/11/9/9
```
