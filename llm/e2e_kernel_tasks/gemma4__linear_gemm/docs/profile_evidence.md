# Profile evidence — gemma4__linear_gemm

**e2e-optimization target: 29.0% of total GPU time** (max across scenarios) on
`google/gemma-4-26B-A4B-it`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `google/gemma-4-26B-A4B-it` (slug `gemma4`, tp=1)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x192_64x7_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_128x256_64x4_1x2_h_bz_TNT`, `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_256x8_64x6_2x1_v_bz_TNT`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x64_64x16_2x2_2cta_h_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 28.06% |
| random | conc 32 | 15.97% |
| random | conc 100 | 2.17% |
| sharegpt | conc 1 | 29.00% |
| sharegpt | conc 32 | 12.41% |

**Peak: 29.0% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 1], [1, 1], []]`
- `[[1, 262144], [], []]`
- `[[1, 2816], [2816, 262144]]`
- `[[100], [100], []]`
- `[[100], [], []]`
- `[[11254, 2816], [2816, 10240]]`
- `[[11254, 2816], [2816, 4224]]`
- `[[11254, 2816], [2816, 8192]]`
- `[[1], [1], []]`
- `[[1], [], [], [], [], [], []]`
- `[[1], [], []]`
- `[[2049, 262148], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path google/gemma-4-26B-A4B-it --reasoning-parser gemma4 --tool-call-parser gemma4
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
