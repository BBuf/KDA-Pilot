# Profile evidence — minimax_m27__per_token_group_quant

**e2e-optimization target: 4.8% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.7`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.7` (slug `minimax_m27`, tp=8)
- Python interface: `<confirm via capture; profiler family=per_token_group_quant>`
- Kernel family: `per_token_group_quant`  ·  Category: `quant_gemm`
- GPU kernel(s): `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::Na`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.62% |
| random | conc 32 | 2.74% |
| sharegpt | conc 1 | 4.82% |
| sharegpt | conc 32 | 2.57% |

**Peak: 4.8% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1], [1], []]`
- `[[1]]`
- `[[5632, 768], [], [], []]`
- `[[640], [640], []]`
- `[[[640], [59]], []]`
- `[[[64], [576]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.7 --tp 8 --ep 8 --tool-call-parser minimax-m2 --reasoning-parser minimax-append-think
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
