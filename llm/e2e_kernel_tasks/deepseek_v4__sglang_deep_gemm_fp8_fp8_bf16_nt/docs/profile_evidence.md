# Profile evidence — deepseek_v4__sglang_deep_gemm_fp8_fp8_bf16_nt

**e2e-optimization target: 15.9% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-V4-Flash`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `deepseek-ai/DeepSeek-V4-Flash` (slug `deepseek_v4`, tp=4)
- Python interface: `sglang.deep_gemm_fp8_fp8_bf16_nt`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 1`, `void deep_gemm::sm100_tf32_hc_prenorm_gemm_impl<24u, 16384u, 64u, 32u, 64u, 2u, 128u, 12u,`, `void deep_gemm::sm100_tf32_hc_prenorm_gemm_impl<24u, 16384u, 64u, 32u, 64u, 3u, 128u, 12u,`, `void deep_gemm::sm100_tf32_hc_prenorm_gemm_impl<24u, 16384u, 64u, 32u, 64u, 4u, 128u, 12u,`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 5.04% |
| random | conc 32 | 15.92% |
| random | conc 100 | 9.51% |
| sharegpt | conc 1 | 4.87% |

**Peak: 15.9% in `random_mid` (random, concurrency 32).**

## Input shapes (profiler)
- `[[16384, 16384], [], [], []]`
- `[[1], []]`
- `[[1]]`
- `[[4, 1, 4096], [4, 4, 4096], []]`
- `[[4, 4, 4096], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-V4-Flash --tp 4 --moe-runner-backend flashinfer_mxfp4 --trust-remote-code
```
After optimizing, re-run **random_mid** to validate the e2e effect.
