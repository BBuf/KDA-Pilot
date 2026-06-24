# Profile evidence — glm_5__linear_gemm

**e2e-optimization target: 33.9% of total GPU time** (max across scenarios) on
`nvidia/GLM-5-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/GLM-5-NVFP4` (slug `glm_5`, tp=4)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_192x288_64x5_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_TNT`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 32.24% |
| random | conc 32 | 14.22% |
| random | conc 100 | 18.55% |
| sharegpt | conc 1 | 33.85% |
| sharegpt | conc 32 | 15.95% |
| sharegpt | conc 100 | 15.28% |

**Peak: 33.9% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 154880], [], [], []]`
- `[[1, 154880], [], []]`
- `[[1, 1], [1, 1], []]`
- `[[1024, 384], []]`
- `[[16873, 2048], [2048, 4096]]`
- `[[16873, 4096], [4096, 6144]]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[20784, 16, 256], [], []]`
- `[[20784, 2048], [20784, 2048], []]`
- `[[20784, 6144], [6144, 2624]]`
- `[[2128, 202756], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/GLM-5-NVFP4 --tp 4 --quantization modelopt_fp4 --kv-cache-dtype fp8_e4m3
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
