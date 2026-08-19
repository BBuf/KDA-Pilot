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


## Dropping a candidate in

```bash
cp solution/entry.py.template solution/entry.py     # implement the ops listed there
python tools/bench_harness.py nemotron3_nano__mamba2_ssm --json report.json
python nemotron3_nano__mamba2_ssm/tests/test_solution.py
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

* **L2 is flushed before every call** (`--l2 cold`, the default): a buffer twice the size of
  B300's 132.6 MB L2 is written before each call, and the event pair brackets only the call,
  so the flush is not in the number. Back-to-back replay (`--l2 hot`) reads 58-82% faster on
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
| `causal_conv1d_decode` | 0.01 | 0.05 | `test/registered/layers/mamba/test_causal_conv1d.py:163-165` |
| `mamba2_chunk_cumsum` | 0.05 | 0.05 | `test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248` |
| `mamba2_chunk_state` | 0.05 | 0.05 | `test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248` |
| `causal_conv1d_prefill` | 0.01 | 0.05 | `test/registered/layers/mamba/test_causal_conv1d.py:163-165` |
| `mamba2_state_passing` | 0.05 | 0.05 | `test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248` |
| `mamba2_chunk_scan` | 0.05 | 0.05 | `test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248` |
| `mamba2_chunk_state_varlen` | 0.05 | 0.05 | `test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248` |
| `mamba2_chunk_scan_combined_fwd` | 0.05 | 0.05 | `test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248` |
| `mamba2_chunk_scan_combined` | 0.05 | 0.05 | `test/registered/layers/mamba/test_mamba_ssm_ssd.py:244-248` |

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
