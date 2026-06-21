# Kernel Shape Inventory — random_mid

- Model: `openai/gpt-oss-120b`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `797.9 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 13.78 | 4544 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=7819: `Torch-Compiled Region: 1/3` {} |
| 5.26 | 3456 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[320], [320], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 5.22 | 288 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x128x256u2_s4_et128x32_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_lbW8_lsfbW4_dynB_sm100f` | external_id=9576: `Torch-Compiled Region: 1/1` {} |
| 4.41 | 288 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_bias_TNT` | external_id=6218: `Torch-Compiled Region: 1/3` {} |
| 4.28 | 288 | quant_gemm | missing | True | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x128x256u2_s4_et128x64_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | external_id=9576: `Torch-Compiled Region: 1/1` {} |
| 3.80 | 592 | norm | missing | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=9576: `Torch-Compiled Region: 1/1` {} |
| 3.46 | 1404 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::empty` {"Concrete Inputs": ["[1]", "4", "0", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 3.45 | 112 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 3.18 | 48 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o288028801_tensorptrbf16gmemalign16o28801_tensorptrbf16gmemalign128o288028801___True_4__0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.84 | 1512 | quant_gemm | ok | True | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x8x256u2_s4_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `detach_` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.81 | 576 | moe | missing | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | external_id=9576: `Torch-Compiled Region: 1/1` {} |
| 2.46 | 2592 | quant_gemm | ok | True | `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantizationType)2, __nv_bfloat16, 32, true, false, false, false, std::integral_constant<bool, false> >(int, int, int, int, __nv_bfloat16 const*, float const*, void*, unsigned int*, flashinfer::QuantizationSFLayout)` | external_id=9576: `Torch-Compiled Region: 1/1` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
