# Profile evidence — glm_47_flash__linear_gemm

**e2e-optimization target: 15.6% of total GPU time** (max across scenarios) on
`zai-org/GLM-4.7-Flash`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `zai-org/GLM-4.7-Flash` (slug `glm_47_flash`, tp=1)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_128x8_64x12_4x1_v_bz_TNT`, `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 15.64% |
| sharegpt | conc 1 | 14.43% |

**Peak: 15.6% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 154880]]`
- `[[1268645], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path zai-org/GLM-4.7-Flash --tp 1 --attention-backend triton --reasoning-parser glm45 --tool-call-parser glm47
```
After optimizing, re-run **random_low** to validate the e2e effect.
