# Profile evidence — hunyuan3_preview__linear_gemm

**e2e-optimization target: 8.4% of total GPU time** (max across scenarios) on
`tencent/Hy3-preview`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `tencent/Hy3-preview` (slug `hunyuan3_preview`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `gemm`
- GPU kernel(s): `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x128x16_1x1x1_3_tnn_align1_bias_f32_relu`, `nvjet_hsh_32x64_64x16_4x1_v_bz_splitK_TNN`, `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.96% |
| random | conc 32 | 8.42% |
| sharegpt | conc 1 | 5.50% |

**Peak: 8.4% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1, 3], [1, 3], [1], [200], [4], [1, 4], [1, 4], [1, 4], [], [], [], []]`
- `[[1, 3], [1, 3], [1], [248], [4], [1, 4], [1, 4], [1, 4], [], [], [], []]`
- `[[11225, 128], [], [], [], [], []]`
- `[[11225, 4096], [4096, 192]]`
- `[[1], [], [], [], []]`
- `[[1]]`
- `[[2], []]`
- `[[38, 4096], [4096, 192]]`
- `[[38, 4096], [], [], [], [], [], []]`
- `[[4], [4], []]`
- `[[[1, 1], [1, 3]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path tencent/Hy3-preview --tp 8 --speculative-algorithm EAGLE --speculative-num-steps 3 --speculative-eagle-topk 1
```
After optimizing, re-run **random_mid** to validate the e2e effect.
