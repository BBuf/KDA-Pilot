# Profile evidence — ernie45__fused_moe_triton

**e2e-optimization target: 65.0% of total GPU time** (max across scenarios) on
`baidu/ERNIE-4.5-21B-A3B-PT`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `baidu/ERNIE-4.5-21B-A3B-PT` (slug `ernie45`, tp=1)
- Python interface: `<confirm via capture; profiler family=fused_moe_triton>`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 37.00% |
| random | conc 32 | 63.38% |
| random | conc 100 | 64.96% |
| sharegpt | conc 1 | 35.86% |
| sharegpt | conc 32 | 62.86% |
| sharegpt | conc 100 | 64.82% |

**Peak: 65.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- (see trace)

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path baidu/ERNIE-4.5-21B-A3B-PT --tp 1
```
After optimizing, re-run **random_high** to validate the e2e effect.
