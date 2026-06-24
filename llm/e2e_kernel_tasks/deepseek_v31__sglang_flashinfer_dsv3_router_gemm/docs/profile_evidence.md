# Profile evidence — deepseek_v31__sglang_flashinfer_dsv3_router_gemm

**e2e-optimization target: 16.8% of total GPU time** (max across scenarios) on
`deepseek-ai/DeepSeek-V3.1`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `deepseek-ai/DeepSeek-V3.1` (slug `deepseek_v31`, tp=8)
- Python interface: `sglang.flashinfer_dsv3_router_gemm`
- Kernel family: `attention`  ·  Category: `gemm`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSe`, `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ16Kv128PersistentSwa`, `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8,`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 2.38% |
| random | conc 100 | 3.07% |
| sharegpt | conc 1 | 16.82% |
| sharegpt | conc 32 | 8.29% |
| sharegpt | conc 100 | 4.08% |

**Peak: 16.8% in `sharegpt_low` (sharegpt, concurrency 1).**

## Input shapes (profiler)
- `[[1, 129280], [], [], [], [], [], []]`
- `[[1, 4], []]`
- `[[16, 256], [16, 7168], [256, 7168]]`
- `[[229], [], [], []]`
- `[[237], [], [], []]`
- `[[256], [256], []]`
- `[[3, 1, 4], [], [], []]`
- `[[48], [], [], []]`
- `[[5975], [], [], []]`
- `[[640], [], [], [], []]`
- `[[[1], [10797]], []]`
- `[[[4], [4], [4], [1]], [[4], [4], [4], [1]], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path deepseek-ai/DeepSeek-V3.1 --tp 8 --speculative-algorithm EAGLE --trust-remote-code
```
After optimizing, re-run **sharegpt_low** to validate the e2e effect.
