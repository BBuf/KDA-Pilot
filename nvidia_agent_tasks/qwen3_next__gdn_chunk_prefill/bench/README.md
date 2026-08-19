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


## Dropping a candidate in

```bash
cp solution/entry.py.template solution/entry.py     # implement the ops listed there
python tools/bench_harness.py qwen3_next__gdn_chunk_prefill --json report.json
python qwen3_next__gdn_chunk_prefill/tests/test_solution.py
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



## Measurement regime

* **Timing is `triton.testing.do_bench` around a captured CUDA graph** (`--timer do_bench`,
  the default). do_bench clears L2 before every run, brackets each run with its own event
  pair and sizes the repetitions from a time budget; the graph keeps per-launch overhead out
  of kernels that take single-digit microseconds. `--timer graph` runs our own flush+event
  loop instead - the two agree to 0.1% on the K3 GEMM rows.
* **L2 is cold on every call.** Back-to-back replay with a warm L2 reads 58-82% faster on
  these rows - see `../docs/measurement_contract.md`.
* **The baseline is called three times on identical inputs before anything is judged.** A row
  whose reference contains NaN/Inf or does not reproduce is printed as `NO VALID REFERENCE`
  and excluded, rather than judged against uninitialized memory.
* **Per-row trial spread is reported**, and a row whose spread exceeds 10% is marked
  unstable - its speedup is noise until that is fixed.
* Rows whose integer index arguments had to be synthesised are flagged in the row line.

## Correctness tolerances

`torch.testing.assert_close` with the rtol/atol **SGLang's own test for that
kernel uses** - not a threshold invented for this handoff. Same numbers in
`../config.json::correctness.tolerances`, table in `tools/tolerances.py`.

| op | rtol | atol | copied from |
| --- | ---: | ---: | --- |
| `gdn_recompute_w_u` | 0.01 | 0.02 | `test/registered/attention/test_chunk_gated_delta_rule.py:28-29` |
| `gdn_chunk_delta_h` | 0.01 | 0.02 | `test/registered/attention/test_chunk_gated_delta_rule.py:28-29` |
| `gdn_chunk_o` | 0.01 | 0.02 | `test/registered/attention/test_chunk_gated_delta_rule.py:28-29` |
| `gdn_chunk_prefill` | 0.01 | 0.02 | `test/registered/attention/test_chunk_gated_delta_rule.py:28-29` |
| `gdn_decode_causal_conv1d_update` | 0.01 | 0.05 | `test/registered/layers/mamba/test_causal_conv1d.py:163-165` |
| `gdn_decode_packed_triton` | 0.02 | 0.02 | `test/registered/kernels/ops/attention/test_kda_fused_decode.py:207-208` |

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
