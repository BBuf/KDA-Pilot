# Kernel Shape Inventory — random_low

- Model: `deepseek-ai/DeepSeek-Math-V2`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1437.8 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 22.47 | 8712 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=305: `Torch-Compiled Region: 4/2` {} |
| 11.70 | 464 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` | external_id=305: `Torch-Compiled Region: 4/2` {} |
| 8.47 | 16592 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[2560, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 5.94 | 7808 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 32u, 16u, 128u, 1u, 128u, 128u, 32u, 32u, 128u, 128u, 1u, false, 148u, false, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.49 | 464 | quant_gemm | missing | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | external_id=305: `Torch-Compiled Region: 4/2` {} |
| 2.22 | 2784 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schedS_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | timestamp_enclosure: `aten::sum` {"Concrete Inputs": ["", "[]", "False", ""], "Input Dims": [[1], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "Scalar", ""]} |
| 2.21 | 1856 | quant_gemm | missing | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=305: `Torch-Compiled Region: 4/2` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
