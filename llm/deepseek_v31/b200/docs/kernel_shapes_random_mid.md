# Kernel Shape Inventory — random_mid

- Model: `deepseek-ai/DeepSeek-V3.1`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `7771.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 13.78 | 7920 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=30319: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[39, 7168], [39, 7168], [7168], [], [], [], [], [], []], "Input ... |
| 4.89 | 472 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT` | external_id=30336: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[39, 7168], [7168, 256]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.66 | 2537 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[32]", "[1]", "0"], "Input Dims": [[48], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scala... |
| 4.22 | 472 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` | external_id=31827: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "8", "4", "256", "0", "256", "2.5", "2", "False", "0", "", "16384", "1", "3"], "Input Dims": [[11210, 256], [256... |
| 3.57 | 472 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=31827: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "8", "4", "256", "0", "256", "2.5", "2", "False", "0", "", "16384", "1", "3"], "Input Dims": [[11210, 256], [256... |
| 2.43 | 2537 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "896"], "Input Dims": [[896], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |

The CSV/JSON siblings contain full sample metadata and trace paths.
