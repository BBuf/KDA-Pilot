# bench/ - how to run this task

```bash
# 1. does the package have everything?  (CPU only, no SGLang import)
python tools/check_task.py minimax_h3__sm103_block_sparse_attention
python minimax_h3__sm103_block_sparse_attention/tests/test_contract.py

# 2. time the baseline on every workload row (needs a GPU + the SGLang env)
python tools/bench_harness.py minimax_h3__sm103_block_sparse_attention

# 3. write solution/entry.py with the same OPS keys, then A/B it
python tools/bench_harness.py minimax_h3__sm103_block_sparse_attention --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, restores in-place
inputs between iterations, checks correctness before reporting a speedup, and uses the
real captured tensors for a row whenever this task ships a payload that matches it
(the per-row line prints how many inputs were real).

## What runs today

Verified on 1x B300 with SGLang main @ 43226af: **0 of 3 ops produce a CUDA-graph-timed baseline** from the recorded rows.

The rest need a small reconstruction step in `baseline/entry.py`'s
`RECONSTRUCT` hook, because the capture could record an argument's contents but
not the object around it:

* `diffusion_attention_cudnn_sdpa` - bound method on the backend impl; RECONSTRUCT must instantiate it with the recorded head geometry
* `diffusion_attention_fa4` - same
* `diffusion_attention_sdpa` - same

The harness reports those rows as `NOT RUNNABLE` with the missing argument
named, and keeps going with the rest.

## What is in here

| file | contents |
| --- | --- |
| `workloads*.json` | frozen call signatures with their real-traffic call counts |

| op | real calls | rows |
| --- | ---: | ---: |
| `diffusion_attention_cudnn_sdpa` | 216 | 4 |
| `diffusion_attention_fa4` | 200 | 1 |
| `diffusion_attention_sdpa` | 16 | 3 |
