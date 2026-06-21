# Kernel Shape Inventory — random_high

- Model: `deepseek-ai/DeepSeek-Math-V2`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3403.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 12.57 | 1936 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 8>, std::array<int, 8>)` | external_id=1059449: `Torch-Compiled Region: 4/1` {} |
| 11.25 | 2784 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[163844]", "[1]", "62424564"], "Input Dims": [[4097, 163844], [], [], []], "Input Strides": [[163844, 1], [], [], []], "Input type": ["int", "ScalarLis... |
| 10.50 | 6776 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=36465: `Torch-Compiled Region: 4/2` {} |
| 5.59 | 2784 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[100], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 5.33 | 928 | quant_gemm | missing | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` | external_id=43863: `Torch-Compiled Region: 4/1` {} |
| 4.59 | 3904 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128PersistentSwapsAbForGen` | external_id=43908: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "0", "", "", "", "", "False", "", ""], "Input Dims": [[1792, 16, 512], [1792, 1, 512], [1792, 1, 512], [1792, 8192], [], [], [1792, ... |
| 4.12 | 464 | quant_gemm | missing | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` | external_id=36465: `Torch-Compiled Region: 4/2` {} |
| 3.46 | 4176 | moe | missing | True | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true> >(moe::dev::activation::KernelParams<cutlass::float_e4m3_t, 4, true>)` | external_id=43863: `Torch-Compiled Region: 4/1` {} |
| 2.48 | 870 | quant_gemm | missing | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=43863: `Torch-Compiled Region: 4/1` {} |
| 2.23 | 8784 | other | missing | True | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` | external_id=43863: `Torch-Compiled Region: 4/1` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
