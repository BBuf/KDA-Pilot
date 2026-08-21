# solution/

1. `cp entry.py.template entry.py` and implement the ops listed there.
2. `python tools/bench_harness.py qwen3_next__gdn_packed_decode --json report.json` - interleaved A/B against
   the copied baseline, correctness before performance.
3. `python qwen3_next__gdn_packed_decode/tests/test_solution.py` - the correctness gate alone, no timing.

The gate for this task is `tolerance` (see `../config.json` and
`../../docs/anti_hack_contract.md`).
