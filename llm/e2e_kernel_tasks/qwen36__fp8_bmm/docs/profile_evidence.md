# Profile evidence — qwen36__fp8_bmm

**e2e-optimization target: 15.9% of total GPU time** (max across scenarios) on
`Qwen/Qwen3.6-35B-A3B-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3.6-35B-A3B-FP8` (slug `qwen36`, tp=1)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `quant_gemm`
- GPU kernel(s): `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_d`, `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_ds`, `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsF`, `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 15.94% |
| random | conc 100 | 9.06% |
| sharegpt | conc 1 | 6.49% |
| sharegpt | conc 100 | 4.67% |

**Peak: 15.9% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[128], [128], []]`
- `[[188, 248320], [], []]`
- `[[188], [188], []]`
- `[[1]]`
- `[[32, 4], [32, 4], []]`
- `[[4, 2048], [], [], []]`
- `[[44], [44], [44]]`
- `[[46], [], []]`
- `[[47], [47], []]`
- `[[48], [48], []]`
- `[[49], [49], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3.6-35B-A3B-FP8 --reasoning-parser qwen3 --tool-call-parser qwen3_coder --speculative-algorithm EAGLE --speculative-num-steps 3 --speculative-eagle-topk 1
```
After optimizing, re-run **random_mid** to validate the e2e effect.
