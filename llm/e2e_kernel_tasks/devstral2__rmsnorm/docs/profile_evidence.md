# Profile evidence — devstral2__rmsnorm

**e2e-optimization target: 8.5% of total GPU time** (max across scenarios) on
`mistralai/Devstral-2-123B-Instruct-2512`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `mistralai/Devstral-2-123B-Instruct-2512` (slug `devstral2`, tp=8)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `norm`
- GPU kernel(s): `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloa`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 8.32% |
| random | conc 100 | 6.15% |
| sharegpt | conc 32 | 8.45% |
| sharegpt | conc 100 | 5.53% |

**Peak: 8.5% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[1240, 1536], [1240, 1536], []]`
- `[[1280, 1536], [1280, 1, 128], [1280, 1, 128], [1280, 1536], [], [], [], [], [],`
- `[[1392, 128], [1392, 128], [3200384, 128], [3200384, 128], [1392], [], [], []]`
- `[[1392, 1536], [1392, 1536], []]`
- `[[1], [1], []]`
- `[[1]]`
- `[[7807, 128], [7807, 128], [3200384, 128], [3200384, 128], [7807], [], [], []]`
- `[[8192, 1536], [], [], [], []]`
- `[[8704, 1536], [], [], [], []]`
- `[[[1], [39375]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Devstral-2-123B-Instruct-2512 --tp 8 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
