# Profile evidence — lfm25__sglang_run_activation_inplace

**Why this kernel is an e2e-optimization target:** it is **4.4% of total GPU
time** (max across scenarios) on `LiquidAI/LFM2.5-8B-A1B`, measured by profiling the exact
cookbook deployment. Clean Python interface from profiler provenance.

- Model: `LiquidAI/LFM2.5-8B-A1B` (slug `lfm25`, tp=1)
- Python interface: `sglang._run_activation_inplace`
- Category: `other`
- GPU kernel(s): `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::Acti`
- Profiler op provenance: `aten::copy_`, `aten::select`, `sglang::_run_activation_inplace`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| random_low | random (conc 1) | 2.94% |
| random_mid | random (conc 32) | 3.54% |
| random_high | random (conc 100) | 4.35% |
| sharegpt_low | sharegpt (conc 1) | 3.16% |
| sharegpt_mid | sharegpt (conc 32) | 3.51% |
| sharegpt_high | sharegpt (conc 100) | 3.73% |

**Peak: 4.4% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[1], [], []]`
- `[[], [16384, 14336], [16384, 7168]]`
- `[[], [2496, 3584], [2496, 1792]]`
- `[[], [28772, 3584], [28772, 1792]]`
- `[[], [30020, 3584], [30020, 1792]]`
- `[[], [412, 3584], [412, 1792]]`
- `[[], [65536, 3584], [65536, 1792]]`
- `[[], [7193, 14336], [7193, 7168]]`
- `[[], [7505, 14336], [7505, 7168]]`
- `[[], [], []]`

## Reproduce the deployment (cookbook-aligned)
```bash
sglang serve --model-path LiquidAI/LFM2.5-8B-A1B --tp 1 --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2
```

After optimizing, re-run the **random_high** scenario to validate the e2e effect:
`bench_serving --dataset-name random ... --max-concurrency 100`.
