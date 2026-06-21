# Kernel Shape Inventory — random_mid

- Model: `zai-org/GLM-5.1-FP8`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `7798.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 19.57 | 10096 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=50549: `aten::alias` {"Concrete Inputs": [""], "Input Dims": [[1, 154880]], "Input Strides": [[154880, 1]], "Input type": ["c10::BFloat16"]} |
| 8.43 | 608 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=50566: `aten::index_put_` {"Concrete Inputs": ["", "", "", "False"], "Input Dims": [[49, 1], [], [], []], "Input Strides": [[1, 1], [], [], []], "Input type": ["float", "", "float", "Scalar"]} |
| 6.90 | 4976 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[149, 2]", "3", "0", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 4.75 | 608 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` | external_id=62409: `aten::reshape` {"Concrete Inputs": ["", "[11247, 128]"], "Input Dims": [[11247, 128], []], "Input Strides": [[128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 3.95 | 608 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=62409: `aten::reshape` {"Concrete Inputs": ["", "[11247, 128]"], "Input Dims": [[11247, 128], []], "Input Strides": [[128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 3.39 | 4430 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[149, 2]", "3", "0", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 2.78 | 224 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=73387: `aten::mm` {"Concrete Inputs": ["", "", "6", ""], "Input Dims": [[128, 6144], [6144, 32], [], [128, 32]], "Input Strides": [[6144, 1], [1, 6144], [], [32, 1]], "Input type": ["c10::BFloat1... |

The CSV/JSON siblings contain full sample metadata and trace paths.
