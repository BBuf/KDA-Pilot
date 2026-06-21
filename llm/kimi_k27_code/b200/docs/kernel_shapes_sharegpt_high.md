# Kernel Shape Inventory — sharegpt_high

- Model: `moonshotai/Kimi-K2.7-Code`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5413.5 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 28.88 | 7744 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=139104: `aten::matmul` {"Concrete Inputs": ["", ""], "Input Dims": [[51, 7168], [7168, 512]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 8.16 | 960 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` | external_id=139121: `aten::empty_strided` {"Concrete Inputs": ["[51, 7168]", "[7168, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Scala... |
| 6.60 | 2400 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["long unsigned int", "long unsigned int", "Scalar"]} |
| 5.97 | 976 | quant_gemm | ok | True | `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitK_TNT` | external_id=140408: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[51, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.37 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m128x32x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[2668, 8]", "6", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 3.85 | 2400 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["long unsigned int", "long unsigned int", "Scalar"]} |
| 3.40 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` | external_id=163414: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[65, 7168], [7168, 384]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.35 | 488 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | external_id=108687: `sgl_kernel::dsv3_fused_a_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[15, 2112], [15, 7168], [7168, 2112]], "Input Strides": [[2112, 1], [7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10:... |
| 2.73 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT` | external_id=162383: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[65, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.50 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m128x32x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `nccl:all_reduce` {"Concrete Inputs": [""], "Input Dims": [[2668, 7168]], "Input Strides": [[7168, 1]], "Input type": ["c10::BFloat16"]} |
| 2.31 | 1952 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ8Kv128PersistentSwapsAbForGen` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[2], [4862]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
