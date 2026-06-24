# Profile evidence — laguna_m1__linear_gemm

**e2e-optimization target: 36.6% of total GPU time** (max across scenarios) on
`poolside/Laguna-M.1-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `poolside/Laguna-M.1-NVFP4` (slug `laguna_m1`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalINS1_17GroupProblemShapeIN4cute5t`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 25.39% |
| random | conc 32 | 30.37% |
| random | conc 100 | 36.60% |
| sharegpt | conc 1 | 25.53% |
| sharegpt | conc 32 | 28.22% |
| sharegpt | conc 100 | 35.54% |

**Peak: 36.6% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[100], [100], []]`
- `[[10526, 1024], [10526, 1024], []]`
- `[[15], [], [], []]`
- `[[17], [], [], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[2276, 1024], [2276, 1024], []]`
- `[[256], [256], []]`
- `[[262148], [], [], []]`
- `[[2656, 1024], [2656, 1024], []]`
- `[[2731], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path poolside/Laguna-M.1-NVFP4 --tp 8 --trust-remote-code --reasoning-parser poolside_v1 --tool-call-parser poolside_v1
```
After optimizing, re-run **random_high** to validate the e2e effect.
