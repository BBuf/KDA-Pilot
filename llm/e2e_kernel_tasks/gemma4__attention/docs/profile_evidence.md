# Profile evidence — gemma4__attention

**e2e-optimization target: 12.0% of total GPU time** (max across scenarios) on
`google/gemma-4-26B-A4B-it`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `google/gemma-4-26B-A4B-it` (slug `gemma4`, tp=1)
- Python interface: `<confirm via capture; profiler family=attention>`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64MultiCtasKvCgaVar`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128Pe`, `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128Pers`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.07% |
| random | conc 32 | 5.69% |
| random | conc 100 | 12.04% |
| sharegpt | conc 1 | 4.14% |
| sharegpt | conc 32 | 6.32% |
| sharegpt | conc 100 | 7.92% |

**Peak: 12.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[1, 262144], [], [], []]`
- `[[100]]`
- `[[104, 262144], [], [], []]`
- `[[1]]`
- `[[2816, 4096]]`
- `[[32, 16], [32, 16], []]`
- `[[32, 262144], [], [], []]`
- `[[32]]`
- `[[384]]`
- `[[51], [], [], []]`
- `[[[1], [1], [1], [1]], [[1], [1], [1], [1]], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path google/gemma-4-26B-A4B-it --reasoning-parser gemma4 --tool-call-parser gemma4
```
After optimizing, re-run **random_high** to validate the e2e effect.
