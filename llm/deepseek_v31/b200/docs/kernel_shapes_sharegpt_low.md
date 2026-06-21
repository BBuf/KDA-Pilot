# Kernel Shape Inventory — sharegpt_low

- Model: `deepseek-ai/DeepSeek-V3.1`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2853.2 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 35.26 | 8912 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=88986: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "False"], "Input Dims": [[16, 7168], [16, 7168], [7168], [], [], [], [], [], []], "Input... |
| 14.68 | 472 | gemm | ok | True | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` | external_id=98716: `sglang::flashinfer_dsv3_router_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[16, 256], [16, 7168], [256, 7168]], "Input Strides": [[256, 1], [7168, 1], [7168, 1]], "Input type": ["float", "c10::BFloat16",... |
| 5.50 | 18864 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `aten::to` {"Concrete Inputs": ["", "3", "0", "", "", "True", "False", ""], "Input Dims": [[1], [], [], [], [], [], [], []], "Input Strides": [[1], [], [], [], [], [], [], []], "Input type... |
| 2.25 | 4012 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=87818: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "8", "4", "256", "0", "256", "2.5", "2", "False", "0", "", "16", "1", "3"], "Input Dims": [[16, 256], [256], [16... |
| 2.14 | 4096 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSeqQ16Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1]", "[1]", "0"], "Input Dims": [[48], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
