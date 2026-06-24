# Profile evidence — minimax_m25__per_token_group_quant

**e2e-optimization target: 4.2% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.5`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.5` (slug `minimax_m25`, tp=8)
- Python interface: `<confirm via capture; profiler family=per_token_group_quant>`
- Kernel family: `per_token_group_quant`  ·  Category: `quant_gemm`
- GPU kernel(s): `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::Na`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.16% |
| random | conc 32 | 3.61% |
| random | conc 100 | 2.63% |
| sharegpt | conc 1 | 4.19% |
| sharegpt | conc 32 | 3.48% |
| sharegpt | conc 100 | 2.62% |

**Peak: 4.2% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[4097], [], [], [], []]`
- `[[4150976, 1, 128], []]`
- `[[48, 1, 128], [], [], []]`
- `[[5632, 768], [], [], []]`
- `[[699], [], [], []]`
- `[[9216, 1, 128], [], [], []]`
- `[[[64], [576]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.5 --tp 8 --ep 8 --reasoning-parser minimax-append-think
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
