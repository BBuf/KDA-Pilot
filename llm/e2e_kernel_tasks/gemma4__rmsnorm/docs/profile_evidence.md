# Profile evidence — gemma4__rmsnorm

**e2e-optimization target: 18.9% of total GPU time** (max across scenarios) on
`google/gemma-4-26B-A4B-it`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `google/gemma-4-26B-A4B-it` (slug `gemma4`, tp=1)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `_gemma_dual_rmsnorm_residual_kernel`, `_gemma_qkv_rmsnorm_kernel`, `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gm`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 18.58% |
| random | conc 32 | 9.54% |
| random | conc 100 | 7.03% |
| sharegpt | conc 1 | 18.89% |
| sharegpt | conc 32 | 9.75% |
| sharegpt | conc 100 | 7.46% |

**Peak: 18.9% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 1], [1, 1], []]`
- `[[1, 262144], [], []]`
- `[[17, 8192], [], [], []]`
- `[[1785, 16, 256], [1785, 8, 256], [262400, 256], [1785], [], []]`
- `[[1785, 8, 256], []]`
- `[[1902, 2816], [2816, 128]]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[2049, 262148], []]`
- `[[38, 2048], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path google/gemma-4-26B-A4B-it --reasoning-parser gemma4 --tool-call-parser gemma4
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
