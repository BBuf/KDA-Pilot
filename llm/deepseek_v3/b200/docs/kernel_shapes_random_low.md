# Kernel Shape Inventory — random_low

- Model: `deepseek-ai/DeepSeek-V3`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2752.2 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.54 | 8912 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=3421: `aten::as_strided` {"Concrete Inputs": ["", "[39, 1]", "[1, 40]", "0"], "Input Dims": [[40, 1], [], [], []], "Input Strides": [[1, 40], [], [], []], "Input type": ["int", "ScalarList", "ScalarList... |
| 14.14 | 472 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT` | external_id=13144: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[39, 7168], [7168, 256]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.53 | 17872 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[49], [49], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.45 | 4012 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=2016: `aten::transpose` {"Concrete Inputs": ["", "0", "1"], "Input Dims": [[39, 56], [], []], "Input Strides": [[56, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 2.22 | 4096 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSeqQ16Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::_foreach_copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[[4], [4], [4], [1]], [[4], [4], [4], [1]], []], "Input Strides": [[[1], [1], [1], [1]], [[1], [1], [1], [1]], []], "Input ... |
| 2.06 | 544 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[4], [4], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
