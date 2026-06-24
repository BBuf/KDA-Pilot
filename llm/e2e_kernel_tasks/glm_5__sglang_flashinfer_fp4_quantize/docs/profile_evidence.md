# Profile evidence — glm_5__sglang_flashinfer_fp4_quantize

**e2e-optimization target: 13.1% of total GPU time** (max across scenarios) on
`nvidia/GLM-5-NVFP4`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `nvidia/GLM-5-NVFP4` (slug `glm_5`, tp=4)
- Python interface: `sglang.flashinfer_fp4_quantize`
- Kernel family: `attention`  ·  Category: `attention`
- GPU kernel(s): `fmhaSm100fKernel_QkvBfloat16OBfloat16H256SeparateQkvCausalVarSeqQ128Kv128PersistentContext`, `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512HVPerCta128PagedKvDenseStaticTokenSparseP1Mult`, `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128P`, `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPer`, `kernel_cutlass_kernel_flashinferquantizationkernelsnvfp4_quantizeNVFP4QuantizeSwizzledKern`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 11.86% |
| random | conc 32 | 2.03% |
| random | conc 100 | 4.89% |
| sharegpt | conc 1 | 11.40% |
| sharegpt | conc 32 | 8.39% |
| sharegpt | conc 100 | 13.10% |

**Peak: 13.1% in `sharegpt_high` (sharegpt, concurrency 100).**

## Input shapes (profiler)
- `[[1, 1], [1, 1], []]`
- `[[16873, 16, 256], []]`
- `[[16873, 3072], [3072, 6144], [16896, 384], [384, 6144], [], [], []]`
- `[[1], [1], []]`
- `[[1], [], [], []]`
- `[[1], [], []]`
- `[[201]]`
- `[[20784, 1, 16, 512], []]`
- `[[20784, 1, 16, 576], []]`
- `[[30796, 3072], [3072, 1024], [30848, 384], [384, 1024], [], [], []]`
- `[[30796, 3072], [3072, 6144], [30848, 384], [384, 6144], [], [], []]`
- `[[], [], [], [], [], []]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/GLM-5-NVFP4 --tp 4 --quantization modelopt_fp4 --kv-cache-dtype fp8_e4m3
```
After optimizing, re-run **sharegpt_high** to validate the e2e effect.
