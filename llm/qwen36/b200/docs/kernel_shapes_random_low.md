# Kernel Shape Inventory — random_low

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `66.1 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 15.77 | 1499 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `aten::ones_like` {"Concrete Inputs": ["", "6", "", "", "False", ""], "Input Dims": [[1, 1], [], [], [], [], []], "Input Strides": [[1, 1], [], [], [], [], []], "Input type": ["long int", "Scalar... |
| 10.37 | 369 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | external_id=626: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "64", "1", "3"], "Input Dims": [[38, 256], [], [38, 2048... |
| 7.78 | 34 | quant_gemm | ok | True | `nvjet_sm100_tst_192x8_64x8_2x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[49], [49], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 7.76 | 369 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=626: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "64", "1", "3"], "Input Dims": [[38, 256], [], [38, 2048... |
| 3.51 | 770 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[55524]", "[1]", "2"], "Input Dims": [[55524], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", ... |
| 2.85 | 344 | moe | ok | True | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 1, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 1, true>)` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[49], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "", "long int", "Sca... |
| 2.64 | 385 | moe | ok | True | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | external_id=2631: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "", "", "512", "0", "256", "1.", "4", "False", "0", "", "64", "1", "3"], "Input Dims": [[38, 256], [], [38, 2048... |
| 2.32 | 368 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[4]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", ... |

The CSV/JSON siblings contain full sample metadata and trace paths.
