# Profile evidence — lfm25__sglang_inplace_fused_experts

**Why this kernel is an e2e-optimization target:** it is **50.5% of total GPU
time** (max across scenarios) on `LiquidAI/LFM2.5-8B-A1B`, measured by profiling the exact
cookbook deployment. Clean Python interface from profiler provenance.

- Model: `LiquidAI/LFM2.5-8B-A1B` (slug `lfm25`, tp=1)
- Python interface: `sglang.inplace_fused_experts`
- Category: `moe`
- GPU kernel(s): `fused_moe_kernel`
- Profiler op provenance: `sglang::inplace_fused_experts`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| random_low | random (conc 1) | 32.96% |
| random_mid | random (conc 32) | 50.52% |
| random_high | random (conc 100) | 45.03% |
| sharegpt_low | sharegpt (conc 1) | 34.12% |
| sharegpt_mid | sharegpt (conc 32) | 47.66% |
| sharegpt_high | sharegpt (conc 100) | 42.22% |

**Peak: 50.5% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[103, 2048], [32, 3584, 2048], [32, 2048, 1792], [103, 4], [103, 4], [], [], []`
- `[[16384, 2048], [32, 3584, 2048], [32, 2048, 1792], [16384, 4], [16384, 4], [], `
- `[[624, 2048], [32, 3584, 2048], [32, 2048, 1792], [624, 4], [624, 4], [], [], []`
- `[[7193, 2048], [32, 3584, 2048], [32, 2048, 1792], [7193, 4], [7193, 4], [], [],`
- `[[7505, 2048], [32, 3584, 2048], [32, 2048, 1792], [7505, 4], [7505, 4], [], [],`

## Reproduce the deployment (cookbook-aligned)
```bash
sglang serve --model-path LiquidAI/LFM2.5-8B-A1B --tp 1 --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2
```

After optimizing, re-run the **random_mid** scenario to validate the e2e effect:
`bench_serving --dataset-name random ... --max-concurrency 32`.
