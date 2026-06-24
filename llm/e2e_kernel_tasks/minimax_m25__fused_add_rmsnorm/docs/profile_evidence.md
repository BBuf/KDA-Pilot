# Profile evidence — minimax_m25__fused_add_rmsnorm

**e2e-optimization target: 10.8% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.5`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.5` (slug `minimax_m25`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 10.79% |
| random | conc 32 | 2.91% |
| sharegpt | conc 1 | 10.78% |
| sharegpt | conc 32 | 2.51% |
| sharegpt | conc 100 | 2.97% |

**Peak: 10.8% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[192], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[32], [32], []]`
- `[[32], [], [], []]`
- `[[32], [], []]`
- `[[36], [], [], []]`
- `[[4097], [], [], [], []]`
- `[[[64], [576]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.5 --tp 8 --ep 8 --reasoning-parser minimax-append-think
```
After optimizing, re-run **random_low** to validate the e2e effect.
