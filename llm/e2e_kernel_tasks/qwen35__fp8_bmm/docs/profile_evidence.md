# Profile evidence — qwen35__fp8_bmm

**e2e-optimization target: 16.0% of total GPU time** (max across scenarios) on
`nvidia/Qwen3.5-397B-A17B-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` (slug `qwen35`, tp=4)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x8x256_s9_et128x8_m128x8x64_c1x1x1_rM_TN_transOut`, `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x128x256_s6_et128x128_m256x128x64_c2x1x1_r`, `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x`, `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOu`, `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512u2_s5_et128x8_m128x8x64_c1x1x1_rM_TN_trans`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 15.98% |
| random | conc 100 | 13.66% |
| sharegpt | conc 32 | 2.19% |
| sharegpt | conc 100 | 5.21% |

**Peak: 16.0% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1, 20968, 4, 128], [1, 20968, 4, 128], [1, 20968, 16, 128], [1, 20968, 16], [1`
- `[[100], [], []]`
- `[[104], [], [], []]`
- `[[17070, 16, 128], []]`
- `[[17070, 4096], [4096, 1]]`
- `[[17070, 4096], [], [], [], [], [], []]`
- `[[17070, 4096], []]`
- `[[1]]`
- `[[20968, 2048], [2048, 4096]]`
- `[[3, 32], [3, 32], []]`
- `[[30758, 4096], []]`
- `[[31, 62080]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/Qwen3.5-397B-A17B-NVFP4 --tp 4 --reasoning-parser qwen3 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_mid** to validate the e2e effect.
