# Profile evidence — qwen3__linear_gemm

**e2e-optimization target: 28.8% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-235B-A22B-Instruct-2507`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507` (slug `qwen3`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x16_64x16_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_64x16_64x16_2x2_2cta_h_bz_TNT`, `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 25.06% |
| random | conc 32 | 7.36% |
| random | conc 100 | 7.88% |
| sharegpt | conc 1 | 28.85% |
| sharegpt | conc 32 | 8.49% |
| sharegpt | conc 100 | 7.54% |

**Peak: 28.8% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[0], [0], []]`
- `[[1, 151936], [], []]`
- `[[1, 1], [1, 1], []]`
- `[[100], [100], []]`
- `[[10752, 1024], [10752, 1, 128], [10752, 1, 128], [10752, 1024], [], [], [], [],`
- `[[17, 1024], [17, 1024], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[20, 1, 128], [], [], [], []]`
- `[[20, 1024], [20, 1, 128], [20, 1, 128], [20, 1024], [], [], [], [], [], [], [],`
- `[[20, 1024], [], [], [], []]`
- `[[252], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-235B-A22B-Instruct-2507 --tp 8
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
