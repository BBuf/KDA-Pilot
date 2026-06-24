# Profile evidence — nemotron3_super__fp8_bmm

**e2e-optimization target: 18.0% of total GPU time** (max across scenarios) on
`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` (slug `nemotron3_super`, tp=4)
- Python interface: `<confirm via capture; profiler family=fp8_bmm>`
- Kernel family: `fp8_bmm`  ·  Category: `other`
- GPU kernel(s): `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128_s4_et128x16_m128x16x16_c1x1x1_rM_BN_transOu`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128_s5_et128x16_m128x16x16_c1x1x1_rM_BN_transOu`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s4_et128x16_m128x16x16_c1x1x1_rM_BN_trans`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s6_et128x16_m128x16x16_c1x1x1_rM_BN_trans`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_trans`, `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_s`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.99% |
| random | conc 32 | 11.82% |
| random | conc 100 | 17.99% |
| sharegpt | conc 1 | 2.18% |
| sharegpt | conc 32 | 17.43% |
| sharegpt | conc 100 | 13.84% |

**Peak: 18.0% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[10111, 4096], [], []]`
- `[[10240, 4096], [10240, 4096], []]`
- `[[11821680, 1, 128], []]`
- `[[16384, 4096], [16384, 4096], []]`
- `[[16384, 4096], [4096, 4640]]`
- `[[16384, 4096], [], [], [], []]`
- `[[165], [], [], []]`
- `[[20, 4096], [20, 4096], []]`
- `[[30], [30], []]`
- `[[31], [31], []]`
- `[[32, 131072], [], []]`
- `[[32], [32], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 --tp 4 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
