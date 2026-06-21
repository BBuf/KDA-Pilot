# Kernel Shape Inventory — sharegpt_high

- Model: `moonshotai/Kimi-K2.6`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `8378.0 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.20 | 7744 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=143071: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "False"], "Input Dims": [[51, 7168], [51, 7168], [7168], [], [], [], [], [], []], "Input... |
| 9.32 | 960 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` | external_id=143209: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[51, 7168], [7168, 384]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 8.85 | 976 | quant_gemm | ok | True | `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitK_TNT` | external_id=143088: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[51, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.22 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` | external_id=164456: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[65, 7168], [7168, 384]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.02 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT` | external_id=166701: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[65, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.70 | 2100 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256u2_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["long unsigned int", "long unsigned int", "Scalar"]} |
| 3.40 | 488 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | external_id=112537: `sgl_kernel::dsv3_fused_a_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[15, 2112], [15, 7168], [7168, 2112]], "Input Strides": [[2112, 1], [7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10:... |
| 2.46 | 2400 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x32x256_s3_et128x32_m256x32x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["long unsigned int", "long unsigned int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
