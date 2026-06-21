# Kernel Shape Inventory — random_high

- Model: `zai-org/GLM-5.1-FP8`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `7485.8 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 24.12 | 10096 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=128277: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "True"], "Input Dims": [[192, 6144], [192, 6144], [6144], [], [], [], [], [], []], "Inpu... |
| 15.77 | 1248 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 8>, std::array<int, 8>)` | external_id=127298: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "True"], "Input Dims": [[1566, 6144], [1566, 6144], [6144], [], [], [], [], [], []], "In... |
| 9.96 | 608 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=102662: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 6144], [6144, 256]], "Input Strides": [[6144, 1], [1, 6144]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 7.26 | 4256 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[149, 2]", "3", "0", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 3.36 | 3724 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[169]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar"... |

The CSV/JSON siblings contain full sample metadata and trace paths.
