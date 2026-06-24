# Profile evidence — minimax_m25__void_moe_sum_reduce_kernel_warp

**e2e-optimization target: 3.3% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.5`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.5` (slug `minimax_m25`, tp=8)
- Python interface: `<confirm via capture; profiler family=void_moe_sum_reduce_kernel_warp>`
- Kernel family: `void_moe_sum_reduce_kernel_warp`  ·  Category: `moe`
- GPU kernel(s): `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, `

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 3.34% |
| sharegpt | conc 32 | 3.21% |

**Peak: 3.3% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[5632, 768], [], [], []]`
- `[[9216, 1, 128], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.5 --tp 8 --ep 8 --reasoning-parser minimax-append-think
```
After optimizing, re-run **random_mid** to validate the e2e effect.
