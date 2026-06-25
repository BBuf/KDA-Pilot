# Profile evidence — mistral_medium35__sgl_kernel_fp8_scaled_mm

**e2e-optimization target: 63.5% of total GPU time** (max across scenarios) on
`mistralai/Mistral-Medium-3.5-128B`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `mistralai/Mistral-Medium-3.5-128B` (slug `mistral_medium35`, tp=2)
- Python interface: `sgl_kernel.fp8_scaled_mm`
- Kernel family: `linear_gemm`  ·  Category: `gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10colle`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 50.27% |
| random | conc 32 | 9.61% |
| random | conc 100 | 56.06% |
| sharegpt | conc 1 | 49.77% |
| sharegpt | conc 32 | 63.53% |
| sharegpt | conc 100 | 40.95% |

**Peak: 63.5% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[100], [], []]`
- `[[104], [104], []]`
- `[[11, 12288], [12288, 28672], [11, 1], [28672, 1], [], []]`
- `[[14269, 6144], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[2440, 12288], [12288, 28672], [2440, 1], [28672, 1], [], []]`
- `[[30, 12288], [12288, 28672], [30, 1], [28672, 1], [], []]`
- `[[30, 6144], []]`
- `[[310656, 4, 128], []]`
- `[[320], [320], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Mistral-Medium-3.5-128B --tp 2 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
