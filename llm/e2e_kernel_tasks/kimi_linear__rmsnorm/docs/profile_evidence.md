# Profile evidence — kimi_linear__rmsnorm

**e2e-optimization target: 26.0% of total GPU time** (max across scenarios) on
`moonshotai/Kimi-Linear-48B-A3B-Instruct`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct` (slug `kimi_linear`, tp=4)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `norm`
- GPU kernel(s): `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloa`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 8.58% |
| sharegpt | conc 1 | 25.98% |
| sharegpt | conc 32 | 16.44% |

**Peak: 26.0% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1024, 15], [], [], [], [], []]`
- `[[1024, 38], [], []]`
- `[[16, 3072], [1, 16, 8, 128], [1, 16, 8], [1, 16, 8, 128], []]`
- `[[1], []]`
- `[[1]]`
- `[[257, 8, 128], [], [], []]`
- `[[48, 8, 512], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path moonshotai/Kimi-Linear-48B-A3B-Instruct --tp 4 --trust-remote-code
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
