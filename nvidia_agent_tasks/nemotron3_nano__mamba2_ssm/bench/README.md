# bench/ - how to run this task

```bash
# 1. does the package have everything?  (CPU only, no SGLang import)
python tools/check_task.py nemotron3_nano__mamba2_ssm
python nemotron3_nano__mamba2_ssm/tests/test_contract.py

# 2. time the baseline on every workload row (needs a GPU + the SGLang env)
python tools/bench_harness.py nemotron3_nano__mamba2_ssm

# 3. write solution/entry.py with the same OPS keys, then A/B it
python tools/bench_harness.py nemotron3_nano__mamba2_ssm --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, restores in-place
inputs between iterations, checks correctness before reporting a speedup, and uses the
real captured tensors for a row whenever this task ships a payload that matches it
(the per-row line prints how many inputs were real).

## What runs today

Verified on 1x B300 with SGLang main @ 43226af: **9 of 9 ops produce a CUDA-graph-timed baseline** from the recorded rows.

## What is in here

| file | contents |
| --- | --- |
| `workloads*.json` | frozen call signatures with their real-traffic call counts |
| `tensors/` | real captured tensors (inputs, outputs, state rows) |

| op | real calls | rows |
| --- | ---: | ---: |
| `causal_conv1d_decode` | 275,863 | 5 |
| `mamba2_chunk_cumsum` | 7,130 | 14 |
| `mamba2_chunk_state` | 7,130 | 14 |
| `causal_conv1d_prefill` | 7,130 | 15 |
| `mamba2_state_passing` | 7,130 | 15 |
| `mamba2_chunk_scan` | 7,130 | 15 |
| `mamba2_chunk_state_varlen` | 7,130 | 15 |
| `mamba2_chunk_scan_combined_fwd` | 7,130 | 15 |
| `mamba2_chunk_scan_combined` | 7,130 | 15 |
