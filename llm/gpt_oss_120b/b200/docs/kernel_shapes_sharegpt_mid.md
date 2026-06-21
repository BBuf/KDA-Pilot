# Kernel Shape Inventory — sharegpt_mid

- Model: `openai/gpt-oss-120b`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `614.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 17.00 | 3976 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=26913: `Torch-Compiled Region: 1/3` {} |
| 12.45 | 3456 | quant_gemm | missing | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` | external_id=34900: `Torch-Compiled Region: 1/3` {} |
| 11.89 | 1168 | comm | missing | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=29581: `Torch-Compiled Region: 1/2` {} |
| 5.06 | 288 | quant_gemm | missing | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_bias_TNT` | external_id=26913: `Torch-Compiled Region: 1/3` {} |
| 3.85 | 360 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x128x256_s4x4x4x4x1x4_et128x32_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | external_id=31354: `Torch-Compiled Region: 1/2` {} |
| 3.43 | 1188 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | external_id=26913: `Torch-Compiled Region: 1/3` {} |
| 2.91 | 360 | quant_gemm | missing | True | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x128x128_s7_et128x64_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | external_id=31354: `Torch-Compiled Region: 1/2` {} |
| 2.81 | 1260 | quant_gemm | ok | True | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x8x256u2_s4_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[50]", "[1]", "110759220"], "Input Dims": [[50], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "Sc... |
| 2.29 | 2592 | quant_gemm | missing | True | `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantizationType)2, __nv_bfloat16, 32, true, false, false, false, std::integral_constant<bool, false> >(int, int, int, int, __nv_bfloat16 const*, float const*, void*, unsigned int*, flashinfer::QuantizationSFLayout)` | external_id=31354: `Torch-Compiled Region: 1/2` {} |
| 2.29 | 216 | quant_gemm | missing | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x128x256u2_s4x4x4x4x1x4_et128x32_m256x128x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | external_id=31354: `Torch-Compiled Region: 1/2` {} |
| 2.24 | 1168 | norm | missing | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=29581: `Torch-Compiled Region: 1/2` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
