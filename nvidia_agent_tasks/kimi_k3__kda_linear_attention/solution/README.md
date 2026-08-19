# solution/

1. `cp entry.py.template entry.py` and implement the ops listed there.
2. `python tools/bench_harness.py kimi_k3__kda_linear_attention --json report.json` - interleaved A/B against
   the copied baseline, correctness before performance.
3. `python kimi_k3__kda_linear_attention/tests/test_solution.py` - the correctness gate alone, no timing.

The gate for this task is `chained_state` (see `../config.json` and
`../../docs/anti_hack_contract.md`).
