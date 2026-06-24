# Profile evidence — nemotron3_super__rmsnorm

**e2e-optimization target: 8.8% of total GPU time** (max across scenarios) on
`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` (slug `nemotron3_super`, tp=4)
- Python interface: `<confirm via capture; profiler family=rmsnorm>`
- Kernel family: `rmsnorm`  ·  Category: `norm`
- GPU kernel(s): `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloa`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 8.85% |
| random | conc 32 | 4.14% |
| random | conc 100 | 3.57% |
| sharegpt | conc 1 | 8.42% |
| sharegpt | conc 32 | 3.62% |
| sharegpt | conc 100 | 3.12% |

**Peak: 8.8% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[18, 1024], [18, 1024], []]`
- `[[18, 2048], [2048, 4096]]`
- `[[18, 4096], [4096, 4640]]`
- `[[1], [1], []]`
- `[[2, 4096], []]`
- `[[20, 4096], [20, 4096], []]`
- `[[38, 1024], [38, 1024], []]`
- `[[38, 4096], [4096, 4640]]`
- `[[38], [], []]`
- `[[40, 1025, 2560, 3], [], []]`
- `[[48, 4096], [48, 4096], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 --tp 4 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
