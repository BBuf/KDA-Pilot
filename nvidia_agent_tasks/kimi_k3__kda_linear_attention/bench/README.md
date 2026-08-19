# bench/ - how to run this task

```bash
# 1. does the package have everything?  (CPU only, no SGLang import)
python tools/check_task.py kimi_k3__kda_linear_attention
python kimi_k3__kda_linear_attention/tests/test_contract.py

# 2. time the baseline on every workload row (needs a GPU + the SGLang env)
python tools/bench_harness.py kimi_k3__kda_linear_attention

# 3. write solution/entry.py with the same OPS keys, then A/B it
python tools/bench_harness.py kimi_k3__kda_linear_attention --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, restores in-place
inputs between iterations, checks correctness before reporting a speedup, and uses the
real captured tensors for a row whenever this task ships a payload that matches it
(the per-row line prints how many inputs were real).

## What runs today

Verified on 1x B300 with SGLang main @ 43226af: **2 of 2 ops produce a CUDA-graph-timed baseline** from the recorded rows.

## What is in here

| file | contents |
| --- | --- |
| `workloads*.json` | frozen call signatures with their real-traffic call counts |
| `tensors/` | real captured tensors (inputs, outputs, state rows) |

| op | real calls | rows |
| --- | ---: | ---: |
| `k3_kda_fused_decode` | 308,024 | 10 |
| `k3_kda_chunk_prefill` | 5,520 | 9 |
