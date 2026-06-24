# Profile evidence — step_37_flash__fused_add_rmsnorm

**e2e-optimization target: 32.1% of total GPU time** (max across scenarios) on
`stepfun-ai/Step-3.7-Flash-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4` (slug `step_37_flash`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 32.09% |
| random | conc 100 | 3.53% |
| sharegpt | conc 32 | 21.82% |

**Peak: 32.1% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[16, 1, 128], [], [], []]`
- `[[16, 4096], [4096, 1792]]`
- `[[1]]`
- `[[2977, 4096]]`
- `[[2977, 8], [2977, 8], [2977, 288], [], [288]]`
- `[[8, 1, 16112], [], []]`
- `[[], [16, 320], [16, 160]]`
- `[[], [2977, 320], [2977, 160]]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path stepfun-ai/Step-3.7-Flash-NVFP4 --tp 8 --ep 8 --moe-runner-backend flashinfer_trtllm --kv-cache-dtype fp8_e4m3
```
After optimizing, re-run **random_low** to validate the e2e effect.
