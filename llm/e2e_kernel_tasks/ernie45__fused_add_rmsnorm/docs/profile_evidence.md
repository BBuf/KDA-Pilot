# Profile evidence — ernie45__fused_add_rmsnorm

**e2e-optimization target: 4.5% of total GPU time** (max across scenarios) on
`baidu/ERNIE-4.5-21B-A3B-PT`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `baidu/ERNIE-4.5-21B-A3B-PT` (slug `ernie45`, tp=1)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.34% |
| sharegpt | conc 1 | 4.46% |

**Peak: 4.5% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 103424], [], [], []]`
- `[[1, 1], [1, 1], []]`
- `[[1], [], [], [], []]`
- `[[1]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path baidu/ERNIE-4.5-21B-A3B-PT --tp 1
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
