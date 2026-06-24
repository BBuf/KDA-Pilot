# Profile evidence — qwen3__rmsnorm

**e2e-optimization target: 3.9% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-235B-A22B-Instruct-2507`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507` (slug `qwen3`, tp=8)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `norm`
- GPU kernel(s): `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloa`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 3.94% |
| sharegpt | conc 32 | 3.05% |

**Peak: 3.9% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[10752, 1024], [10752, 1, 128], [10752, 1, 128], [10752, 1024], [], [], [], [],`
- `[[14, 151936], [], [], []]`
- `[[2500, 1024], [2500, 1024], []]`
- `[[2500, 8, 128], [], [], [], [], []]`
- `[[714], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-235B-A22B-Instruct-2507 --tp 8
```
After optimizing, re-run **random_mid** to validate the e2e effect.
