# Profile evidence — ernie45__sglang_unified_attention_with_output

**e2e-optimization target: 8.0% of total GPU time** (max across scenarios) on
`baidu/ERNIE-4.5-21B-A3B-PT`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `baidu/ERNIE-4.5-21B-A3B-PT` (slug `ernie45`, tp=1)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwa`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbFor`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.83% |
| random | conc 32 | 2.35% |
| random | conc 100 | 8.02% |
| sharegpt | conc 1 | 5.96% |
| sharegpt | conc 32 | 4.07% |
| sharegpt | conc 100 | 7.81% |

**Peak: 8.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[0], [], [], []]`
- `[[100]]`
- `[[104, 17], [104, 17], []]`
- `[[11264, 2560], [11264, 4, 128], [11264, 4, 128], [11264, 2560], [], [], [], [],`
- `[[1], [1], []]`
- `[[1]]`
- `[[256], [256], []]`
- `[[2816, 2560], [2816, 4, 128], [2816, 4, 128], [2816, 2560], [], [], [], [], [],`
- `[[5120, 2560], [5120, 4, 128], [5120, 4, 128], [5120, 2560], [], [], [], [], [],`
- `[[55], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path baidu/ERNIE-4.5-21B-A3B-PT --tp 1
```
After optimizing, re-run **random_high** to validate the e2e effect.
