# Profile evidence — kimi_k26__fp8_bmm

**e2e-optimization target: 21.0% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-K2.6`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `moonshotai/Kimi-K2.6` (slug `kimi_k26`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m128x16x16_c1x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m256x16x16_c2x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256u2_s3_et128x16_m256x16x16_c2`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m256x32x16_c2x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m256x32x16_c2`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256_s3_et128x64_m128x64x16_c1x1`, `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256u2_s3_et128x64_m128x64x16_c1`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.36% |
| random | conc 32 | 20.65% |
| random | conc 100 | 21.05% |
| sharegpt | conc 1 | 5.98% |
| sharegpt | conc 32 | 15.32% |
| sharegpt | conc 100 | 6.16% |

**Peak: 21.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[0], [0], []]`
- `[[0], [], [], []]`
- `[[100], [100], []]`
- `[[1], [1], []]`
- `[[1]]`
- `[[256], [256], []]`
- `[[257], [], [], []]`
- `[[2], [2], []]`
- `[[32], [32], []]`
- `[[32], [], []]`
- `[[32], []]`
- `[[4527, 256], [256, 7168]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-K2.6 --tp 8 --reasoning-parser kimi_k2 --tool-call-parser kimi_k2
```
After optimizing, re-run **random_high** to validate the e2e effect.
