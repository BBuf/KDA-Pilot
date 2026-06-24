# Profile evidence — step35_flash__void_moe_top_k_256_float_const_b

**e2e-optimization target: 3.3% of total GPU time** (max across scenarios) on
`stepfun-ai/Step-3.5-Flash`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `stepfun-ai/Step-3.5-Flash` (slug `step35_flash`, tp=4)
- Python interface: `<confirm via capture; profiler family=void_moe_top_k_256_float_const_b>`
- Kernel family: `void_moe_top_k_256_float_const_b`  ·  Category: `moe`
- GPU kernel(s): `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.79% |
| random | conc 32 | 3.09% |
| random | conc 100 | 2.85% |
| sharegpt | conc 1 | 3.00% |
| sharegpt | conc 32 | 2.88% |
| sharegpt | conc 100 | 3.28% |

**Peak: 3.3% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[1603073], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[[0], [38]], []]`
- `[[[1]], [], [], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path stepfun-ai/Step-3.5-Flash --tp 4 --trust-remote-code --reasoning-parser step3p5
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
