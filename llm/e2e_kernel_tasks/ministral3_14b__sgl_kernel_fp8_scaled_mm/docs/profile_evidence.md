# Profile evidence — ministral3_14b__sgl_kernel_fp8_scaled_mm

**e2e-optimization target: 69.4% of total GPU time** (max across scenarios) on
`mistralai/Ministral-3-14B-Instruct-2512`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `mistralai/Ministral-3-14B-Instruct-2512` (slug `ministral3_14b`, tp=1)
- Python interface: `sgl_kernel.fp8_scaled_mm`
- Kernel family: `linear_gemm`  ·  Category: `gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10colle`, `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 61.43% |
| random | conc 32 | 69.38% |
| random | conc 100 | 56.80% |
| sharegpt | conc 1 | 60.67% |
| sharegpt | conc 32 | 63.77% |
| sharegpt | conc 100 | 54.72% |

**Peak: 69.4% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[1, 5120], [5120, 131072]]`
- `[[100, 131072], [], []]`
- `[[100]]`
- `[[1055, 5120], [5120, 32768], [1055, 1], [32768, 1], [], []]`
- `[[1228, 5120], [5120, 32768], [1228, 1], [32768, 1], [], []]`
- `[[1316, 5120], [5120, 32768], [1316, 1], [32768, 1], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], [], [], [], []]`
- `[[1], [], []]`
- `[[1]]`
- `[[2049], [], [100], [], []]`
- `[[2049], [], [32], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path mistralai/Ministral-3-14B-Instruct-2512 --tp 1 --trust-remote-code
```
After optimizing, re-run **random_mid** to validate the e2e effect.
