# Profile evidence — deepseek_math_v2__fp8_bmm

**e2e-optimization target: 24.7% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-Math-V2`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `deepseek-ai/DeepSeek-Math-V2` (slug `deepseek_math_v2`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_ds`, `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_sc`, `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.93% |
| random | conc 100 | 24.66% |
| sharegpt | conc 1 | 2.33% |
| sharegpt | conc 32 | 9.02% |
| sharegpt | conc 100 | 21.99% |

**Peak: 24.7% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[1, 1], [1, 1], []]`
- `[[100], [100], []]`
- `[[100], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[32], [32], []]`
- `[[32], [], []]`
- `[[3], [3], []]`
- `[[4097, 163844], [], [], []]`
- `[[768], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-Math-V2 --tp 8 --ep 8 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
