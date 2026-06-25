# Profile evidence — glm_46__rmsnorm

**e2e-optimization target: 3.4% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.6-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-4.6-FP8` (slug `glm_46`, tp=8)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `norm`
- GPU kernel(s): `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloa`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 2.82% |
| sharegpt | conc 32 | 3.35% |

**Peak: 3.4% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[14, 18944]]`
- `[[1], []]`
- `[[7680, 1, 128], [], [], [], []]`
- `[[8125, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [27], [], [], `

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.6-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
