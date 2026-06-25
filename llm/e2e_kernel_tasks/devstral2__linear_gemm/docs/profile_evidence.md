# Profile evidence — devstral2__linear_gemm

**e2e-optimization target: 38.5% of total GPU time** (max across scenarios) on
`mistralai/Devstral-2-123B-Instruct-2512`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Devstral-2-123B-Instruct-2512` (slug `devstral2`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10colle`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 38.34% |
| random | conc 32 | 35.14% |
| random | conc 100 | 30.00% |
| sharegpt | conc 1 | 38.45% |
| sharegpt | conc 32 | 35.75% |
| sharegpt | conc 100 | 29.17% |

**Peak: 38.5% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[0], [0], []]`
- `[[100]]`
- `[[1240, 1536], [1240, 1536], []]`
- `[[1280, 1536], [1280, 1, 128], [1280, 1, 128], [1280, 1536], [], [], [], [], [],`
- `[[1280, 1536], [], [], [], []]`
- `[[1392, 1536], [1392, 1536], []]`
- `[[1], [], [], [], [], []]`
- `[[1]]`
- `[[2240], [], [], []]`
- `[[256], [], [], [], []]`
- `[[294], [], [], []]`
- `[[32, 1, 128], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Devstral-2-123B-Instruct-2512 --tp 8 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
