# Kernel Shape Inventory — random_low

- Model: `deepseek-ai/DeepSeek-V3.1`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2568.8 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 33.11 | 8912 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=3421: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "False"], "Input Dims": [[39, 7168], [39, 7168], [7168], [], [], [], [], [], []], "Input... |
| 13.28 | 472 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT` | external_id=13144: `aten::t` {"Concrete Inputs": [""], "Input Dims": [[39, 56]], "Input Strides": [[56, 1]], "Input type": ["float"]} |
| 5.91 | 17872 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.93 | 544 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "0", "4", "1"], "Input Dims": [[4, 129280], [], [], [], []], "Input Strides": [[129280, 1], [], [], [], []], "Input type": ["float", "Scalar", "Sca... |
| 2.71 | 4071 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=12639: `aten::empty` {"Concrete Inputs": ["[39, 8]", "3", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "... |
| 2.38 | 4096 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSeqQ16Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
