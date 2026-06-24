# Profile evidence — qwen35__fused_add_rmsnorm

**e2e-optimization target: 3.3% of total GPU time** (max across scenarios) on
`nvidia/Qwen3.5-397B-A17B-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4` (slug `qwen35`, tp=4)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 2.52% |
| random | conc 100 | 3.31% |

**Peak: 3.3% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[1], [1], []]`
- `[[1]]`
- `[[38, 4096], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/Qwen3.5-397B-A17B-NVFP4 --tp 4 --reasoning-parser qwen3 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_high** to validate the e2e effect.
