# Profile evidence — ring_25_1t__fused_add_rmsnorm

**e2e-optimization target: 3.6% of total GPU time** (max across scenarios) on
`inclusionAI/Ring-2.5-1T`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `inclusionAI/Ring-2.5-1T` (slug `ring_25_1t`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 100 | 3.60% |

**Peak: 3.6% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[41]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path inclusionAI/Ring-2.5-1T --tp 8 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
