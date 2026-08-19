# Low-latency BF16 GEMM on the Kimi-K3 decode path

**Task:** `kimi_k3__tgv_bf16_tiny_gemm`

**Model:** `moonshotai/Kimi-K3` (2.8T mxfp4, TP8)
**Serving command this workload came from (the deployment we run in production):**

```bash
python3 -m sglang.launch_server --model-path moonshotai/Kimi-K3 \
  --trust-remote-code --tp-size 8 --mem-fraction-static 0.85 \
  --reasoning-parser kimi_k3 --tool-call-parser kimi_k3
```

**Measured share:** the CuTe TGV kernels are **7.69%** of serving GPU time at random
1k/256 concurrency 16 and **41.2%** at batch 1 - the regime this path exists for; the
`tiny_n_gemm` fast path is a further **1.64%**.

## Kernels in scope - two entry points, two different kernels

| entry point | kernel it produces | real calls | signatures |
| --- | --- | ---: | ---: |
| `kernels/ops/gemm/cutedsl_bf16_gemm.py::cutedsl_bf16_gemm_out` | `TgvGemmCuteExtKernel_*` | 571,784 | 21 |
| `...::cutedsl_bf16_gemm` | same family | 244,624 | 36 |
| `kernels/ops/kimi_k3/__init__.py::kimi_k3_tiny_gemm` | dispatcher only, no kernel | 433,920 | 44 |
| `kernels/ops/gemm/tiny_gemm.py::tiny_n_gemm_bf16` | `sglang::tiny_n_gemm_kernel` | 213,096 | 15 |
| `...::tiny_k_gemm_bf16` | `sglang::tiny_k_gemm_kernel` | 163,416 | 11 |

`kimi_k3_tiny_gemm` is a shape dispatcher, not a kernel: it routes
`(n,k)=(144,7168)` with `m<=16` and `(896,7168)` with `m<=8` to `tiny_n_gemm_bf16`,
`(1536,128)` with `m<=12` to `tiny_k_gemm_bf16`, and everything else to `F.linear`. The
dispatch tables are part of the problem - a kernel with a wider profitable range moves
more traffic than a faster kernel alone.

Baseline sources are copied into `baseline/` from SGLang main @ 43226af: the CuTe TGV
implementation, the tiny-GEMM implementations, and the K3 dispatcher.

## Why we are asking for this one

- Kimi-K3 decode issues ~302 GEMM launches per step, one per layer per projection, with
  different k (7168, 1536, 768, 4224). At batch 1 they are the largest single block of GPU
  time in the model, which is why the CuTe TGV path exists at all.
- **Read this before tuning.** We already swept the full TGV tactic ladder on the six real
  m=1 shapes: total available saving from retuning is **1.6 us/step = 0.01 tok/s**, and the
  shipped tactic 18 is best on 4 of 6 shapes and within 0.05 us on the rest. The ask is a
  better kernel, not a better tactic - and the bar is a CuTe kernel already at **72% of HBM
  peak** on the hottest (6016,7168) m=1 shape.
- Launch count is part of the budget: a trivial in-graph elementwise kernel costs 2.20 us
  on this box, so a candidate that removes launches from the 302 wins more than one that
  shaves each of them.

## Correctness gate

- Stateless: exact-shape output comparison per row against the copied baseline.
- The m=1 and small-m rows dominate; a candidate that only wins at larger m has not moved
  this model.
- If you widen a dispatch range, the newly covered rows must still beat `F.linear`, which
  is what they fall back to today.

## Workload

`bench/workloads.json`: 53 rows across the five entry points, captured on 8x B300
(TP8) with real GSM8K at 5-shot serial and 16-shot 16-way, **accuracy 1.000 on both**.
`bench/tensors/` holds real inputs and outputs. Provenance in `docs/capture_provenance.md`.

## Deliverable

1. Kernel source in `solution/`, exposing the same `OPS` keys as `baseline/entry.py`.
2. `python tools/bench_harness.py kimi_k3__tgv_bf16_tiny_gemm --json report.json` output.
3. The correctness-gate result, and Nsight Compute evidence for any bottleneck claim.
