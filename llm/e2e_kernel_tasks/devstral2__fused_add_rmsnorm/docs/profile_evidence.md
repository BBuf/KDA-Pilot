# Profile evidence — devstral2__fused_add_rmsnorm

**e2e-optimization target: 10.6% of total GPU time** (max across scenarios) on
`mistralai/Devstral-2-123B-Instruct-2512`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Devstral-2-123B-Instruct-2512` (slug `devstral2`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 10.64% |
| random | conc 32 | 2.60% |
| random | conc 100 | 2.39% |
| sharegpt | conc 1 | 10.50% |
| sharegpt | conc 32 | 2.59% |
| sharegpt | conc 100 | 3.10% |

**Peak: 10.6% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[100], [], []]`
- `[[121], [], [], []]`
- `[[1760], [], [], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[256], [], [], [], [], [], []]`
- `[[32], [32], []]`
- `[[32], [], []]`
- `[[32], []]`
- `[[477], [], [], []]`
- `[[97], []]`
- `[[[768], [17]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Devstral-2-123B-Instruct-2512 --tp 8 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **random_low** to validate the e2e effect.
