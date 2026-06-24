# Profile evidence — kimi_k25__fp8_bmm

**e2e-optimization target: 22.7% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-K2.5`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `moonshotai/Kimi-K2.5` (slug `kimi_k25`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m128x16x16_c1x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m256x16x16_c2x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256u2_s3_et128x16_m256x16x16_c2`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m128x32x16_c1x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m256x32x16_c2x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m128x32x16_c1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m256x32x16_c2`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256_s3_et128x64_m128x64x16_c1x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256u2_s3_et128x64_m128x64x16_c1`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.66% |
| random | conc 32 | 18.79% |
| random | conc 100 | 22.72% |
| sharegpt | conc 1 | 5.23% |
| sharegpt | conc 100 | 8.31% |

**Peak: 22.7% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[100], [100], []]`
- `[[100], [], []]`
- `[[11218, 7168], [7168, 2112]]`
- `[[15, 7168], [7168, 512]]`
- `[[1], [1], []]`
- `[[1]]`
- `[[2957, 7168]]`
- `[[2], [2], []]`
- `[[32], [32], []]`
- `[[32], [], []]`
- `[[[11218, 7168]], [], [], [], [], []]`
- `[[[256]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-K2.5 --tp 8 --reasoning-parser kimi_k2 --tool-call-parser kimi_k2
```
After optimizing, re-run **random_high** to validate the e2e effect.
