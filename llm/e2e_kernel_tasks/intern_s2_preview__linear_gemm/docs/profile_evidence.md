# Profile evidence — intern_s2_preview__linear_gemm

**e2e-optimization target: 42.0% of total GPU time** (max across scenarios) on
`internlm/Intern-S2-Preview`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `internlm/Intern-S2-Preview` (slug `intern_s2_preview`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_1x2_h_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 41.99% |
| random | conc 32 | 17.59% |
| random | conc 100 | 5.37% |
| sharegpt | conc 1 | 41.84% |
| sharegpt | conc 32 | 24.46% |
| sharegpt | conc 100 | 21.69% |

**Peak: 42.0% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 2048], [], []]`
- `[[1, 251392], [], [], []]`
- `[[1, 251392], [], []]`
- `[[17, 2048], [2048, 128]]`
- `[[17, 2048], [2048, 1536]]`
- `[[1], [1], []]`
- `[[267, 2048], [2048, 128]]`
- `[[267, 2048], []]`
- `[[274, 2048], [2048, 128]]`
- `[[38, 2048], [2048, 128]]`
- `[[38, 2048], [2048, 1536]]`
- `[[46, 2048], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path internlm/Intern-S2-Preview --tp 8 --reasoning-parser qwen3 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_low** to validate the e2e effect.
