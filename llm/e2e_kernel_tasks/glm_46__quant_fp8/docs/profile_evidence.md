# Profile evidence — glm_46__quant_fp8

**e2e-optimization target: 6.4% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.6-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-4.6-FP8` (slug `glm_46`, tp=8)
- Python interface: `<confirm via capture; profiler family=quant_fp8>`
- Kernel family: `quant_fp8`  ·  Category: `quant_gemm`
- GPU kernel(s): `void per_token_quant_fp8_kernel<__nv_bfloat16, __nv_fp8_e4m3, 8, 16, false>(__nv_bfloat16 `, `void per_token_quant_fp8_small_batch_kernel<__nv_bfloat16, __nv_fp8_e4m3, 16>(__nv_bfloat1`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.42% |
| random | conc 100 | 2.58% |
| sharegpt | conc 1 | 6.15% |
| sharegpt | conc 32 | 2.22% |
| sharegpt | conc 100 | 3.10% |

**Peak: 6.4% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[103], [], [], []]`
- `[[1299, 1536], [1299, 1536], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[2048, 1536], [2048, 1, 128], [2048, 1, 128], [2048, 1536], [], [], [], [], [],`
- `[[2193, 12, 128]]`
- `[[2310, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [37], [], [], `
- `[[32], [32], []]`
- `[[[512]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.6-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **random_low** to validate the e2e effect.
