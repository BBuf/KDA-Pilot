# Profile evidence — minimax_m25__fused_moe_triton

**e2e-optimization target: 31.7% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.5`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `MiniMaxAI/MiniMax-M2.5` (slug `minimax_m25`, tp=8)
- Python interface: `<confirm via capture; profiler family=fused_moe_triton>`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 15.14% |
| random | conc 32 | 28.50% |
| random | conc 100 | 31.73% |
| sharegpt | conc 1 | 15.77% |
| sharegpt | conc 32 | 28.53% |
| sharegpt | conc 100 | 30.75% |

**Peak: 31.7% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[4150976, 1, 128], []]`
- `[[48, 1, 128], [], [], []]`
- `[[5632, 768], [], [], []]`
- `[[64859, 64, 1, 128], []]`
- `[[9216, 1, 128], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.5 --tp 8 --ep 8 --reasoning-parser minimax-append-think
```
After optimizing, re-run **random_high** to validate the e2e effect.
