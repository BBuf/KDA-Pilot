# Profile evidence — intern_s2_preview__fp8_bmm

**e2e-optimization target: 9.0% of total GPU time** (max across scenarios) on
`internlm/Intern-S2-Preview`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `internlm/Intern-S2-Preview` (slug `intern_s2_preview`, tp=8)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `other`
- GPU kernel(s): `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOu`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_trans`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 32 | 2.02% |
| random | conc 100 | 8.99% |

**Peak: 9.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[[16384, 2048]], [], [], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path internlm/Intern-S2-Preview --tp 8 --reasoning-parser qwen3 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_high** to validate the e2e effect.
