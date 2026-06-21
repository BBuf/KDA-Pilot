# Kernel Shape Inventory — sharegpt_low

- Model: `nvidia/GLM-5-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `770.2 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 19.38 | 5580 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=100125: `Torch-Compiled Region: 4/3` {} |
| 18.01 | 5508 | quant_gemm | missing | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | external_id=100125: `Torch-Compiled Region: 4/3` {} |
| 6.46 | 7488 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1]", "[1]", "0"], "Input Dims": [[512], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scala... |
| 4.90 | 4992 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", ... |
| 4.47 | 2496 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::_foreach_copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[[1]], [[1]], []], "Input Strides": [[[1]], [[1]], []], "Input type": ["TensorList", "TensorList", "Scalar"]} |
| 4.03 | 3318 | gemm | ok | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID1_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.79 | 2808 | quant_gemm | missing | True | `kernel_cutlass_kernel_flashinferquantizationkernelsnvfp4_quantizeNVFP4QuantizeSwizzledKernel_object_at__tensorptrbf16gmemalign16o614461441_tensorptri8gmemalign16o307230721_tensorptri8gmem_0` | external_id=100125: `Torch-Compiled Region: 4/3` {} |
| 2.69 | 2400 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[3168, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 2.56 | 1800 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 2.29 | 2298 | gemm | ok | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK21111000_PermutationMNK____MMAAtom_ThrID2_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[3168, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 2.29 | 2496 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512HVPerCta128PagedKvDenseStaticTokenSparseP1MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::sum` {"Concrete Inputs": ["", "[]", "False", ""], "Input Dims": [[1], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "Scalar", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
