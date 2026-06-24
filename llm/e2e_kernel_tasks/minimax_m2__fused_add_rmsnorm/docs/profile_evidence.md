# Profile evidence — minimax_m2__fused_add_rmsnorm

**e2e-optimization target: 6.2% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2` (slug `minimax_m2`, tp=4)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.18% |
| random | conc 100 | 2.57% |
| sharegpt | conc 1 | 6.05% |

**Peak: 6.2% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[0], [], [], []]`
- `[[1, 200064], [], []]`
- `[[1], [1], []]`
- `[[1]]`
- `[[[128]], []]`
- `[[[384], [44]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2 --tp 4 --reasoning-parser minimax-append-think --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
