# Kernel Shape Inventory — sharegpt_high

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `167.5 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 12.84 | 246 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | external_id=184300: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "1024", "1", "3"], "Input Dims": [[1020, 256], [], [1020... |
| 4.67 | 205 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[48], [48], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 3.36 | 328 | moe | ok | True | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true>)` | external_id=163729: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "2048", "1", "3"], "Input Dims": [[1233, 256], [], [1233... |
| 3.32 | 92 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | external_id=172400: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "512", "1", "3"], "Input Dims": [[320, 256], [], [320, 2... |
| 3.07 | 41 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | external_id=159698: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "2048", "1", "3"], "Input Dims": [[1233, 256], [], [1233... |
| 2.12 | 410 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 128u, 32u, 128u, 1u, 128u, 128u, 64u, 11u, 128u, 128u, 2u, false, 148u, false, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[53523]", "[1]", "2"], "Input Dims": [[53525], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", ... |
| 2.07 | 41 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=184300: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "1024", "1", "3"], "Input Dims": [[1020, 256], [], [1020... |

The CSV/JSON siblings contain full sample metadata and trace paths.
