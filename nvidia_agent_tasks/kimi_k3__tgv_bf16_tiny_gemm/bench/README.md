# bench/ - how to run this task

```bash
# 1. does the package have everything?  (CPU only, no SGLang import)
python tools/check_task.py kimi_k3__tgv_bf16_tiny_gemm
python kimi_k3__tgv_bf16_tiny_gemm/tests/test_contract.py

# 2. time the baseline on every workload row (needs a GPU + the SGLang env)
python tools/bench_harness.py kimi_k3__tgv_bf16_tiny_gemm

# 3. write solution/entry.py with the same OPS keys, then A/B it
python tools/bench_harness.py kimi_k3__tgv_bf16_tiny_gemm --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, restores in-place
inputs between iterations, checks correctness before reporting a speedup, and uses the
real captured tensors for a row whenever this task ships a payload that matches it
(the per-row line prints how many inputs were real).

## What runs today

Verified on 1x B300 with SGLang main @ 43226af: **5 of 5 ops produce a CUDA-graph-timed baseline** from the recorded rows.


## Dropping a candidate in

```bash
cp solution/entry.py.template solution/entry.py     # implement the ops listed there
python tools/bench_harness.py kimi_k3__tgv_bf16_tiny_gemm --json report.json
python kimi_k3__tgv_bf16_tiny_gemm/tests/test_solution.py
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
| `k3_cutedsl_tgv_bf16_gemm_out` | 0.02 | 2.5 | `test/registered/kernels/ops/gemm/test_cutedsl_bf16_gemm.py:53` |
| `k3_tiny_gemm` | 0.001 | 0.001 | `test/registered/kernels/ops/test_kimi_k3_prerequisite_ops.py:385-386` |
| `k3_cutedsl_tgv_bf16_gemm` | 0.02 | 2.5 | `test/registered/kernels/ops/gemm/test_cutedsl_bf16_gemm.py:53` |
| `k3_tiny_n_gemm_bf16` | 0.001 | 0.001 | `test/registered/kernels/ops/test_kimi_k3_prerequisite_ops.py:385-386` |
| `k3_tiny_k_gemm_bf16` | 0.001 | 0.001 | `test/registered/kernels/ops/test_kimi_k3_prerequisite_ops.py:385-386` |

## What is in here

| file | contents |
| --- | --- |
| `workloads*.json` | frozen call signatures with their real-traffic call counts |
| `tensors/` | real captured tensors (inputs, outputs, state rows) |

| op | real calls | rows |
| --- | ---: | ---: |
| `k3_cutedsl_tgv_bf16_gemm_out` | 571,784 | 11 |
| `k3_tiny_gemm` | 433,920 | 11 |
| `k3_cutedsl_tgv_bf16_gemm` | 244,624 | 11 |
| `k3_tiny_n_gemm_bf16` | 213,096 | 10 |
| `k3_tiny_k_gemm_bf16` | 163,416 | 10 |
