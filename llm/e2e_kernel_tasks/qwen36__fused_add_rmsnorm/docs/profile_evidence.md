# Profile evidence — qwen36__fused_add_rmsnorm

**e2e-optimization target: 3.5% of total GPU time** (max across scenarios) on
`Qwen/Qwen3.6-35B-A3B-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3.6-35B-A3B-FP8` (slug `qwen36`, tp=1)
- Python interface: `<confirm via capture; profiler family=fused_add_rmsnorm>`
- Kernel family: `fused_add_rmsnorm`  ·  Category: `gemm`
- GPU kernel(s): `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_a`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.51% |
| sharegpt | conc 1 | 3.53% |

**Peak: 3.5% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1], [1], []]`
- `[[1]]`
- `[[49, 262152], []]`
- `[[49], [49], []]`
- `[[49], []]`
- `[[55524], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3.6-35B-A3B-FP8 --reasoning-parser qwen3 --tool-call-parser qwen3_coder --speculative-algorithm EAGLE --speculative-num-steps 3 --speculative-eagle-topk 1
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
