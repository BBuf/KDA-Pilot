# Profile evidence — minimax_m27__fused_add_rmsnorm

**e2e-optimization target: 12.6% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.7`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.7` (slug `minimax_m27`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 12.36% |
| random | conc 32 | 3.29% |
| random | conc 100 | 5.75% |
| sharegpt | conc 1 | 12.55% |
| sharegpt | conc 32 | 2.75% |
| sharegpt | conc 100 | 3.24% |

**Peak: 12.6% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[100], [100], []]`
- `[[104], [104], []]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[1], [], []]`
- `[[32], [32], []]`
- `[[32], [], []]`
- `[[512], [], [], []]`
- `[[729], [], [], []]`
- `[[96], [], []]`
- `[[99], [99], []]`
- `[[[0], [21]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.7 --tp 8 --ep 8 --tool-call-parser minimax-m2 --reasoning-parser minimax-append-think
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
