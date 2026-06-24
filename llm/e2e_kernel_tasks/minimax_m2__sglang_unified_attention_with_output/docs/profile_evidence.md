# Profile evidence — minimax_m2__sglang_unified_attention_with_output

**e2e-optimization target: 5.7% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `MiniMaxAI/MiniMax-M2` (slug `minimax_m2`, tp=4)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForG`, `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.53% |
| random | conc 100 | 4.71% |
| sharegpt | conc 1 | 4.58% |
| sharegpt | conc 32 | 2.83% |
| sharegpt | conc 100 | 5.66% |

**Peak: 5.7% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[0], [], [], []]`
- `[[100], [100], []]`
- `[[100]]`
- `[[104], [104], []]`
- `[[1622848, 2, 128], []]`
- `[[2560, 1536], [2560, 2, 128], [2560, 2, 128], [2560, 1536], [], [], [], [], [],`
- `[[2816, 1536], [2816, 2, 128], [2816, 2, 128], [2816, 1536], [], [], [], [], [],`
- `[[371], [], [], []]`
- `[[5632, 1536], [5632, 2, 128], [5632, 2, 128], [5632, 1536], [], [], [], [], [],`
- `[[640], [], [], []]`
- `[[699], [], [], []]`
- `[[[1]], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2 --tp 4 --reasoning-parser minimax-append-think --trust-remote-code
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
