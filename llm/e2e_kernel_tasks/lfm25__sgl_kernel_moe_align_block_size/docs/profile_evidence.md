# Profile evidence — lfm25__sgl_kernel_moe_align_block_size

**Why this kernel is an e2e-optimization target:** it is **5.1% of total GPU
time** (max across scenarios) on `LiquidAI/LFM2.5-8B-A1B`, measured by profiling the exact
cookbook deployment. Clean Python interface from profiler provenance.

- Model: `LiquidAI/LFM2.5-8B-A1B` (slug `lfm25`, tp=1)
- Python interface: `sgl_kernel.moe_align_block_size`
- Category: `moe`
- GPU kernel(s): `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*`
- Profiler op provenance: `sgl_kernel::moe_align_block_size`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| random_low | random (conc 1) | 5.09% |

**Peak: 5.1% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[103, 4], [], [], [907], [57], [1], [34], []]`

## Reproduce the deployment (cookbook-aligned)
```bash
sglang serve --model-path LiquidAI/LFM2.5-8B-A1B --tp 1 --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2
```

After optimizing, re-run the **random_low** scenario to validate the e2e effect:
`bench_serving --dataset-name random ... --max-concurrency 1`.
