# Kernel Shape Inventory — random_high

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `364.6 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 11.83 | 82 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` | external_id=53670: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "16384", "1", "3"], "Input Dims": [[15434, 256], [], [15... |
| 6.94 | 328 | moe | ok | True | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true>)` | external_id=58364: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "16384", "1", "3"], "Input Dims": [[15434, 256], [], [15... |
| 6.10 | 82 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=58364: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "16384", "1", "3"], "Input Dims": [[15434, 256], [], [15... |
| 6.09 | 246 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[188, 248320], [], []], "Input Strides": [[248320, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 4.87 | 205 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 240u, 128u, 128u, 1u, 128u, 128u, 128u, 6u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=53304: `sglang::deep_gemm_fp8_fp8_bf16_nt` {"Concrete Inputs": ["", "", "", "", ""], "Input Dims": [[15434, 2048], [15434, 4], [12288, 2048], [12288, 4], [15434, 12288]], "Input Strides": [[2048, 1], [1, 15436], [2048, 1... |
| 2.97 | 246 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.14 | 328 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | external_id=55139: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "16384", "1", "3"], "Input Dims": [[15434, 256], [], [15... |

The CSV/JSON siblings contain full sample metadata and trace paths.
