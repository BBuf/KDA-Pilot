# Profile evidence — deepseek_v3__sglang_flashinfer_dsv3_router_gemm

**e2e-optimization target: 16.4% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-V3`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `deepseek-ai/DeepSeek-V3` (slug `deepseek_v3`, tp=8)
- Python interface: `sglang.flashinfer_dsv3_router_gemm`
- Kernel family: `attention`  ·  Category: `gemm`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSe`, `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ16Kv128PersistentSwa`, `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8,`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.22% |
| random | conc 100 | 2.94% |
| sharegpt | conc 1 | 16.40% |
| sharegpt | conc 32 | 14.93% |
| sharegpt | conc 100 | 4.41% |

**Peak: 16.4% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 1], [], [], [], [], [], []]`
- `[[128], [], [], []]`
- `[[16, 256], [16, 7168], [256, 7168]]`
- `[[192], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[30], [], [], []]`
- `[[6, 256], [6, 7168], [256, 7168]]`
- `[[[1, 1], [1, 3]], []]`
- `[[[192], [51]], []]`
- `[[[1]], [[1]], []]`
- `[[[4], [4], [4], [1]], [[4], [4], [4], [1]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-V3 --tp 8 --speculative-algorithm EAGLE
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
