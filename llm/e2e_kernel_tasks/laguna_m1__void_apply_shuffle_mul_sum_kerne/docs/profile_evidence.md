# Profile evidence — laguna_m1__void_apply_shuffle_mul_sum_kerne

**e2e-optimization target: 3.9% of total GPU time** (max across scenarios) on
`poolside/Laguna-M.1-NVFP4`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `poolside/Laguna-M.1-NVFP4` (slug `laguna_m1`, tp=8)
- Python interface: `<confirm via capture; profiler family=void_apply_shuffle_mul_sum_kerne>`
- Kernel family: `void_apply_shuffle_mul_sum_kerne`  ·  Category: `other`
- GPU kernel(s): `void apply_shuffle_mul_sum_kernel<__nv_bfloat16>(__nv_bfloat16 const*, __nv_bfloat16*, int`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 3.89% |
| sharegpt | conc 1 | 3.80% |

**Peak: 3.9% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[48, 1024], [48, 1, 128], [48, 1, 128], [48, 1024], [], [], [], [], [], [], [],`
- `[[48, 128], [48, 128], [3980352, 128], [3980352, 128], [48], [], [], []]`
- `[[62193, 64, 1, 128], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path poolside/Laguna-M.1-NVFP4 --tp 8 --trust-remote-code --reasoning-parser poolside_v1 --tool-call-parser poolside_v1
```
After optimizing, re-run **random_low** to validate the e2e effect.
