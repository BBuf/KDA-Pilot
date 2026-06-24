# Profile evidence — qwen3__fp8_bmm

**e2e-optimization target: 32.0% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-235B-A22B-Instruct-2507`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507` (slug `qwen3`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `other`
- GPU kernel(s): `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x128x64u2_s6_et128x128_m256x128x16_c2x1x1_rM_BN_tra`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128_s6_et128x16_m128x16x16_c1x1x1_rM_BN_transOu`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s3_et128x16_m128x16x16_c1x1x1_rM_BN_trans`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s5_et128x16_m128x16x16_c1x1x1_rM_BN_trans`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOu`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_trans`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_s`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_s`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s6_et128x8_m128x8x16_c1x1x1_rM_BN_transOut`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 16.27% |
| random | conc 32 | 31.99% |
| random | conc 100 | 23.82% |
| sharegpt | conc 1 | 10.81% |
| sharegpt | conc 32 | 27.31% |
| sharegpt | conc 100 | 24.30% |

**Peak: 32.0% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[0], [0], []]`
- `[[0], [], [], [], []]`
- `[[1, 151936], [1, 151936], []]`
- `[[1, 1], [1, 1], []]`
- `[[100], [100], []]`
- `[[100], [], []]`
- `[[100]]`
- `[[104, 17], [104, 17], []]`
- `[[10735, 1024], [10735, 1024], []]`
- `[[14, 151936], [], [], []]`
- `[[14]]`
- `[[1], [1], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-235B-A22B-Instruct-2507 --tp 8
```
After optimizing, re-run **random_mid** to validate the e2e effect.
