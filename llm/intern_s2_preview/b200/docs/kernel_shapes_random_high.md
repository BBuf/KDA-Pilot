# Kernel Shape Inventory — random_high

- Model: `internLM/Intern-S2-Preview`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3505.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 13.27 | 3792 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=39533: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[274, 2048], [274, 2048], [2048], [], [], [], [], [], []], "Inpu... |
| 5.37 | 3520 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=41145: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[274, 2048], [2048, 128]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.59 | 960 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `c10d::allreduce_` {"Concrete Inputs": ["", "", "", "", "False", "-1"], "Input Dims": [[[16384, 2048]], [], [], [], [], []], "Input Strides": [[[2048, 1]], [], [], [], [], []], "Input type": ["Ten... |
| 4.41 | 960 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[147200, 2048]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sc... |
| 2.78 | 1280 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[16384, 2048]"], "Input Dims": [[16384, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.22 | 1968 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[30], [30], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
