# bench/ - how to run this task

```bash
# 1. does the package have everything?  (CPU only, no SGLang import)
python tools/check_task.py qwen3_next__gdn_chunk_prefill
python qwen3_next__gdn_chunk_prefill/tests/test_contract.py

# 2. time the baseline on every workload row (needs a GPU + the SGLang env)
python tools/bench_harness.py qwen3_next__gdn_chunk_prefill

# 3. write solution/entry.py with the same OPS keys, then A/B it
python tools/bench_harness.py qwen3_next__gdn_chunk_prefill --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, restores in-place
inputs between iterations, checks correctness before reporting a speedup, and uses the
real captured tensors for a row whenever this task ships a payload that matches it
(the per-row line prints how many inputs were real).

## What runs today

Verified on 1x B300 with SGLang main @ 43226af: **5 of 6 ops produce a CUDA-graph-timed baseline** from the recorded rows.

The rest need a small reconstruction step in `baseline/entry.py`'s
`RECONSTRUCT` hook, because the capture could record an argument's contents but
not the object around it:

* `gdn_decode_packed_triton` - a bound method on TritonGDNKernel - RECONSTRUCT must build an instance (the class holds no per-request state; a default constructor is enough)

The harness reports those rows as `NOT RUNNABLE` with the missing argument
named, and keeps going with the rest.

## What is in here

| file | contents |
| --- | --- |
| `workloads*.json` | frozen call signatures with their real-traffic call counts |
| `tensors/` | real captured tensors (inputs, outputs, state rows) |
| `tensors_prefill/` | real captured tensors (inputs, outputs, state rows) |

| op | real calls | rows |
| --- | ---: | ---: |
| `gdn_recompute_w_u` | 3,744 | 11 |
| `gdn_chunk_delta_h` | 3,744 | 11 |
| `gdn_chunk_o` | 3,744 | 11 |
| `gdn_chunk_prefill` | 3,744 | 11 |
| `gdn_decode_causal_conv1d_update` | 8 | 1 |
| `gdn_decode_packed_triton` | 8 | 1 |
