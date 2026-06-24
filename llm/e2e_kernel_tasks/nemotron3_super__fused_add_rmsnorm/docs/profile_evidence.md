# Profile evidence — nemotron3_super__fused_add_rmsnorm

**e2e-optimization target: 3.6% of total GPU time** (max across scenarios) on
`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` (slug `nemotron3_super`, tp=4)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.57% |
| sharegpt | conc 1 | 3.45% |

**Peak: 3.6% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 131072], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 --tp 4 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
