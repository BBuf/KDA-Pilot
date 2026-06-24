# Profile evidence — minimax_m27__sglang_unified_attention_with_output

**e2e-optimization target: 5.4% of total GPU time** (max across scenarios) on
`MiniMaxAI/MiniMax-M2.7`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `MiniMaxAI/MiniMax-M2.7` (slug `minimax_m27`, tp=8)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwa`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbFor`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.42% |
| random | conc 100 | 4.07% |
| sharegpt | conc 1 | 4.69% |
| sharegpt | conc 32 | 2.85% |
| sharegpt | conc 100 | 5.38% |

**Peak: 5.4% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[1], [], [], [], [], []]`
- `[[1]]`
- `[[3072, 768], [3072, 1, 128], [3072, 1, 128], [3072, 768], [], [], [], [], [], [`
- `[[4148736, 1, 128], []]`
- `[[5552, 768], [5552, 768], []]`
- `[[640], [], [], [], []]`
- `[[64824, 64, 1, 128], [], [], []]`
- `[[[0], [14]], []]`
- `[[[1]], [], [], [], [], []]`
- `[[[448], [19]], []]`
- `[[[64], [576]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path MiniMaxAI/MiniMax-M2.7 --tp 8 --ep 8 --tool-call-parser minimax-m2 --reasoning-parser minimax-append-think
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
