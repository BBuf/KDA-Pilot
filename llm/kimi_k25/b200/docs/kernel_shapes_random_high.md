# Kernel Shape Inventory — random_high

- Model: `moonshotai/Kimi-K2.5`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `4526.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 19.13 | 7744 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=51750: `aten::transpose` {"Concrete Inputs": ["", "0", "1"], "Input Dims": [[2112, 7168], [], []], "Input Strides": [[7168, 1], [], []], "Input type": ["c10::BFloat16", "Scalar", "Scalar"]} |
| 11.77 | 2940 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 8.78 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT` | external_id=51767: `aten::as_strided` {"Concrete Inputs": ["", "[38, 8, 128]", "[1536, 192, 1]", "0"], "Input Dims": [[38, 8, 192], [], [], []], "Input Strides": [[1536, 192, 1], [], [], []], "Input type": ["c10::BF... |
| 7.72 | 3360 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[256]], []], "Input Strides": [[[1]], []], "Input type": ["TensorList", "Scalar"]} |
| 6.33 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` | external_id=56398: `aten::as_strided` {"Concrete Inputs": ["", "[512, 2048]", "[1, 512]", ""], "Input Dims": [[2048, 512], [], [], []], "Input Strides": [[512, 1], [], [], []], "Input type": ["c10::BFloat16", "Scala... |
| 5.68 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m128x32x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[35552, 7168]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sca... |
| 3.23 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m128x32x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `nccl:all_reduce` {"Concrete Inputs": [""], "Input Dims": [[2957, 7168]], "Input Strides": [[7168, 1]], "Input type": ["c10::BFloat16"]} |
| 2.50 | 3416 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[43]", "[1]", "448"], "Input Dims": [[491], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sc... |
| 2.39 | 3416 | quant_gemm | ok | True | `nvjet_sm100_tst_96x64_64x15_2x2_2cta_h_bz_splitK_TNN` | timestamp_enclosure: `aten::floor_divide` {"Concrete Inputs": ["", ""], "Input Dims": [[64], []], "Input Strides": [[1], []], "Input type": ["int", "long int"]} |
| 2.24 | 3360 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_1x4_h_bz_splitK_TNT` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[960], [13]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
