# Profile evidence — qwen3_coder_next__fp8_bmm

**e2e-optimization target: 15.6% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-Coder-Next`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-Coder-Next` (slug `qwen3_coder_next`, tp=2)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `other`
- GPU kernel(s): `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_trans`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s6_et128x8_m128x8x16_c1x1x1_rM_BN_transOut`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 15.65% |
| random | conc 100 | 13.83% |
| sharegpt | conc 1 | 5.75% |
| sharegpt | conc 32 | 11.14% |
| sharegpt | conc 100 | 5.90% |

**Peak: 15.6% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1, 151936], [], [], []]`
- `[[1, 151936], [], []]`
- `[[16384, 2048], [2048, 32]]`
- `[[16384, 2048], []]`
- `[[16384, 2048]]`
- `[[1], [1], []]`
- `[[32, 151936], [], [], []]`
- `[[32, 151936], [], []]`
- `[[32], [32], []]`
- `[[32], [], [], []]`
- `[[33], [33], []]`
- `[[9739, 2048]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-Coder-Next --tp 2 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_mid** to validate the e2e effect.
