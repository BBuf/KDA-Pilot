# Profile evidence — glm_45__quant_fp8

**e2e-optimization target: 6.4% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.5-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-4.5-FP8` (slug `glm_45`, tp=8)
- Python interface: `<confirm via capture; profiler family=quant_fp8>`
- Kernel family: `quant_fp8`  ·  Category: `quant_gemm`
- GPU kernel(s): `void per_token_quant_fp8_small_batch_kernel<__nv_bfloat16, __nv_fp8_e4m3, 16>(__nv_bfloat1`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.42% |
| random | conc 100 | 2.61% |
| sharegpt | conc 1 | 5.99% |
| sharegpt | conc 100 | 2.91% |

**Peak: 6.4% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[0], [], [], []]`
- `[[103, 1536], [103, 1536], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[384], [384], []]`
- `[[384], [], [], []]`
- `[[[640]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.5-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **random_low** to validate the e2e effect.
