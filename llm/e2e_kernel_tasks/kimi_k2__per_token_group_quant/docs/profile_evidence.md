# Profile evidence — kimi_k2__per_token_group_quant

**e2e-optimization target: 12.6% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-K2-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `moonshotai/Kimi-K2-Instruct` (slug `kimi_k2`, tp=8)
- Python interface: `<confirm via capture; profiler family=per_token_group_quant>`
- Kernel family: `per_token_group_quant`  ·  Category: `quant_gemm`
- GPU kernel(s): `void per_token_group_quant_8bit_kernel<NaiveScheduler, 128, 8, __nv_bfloat16, c10::Float8_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 12.64% |
| random | conc 32 | 2.42% |
| random | conc 100 | 6.24% |
| sharegpt | conc 1 | 12.59% |
| sharegpt | conc 32 | 6.30% |
| sharegpt | conc 100 | 6.16% |

**Peak: 12.6% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[15, 4096], [15, 4096], []]`
- `[[16, 8, 512], [16, 1, 512], [16, 1, 512], [16, 4096], [], [], [16, 8, 64], [16,`
- `[[38, 4096], [38, 4096], []]`
- `[[38, 8, 512], []]`
- `[[48, 8, 512], [48, 1, 512], [48, 1, 512], [48, 4096], [], [], [48, 8, 64], [48,`
- `[[51, 4096], [51, 4096], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-K2-Instruct --tp 8 --tool-call-parser kimi_k2
```
After optimizing, re-run **random_low** to validate the e2e effect.
