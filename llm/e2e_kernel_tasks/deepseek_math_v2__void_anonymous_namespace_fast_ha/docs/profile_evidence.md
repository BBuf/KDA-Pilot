# Profile evidence — deepseek_math_v2__void_anonymous_namespace_fast_ha

**e2e-optimization target: 3.8% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-Math-V2`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `deepseek-ai/DeepSeek-Math-V2` (slug `deepseek_math_v2`, tp=8)
- Python interface: `<confirm via capture; profiler family=void_anonymous_namespace_fast_ha>`
- Kernel family: `void_anonymous_namespace_fast_ha`  ·  Category: `other`
- GPU kernel(s): `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHada`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 100 | 2.23% |
| sharegpt | conc 32 | 3.80% |
| sharegpt | conc 100 | 2.17% |

**Peak: 3.8% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[8661, 64, 128], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-Math-V2 --tp 8 --ep 8 --trust-remote-code
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
