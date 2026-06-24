# Profile evidence — qwen3_coder__linear_gemm

**e2e-optimization target: 18.1% of total GPU time** (max across scenarios) on
`Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`, from the exact cookbook-aligned profile. Profiler kernel-family; confirm exact Python interface via SGLANG_KERNEL_API_LOGLEVEL capture.

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` (slug `qwen3_coder`, tp=8)
- Python interface: `<confirm via capture; profiler family=linear_gemm>`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN`, `nvjet_sm100_tst_64x8_64x16_1x2_h_bz_splitK_TNT`, `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 1`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 18.12% |
| random | conc 32 | 3.33% |
| random | conc 100 | 5.88% |
| sharegpt | conc 1 | 16.92% |
| sharegpt | conc 32 | 4.97% |
| sharegpt | conc 100 | 2.94% |

**Peak: 18.1% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[0], [0], []]`
- `[[17], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], [], [], [], []]`
- `[[1]]`
- `[[2825120, 1, 128], []]`
- `[[32], [32], []]`
- `[[4097, 8196], [], [], []]`
- `[[512], [512], []]`
- `[[512], [], [], []]`
- `[[576], [576], []]`
- `[[6, 1536], [6, 1536], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8 --tp 8 --ep 8 --tool-call-parser qwen3_coder
```
After optimizing, re-run **random_low** to validate the e2e effect.
