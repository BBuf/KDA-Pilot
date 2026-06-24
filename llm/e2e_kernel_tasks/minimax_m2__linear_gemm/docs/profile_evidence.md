# Profile evidence — minimax_m2__linear_gemm

**e2e-optimization target: 25.5% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2` (slug `minimax_m2`, tp=4)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `_w8a8_block_fp8_matmul`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu`, `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu`, `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 25.51% |
| random | conc 32 | 22.37% |
| random | conc 100 | 17.31% |
| sharegpt | conc 1 | 25.04% |
| sharegpt | conc 32 | 20.54% |
| sharegpt | conc 100 | 18.10% |

**Peak: 25.5% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[0], [0], []]`
- `[[11], [], [], []]`
- `[[16384], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[25357, 64, 2, 128], [], [], []]`
- `[[256, 2, 128], [], [], [], []]`
- `[[256], [], [], [], []]`
- `[[2797, 2, 128], []]`
- `[[3027, 1536], []]`
- `[[455], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2 --tp 4 --reasoning-parser minimax-append-think --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
