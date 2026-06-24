# Profile evidence — deepseek_r1_fp4__sglang_flashinfer_dsv3_router_gemm

**e2e-optimization target: 19.1% of total GPU time** (max across scenarios) on
`nvidia/DeepSeek-R1-0528-FP4-v2`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2` (slug `deepseek_r1_fp4`, tp=8)
- Python interface: `sglang.flashinfer_dsv3_router_gemm`
- Kernel family: `attention`  ·  Category: `gemm`
- GPU kernel(s): `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSeqQ16`, `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8,`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| sharegpt | conc 1 | 19.13% |
| sharegpt | conc 32 | 12.04% |
| sharegpt | conc 100 | 5.70% |

**Peak: 19.1% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[16, 256], [16, 7168], [256, 7168]]`
- `[[48], [], [], []]`
- `[[6, 256], [6, 7168], [256, 7168]]`
- `[[[1, 1], [1, 3]], []]`
- `[[], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/DeepSeek-R1-0528-FP4-v2 --tp 8 --trust-remote-code
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
