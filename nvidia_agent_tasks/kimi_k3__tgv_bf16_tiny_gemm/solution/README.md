# solution/

Put the candidate kernel here plus an `entry.py` exposing the same `OPS`
keys as `../baseline/entry.py`, then run:

```bash
python tools/bench_harness.py kimi_k3__tgv_bf16_tiny_gemm --json report.json
```
