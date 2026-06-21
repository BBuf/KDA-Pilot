# Kernel Shape Inventory — random_high

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1758.8 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 6.87 | 3388 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=38536: `Torch-Compiled Region: 4/2` {} |
| 5.86 | 754 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x16x512_s5_et128x16_m128x16x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[104, 16], [104, 16], []], "Input Strides": [[2560, 1], [16, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 4.28 | 476 | quant_gemm | missing | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` | external_id=38536: `Torch-Compiled Region: 4/2` {} |
| 3.67 | 348 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[49408, 7168]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sca... |
| 3.10 | 406 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[100], [100], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 3.08 | 754 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x16x512_s5_et128x16_m256x16x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[0], [0], []], "Input Strides": [[1], [1], []], "Input type": ["int", "long int", "Scalar"]} |
| 3.07 | 406 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x32x512u2_s4_et128x32_m128x32x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[100], [100], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.84 | 1708 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ32Kv128PersistentSwapsAbForGen` | external_id=44448: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[31], [31], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 2.79 | 488 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=67849: `aten::as_strided` {"Concrete Inputs": ["", "[32329, 32, 128]", "[8192, 256, 1]", "0"], "Input Dims": [[32329, 32, 256], [], [], []], "Input Strides": [[8192, 256, 1], [], [], []], "Input type": [... |
| 2.49 | 244 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk192HV128SeparateQkvCausalVarSeqQ128Kv128PersistentContext` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[448]", "[1]", "0"], "Input Dims": [[448], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |
| 2.39 | 3706 | gemm | ok | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK21111000_PermutationMNK____MMAAtom_ThrID2_0` | external_id=53932: `sglang::fp4_gemm` {"Concrete Inputs": ["", "", "", "", "", "15", "9216"], "Input Dims": [[2121, 3584], [3584, 9216], [2176, 448], [448, 9216], [], [], []], "Input Strides": [[3584, 1], [1, 3584],... |
| 2.31 | 484 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 4>, std::array<int, 4>)` | external_id=45147: `Torch-Compiled Region: 4/2` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
