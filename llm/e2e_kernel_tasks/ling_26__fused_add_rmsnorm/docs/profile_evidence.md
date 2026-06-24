# Profile evidence — ling_26__fused_add_rmsnorm

**e2e-optimization target: 18.0% of total GPU time** (max across scenarios) on
`inclusionAI/Ling-2.6-flash`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `inclusionAI/Ling-2.6-flash` (slug `ling_26`, tp=4)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 100 | 17.97% |

**Peak: 18.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[39, 4096], [], []]`
- `[[39, 4096], []]`
- `[[], [39, 512], [39, 256]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path inclusionAI/Ling-2.6-flash --tp 4 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
