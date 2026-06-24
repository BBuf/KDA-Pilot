# Profile evidence — kimi_linear__linear_gemm

**e2e-optimization target: 16.5% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-Linear-48B-A3B-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct` (slug `kimi_linear`, tp=4)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_16x64_64x16_2x1_v_bz_TNN`, `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 16.53% |
| random | conc 100 | 2.88% |
| sharegpt | conc 1 | 4.23% |

**Peak: 16.5% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 163840], [], [], [], []]`
- `[[1, 163840], [], [], []]`
- `[[1, 163840], [], []]`
- `[[16384, 2, 128], [], [], []]`
- `[[1], [1], []]`
- `[[1]]`
- `[[2], [2], []]`
- `[[3577], [], [], [], []]`
- `[[47], [], [], []]`
- `[[80], [], [], []]`
- `[[[1]], [], [], [], [], []]`
- `[[], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-Linear-48B-A3B-Instruct --tp 4 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
