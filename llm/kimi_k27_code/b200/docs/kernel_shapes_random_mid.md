# Kernel Shape Inventory — random_mid

- Model: `moonshotai/Kimi-K2.7-Code`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `6126.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 12.17 | 7744 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=19808: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "False"], "Input Dims": [[38, 7168], [38, 7168], [7168], [], [], [], [], [], []], "Input... |
| 7.79 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256u2_s3_et128x64_m128x64x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `nccl:all_reduce` {"Concrete Inputs": [""], "Input Dims": [[11218, 7168]], "Input Strides": [[7168, 1]], "Input type": ["c10::BFloat16"]} |
| 5.62 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT` | external_id=19825: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.43 | 3420 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256u2_s3_et128x16_m256x16x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 4.77 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` | external_id=12794: `aten::t` {"Concrete Inputs": [""], "Input Dims": [[1536, 1536]], "Input Strides": [[1536, 1]], "Input type": ["c10::BFloat16"]} |
| 4.35 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256_s3_et128x64_m128x64x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[5888, 1, 64]", "15", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList",... |
| 3.60 | 3840 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m256x16x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |

The CSV/JSON siblings contain full sample metadata and trace paths.
