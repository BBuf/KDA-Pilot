# Kernel Shape Inventory — random_low

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `575.1 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 17.66 | 4356 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=296: `Torch-Compiled Region: 4/2` {} |
| 11.60 | 476 | quant_gemm | missing | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` | external_id=296: `Torch-Compiled Region: 4/2` {} |
| 8.04 | 5422 | gemm | missing | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID1_0` | external_id=296: `Torch-Compiled Region: 4/2` {} |
| 4.32 | 3904 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[2560, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 3.77 | 1952 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[4097], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "", "long int", "S... |
| 3.19 | 2196 | quant_gemm | ok | True | `kernel_cutlass_kernel_flashinferquantizationkernelsnvfp4_quantizeNVFP4QuantizeSwizzledKernel_object_at__tensorptrbf16gmemalign16o716871681_tensorptri8gmemalign16o358435841_tensorptri8gmem_0` | external_id=296: `Torch-Compiled Region: 4/2` {} |
| 3.15 | 1952 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.67 | 1952 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512HVPerCta128PagedKvDenseStaticTokenSparseP1MultiCtasKvVarSeqQ16Kv128StaticSwapsAbForGen` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.62 | 1450 | quant_gemm | missing | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | external_id=296: `Torch-Compiled Region: 4/2` {} |
| 2.42 | 1392 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schedS_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[2560, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
