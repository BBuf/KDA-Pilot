# Profile evidence — ministral3_14b__fused_add_rmsnorm

**e2e-optimization target: 5.7% of total GPU time** (max across scenarios) on
`mistralai/Ministral-3-14B-Instruct-2512`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Ministral-3-14B-Instruct-2512` (slug `ministral3_14b`, tp=1)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.75% |
| random | conc 32 | 4.56% |
| random | conc 100 | 4.33% |
| sharegpt | conc 1 | 5.69% |
| sharegpt | conc 32 | 4.38% |
| sharegpt | conc 100 | 4.54% |

**Peak: 5.7% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 131072], [1, 131072], []]`
- `[[1228, 32, 128], [1228, 8, 128], [262400, 128], [1228], [], []]`
- `[[1316, 32, 128], [1316, 8, 128], [262400, 128], [1316], [], []]`
- `[[1316], []]`
- `[[1316]]`
- `[[1], [1], []]`
- `[[30, 5120], []]`
- `[[32], [32], []]`
- `[[39, 5120], []]`
- `[[512], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Ministral-3-14B-Instruct-2512 --tp 1 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
