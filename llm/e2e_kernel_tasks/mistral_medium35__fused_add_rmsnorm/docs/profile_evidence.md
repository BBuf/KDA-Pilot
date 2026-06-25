# Profile evidence — mistral_medium35__fused_add_rmsnorm

**e2e-optimization target: 6.5% of total GPU time** (max across scenarios) on
`mistralai/Mistral-Medium-3.5-128B`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Mistral-Medium-3.5-128B` (slug `mistral_medium35`, tp=2)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 6.47% |

**Peak: 6.5% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[39, 12288], [12288, 7168], [39, 1], [7168, 1], [], []]`
- `[[39, 14336], []]`
- `[[39], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Mistral-Medium-3.5-128B --tp 2 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **random_mid** to validate the e2e effect.
