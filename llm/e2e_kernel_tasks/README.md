# e2e_kernel_tasks — profile-filtered, cookbook-aligned kernel optimization tasks

This is a **flat** folder of LLM kernel-optimization tasks selected on one criterion:
the kernel is a **meaningful fraction of the real end-to-end (e2e) GPU workflow**,
measured by profiling the **exact sgl-cookbook deployment command**. The model is
encoded in each task's folder name (`<model_slug>__<python_op_slug>/`) — there is no
per-model sub-tree.

## Why this folder exists (the lesson)

Earlier kernel tasks were captured at the Python interface **without** aligning to the
cookbook deployment and **without** checking each kernel's share of e2e time. Result:
real isolated-kernel speedups that **do not move e2e** — and one that even regressed it:

- **fp8 M=1 GEMV** (`#29126`): isolated 1.8–2× on small linears, but a dispatch-gate bug
  fired it on the large MLP linears where it loses → **+18% e2e decode regression** on a
  dense fp8 model; parity at best after fixing the gate.
- **fused `topk_sigmoid`** (`#29134`): isolated 1.48× geomean, bit-exact — but profiling
  Step-3.7-Flash showed the router kernel is only **~2.94%** of e2e GPU time, while
  `fused_add_rmsnorm` (ignored) was **~23%**. e2e parity.

**Conclusion:** a kernel that is a small fraction of the forward cannot move e2e no matter
how fast it gets. This folder only admits tasks backed by a profiler-measured e2e share.

## Methodology (per model)

1. **Serve with the EXACT cookbook command** — from
   `sglang/docs_new/cookbook/autoregressive/<Org>/<Model>.mdx`. No deviations
   (same model id, quant, tp/ep, attention/moe backends, flags).
2. **Benchmark + profile** 6 scenarios: `{random, sharegpt} × {low (conc=1), mid (conc=32),
   high (conc=100)}`, ISL/OSL ≈ 1000/1000, via `sglang.bench_serving --profile`
   (`SGLANG_PROFILE_RECORD_SHAPES=1`). Covers prefill-heavy (high conc) and decode-heavy
   (low conc) regimes.
3. **Extract e2e shares** — `extract_kernel_shapes.py --threshold 2.0`: every GPU kernel
   whose cumulative GPU-time share `> 2%` in a scenario, with its **Python-op provenance**
   (the `cpu_op` that launched it, e.g. `sgl_kernel::topk_sigmoid`) and **input shapes**.
4. **Define tasks from the Python call-site** — the kernel-interface capture
   (`SGLANG_KERNEL_API_LOGLEVEL=3` → `build_kernel_interface_tasks.py`) names/builds tasks
   exactly like the per-model `llm/<model>/` tasks (`sgl_kernel.X`, `jit_kernel.X`,
   `srt.layers...`). The profiler is used **only** to measure each such Python op's share.
5. **Keep only e2e-impactful, single-GPU-optimizable kernels:** kernel share `≥` threshold
   in `≥1` scenario **and** not a communication kernel (all-reduce / all-to-all / dispatch
   — those are not single-kernel optimizable and are explicitly out of scope here).

## Each task folder `<model_slug>__<op_slug>/`

Standard KDA scaffold (`config.toml`, `prompt.md`, `docs/evidence.json`, `baseline/`,
`solution/`, `bench/`, `tests/`) **plus**:

- **`docs/profile_evidence.md`** — the justification KDA needs to validate e2e quickly:
  model, exact cookbook serve command, the kernel name + category, **%-of-GPU per scenario**
  (which dataset + concurrency), and the captured input shapes. After KDA optimizes the
  kernel, the recorded scenario is exactly the one to re-run for the e2e A/B.

## Scope & ordering

Single-node sgl-cookbook **autoregressive** models, run **small → large** (tp 1 → 8).
Excluded: communication kernels, multi-node-only recipes, and non-text models
(OCR / reranker / diffusion). One PR per model.

## Index

| Model (slug) | tp | Quant | # tasks | Top kept kernels (max % of GPU) |
|---|---|---|---|---|
| nemotron3_nano | 1 | FP8 | 6 | `sglang.nemotron_mamba2_with_output` 55.8% · `linear_gemm` 26.7% · `sglang.flashinfer_bmm_fp8` 20.7% · `sglang.unified_attention_with_output` 6.1% · `fused_add_rmsnorm` 4.4% · `static_quant_fp8` 4.1% |
