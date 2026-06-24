# Profile evidence — minimax_m25__linear_gemm

**e2e-optimization target: 22.5% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.5`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.5` (slug `minimax_m25`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `_w8a8_block_fp8_matmul`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu`, `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 20.52% |
| random | conc 32 | 19.39% |
| random | conc 100 | 19.55% |
| sharegpt | conc 1 | 22.49% |
| sharegpt | conc 32 | 21.33% |
| sharegpt | conc 100 | 18.76% |

**Peak: 22.5% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[100], [100], []]`
- `[[196612], [], [], []]`
- `[[1], [1], []]`
- `[[1]]`
- `[[284], [], [], []]`
- `[[288, 768], [], [], [], []]`
- `[[3072, 1, 128], [], [], []]`
- `[[48, 1, 128], [], [], []]`
- `[[5632, 768], [], [], []]`
- `[[640], [640], []]`
- `[[64859, 1, 64, 128], [], [], []]`
- `[[64859, 64, 1, 128], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.5 --tp 8 --ep 8 --reasoning-parser minimax-append-think
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
