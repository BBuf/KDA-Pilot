# Kernel Shape Inventory — random_low

- Model: `moonshotai/Kimi-K2.5`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1760.8 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 35.23 | 8712 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=8946: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "False"], "Input Dims": [[38, 7168], [38, 7168], [7168], [], [], [], [], [], []], "Input... |
| 16.85 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT` | external_id=8963: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 12.90 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` | external_id=3106: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 7168], [7168, 384]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.98 | 3904 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[0], [38]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 2.72 | 11712 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 163840]", "[163840, 1]", "0"], "Input Dims": [[1, 163840], [], [], []], "Input Strides": [[163840, 1], [], [], []], "Input type": ["float", "Scalar... |
| 2.66 | 1920 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m256x16x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.65 | 3840 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.56 | 3904 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 163840], [], []], "Input Strides": [[163840, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 2.00 | 1440 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256u2_s3_et128x16_m256x16x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
