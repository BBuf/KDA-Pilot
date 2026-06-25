# Profile evidence — glm_45__fused_moe_triton

**e2e-optimization target: 34.9% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.5-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `zai-org/GLM-4.5-FP8` (slug `glm_45`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_moe_triton>`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 19.87% |
| random | conc 32 | 31.27% |
| random | conc 100 | 34.90% |
| sharegpt | conc 1 | 17.99% |
| sharegpt | conc 32 | 30.52% |
| sharegpt | conc 100 | 30.44% |

**Peak: 34.9% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[0], [], []]`
- `[[103, 12, 128], [19181, 128, 1, 128], [19181, 128, 1, 128], [], [2], [], [], [1`
- `[[112, 1536], [112, 1, 128], [112, 1, 128], [112, 1536], [], [], [], [], [], [],`
- `[[1], [1], []]`
- `[[1], []]`
- `[[7639, 1536], []]`
- `[[80, 1536], [80, 1, 128], [80, 1, 128], [80, 1536], [], [], [], [], [], [], [],`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.5-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **random_high** to validate the e2e effect.
