# Profile evidence — qwen3_coder__per_token_group_quant

**e2e-optimization target: 17.2% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` (slug `qwen3_coder`, tp=8)
- Python interface: `<confirm via capture; profiler family=per_token_group_quant>`
- Kernel family: `per_token_group_quant`  ·  Category: `quant_gemm`
- GPU kernel(s): `void per_token_group_quant_8bit_kernel<NaiveScheduler, 128, 8, __nv_bfloat16, c10::Float8_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 17.25% |
| random | conc 100 | 8.00% |
| sharegpt | conc 1 | 16.25% |
| sharegpt | conc 32 | 7.58% |

**Peak: 17.2% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[17, 1536], [17, 1536], []]`
- `[[20, 1536], [20, 1, 128], [20, 1, 128], [20, 1536], [], [], [], [], [], [], [],`
- `[[2825120, 1, 128], []]`
- `[[31], [31], []]`
- `[[6, 1536], [6, 1536], []]`
- `[[8, 1536], [8, 1, 128], [8, 1, 128], [8, 1536], [], [], [], [], [], [], [], [],`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --tp 8 --ep 8 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_low** to validate the e2e effect.
