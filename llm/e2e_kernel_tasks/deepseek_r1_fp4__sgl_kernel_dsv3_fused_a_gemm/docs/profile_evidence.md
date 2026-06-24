# Profile evidence — deepseek_r1_fp4__sgl_kernel_dsv3_fused_a_gemm

**e2e-optimization target: 42.4% of total GPU time** (max across scenarios) on
`nvidia/DeepSeek-R1-0528-FP4-v2`, from the exact cookbook-aligned profile. Clean Python interface (profiler provenance).

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2` (slug `deepseek_r1_fp4`, tp=8)
- Python interface: `sgl_kernel.dsv3_fused_a_gemm`
- Kernel family: `linear_gemm`  ·  Category: `quant_gemm`
- GPU kernel(s): `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalINS1_17GroupProblemShapeIN4cute5t`, `nvjet_sm100_tst_64x16_64x16_1x2_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x64_64x16_2x1_2cta_v_bz_TNT`, `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT`, `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT`, `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 con`, `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 cons`, `void tensorrt_llm::kernels::cutlass_kernels::expandInputRowsKernel<__nv_bfloat16, __nv_fp4`, `void tensorrt_llm::kernels::cutlass_kernels::finalizeMoeRoutingKernel<__nv_bfloat16, __nv_`

## % of GPU time by scenario

| dataset | concurrency | % of GPU time |
|---|---|---|
| random | conc 1 | 37.04% |
| random | conc 32 | 21.69% |
| random | conc 100 | 42.43% |
| sharegpt | conc 1 | 22.45% |
| sharegpt | conc 32 | 29.47% |
| sharegpt | conc 100 | 25.94% |

**Peak: 42.4% in `random_high` (random, concurrency 100).**

## Input shapes (profiler)
- `[[0], [], []]`
- `[[11210, 14336], [14336, 7168]]`
- `[[11210, 7168]]`
- `[[128], [128], []]`
- `[[1427, 1, 576], [], [], []]`
- `[[1427, 7168], []]`
- `[[1502, 1024], [1024, 7168], [1536, 128], [128, 7168], [], [], []]`
- `[[1502, 16, 192], [1502, 16, 192], []]`
- `[[16, 2112], [16, 7168], [7168, 2112]]`
- `[[16], [], [], []]`
- `[[1], [1], []]`
- `[[1]]`

## Reproduce (cookbook-aligned)
```bash
sglang serve --model-path nvidia/DeepSeek-R1-0528-FP4-v2 --tp 8 --trust-remote-code
```
After optimizing, re-run **random_high** to validate the e2e effect.
