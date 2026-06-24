# Profile evidence — glm_5__void_anonymous_namespace_fast_ha

**e2e-optimization target: 3.7% of total GPU time** (max across scenarios) on
`nvidia/GLM-5-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/GLM-5-NVFP4` (slug `glm_5`, tp=4)
- Python interface: `<confirm via capture; profiler family=void_anonymous_namespace_fast_ha>`
- Kernel family: `void_anonymous_namespace_fast_ha`  ·  Category: `other`
- GPU kernel(s): `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHada`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| sharegpt | conc 32 | 2.73% |
| sharegpt | conc 100 | 3.73% |

**Peak: 3.7% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[20784, 32, 128], []]`
- `[[9962, 32, 128], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/GLM-5-NVFP4 --tp 4 --quantization modelopt_fp4 --kv-cache-dtype fp8_e4m3
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
