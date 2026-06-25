# Profile evidence — glm_46__fused_moe_triton

**e2e-optimization target: 34.8% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.6-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `zai-org/GLM-4.6-FP8` (slug `glm_46`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_moe_triton>`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 19.81% |
| random | conc 32 | 32.49% |
| random | conc 100 | 34.80% |
| sharegpt | conc 1 | 18.43% |
| sharegpt | conc 32 | 28.40% |
| sharegpt | conc 100 | 32.75% |

**Peak: 34.8% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[112, 1536], [112, 1, 128], [112, 1, 128], [112, 1536], [], [], [], [], [], [],`
- `[[112, 1536], [], [], []]`
- `[[1536, 1, 128], [], [], []]`
- `[[1], []]`
- `[[2193, 12, 128]]`
- `[[2816, 1, 128], [], [], []]`
- `[[325], [], [], []]`
- `[[32], [32], []]`
- `[[80, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [2], [], [], [1]`
- `[[80, 1536], [80, 1536], []]`
- `[[8125, 12, 128], [19176, 128, 1, 128], [19176, 128, 1, 128], [], [27], [], [], `

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.6-FP8 --tp 8 --reasoning-parser glm45 --tool-call-parser glm45 --attention-backend fa4
```
After optimizing, re-run **random_high** to validate the e2e effect.
