# Profile evidence — kimi_k26__sgl_kernel_dsv3_fused_a_gemm

**e2e-optimization target: 39.0% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-K2.6`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `moonshotai/Kimi-K2.6` (slug `kimi_k26`, tp=8)
- Python interface: `sgl_kernel.dsv3_fused_a_gemm`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x16_64x16_1x4_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitK_TNT`, `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT`, `nvjet_sm100_tst_96x64_64x15_2x2_2cta_h_bz_splitK_TNN`, `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 con`, `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 cons`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 38.96% |
| random | conc 32 | 9.78% |
| random | conc 100 | 18.70% |
| sharegpt | conc 1 | 25.96% |
| sharegpt | conc 32 | 14.93% |
| sharegpt | conc 100 | 29.82% |

**Peak: 39.0% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 2112], [1, 7168], [7168, 2112]]`
- `[[15, 2112], [15, 7168], [7168, 2112]]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[38, 7168], [512, 7168], []]`
- `[[38, 7168], [7168, 2112]]`
- `[[38, 7168], [7168, 384]]`
- `[[38, 8, 256], [], [], []]`
- `[[3943, 128004], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-K2.6 --tp 8 --reasoning-parser kimi_k2 --tool-call-parser kimi_k2
```
After optimizing, re-run **random_low** to validate the e2e effect.
