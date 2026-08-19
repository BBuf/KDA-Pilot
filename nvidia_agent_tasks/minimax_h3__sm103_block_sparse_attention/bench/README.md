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


## Dropping a candidate in

```bash
cp solution/entry.py.template solution/entry.py     # implement the ops listed there
python tools/bench_harness.py minimax_h3__sm103_block_sparse_attention --json report.json
python minimax_h3__sm103_block_sparse_attention/tests/test_solution.py
```

`solution/entry.py` exposes the same `OPS` keys as `baseline/entry.py`, so the harness
calls both arms with identical inputs. The path is validated end to end with an identity
candidate (one that just calls the baseline): **1.002x geomean with every gate green**,
which is also this harness's measurement floor - trials alternate which arm runs first,
because running the candidate second in every trial was worth ~2% on its own.

`tests/test_solution.py` runs the same gate without timing: every row through
`config.json::correctness.mode`, plus - where the task ships a state chain - the chained
final-state gate (`gates.replay_chain` feeds each step's produced state into the next and
compares the final one; on the identity candidate that reads `final state rel err 0 over
N chained steps`).

A row whose integer index arguments had to be allocated can address out of bounds and take
the CUDA context down; the harness and the test detect that, name the row, and stop rather
than reporting nonsense for every row after it.


## Correctness tolerances

`torch.testing.assert_close` with the rtol/atol **SGLang's own test for that
kernel uses** - not a threshold invented for this handoff. Same numbers in
`../config.json::correctness.tolerances`, table in `tools/tolerances.py`.

| op | rtol | atol | copied from |
| --- | ---: | ---: | --- |
| `diffusion_attention_cudnn_sdpa` | 0.01 | 0.02 | `test/registered/attention/test_verify_splitkv.py:40-41 and test_verify_shared_kv.py:19-22` |
| `diffusion_attention_fa4` | 0.01 | 0.02 | `test/registered/attention/test_verify_splitkv.py:40-41 and test_verify_shared_kv.py:19-22` |
| `diffusion_attention_sdpa` | 0.01 | 0.02 | `test/registered/attention/test_verify_splitkv.py:40-41 and test_verify_shared_kv.py:19-22` |

## What is in here

| file | contents |
| --- | --- |
| `workloads*.json` | frozen call signatures with their real-traffic call counts |

| op | real calls | rows |
| --- | ---: | ---: |
| `diffusion_attention_cudnn_sdpa` | 216 | 4 |
| `diffusion_attention_fa4` | 200 | 1 |
| `diffusion_attention_sdpa` | 16 | 3 |
