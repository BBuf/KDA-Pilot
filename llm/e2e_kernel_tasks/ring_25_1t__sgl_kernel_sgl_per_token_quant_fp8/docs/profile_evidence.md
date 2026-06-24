# Profile evidence — ring_25_1t__sgl_kernel_sgl_per_token_quant_fp8

**e2e-optimization target: 4.4% of total GPU time** (max across scenarios) on
`inclusionAI/Ring-2.5-1T`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `inclusionAI/Ring-2.5-1T` (slug `ring_25_1t`, tp=8)
- Python interface: `sgl_kernel.sgl_per_token_quant_fp8`
- Kernel family: `quant_fp8`  ·  Category: `quant_gemm`
- GPU kernel(s): `void per_token_quant_fp8_kernel<__nv_bfloat16, __nv_fp8_e4m3, 8, 16, false>(__nv_bfloat16 `, `void per_token_quant_fp8_small_batch_kernel<__nv_bfloat16, __nv_fp8_e4m3, 16>(__nv_bfloat1`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 4.13% |
| random | conc 32 | 2.67% |
| random | conc 100 | 4.37% |
| sharegpt | conc 1 | 4.19% |
| sharegpt | conc 32 | 3.23% |

**Peak: 4.4% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[14375, 8192], [14375, 8192], [14375, 1]]`
- `[[16384, 8192], [16384, 8192], [16384, 1]]`
- `[[1], [1], []]`
- `[[9780, 8192], [9780, 8192], [9780, 1]]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path inclusionAI/Ring-2.5-1T --tp 8 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
