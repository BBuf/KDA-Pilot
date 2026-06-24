# Profile evidence — minimax_m2__per_token_group_quant

**e2e-optimization target: 4.7% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2` (slug `minimax_m2`, tp=4)
- Python interface: `<confirm via capture; profiler family=per_token_group_quant>`
- Kernel family: `per_token_group_quant`  ·  Category: `quant_gemm`
- GPU kernel(s): `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::Na`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.72% |
| random | conc 32 | 2.21% |
| sharegpt | conc 1 | 4.65% |
| sharegpt | conc 32 | 2.09% |

**Peak: 4.7% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 200064], [], []]`
- `[[1]]`
- `[[25357, 64, 2, 128], [], [], []]`
- `[[9468, 2, 128], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2 --tp 4 --reasoning-parser minimax-append-think --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
