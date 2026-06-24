# Profile evidence — lfm25__linear_gemm

**Why this kernel is an e2e-optimization target:** it is **19.0% of total GPU
time** (max across scenarios) on `LiquidAI/LFM2.5-8B-A1B`, measured by profiling the exact
cookbook deployment. Profiler role name; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `LiquidAI/LFM2.5-8B-A1B` (slug `lfm25`, tp=1)
- Python interface: `<confirm via capture; profiler role=linear_gemm>`
- Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT`, `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_256x128_64x5_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_1x1_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT`
- Profiler op provenance: `aten::_index_put_impl_`, `aten::add`, `aten::as_strided`, `aten::cat`, `aten::copy_`, `aten::cumsum`

## % of GPU time by scenario

| dataset | scenario (concurrency) | % of GPU time |
|---|---|---|
| random_low | random (conc 1) | 19.02% |
| random_mid | random (conc 32) | 5.08% |
| random_high | random (conc 100) | 11.24% |
| sharegpt_low | sharegpt (conc 1) | 17.51% |
| sharegpt_mid | sharegpt (conc 32) | 5.65% |
| sharegpt_high | sharegpt (conc 100) | 8.73% |

**Peak: 19.0% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 128000], [], [], []]`
- `[[1, 2048], [2048, 128000]]`
- `[[102], [], [], []]`
- `[[103], [103], []]`
- `[[103], [], [], []]`
- `[[14750, 2048], [2048, 14336]]`
- `[[16384, 2048], [2048, 14336]]`
- `[[16384, 7168], [7168, 2048]]`
- `[[1], [], [], [], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`

## Reproduce the deployment (cookbook-aligned)
```bash
sglang serve --model-path LiquidAI/LFM2.5-8B-A1B --tp 1 --attention-backend flashinfer --reasoning-parser qwen3 --tool-call-parser lfm2
```

After optimizing, re-run the **random_low** scenario to validate the e2e effect:
`bench_serving --dataset-name random ... --max-concurrency 1`.
