# Profile evidence — ministral3_14b__attention

**e2e-optimization target: 18.5% of total GPU time** (max across scenarios) on
`mistralai/Ministral-3-14B-Instruct-2512`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Ministral-3-14B-Instruct-2512` (slug `ministral3_14b`, tp=1)
- Python interface: `<confirm via capture; profiler family=attention>`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwa`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbFor`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.21% |
| random | conc 32 | 6.48% |
| random | conc 100 | 17.59% |
| sharegpt | conc 1 | 6.50% |
| sharegpt | conc 32 | 13.23% |
| sharegpt | conc 100 | 18.54% |

**Peak: 18.5% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[100], [100], []]`
- `[[100]]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[2727], [], [], []]`
- `[[32, 131072], [], [], []]`
- `[[32], [32], []]`
- `[[32]]`
- `[[512], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Ministral-3-14B-Instruct-2512 --tp 1 --trust-remote-code
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
