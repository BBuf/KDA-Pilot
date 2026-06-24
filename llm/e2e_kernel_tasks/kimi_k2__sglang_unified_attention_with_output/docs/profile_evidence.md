# Profile evidence — kimi_k2__sglang_unified_attention_with_output

**e2e-optimization target: 9.5% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-K2-Instruct`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `moonshotai/Kimi-K2-Instruct` (slug `kimi_k2`, tp=8)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSe`, `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64MultiCtasKvVarSeqQ8Kv128Sta`, `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ8Kv128PersistentSwap`, `void flashinfer::mla::BatchMLAPagedAttentionKernel<flashinfer::mla::KernelTraits<true, 2u,`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.73% |
| random | conc 100 | 2.62% |
| sharegpt | conc 1 | 6.01% |
| sharegpt | conc 32 | 2.40% |
| sharegpt | conc 100 | 9.49% |

**Peak: 9.5% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[1, 163840], [], []]`
- `[[1536, 8, 512], [1536, 1, 512], [1536, 1, 512], [1536, 4096], [], [], [1536, 8,`
- `[[1]]`
- `[[2112], [2112], []]`
- `[[255], [], [], []]`
- `[[25], [], [], []]`
- `[[320], [320], []]`
- `[[50], [], [], []]`
- `[[512], [], [], []]`
- `[[543], [], [], []]`
- `[[[1]], [], [], [], [], []]`
- `[[[320], [38]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-K2-Instruct --tp 8 --tool-call-parser kimi_k2
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
