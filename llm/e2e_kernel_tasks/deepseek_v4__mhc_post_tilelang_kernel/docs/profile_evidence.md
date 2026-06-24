# Profile evidence — deepseek_v4__mhc_post_tilelang_kernel

**e2e-optimization target: 4.2% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-V4-Flash`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `deepseek-ai/DeepSeek-V4-Flash` (slug `deepseek_v4`, tp=4)
- Python interface: `<confirm via capture; profiler family=mhc_post_tilelang_kernel>`
- Kernel family: `mhc_post_tilelang_kernel`  ·  Category: `other`
- GPU kernel(s): `mhc_post_tilelang_kernel`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 4.23% |

**Peak: 4.2% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[38, 1, 64, 512], [1988, 256, 1, 584], [38, 1, 128], [38], [64], [148, 8], [39]`
- `[[38, 4, 4096], []]`
- `[[38, 4096], [38, 8], [1536, 4096], [1536, 8], [38, 1536]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-V4-Flash --tp 4 --moe-runner-backend flashinfer_mxfp4 --trust-remote-code
```
After optimizing, re-run **random_mid** to validate the e2e effect.
