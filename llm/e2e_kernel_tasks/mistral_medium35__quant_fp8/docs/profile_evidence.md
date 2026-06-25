# Profile evidence — mistral_medium35__quant_fp8

**e2e-optimization target: 3.5% of total GPU time** (max across scenarios) on
`mistralai/Mistral-Medium-3.5-128B`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Mistral-Medium-3.5-128B` (slug `mistral_medium35`, tp=2)
- Python interface: `<confirm via capture; profiler family=quant_fp8>`
- Kernel family: `quant_fp8`  ·  Category: `quant_gemm`
- GPU kernel(s): `_static_quant_fp8`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.53% |
| random | conc 32 | 3.17% |
| random | conc 100 | 3.20% |
| sharegpt | conc 1 | 3.51% |
| sharegpt | conc 32 | 3.05% |
| sharegpt | conc 100 | 2.33% |

**Peak: 3.5% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[14269, 48, 128], [14269, 1, 1]]`
- `[[14269, 6144], [6144, 12288], [14269, 1], [12288, 1], [], []]`
- `[[14269], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[64], [64], []]`
- `[[9778, 48, 128], [9778, 1, 1]]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Mistral-Medium-3.5-128B --tp 2 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **random_low** to validate the e2e effect.
