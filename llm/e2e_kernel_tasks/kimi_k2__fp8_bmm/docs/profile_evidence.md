# Profile evidence — kimi_k2__fp8_bmm

**e2e-optimization target: 38.5% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-K2-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `moonshotai/Kimi-K2-Instruct` (slug `kimi_k2`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_d`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_d`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_ds`, `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 13.16% |
| random | conc 32 | 6.77% |
| random | conc 100 | 21.20% |
| sharegpt | conc 1 | 10.91% |
| sharegpt | conc 32 | 14.13% |
| sharegpt | conc 100 | 38.52% |

**Peak: 38.5% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[100], [100], []]`
- `[[104, 163840], [], [], []]`
- `[[104], [], [], []]`
- `[[1450, 4096], [1450, 4096], []]`
- `[[1536, 8, 512], [1536, 1, 512], [1536, 1, 512], [1536, 4096], [], [], [1536, 8,`
- `[[17, 7168], [7168, 20480]]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[24], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-K2-Instruct --tp 8 --tool-call-parser kimi_k2
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
