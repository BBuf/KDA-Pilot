# bench/ - how to run this task

```bash
# 1. does the package have everything?  (CPU only, no SGLang import)
python tools/check_task.py deepseek_v4_flash__dsa_sparse_attention
python deepseek_v4_flash__dsa_sparse_attention/tests/test_contract.py

# 2. time the baseline on every workload row (needs a GPU + the SGLang env)
python tools/bench_harness.py deepseek_v4_flash__dsa_sparse_attention

# 3. write solution/entry.py with the same OPS keys, then A/B it
python tools/bench_harness.py deepseek_v4_flash__dsa_sparse_attention --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, restores in-place
inputs between iterations, checks correctness before reporting a speedup, and uses the
real captured tensors for a row whenever this task ships a payload that matches it
(the per-row line prints how many inputs were real).

## What runs today

Verified on 1x B300 with SGLang main @ 43226af: **8 of 12 ops produce a CUDA-graph-timed baseline** from the recorded rows.

The rest need a small reconstruction step in `baseline/entry.py`'s
`RECONSTRUCT` hook, because the capture could record an argument's contents but
not the object around it:

* `dsa_compress_forward` - takes a CompressorPrefillPlan/DecodePlan namedtuple; the capture recorded its tensor fields, so RECONSTRUCT can rebuild it
* `dsa_compress_norm_rope_store` - same plan object
* `mhc_pre` - reads the tensor-parallel group; run under a single-rank torch.distributed init, or call the *_tilelang entry directly (which does time)
* `mhc_post` - same

The harness reports those rows as `NOT RUNNABLE` with the missing argument
named, and keeps going with the rest.


## Dropping a candidate in

```bash
cp solution/entry.py.template solution/entry.py     # implement the ops listed there
python tools/bench_harness.py deepseek_v4_flash__dsa_sparse_attention --json report.json
python deepseek_v4_flash__dsa_sparse_attention/tests/test_solution.py
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

## What is in here

| file | contents |
| --- | --- |
| `workloads*.json` | frozen call signatures with their real-traffic call counts |
| `tensors/` | real captured tensors (inputs, outputs, state rows) |
| `tensors_mhc/` | real captured tensors (inputs, outputs, state rows) |

| op | real calls | rows |
| --- | ---: | ---: |
| `dsa_compress_forward` | 183,527 | 11 |
| `dsa_compress_norm_rope_store` | 183,526 | 11 |
| `dsa_fused_q_indexer_rope_hadamard_quant` | 62,164 | 8 |
| `dsa_indexer_logits_deepgemm_DEFAULT` | 62,164 | 8 |
| `dsa_topk_transform_v2` | 59,808 | 7 |
| `dsa_sparse_attention_flash_mla_alt` | 4,825 | 12 |
| `dsa_paged_mqa_logits_metadata` | 2,964 | 8 |
| `dsa_topk_transform` | 2,356 | 10 |
| `mhc_pre_big_fuse_with_norm_tilelang` | 155,492 | 9 |
| `mhc_pre` | 155,492 | 9 |
| `mhc_post_tilelang` | 155,492 | 9 |
| `mhc_post` | 155,492 | 9 |
