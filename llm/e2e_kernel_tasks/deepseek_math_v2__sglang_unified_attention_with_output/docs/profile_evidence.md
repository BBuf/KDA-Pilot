# Profile evidence — deepseek_math_v2__sglang_unified_attention_with_output

**e2e-optimization target: 11.8% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-Math-V2`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `deepseek-ai/DeepSeek-Math-V2` (slug `deepseek_math_v2`, tp=8)
- Python interface: `sglang.unified_attention_with_output`
- Kernel family: `attention`  ·  Category: `gemm`
- GPU kernel(s): `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128P`, `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8,`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 100 | 4.59% |
| sharegpt | conc 1 | 11.77% |
| sharegpt | conc 32 | 10.55% |
| sharegpt | conc 100 | 9.65% |

**Peak: 11.8% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1536, 16, 512], [1536, 1, 512], [1536, 1, 512], [1536, 8192], [], [], [1536, 1`
- `[[1792, 16, 512], [1792, 1, 512], [1792, 1, 512], [1792, 8192], [], [], [1792, 1`
- `[[8661, 1, 16, 576], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-Math-V2 --tp 8 --ep 8 --trust-remote-code
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
