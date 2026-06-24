# Profile evidence — gpt_oss_120b__rmsnorm

**e2e-optimization target: 7.0% of total GPU time** (max across scenarios) on
`openai/gpt-oss-120b`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `openai/gpt-oss-120b` (slug `gpt_oss_120b`, tp=8)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `norm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gm`, `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloa`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.46% |
| random | conc 32 | 6.98% |
| sharegpt | conc 32 | 2.24% |

**Peak: 7.0% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1], [], [], [], [], []]`
- `[[1], []]`
- `[[32], [32], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path openai/gpt-oss-120b --tp 8
```
After optimizing, re-run **random_mid** to validate the e2e effect.
