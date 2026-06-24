# Profile evidence — step35_flash__linear_gemm

**e2e-optimization target: 6.9% of total GPU time** (max across scenarios) on
`stepfun-ai/Step-3.5-Flash`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `stepfun-ai/Step-3.5-Flash` (slug `step35_flash`, tp=4)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_tst_32x64_64x16_4x1_v_bz_TNN`, `nvjet_tst_64x8_64x16_4x1_v_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.26% |
| random | conc 32 | 5.82% |
| random | conc 100 | 5.37% |
| sharegpt | conc 1 | 6.29% |
| sharegpt | conc 32 | 6.04% |
| sharegpt | conc 100 | 6.87% |

**Peak: 6.9% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[1, 1], [1, 1], []]`
- `[[16, 4096], [4096, 3584]]`
- `[[1], []]`
- `[[1]]`
- `[[[1]], [], [], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path stepfun-ai/Step-3.5-Flash --tp 4 --trust-remote-code --reasoning-parser step3p5
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
