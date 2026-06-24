# Profile evidence — mistral_small4__sgl_kernel_fp8_scaled_mm

**e2e-optimization target: 28.4% of total GPU time** (max across scenarios) on
`mistralai/Mistral-Small-4-119B-2603`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `mistralai/Mistral-Small-4-119B-2603` (slug `mistral_small4`, tp=1)
- Python interface: `sgl_kernel.fp8_scaled_mm`
- Kernel family: `linear_gemm`  ·  Category: `gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10colle`, `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 26.95% |
| random | conc 32 | 15.26% |
| random | conc 100 | 10.18% |
| sharegpt | conc 1 | 28.39% |
| sharegpt | conc 32 | 12.38% |
| sharegpt | conc 100 | 9.40% |

**Peak: 28.4% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 4096], [4096, 131072]]`
- `[[100], [100], []]`
- `[[100]]`
- `[[104], [], [], []]`
- `[[11179, 4096], [4096, 4096], [11179, 1], [4096, 1], [], []]`
- `[[18, 4096], [4096, 4096], [18, 1], [4096, 1], [], []]`
- `[[18], [], [], []]`
- `[[19593, 256], [256, 6144], [19593, 1], [6144, 1], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[1], [], []]`
- `[[1]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Mistral-Small-4-119B-2603 --tp 1 --reasoning-parser mistral --tool-call-parser mistral
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
