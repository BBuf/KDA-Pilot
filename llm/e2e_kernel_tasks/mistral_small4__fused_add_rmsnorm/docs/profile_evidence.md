# Profile evidence — mistral_small4__fused_add_rmsnorm

**e2e-optimization target: 3.8% of total GPU time** (max across scenarios) on
`mistralai/Mistral-Small-4-119B-2603`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Mistral-Small-4-119B-2603` (slug `mistral_small4`, tp=1)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.67% |
| sharegpt | conc 1 | 3.79% |
| sharegpt | conc 32 | 2.44% |

**Peak: 3.8% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[0], [], [], [], []]`
- `[[18, 4096], [18, 4096], []]`
- `[[38, 4096], [38, 4096], []]`
- `[[5519, 4096], []]`
- `[[5519, 6144], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Mistral-Small-4-119B-2603 --tp 1 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
