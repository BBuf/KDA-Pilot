# Profile evidence — kimi_linear__fused_add_rmsnorm

**e2e-optimization target: 5.6% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-Linear-48B-A3B-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct` (slug `kimi_linear`, tp=4)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.62% |
| random | conc 100 | 2.66% |
| sharegpt | conc 1 | 2.09% |
| sharegpt | conc 100 | 2.64% |

**Peak: 5.6% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 16384, 8, 64], []]`
- `[[16384, 1024], [1024, 2304]]`
- `[[16384, 2304], [256, 512, 2304], [256, 2304, 256], [16384, 8], [16384, 8], [], `
- `[[16384, 2304]]`
- `[[1], [], [], [], []]`
- `[[1]]`
- `[[2], [2], []]`
- `[[35], [], [], [], [], [], [], []]`
- `[[38], [38], []]`
- `[[[1], [1], [1], [1]], [[1], [1], [1], [1]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-Linear-48B-A3B-Instruct --tp 4 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
