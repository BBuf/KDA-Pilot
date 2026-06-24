# Profile evidence — qwen35__linear_gemm

**e2e-optimization target: 40.7% of total GPU time** (max across scenarios) on
`nvidia/Qwen3.5-397B-A17B-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` (slug `qwen35`, tp=4)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT`, `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_TNT`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x16_64x16_1x2_h_bz_TNT`, `nvjet_sm100_tst_64x24_64x16_2x1_v_bz_splitK_TNT`, `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT`, `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 40.32% |
| random | conc 32 | 19.52% |
| random | conc 100 | 19.78% |
| sharegpt | conc 1 | 40.69% |
| sharegpt | conc 32 | 20.52% |
| sharegpt | conc 100 | 10.03% |

**Peak: 40.7% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 20968, 16, 128], []]`
- `[[10501, 4096], [4096, 5120]]`
- `[[17, 4096], [4096, 4608]]`
- `[[17, 4096], [4096, 5120]]`
- `[[17, 4096], [4096, 512]]`
- `[[17, 4096], [], [], [], [], []]`
- `[[17070, 4096], [1, 4096], []]`
- `[[17070, 4096], [4096, 512]]`
- `[[1], [1], []]`
- `[[1]]`
- `[[20968, 8, 256], [], [], [], [], []]`
- `[[267, 4096], [4096, 512]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/Qwen3.5-397B-A17B-NVFP4 --tp 4 --reasoning-parser qwen3 --tool-call-parser qwen3_coder
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
