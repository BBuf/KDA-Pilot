# Profile evidence — qwen3__sglang_unified_attention_with_output

**e2e-optimization target: 7.8% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-235B-A22B-Instruct-2507`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507` (slug `qwen3`, tp=8)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwa`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbFor`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.22% |
| random | conc 100 | 5.56% |
| sharegpt | conc 1 | 6.21% |
| sharegpt | conc 32 | 3.59% |
| sharegpt | conc 100 | 7.83% |

**Peak: 7.8% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[14]]`
- `[[1]]`
- `[[2560, 1, 128], [], [], []]`
- `[[2560, 1024], [2560, 1, 128], [2560, 1, 128], [2560, 1024], [], [], [], [], [],`
- `[[264], [], [], []]`
- `[[384], [], [], []]`
- `[[448], [], [], []]`
- `[[576, 1024], [576, 1, 128], [576, 1, 128], [576, 1024], [], [], [], [], [], [],`
- `[[576], [], [], []]`
- `[[62], [], [], []]`
- `[[832], [], [], [], []]`
- `[[[1]], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-235B-A22B-Instruct-2507 --tp 8
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
