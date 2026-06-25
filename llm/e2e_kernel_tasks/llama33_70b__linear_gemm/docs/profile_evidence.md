# Profile evidence — llama33_70b__linear_gemm

**e2e-optimization target: 86.6% of total GPU time** (max across scenarios) on
`meta-llama/Llama-3.3-70B-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `meta-llama/Llama-3.3-70B-Instruct` (slug `llama33_70b`, tp=1)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_128x256_64x6_2x2_2cta_h_bz_TNT`, `nvjet_sm100_tst_128x32_64x10_4x1_v_bz_splitK_TNT`, `nvjet_sm100_tst_128x48_64x9_4x1_v_bz_splitK_TNT`, `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_splitK_TNT`, `nvjet_sm100_tst_192x256_64x5_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_256x24_64x6_2x1_v_bz_splitK_TNT`, `nvjet_sm100_tst_256x256_64x4_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_256x256_64x4_2x2_2cta_h_bz_TNT`, `nvjet_sm100_tst_256x8_64x6_2x1_v_bz_splitK_TNT`, `nvjet_sm100_tst_320x192_64x4_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_320x192_64x4_2x2_2cta_h_bz_TNT`, `nvjet_sm100_tst_448x64_64x3_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_512x24_64x3_4x1_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_2x1_v_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 86.06% |
| random | conc 32 | 86.60% |
| random | conc 100 | 86.53% |
| sharegpt | conc 1 | 85.57% |
| sharegpt | conc 32 | 84.35% |
| sharegpt | conc 100 | 85.58% |

**Peak: 86.6% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1, 128256], [], [], []]`
- `[[1, 128256]]`
- `[[1, 8192], [8192, 128256]]`
- `[[103], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[20, 8192], [20, 8, 128], [20, 8, 128], [20, 8192], [], [], [], [], [], [], [],`
- `[[30], [30], []]`
- `[[32, 128256], [], [], []]`
- `[[32], [32], []]`
- `[[32]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path meta-llama/Llama-3.3-70B-Instruct --tp 1 --tool-call-parser llama3
```
After optimizing, re-run **random_mid** to validate the e2e effect.
