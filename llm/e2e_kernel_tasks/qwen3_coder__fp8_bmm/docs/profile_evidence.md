# Profile evidence — qwen3_coder__fp8_bmm

**e2e-optimization target: 34.0% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` (slug `qwen3_coder`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_E4m3E4m3_Fp32_t128x128x128u2_s5_et64x128_m64x128x32_c1x1x1_rM_TN_transOut_noS`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_ds`, `bmm_E4m3_E4m3E4m3_Fp32_t128x128x128u2_s5_et64x128_m64x128x32_c1x1x1_rM_TN_transOut_noShfl_`, `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 7.23% |
| random | conc 32 | 10.12% |
| random | conc 100 | 34.04% |
| sharegpt | conc 1 | 10.72% |
| sharegpt | conc 32 | 29.35% |
| sharegpt | conc 100 | 32.19% |

**Peak: 34.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[0], [0], []]`
- `[[1, 2], [1, 2], []]`
- `[[100], [], []]`
- `[[100]]`
- `[[104, 91], [104, 91], []]`
- `[[1950], [], [], [], [], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], [], [], [], []]`
- `[[1], [], [], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[2048, 1536], [2048, 1, 128], [2048, 1, 128], [2048, 1536], [], [], [], [], [],`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --tp 8 --ep 8 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_high** to validate the e2e effect.
