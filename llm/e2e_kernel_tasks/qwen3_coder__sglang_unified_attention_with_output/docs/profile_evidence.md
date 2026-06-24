# Profile evidence — qwen3_coder__sglang_unified_attention_with_output

**e2e-optimization target: 6.8% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` (slug `qwen3_coder`, tp=8)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP32MultiCtasKvCgaVarSeqQ16Kv128Stati`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP32VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP32VarSeqQ16Kv128PersistentSwapsAbFo`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.68% |
| random | conc 100 | 3.18% |
| sharegpt | conc 1 | 4.71% |
| sharegpt | conc 32 | 2.67% |
| sharegpt | conc 100 | 6.80% |

**Peak: 6.8% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[1536, 1536], [1536, 1, 128], [1536, 1, 128], [1536, 1536], [], [], [], [], [],`
- `[[1], [1], []]`
- `[[1], [], [], [], [], []]`
- `[[1]]`
- `[[2560, 1536], [2560, 1, 128], [2560, 1, 128], [2560, 1536], [], [], [], [], [],`
- `[[66939], [], [], []]`
- `[[768, 1536], [], [], []]`
- `[[8], [], [], []]`
- `[[[1]], [], [], [], [], []]`
- `[[]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --tp 8 --ep 8 --tool-call-parser qwen3_coder
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
