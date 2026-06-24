# Profile evidence — minimax_m2__fused_moe_triton

**e2e-optimization target: 48.1% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

> Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

- Model: `MiniMaxAI/MiniMax-M2` (slug `minimax_m2`, tp=4)
- Python interface: `<confirm via capture; profiler family=fused_moe_triton>`
- Kernel family: `fused_moe_triton`  ·  Category: `moe`
- GPU kernel(s): `fused_moe_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 23.61% |
| random | conc 32 | 43.66% |
| random | conc 100 | 48.15% |
| sharegpt | conc 1 | 24.78% |
| sharegpt | conc 32 | 43.36% |
| sharegpt | conc 100 | 47.91% |

**Peak: 48.1% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[25357, 64, 2, 128], [], [], []]`
- `[[256], [], [], [], []]`
- `[[2797, 2, 128], []]`
- `[[9468, 2, 128], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2 --tp 4 --reasoning-parser minimax-append-think --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
