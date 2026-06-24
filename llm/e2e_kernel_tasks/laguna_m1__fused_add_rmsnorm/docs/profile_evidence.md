# Profile evidence — laguna_m1__fused_add_rmsnorm

**e2e-optimization target: 5.5% of total GPU time** (max across scenarios) on
`poolside/Laguna-M.1-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `poolside/Laguna-M.1-NVFP4` (slug `laguna_m1`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.50% |
| random | conc 100 | 2.41% |
| sharegpt | conc 1 | 5.51% |
| sharegpt | conc 100 | 2.01% |

**Peak: 5.5% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[104], [104], []]`
- `[[192], [192], []]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[1], []]`
- `[[256], [256], []]`
- `[[[0], [5]], []]`
- `[[[256], [21]], []]`
- `[[[512], [55]], []]`
- `[[]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path poolside/Laguna-M.1-NVFP4 --tp 8 --trust-remote-code --reasoning-parser poolside_v1 --tool-call-parser poolside_v1
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
