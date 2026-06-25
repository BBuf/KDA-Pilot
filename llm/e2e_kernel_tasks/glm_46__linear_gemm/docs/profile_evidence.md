# Profile evidence — glm_46__linear_gemm

**e2e-optimization target: 7.1% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.6-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-4.6-FP8` (slug `glm_46`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10colle`, `cutlass3x_sm100_tensorop_s128x64x8tf32gemm_f32_f32_f32_f32_f32_128x64x32_0_tnn_align4_2sm_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 7.10% |
| random | conc 32 | 2.27% |
| random | conc 100 | 2.70% |
| sharegpt | conc 1 | 6.87% |
| sharegpt | conc 100 | 3.03% |

**Peak: 7.1% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[128], [], [], []]`
- `[[1299, 1536], [1299, 1536], []]`
- `[[19176, 128, 1, 128]]`
- `[[1], [1], []]`
- `[[1], []]`
- `[[1]]`
- `[[[0], [103]], []]`
- `[[[256], [111]], []]`
- `[[[384], [4]], []]`
- `[[[768]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.6-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **random_low** to validate the e2e effect.
