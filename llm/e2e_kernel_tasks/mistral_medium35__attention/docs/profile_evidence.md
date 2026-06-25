# Profile evidence — mistral_medium35__attention

**e2e-optimization target: 9.7% of total GPU time** (max across scenarios) on
`mistralai/Mistral-Medium-3.5-128B`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Mistral-Medium-3.5-128B` (slug `mistral_medium35`, tp=2)
- Python interface: `<confirm via capture; profiler family=attention>`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ16Kv128StaticSw`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ16Kv128PersistentSwapsAbFo`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.93% |
| random | conc 32 | 2.49% |
| random | conc 100 | 9.69% |
| sharegpt | conc 1 | 2.96% |
| sharegpt | conc 32 | 5.02% |
| sharegpt | conc 100 | 6.98% |

**Peak: 9.7% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[1, 131072], [], [], [], []]`
- `[[100], [100], []]`
- `[[100]]`
- `[[104], [104], []]`
- `[[14269, 12288]]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Mistral-Medium-3.5-128B --tp 2 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **random_high** to validate the e2e effect.
