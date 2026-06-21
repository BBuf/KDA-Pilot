# Kernel Shape Inventory — sharegpt_high

- Model: `deepseek-ai/DeepSeek-V3.1`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `9239.7 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.66 | 7888 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=215892: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[49, 7168], [49, 7168], [7168], [], [], [], [], [], []], "Input ... |
| 11.95 | 944 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=215909: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[49, 7168], [7168, 256]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 9.60 | 976 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 8>, std::array<int, 8>)` | external_id=181373: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[1502, 7168], [1502, 7168], [7168], [], [], [], [], [], []], "In... |
| 4.96 | 2832 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | external_id=171418: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "8", "4", "256", "0", "256", "2.5", "2", "False", "0", "", "2048", "1", "3"], "Input Dims": [[1502, 256], [256],... |
| 4.08 | 472 | gemm | ok | True | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` | external_id=164556: `sglang::flashinfer_dsv3_router_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[16, 256], [16, 7168], [256, 7168]], "Input Strides": [[256, 1], [7168, 1], [7168, 1]], "Input type": ["float", "c10::BFloat16",... |
| 2.92 | 2832 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=167202: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "8", "4", "256", "0", "256", "2.5", "2", "False", "0", "", "2048", "1", "3"], "Input Dims": [[1502, 256], [256],... |

The CSV/JSON siblings contain full sample metadata and trace paths.
