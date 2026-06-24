# Profile evidence — nemotron3_super__linear_gemm

**e2e-optimization target: 18.8% of total GPU time** (max across scenarios) on
`nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` (slug `nemotron3_super`, tp=4)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tss_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN`, `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x8_64x16_2x1_v_bz_splitK_TNT`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 18.79% |
| random | conc 32 | 6.77% |
| random | conc 100 | 9.34% |
| sharegpt | conc 1 | 18.12% |
| sharegpt | conc 32 | 5.51% |
| sharegpt | conc 100 | 7.85% |

**Peak: 18.8% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 131072], [], [], [], []]`
- `[[1, 131072], [], [], []]`
- `[[1, 131072], [], []]`
- `[[10111, 4096], [4096, 4640]]`
- `[[1025, 32, 64, 128], [], [30, 32, 64, 128], []]`
- `[[11821680, 1, 128], [], [], []]`
- `[[14375, 4096], [4096, 4640]]`
- `[[14599, 4096], [4096, 4640]]`
- `[[16384, 2048], [2048, 4096]]`
- `[[16384, 2560], [], [], [], []]`
- `[[16384, 4096], [4096, 4640]]`
- `[[1], [1], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16 --tp 4 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
