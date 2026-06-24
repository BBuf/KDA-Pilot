# Profile evidence — deepseek_v4__sgl_kernel_sparse_decode_fwd

**e2e-optimization target: 4.1% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-V4-Flash`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `deepseek-ai/DeepSeek-V4-Flash` (slug `deepseek_v4`, tp=4)
- Python interface: `sgl_kernel.sparse_decode_fwd`
- Kernel family: `attention`  ·  Category: `quant_gemm`
- GPU kernel(s): `void sm100::decode::head64::flash_fwd_splitkv_mla_fp8_sparse_kernel<sm100::decode::head64:`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| sharegpt | conc 32 | 4.11% |
| sharegpt | conc 100 | 2.70% |

**Peak: 4.1% in `sharegpt_mid` (sharegpt, concurrency 32).**

## Input shapes (profiler)
- `[[1741, 1, 64, 512], [1988, 256, 1, 584], [1741, 1, 128], [1741], [64], [148, 8]`
- `[[3286, 1, 64, 512], [1988, 256, 1, 584], [3286, 1, 128], [3286], [64], [148, 8]`
- `[[3286, 1, 64, 512], [1988, 256, 1, 584], [3286, 1, 128], [3286], [64], [], [], `

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-V4-Flash --tp 4 --moe-runner-backend flashinfer_mxfp4 --trust-remote-code
```
After optimizing, re-run **sharegpt_mid** to validate the e2e effect.
