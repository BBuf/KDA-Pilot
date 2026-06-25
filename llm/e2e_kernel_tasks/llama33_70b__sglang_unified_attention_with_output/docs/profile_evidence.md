# Profile evidence — llama33_70b__sglang_unified_attention_with_output

**e2e-optimization target: 3.6% of total GPU time** (max across scenarios) on
`meta-llama/Llama-3.3-70B-Instruct`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `meta-llama/Llama-3.3-70B-Instruct` (slug `llama33_70b`, tp=1)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwa`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.19% |
| random | conc 32 | 2.22% |
| random | conc 100 | 2.26% |
| sharegpt | conc 1 | 2.25% |
| sharegpt | conc 32 | 3.60% |
| sharegpt | conc 100 | 3.55% |

**Peak: 3.6% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[15360, 8192], [15360, 8, 128], [15360, 8, 128], [15360, 8192], [], [], [], [],`
- `[[15872, 8192], [15872, 8, 128], [15872, 8, 128], [15872, 8192], [], [], [], [],`
- `[[1], [1], []]`
- `[[1]]`
- `[[5120, 8192], [5120, 8, 128], [5120, 8, 128], [5120, 8192], [], [], [], [], [],`
- `[[9728, 8192], [9728, 8, 128], [9728, 8, 128], [9728, 8192], [], [], [], [], [],`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path meta-llama/Llama-3.3-70B-Instruct --tp 1 --tool-call-parser llama3
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
