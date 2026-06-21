# Empty-Shape Kernel Rows

- Generated at: `2026-06-21T01:28:45Z`
- Empty-shape rows: `119`
- Promotion status: not promoted to KDA task cards.
- Reason: the GPU kernel passed the strict `>2%` filter, but every retained profiler sample had empty `shape_args`.
- Common pattern: the row is attributed only to a `Torch-Compiled Region`, which is not enough to define a reusable kernel shape test.

## By Category

| Category | Rows |
|---|---:|
| `comm` | 25 |
| `gemm` | 11 |
| `moe` | 20 |
| `norm` | 10 |
| `other` | 3 |
| `quant_gemm` | 47 |
| `rope` | 3 |

## By Model

| Model slug | Rows |
|---|---:|
| `deepseek_math_v2` | 22 |
| `deepseek_v32` | 16 |
| `ernie45` | 11 |
| `glm_47_flash` | 3 |
| `glm_5` | 11 |
| `gpt_oss_120b` | 20 |
| `minimax_m25` | 9 |
| `minimax_m27` | 5 |
| `minimax_m3` | 18 |
| `poolside_laguna_xs2` | 4 |

## Rows

| Model slug | Workload | Category | % GPU | Top CPU ops | Kernel |
|---|---|---|---:|---|---|
| `deepseek_math_v2` | `random_low` | `comm` | 22.47 | `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `deepseek_math_v2` | `random_low` | `quant_gemm` | 2.49 | `Torch-Compiled Region: 4/2` | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` |
| `deepseek_math_v2` | `random_low` | `quant_gemm` | 2.21 | `Torch-Compiled Region: 4/2` | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` |
| `deepseek_math_v2` | `random_high` | `comm` | 12.57 | `Torch-Compiled Region: 4/1` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfe...` |
| `deepseek_math_v2` | `random_high` | `comm` | 10.50 | `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `deepseek_math_v2` | `random_high` | `quant_gemm` | 5.33 | `Torch-Compiled Region: 4/1` | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` |
| `deepseek_math_v2` | `random_high` | `quant_gemm` | 4.12 | `Torch-Compiled Region: 4/2` | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `deepseek_math_v2` | `random_high` | `moe` | 3.46 | `Torch-Compiled Region: 4/1` | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t...` |
| `deepseek_math_v2` | `random_high` | `quant_gemm` | 2.48 | `Torch-Compiled Region: 4/1` | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` |
| `deepseek_math_v2` | `random_high` | `other` | 2.23 | `Torch-Compiled Region: 4/1` | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` |
| `deepseek_math_v2` | `sharegpt_low` | `comm` | 22.21 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `deepseek_math_v2` | `sharegpt_low` | `gemm` | 11.77 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` |
| `deepseek_math_v2` | `sharegpt_mid` | `comm` | 7.22 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `deepseek_math_v2` | `sharegpt_mid` | `gemm` | 3.18 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` |
| `deepseek_math_v2` | `sharegpt_mid` | `comm` | 2.85 | `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfe...` |
| `deepseek_math_v2` | `sharegpt_high` | `comm` | 14.02 | `Torch-Compiled Region: 4/3`, `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `deepseek_math_v2` | `sharegpt_high` | `comm` | 10.34 | `Torch-Compiled Region: 4/1`, `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfe...` |
| `deepseek_math_v2` | `sharegpt_high` | `quant_gemm` | 7.85 | `Torch-Compiled Region: 4/2`, `Torch-Compiled Region: 4/1` | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` |
| `deepseek_math_v2` | `sharegpt_high` | `gemm` | 4.65 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` |
| `deepseek_math_v2` | `sharegpt_high` | `quant_gemm` | 3.50 | `Torch-Compiled Region: 4/1` | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` |
| `deepseek_math_v2` | `sharegpt_high` | `moe` | 3.27 | `Torch-Compiled Region: 4/1` | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t...` |
| `deepseek_math_v2` | `sharegpt_high` | `other` | 2.17 | `Torch-Compiled Region: 4/1` | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` |
| `deepseek_v32` | `random_low` | `comm` | 17.66 | `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `deepseek_v32` | `random_low` | `quant_gemm` | 11.60 | `Torch-Compiled Region: 4/2` | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `deepseek_v32` | `random_low` | `gemm` | 8.04 | `Torch-Compiled Region: 4/2` | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAA...` |
| `deepseek_v32` | `random_low` | `quant_gemm` | 2.62 | `Torch-Compiled Region: 4/2` | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` |
| `deepseek_v32` | `random_high` | `comm` | 6.87 | `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `deepseek_v32` | `random_high` | `quant_gemm` | 4.28 | `Torch-Compiled Region: 4/2` | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `deepseek_v32` | `sharegpt_low` | `comm` | 19.26 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `deepseek_v32` | `sharegpt_low` | `gemm` | 13.24 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` |
| `deepseek_v32` | `sharegpt_low` | `quant_gemm` | 3.34 | `Torch-Compiled Region: 4/3` | `kernel_cutlass_kernel_flashinferquantizationkernelsnvfp4_quantizeNVFP4QuantizeSwizzledKernel_object_at__tensorptrbf16gmemalign16o716871681_tensorptri8gmemalign16o358435841_tenso...` |
| `deepseek_v32` | `sharegpt_low` | `quant_gemm` | 2.69 | `Torch-Compiled Region: 4/3` | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` |
| `deepseek_v32` | `sharegpt_mid` | `comm` | 7.45 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `deepseek_v32` | `sharegpt_mid` | `gemm` | 3.58 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` |
| `deepseek_v32` | `sharegpt_high` | `comm` | 12.32 | `Torch-Compiled Region: 4/2`, `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `deepseek_v32` | `sharegpt_high` | `gemm` | 5.32 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` |
| `deepseek_v32` | `sharegpt_high` | `quant_gemm` | 4.27 | `Torch-Compiled Region: 4/2` | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x32x512u2_s4_et128x32_m128x32x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` |
| `deepseek_v32` | `sharegpt_high` | `other` | 2.47 | `Torch-Compiled Region: 4/1` | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` |
| `ernie45` | `random_low` | `moe` | 37.00 | `Torch-Compiled Region: 4/1` | `fused_moe_kernel` |
| `ernie45` | `random_low` | `rope` | 2.33 | `Torch-Compiled Region: 4/1` | `void (anonymous namespace)::fused_rope_kernel<false, 128l, true, __nv_bfloat16, long, 16u>((anonymous namespace)::FusedRopeParams)` |
| `ernie45` | `random_mid` | `moe` | 63.38 | `Torch-Compiled Region: 4/1` | `fused_moe_kernel` |
| `ernie45` | `random_mid` | `quant_gemm` | 6.74 | `Torch-Compiled Region: 4/1` | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `ernie45` | `random_mid` | `quant_gemm` | 4.19 | `Torch-Compiled Region: 4/1` | `nvjet_sm100_tst_128x256_64x6_2x2_2cta_h_bz_TNT` |
| `ernie45` | `random_mid` | `norm` | 2.16 | `Torch-Compiled Region: 4/1` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `ernie45` | `random_high` | `moe` | 64.96 | `Torch-Compiled Region: 4/1` | `fused_moe_kernel` |
| `ernie45` | `sharegpt_low` | `moe` | 35.86 | `Torch-Compiled Region: 4/1` | `fused_moe_kernel` |
| `ernie45` | `sharegpt_mid` | `moe` | 62.86 | `Torch-Compiled Region: 4/1` | `fused_moe_kernel` |
| `ernie45` | `sharegpt_mid` | `quant_gemm` | 6.63 | `Torch-Compiled Region: 4/1` | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `ernie45` | `sharegpt_high` | `moe` | 64.82 | `Torch-Compiled Region: 4/1` | `fused_moe_kernel` |
| `glm_47_flash` | `random_low` | `moe` | 21.80 | `Torch-Compiled Region: 5/1` | `fused_moe_kernel` |
| `glm_47_flash` | `random_high` | `moe` | 27.34 | `Torch-Compiled Region: 5/0` | `fused_moe_kernel` |
| `glm_47_flash` | `sharegpt_low` | `moe` | 20.23 | `Torch-Compiled Region: 5/1` | `fused_moe_kernel` |
| `glm_5` | `random_low` | `comm` | 17.24 | `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `glm_5` | `random_low` | `quant_gemm` | 11.22 | `Torch-Compiled Region: 4/2` | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `glm_5` | `random_mid` | `comm` | 4.76 | `Torch-Compiled Region: 4/2` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `glm_5` | `random_mid` | `quant_gemm` | 3.84 | `Torch-Compiled Region: 4/2` | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x16x512u2_s5_et128x16_m128x16x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` |
| `glm_5` | `sharegpt_low` | `comm` | 19.38 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `glm_5` | `sharegpt_low` | `quant_gemm` | 18.01 | `Torch-Compiled Region: 4/3` | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` |
| `glm_5` | `sharegpt_low` | `quant_gemm` | 2.79 | `Torch-Compiled Region: 4/3` | `kernel_cutlass_kernel_flashinferquantizationkernelsnvfp4_quantizeNVFP4QuantizeSwizzledKernel_object_at__tensorptrbf16gmemalign16o614461441_tensorptri8gmemalign16o307230721_tenso...` |
| `glm_5` | `sharegpt_mid` | `comm` | 6.67 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `glm_5` | `sharegpt_mid` | `quant_gemm` | 5.96 | `Torch-Compiled Region: 4/3` | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` |
| `glm_5` | `sharegpt_high` | `comm` | 3.57 | `Torch-Compiled Region: 4/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>...` |
| `glm_5` | `sharegpt_high` | `quant_gemm` | 2.51 | `Torch-Compiled Region: 4/3` | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` |
| `gpt_oss_120b` | `random_low` | `rope` | 2.31 | `Torch-Compiled Region: 1/3` | `void (anonymous namespace)::fused_rope_kernel<true, 64l, true, __nv_bfloat16, long, 8u>((anonymous namespace)::FusedRopeParams)` |
| `gpt_oss_120b` | `random_mid` | `quant_gemm` | 4.28 | `Torch-Compiled Region: 1/1` | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x128x256u2_s4_et128x64_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` |
| `gpt_oss_120b` | `random_mid` | `norm` | 3.80 | `Torch-Compiled Region: 1/1` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `gpt_oss_120b` | `random_mid` | `moe` | 2.81 | `Torch-Compiled Region: 1/1` | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bf...` |
| `gpt_oss_120b` | `random_high` | `comm` | 27.69 | `Torch-Compiled Region: 1/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `gpt_oss_120b` | `random_high` | `quant_gemm` | 8.01 | `Torch-Compiled Region: 1/3` | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_bias_TNT` |
| `gpt_oss_120b` | `sharegpt_low` | `quant_gemm` | 27.11 | `Torch-Compiled Region: 1/3` | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` |
| `gpt_oss_120b` | `sharegpt_low` | `comm` | 24.00 | `Torch-Compiled Region: 1/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `gpt_oss_120b` | `sharegpt_low` | `quant_gemm` | 3.08 | `Torch-Compiled Region: 1/3` | `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantizationType)2, __nv_bfloat16, 32, true, false, false, false, std::integral_constant<bool, fals...` |
| `gpt_oss_120b` | `sharegpt_low` | `moe` | 2.99 | `Torch-Compiled Region: 1/3` | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_...` |
| `gpt_oss_120b` | `sharegpt_low` | `rope` | 2.41 | `Torch-Compiled Region: 1/3` | `void (anonymous namespace)::fused_rope_kernel<true, 64l, true, __nv_bfloat16, long, 8u>((anonymous namespace)::FusedRopeParams)` |
| `gpt_oss_120b` | `sharegpt_mid` | `comm` | 17.00 | `Torch-Compiled Region: 1/3` | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>...` |
| `gpt_oss_120b` | `sharegpt_mid` | `quant_gemm` | 12.45 | `Torch-Compiled Region: 1/3` | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` |
| `gpt_oss_120b` | `sharegpt_mid` | `comm` | 11.89 | `Torch-Compiled Region: 1/2` | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distribu...` |
| `gpt_oss_120b` | `sharegpt_mid` | `quant_gemm` | 5.06 | `Torch-Compiled Region: 1/3` | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_bias_TNT` |
| `gpt_oss_120b` | `sharegpt_mid` | `quant_gemm` | 2.91 | `Torch-Compiled Region: 1/2` | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x128x128_s7_et128x64_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` |
| `gpt_oss_120b` | `sharegpt_mid` | `quant_gemm` | 2.29 | `Torch-Compiled Region: 1/2` | `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantizationType)2, __nv_bfloat16, 32, true, false, false, false, std::integral_constant<bool, fals...` |
| `gpt_oss_120b` | `sharegpt_mid` | `quant_gemm` | 2.29 | `Torch-Compiled Region: 1/2` | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x128x256u2_s4x4x4x4x1x4_et128x32_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGl...` |
| `gpt_oss_120b` | `sharegpt_mid` | `norm` | 2.24 | `Torch-Compiled Region: 1/2` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `gpt_oss_120b` | `sharegpt_high` | `quant_gemm` | 5.65 | `Torch-Compiled Region: 1/3` | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` |
| `minimax_m25` | `random_high` | `gemm` | 6.04 | `Torch-Compiled Region: 5/3` | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `minimax_m25` | `random_high` | `gemm` | 4.19 | `Torch-Compiled Region: 5/3` | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` |
| `minimax_m25` | `random_high` | `quant_gemm` | 2.63 | `Torch-Compiled Region: 5/3` | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half c...` |
| `minimax_m25` | `random_high` | `norm` | 2.54 | `Torch-Compiled Region: 5/3` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` |
| `minimax_m25` | `sharegpt_low` | `moe` | 15.77 | `Torch-Compiled Region: 5/3` | `fused_moe_kernel` |
| `minimax_m25` | `sharegpt_low` | `comm` | 13.30 | `Torch-Compiled Region: 5/3` | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` |
| `minimax_m25` | `sharegpt_low` | `moe` | 3.13 | `Torch-Compiled Region: 5/3` | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` |
| `minimax_m25` | `sharegpt_low` | `norm` | 2.07 | `Torch-Compiled Region: 5/3` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` |
| `minimax_m25` | `sharegpt_low` | `gemm` | 2.03 | `Torch-Compiled Region: 5/3` | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` |
| `minimax_m27` | `random_low` | `moe` | 3.39 | `Torch-Compiled Region: 5/3` | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` |
| `minimax_m27` | `random_low` | `gemm` | 2.12 | `Torch-Compiled Region: 5/3` | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` |
| `minimax_m27` | `random_mid` | `quant_gemm` | 2.74 | `Torch-Compiled Region: 5/1` | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __nv_bfloat16, __nv_fp8_e4m3, false, false, false, true, float>(_...` |
| `minimax_m27` | `sharegpt_low` | `moe` | 3.59 | `Torch-Compiled Region: 5/3` | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` |
| `minimax_m27` | `sharegpt_high` | `moe` | 32.22 | `Torch-Compiled Region: 5/3` | `fused_moe_kernel` |
| `minimax_m3` | `random_low` | `norm` | 18.45 | `Torch-Compiled Region: 5/4` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `minimax_m3` | `random_low` | `quant_gemm` | 8.90 | `Torch-Compiled Region: 5/4` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `random_mid` | `quant_gemm` | 11.97 | `Torch-Compiled Region: 5/2` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `random_mid` | `quant_gemm` | 9.80 | `Torch-Compiled Region: 5/2` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `random_mid` | `quant_gemm` | 6.87 | `Torch-Compiled Region: 5/2` | `_mxfp8_block_scaled_matmul_kernel` |
| `minimax_m3` | `random_mid` | `quant_gemm` | 2.06 | `Torch-Compiled Region: 5/2` | `void (anonymous namespace)::per_token_quant_ue8m0_scatter_kernel<32u, 5u, true>((anonymous namespace)::PerTokenQuantUe8m0ScatterParams)` |
| `minimax_m3` | `random_high` | `quant_gemm` | 14.68 | `Torch-Compiled Region: 5/2` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `random_high` | `quant_gemm` | 10.64 | `Torch-Compiled Region: 5/2` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `sharegpt_low` | `norm` | 19.57 | `Torch-Compiled Region: 5/4` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `minimax_m3` | `sharegpt_low` | `quant_gemm` | 8.46 | `Torch-Compiled Region: 5/4` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `sharegpt_low` | `quant_gemm` | 6.24 | `Torch-Compiled Region: 5/4` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `sharegpt_mid` | `comm` | 12.10 | `Torch-Compiled Region: 5/4` | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` |
| `minimax_m3` | `sharegpt_mid` | `norm` | 12.08 | `Torch-Compiled Region: 5/4` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `minimax_m3` | `sharegpt_mid` | `quant_gemm` | 10.59 | `Torch-Compiled Region: 5/2` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `sharegpt_high` | `norm` | 8.78 | `Torch-Compiled Region: 5/4` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `minimax_m3` | `sharegpt_high` | `quant_gemm` | 8.59 | `Torch-Compiled Region: 5/2` | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u,...` |
| `minimax_m3` | `sharegpt_high` | `comm` | 7.06 | `Torch-Compiled Region: 5/4` | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` |
| `minimax_m3` | `sharegpt_high` | `quant_gemm` | 4.70 | `Torch-Compiled Region: 5/2` | `_mxfp8_block_scaled_matmul_kernel` |
| `poolside_laguna_xs2` | `sharegpt_low` | `moe` | 11.02 | `Torch-Compiled Region: 5/3` | `fused_moe_kernel` |
| `poolside_laguna_xs2` | `sharegpt_low` | `norm` | 3.10 | `Torch-Compiled Region: 5/3` | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` |
| `poolside_laguna_xs2` | `sharegpt_mid` | `moe` | 19.07 | `Torch-Compiled Region: 5/1` | `fused_moe_kernel` |
| `poolside_laguna_xs2` | `sharegpt_mid` | `quant_gemm` | 2.83 | `Torch-Compiled Region: 5/1` | `nvjet_sm100_tst_128x256_64x6_2x2_2cta_h_bz_TNT` |
