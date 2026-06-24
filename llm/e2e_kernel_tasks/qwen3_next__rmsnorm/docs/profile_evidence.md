# Profile evidence — qwen3_next__rmsnorm

**e2e-optimization target: 6.8% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-Next-80B-A3B-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct` (slug `qwen3_next`, tp=8)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gm`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.00% |
| random | conc 32 | 6.79% |

**Peak: 6.8% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[2], [2], []]`
- `[[33], [33], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-Next-80B-A3B-Instruct --tp 8
```
After optimizing, re-run **random_mid** to validate the e2e effect.
