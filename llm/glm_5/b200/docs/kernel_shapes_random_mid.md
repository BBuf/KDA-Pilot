# Kernel Shape Inventory — random_mid

- Model: `nvidia/GLM-5-NVFP4`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2430.0 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 11.82 | 936 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=32195: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16873, 4096], [4096, 6144]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 6.91 | 300 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 5.52 | 300 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x128x256u2_s6_et128x128_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 4.76 | 4960 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=10641: `Torch-Compiled Region: 4/2` {} |
| 3.84 | 1200 | quant_gemm | missing | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x16x512u2_s5_et128x16_m128x16x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | external_id=10641: `Torch-Compiled Region: 4/2` {} |
| 3.55 | 600 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 3.23 | 1050 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512u2_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[2128, 202756], [], [32], [], []], "Input Strides": [[202756, 1], [], [1], [], []], "Input type": ["int", "", ... |
| 3.20 | 652 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16873, 2048], [2048, 4096]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.40 | 312 | quant_gemm | ok | True | `nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_TNT` | external_id=34008: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16873, 2048], [2048, 4096]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.03 | 2652 | gemm | ok | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID1_0` | external_id=20168: `sglang::fp4_gemm` {"Concrete Inputs": ["", "", "", "", "", "15", "6144"], "Input Dims": [[16873, 3072], [3072, 6144], [16896, 384], [384, 6144], [], [], []], "Input Strides": [[3072, 1], [1, 3072... |

The CSV/JSON siblings contain full sample metadata and trace paths.
