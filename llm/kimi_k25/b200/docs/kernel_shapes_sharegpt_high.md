# Kernel Shape Inventory — sharegpt_high

- Model: `moonshotai/Kimi-K2.5`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `9104.9 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.48 | 7744 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=152818: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "True"], "Input Dims": [[51, 7168], [51, 7168], [7168], [], [], [], [], [], []], "Input ... |
| 8.78 | 960 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` | external_id=152835: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[51, 7168], [7168, 384]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 8.40 | 976 | quant_gemm | ok | True | `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitK_TNT` | external_id=152714: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[51, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.50 | 488 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | external_id=122169: `aten::empty` {"Concrete Inputs": ["[120]", "3", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "",... |
| 4.08 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT` | external_id=177393: `aten::view` {"Concrete Inputs": ["", "[-1, 512]"], "Input Dims": [[65, 512], []], "Input Strides": [[512, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 4.07 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` | external_id=183910: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[65, 7168], [7168, 384]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.40 | 2100 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["long unsigned int", "long unsigned int", "Scalar"]} |
| 2.65 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m128x32x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[33248, 7168]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sca... |
| 2.26 | 2400 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
