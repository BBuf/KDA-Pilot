# Profile evidence — glm_51__fp8_bmm

**e2e-optimization target: 19.0% of total GPU time** (max across scenarios) on
`zai-org/GLM-5.1-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-5.1-FP8` (slug `glm_51`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_d`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_ds`, `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 18.98% |
| random | conc 100 | 10.63% |
| sharegpt | conc 32 | 6.46% |
| sharegpt | conc 100 | 2.97% |

**Peak: 19.0% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[11247, 128], []]`
- `[[13693], [], [], []]`
- `[[1], [1], []]`
- `[[31], [], [], [], [], [], []]`
- `[[49], [49], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-5.1-FP8 --tp 8 --tool-call-parser glm47 --reasoning-parser glm45
```
After optimizing, re-run **random_mid** to validate the e2e effect.
