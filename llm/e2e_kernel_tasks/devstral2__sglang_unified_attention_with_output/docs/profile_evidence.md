# Profile evidence — devstral2__sglang_unified_attention_with_output

**e2e-optimization target: 10.5% of total GPU time** (max across scenarios) on
`mistralai/Devstral-2-123B-Instruct-2512`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `mistralai/Devstral-2-123B-Instruct-2512` (slug `devstral2`, tp=8)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ16Kv128StaticSw`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ16Kv128PersistentSwapsAbFo`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.94% |
| random | conc 100 | 5.05% |
| sharegpt | conc 1 | 6.11% |
| sharegpt | conc 32 | 3.29% |
| sharegpt | conc 100 | 10.47% |

**Peak: 10.5% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[100], [], []]`
- `[[1280, 1536], [1280, 1, 128], [1280, 1, 128], [1280, 1536], [], [], [], [], [],`
- `[[1280, 1536], [], [], []]`
- `[[15, 8, 16384], [15, 8, 16384], []]`
- `[[193], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[4097, 262148], [], [], []]`
- `[[480, 1536], [480, 1, 128], [480, 1, 128], [480, 1536], [], [], [], [], [], [],`
- `[[768], [], [], [], []]`
- `[[8641, 1536], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Devstral-2-123B-Instruct-2512 --tp 8 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
