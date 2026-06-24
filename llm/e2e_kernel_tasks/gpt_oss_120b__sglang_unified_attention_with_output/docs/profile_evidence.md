# Profile evidence — gpt_oss_120b__sglang_unified_attention_with_output

**e2e-optimization target: 8.4% of total GPU time** (max across scenarios) on
`openai/gpt-oss-120b`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `openai/gpt-oss-120b` (slug `gpt_oss_120b`, tp=8)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwap`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128Persi`, `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantization`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 8.34% |
| random | conc 32 | 2.46% |
| sharegpt | conc 1 | 8.44% |
| sharegpt | conc 32 | 2.29% |
| sharegpt | conc 100 | 2.55% |

**Peak: 8.4% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 201088], [], [], []]`
- `[[1, 201088], [], []]`
- `[[1], []]`
- `[[2373, 1, 64], []]`
- `[[2560, 512], [2560, 1, 64], [2560, 1, 64], [2560, 512], [], [], [], [], [8], []`
- `[[[0], [15]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path openai/gpt-oss-120b --tp 8
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
