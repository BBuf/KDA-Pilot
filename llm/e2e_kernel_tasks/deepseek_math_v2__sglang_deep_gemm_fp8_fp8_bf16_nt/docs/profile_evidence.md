# Profile evidence — deepseek_math_v2__sglang_deep_gemm_fp8_fp8_bf16_nt

**e2e-optimization target: 26.1% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-Math-V2`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `deepseek-ai/DeepSeek-Math-V2` (slug `deepseek_math_v2`, tp=8)
- Python interface: `sglang.deep_gemm_fp8_fp8_bf16_nt`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT`, `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 1`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 26.11% |
| random | conc 32 | 5.81% |
| random | conc 100 | 4.12% |
| sharegpt | conc 1 | 18.36% |
| sharegpt | conc 32 | 5.54% |

**Peak: 26.1% in `random_low` (random, concurrency 1).**

## Input shapes (profiler)
- `[[1, 1], [1, 1], []]`
- `[[11101, 7168], [11101, 14], [4608, 7168], [4608, 14], [11101, 4608]]`
- `[[1], [1], []]`
- `[[1], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[32], [], []]`
- `[[4097, 45], []]`
- `[[8661, 7168], [8661, 14], [4608, 7168], [4608, 14], [8661, 4608]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-Math-V2 --tp 8 --ep 8 --trust-remote-code
```
After optimizing, re-run **random_low** to validate the e2e effect.
