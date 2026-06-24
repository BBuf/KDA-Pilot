# Profile evidence — deepseek_v31__fp8_bmm

**e2e-optimization target: 12.1% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-V3.1`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `deepseek-ai/DeepSeek-V3.1` (slug `deepseek_v31`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_d`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_ds`, `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsF`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.71% |
| random | conc 32 | 7.09% |
| sharegpt | conc 32 | 12.14% |

**Peak: 12.1% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[1]]`
- `[[256], [], [], [], []]`
- `[[262], [], [], []]`
- `[[31]]`
- `[[32], [], [], []]`
- `[[32]]`
- `[[48], [], [], []]`
- `[[5333, 1, 512], []]`
- `[[74], [], [], []]`
- `[[896], [], [], []]`
- `[[[1]], [], [], [], [], []]`
- `[[[37], [6]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-V3.1 --tp 8 --speculative-algorithm EAGLE --trust-remote-code
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
