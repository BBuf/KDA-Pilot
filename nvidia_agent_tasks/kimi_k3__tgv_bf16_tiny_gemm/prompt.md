# Low-latency BF16 tiny GEMM (Kimi-K3, TGV CuTe path)

**Task:** `kimi_k3__tgv_bf16_tiny_gemm`

**Model:** `moonshotai/Kimi-K3`
**Serving command this workload came from (the deployment we run in production):**

```bash
python3 -m sglang.launch_server --model-path moonshotai/Kimi-K3 \
  --trust-remote-code --tp-size 8 --mem-fraction-static 0.85 \
  --reasoning-parser kimi_k3 --tool-call-parser kimi_k3
```

**Measured share:** **7.69%** of serving GPU time at random 1k/256 concurrency 16 (two `TgvGemmCuteExtKernel` variants, 4.99% + 2.70%); **41.2%** at the bs=1 latency point, which is the regime this kernel exists for

## Kernels in scope

- `k3_tiny_gemm`

Baseline sources are copied into `baseline/` from SGLang main @ 43226af (python/sglang, editable install). Do not benchmark against a
naive PyTorch reference; the bar is the shipped kernel.

## Why we are asking for this one

- Kimi-K3's decode path issues 302 of these per step - one per layer per projection,
  with different k (7168, 1536, 768, 4224) - so at batch 1 they are the single largest
  block of GPU time in the model. 627,088 real calls across 96 distinct signatures in
  this capture.
- **Read this before tuning**: we already swept the full TGV tactic ladder ourselves on
  the six real m=1 shapes. Total available saving from retuning is **1.6 us/step = 0.01
  tok/s**, and the shipped tactic 18 is best on 4 of 6 and within 0.05 us on the rest.
  The ask is therefore a *better kernel*, not a better tactic - and the bar to beat is a
  CuTe kernel already running at 72% of HBM peak on the (6016,7168) m=1 shape.
- Two independent measurements say the same thing about where the ceiling is: at m=1 a
  trivial in-graph elementwise kernel costs 2.20 us on this box, so per-launch cost is a
  real part of the budget - a candidate that fuses several of the 302 launches wins more
  than one that shaves each.

## Correctness gate

- Stateless: exact-shape output comparison per row against the copied baseline.
- The m=1 rows dominate; a candidate that only wins at larger m has not moved this
  model.

## Workload

`bench/workloads.json` holds the frozen call signatures with their real-traffic call
counts, captured on 8x B300 (TP8) with GSM8K 5-shot serial, 16-shot 16-way and 5-shot
32-way - **accuracy 1.000 on all three**. `docs/capture_provenance.md` has the details.

## Notes

- The task ships the shapes from a live TP8 run, not from a shape list: `x[T, 7168]`
  with T from 1 to 16,143 and the weight geometries the model actually uses.
- This task started life in our internal evaluation harness (`captured_sglang` group)
  with shapes replayed on H200; this version is captured on B300 through the cookbook
  command, with GSM8K 1.000 on the capture run.

## Deliverable

1. Kernel source in `solution/`, exposing the same `OPS` keys as `baseline/entry.py`.
2. `python tools/bench_harness.py kimi_k3__tgv_bf16_tiny_gemm --json report.json` output.
3. The correctness-gate result, and the Nsight Compute evidence for any bottleneck claim.
