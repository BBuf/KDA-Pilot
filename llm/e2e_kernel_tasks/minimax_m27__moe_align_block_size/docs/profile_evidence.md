# Profile evidence — minimax_m27__moe_align_block_size

**e2e-optimization target: 3.6% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.7`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.7` (slug `minimax_m27`, tp=8)
- Python interface: `<confirm via capture; profiler family=moe_align_block_size>`
- Kernel family: `moe_align_block_size`  ·  Category: `moe`
- GPU kernel(s): `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.39% |
| random | conc 100 | 2.34% |
| sharegpt | conc 1 | 3.59% |

**Peak: 3.6% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[128], [128], []]`
- `[[131], [], [], [], []]`
- `[[256], [], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.7 --tp 8 --ep 8 --tool-call-parser minimax-m2 --reasoning-parser minimax-append-think
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
