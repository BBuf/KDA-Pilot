# Profile evidence — qwen3_next__linear_gemm

**e2e-optimization target: 44.3% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-Next-80B-A3B-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct` (slug `qwen3_next`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x8_64x16_1x2_h_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 41.20% |
| random | conc 32 | 16.21% |
| random | conc 100 | 29.40% |
| sharegpt | conc 1 | 44.27% |
| sharegpt | conc 32 | 22.66% |
| sharegpt | conc 100 | 18.96% |

**Peak: 44.3% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 151936], [], [], []]`
- `[[17, 2048], [2048, 128]]`
- `[[17, 2048], [2048, 1536]]`
- `[[17, 2048], [2048, 8]]`
- `[[17, 2048], []]`
- `[[1], [1], []]`
- `[[2048, 64]]`
- `[[262, 2048], [2048, 128]]`
- `[[262, 4, 128], []]`
- `[[32], [32], []]`
- `[[38, 2048], [2048, 128]]`
- `[[38, 2048], [2048, 1536]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-Next-80B-A3B-Instruct --tp 8
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
