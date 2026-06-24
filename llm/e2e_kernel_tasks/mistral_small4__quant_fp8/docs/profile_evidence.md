# Profile evidence — mistral_small4__quant_fp8

**e2e-optimization target: 7.1% of total GPU time** (max across scenarios) on
`mistralai/Mistral-Small-4-119B-2603`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Mistral-Small-4-119B-2603` (slug `mistral_small4`, tp=1)
- Python interface: `<confirm via capture; profiler family=quant_fp8>`
- Kernel family: `quant_fp8`  ·  Category: `quant_gemm`
- GPU kernel(s): `_static_quant_fp8`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 6.85% |
| random | conc 100 | 2.14% |
| sharegpt | conc 1 | 7.07% |
| sharegpt | conc 32 | 2.83% |
| sharegpt | conc 100 | 2.35% |

**Peak: 7.1% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[512], [], [], []]`
- `[[5519, 1, 320], [], [], [], []]`
- `[[5519, 1, 320], [], [], []]`
- `[[5519, 256], [], [], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Mistral-Small-4-119B-2603 --tp 1 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
