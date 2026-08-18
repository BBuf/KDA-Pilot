# solution/

Put the candidate kernel here, plus an `entry.py` exposing the same
`OPS` keys as `../baseline/entry.py`. Then:

```bash
python tools/bench_harness.py minimax_h3__sparse_backend_fallback --json report.json
```

The harness times inside a CUDA graph, interleaves the two arms, checks correctness
first, and refuses to report a speedup for a row that failed the gate.
