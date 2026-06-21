# Kernel Shape Inventory — random_high

- Model: `moonshotai/Kimi-K2.6`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `4186.5 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 18.31 | 7744 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=41702: `aten::empty` {"Concrete Inputs": ["[38, 8]", "3", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scala... |
| 12.69 | 2940 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[896], [896], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 8.36 | 3360 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "576"], "Input Dims": [[576], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |
| 7.77 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT` | external_id=41719: `aten::linear` {"Concrete Inputs": ["", "", ""], "Input Dims": [[38, 7168], [512, 7168], []], "Input Strides": [[7168, 1], [7168, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", ""]} |
| 5.91 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` | external_id=44142: `aten::as_strided` {"Concrete Inputs": ["", "[38, 8, 128]", "[2048, 256, 1]", "128"], "Input Dims": [[38, 8, 256], [], [], []], "Input Strides": [[2048, 256, 1], [], [], []], "Input type": ["c10::... |
| 3.96 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x128x128_s4_et128x64_m256x128x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `nccl:all_reduce` {"Concrete Inputs": [""], "Input Dims": [[2957, 7168]], "Input Strides": [[7168, 1]], "Input type": ["c10::BFloat16"]} |
| 2.70 | 3416 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[256], [256], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 2.60 | 3416 | quant_gemm | ok | True | `nvjet_sm100_tst_96x64_64x15_2x2_2cta_h_bz_splitK_TNN` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[448], [448], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 2.42 | 3360 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_1x4_h_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "576"], "Input Dims": [[576], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |

The CSV/JSON siblings contain full sample metadata and trace paths.
