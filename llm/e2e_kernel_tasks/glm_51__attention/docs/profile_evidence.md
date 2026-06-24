# Profile evidence — glm_51__attention

**e2e-optimization target: 3.8% of total GPU time** (max across scenarios) on
`zai-org/GLM-5.1-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-5.1-FP8` (slug `glm_51`, tp=8)
- Python interface: `<confirm via capture; profiler family=attention>`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ8Kv128Pe`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| sharegpt | conc 32 | 3.82% |

**Peak: 3.8% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[4842, 1, 8, 576], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-5.1-FP8 --tp 8 --tool-call-parser glm47 --reasoning-parser glm45
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
