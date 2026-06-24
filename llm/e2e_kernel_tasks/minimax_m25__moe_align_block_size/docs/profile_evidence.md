# Profile evidence — minimax_m25__moe_align_block_size

**e2e-optimization target: 3.1% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.5`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `MiniMaxAI/MiniMax-M2.5` (slug `minimax_m25`, tp=8)
- Python interface: `<confirm via capture; profiler family=moe_align_block_size>`
- Kernel family: `moe_align_block_size`  ·  Category: `moe`
- GPU kernel(s): `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.08% |
| sharegpt | conc 1 | 3.13% |

**Peak: 3.1% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[48, 1, 128], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.5 --tp 8 --ep 8 --reasoning-parser minimax-append-think
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
