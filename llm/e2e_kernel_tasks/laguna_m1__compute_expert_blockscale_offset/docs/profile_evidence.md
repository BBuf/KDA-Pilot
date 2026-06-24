# Profile evidence — laguna_m1__compute_expert_blockscale_offset

**e2e-optimization target: 5.7% of total GPU time** (max across scenarios) on
`poolside/Laguna-M.1-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `poolside/Laguna-M.1-NVFP4` (slug `laguna_m1`, tp=8)
- Python interface: `<confirm via capture; profiler family=compute_expert_blockscale_offset>`
- Kernel family: `compute_expert_blockscale_offset`  ·  Category: `moe`
- GPU kernel(s): `compute_expert_blockscale_offsets(int const*, int*, int*, int*, long)`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.73% |
| random | conc 100 | 2.22% |
| sharegpt | conc 1 | 5.64% |
| sharegpt | conc 100 | 2.33% |

**Peak: 5.7% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[256], [256], []]`
- `[[2816, 1, 128], [], [], []]`
- `[[4097, 262148], []]`
- `[[768], [768], []]`
- `[[99], [], []]`
- `[[[256]], []]`
- `[[], [], [], [], [], []]`
- `[[]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path poolside/Laguna-M.1-NVFP4 --tp 8 --trust-remote-code --reasoning-parser poolside_v1 --tool-call-parser poolside_v1
```
After optimizing, re-run **random_low** to validate the e2e effect.
