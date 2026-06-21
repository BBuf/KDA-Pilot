# Kernel Shape Inventory — sharegpt_high

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1460.2 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 12.32 | 3388 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=151589: `Torch-Compiled Region: 4/2` {} |
| 7.20 | 968 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 4>, std::array<int, 4>)` | external_id=132757: `detach_` {"Concrete Inputs": [""], "Input Dims": [[34]], "Input Strides": [[1]], "Input type": ["int"]} |
| 6.49 | 1952 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ32Kv128PersistentSwapsAbForGen` | external_id=144471: `aten::slice` {"Concrete Inputs": ["", "0", "0", "1748", "1"], "Input Dims": [[1792], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "... |
| 5.32 | 232 | gemm | missing | True | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` | external_id=126672: `Torch-Compiled Region: 4/3` {} |
| 5.19 | 580 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x16x512_s5_et128x16_m128x16x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 4.41 | 348 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | external_id=141281: `Torch-Compiled Region: 4/1` {} |
| 4.27 | 464 | quant_gemm | missing | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x32x512u2_s4_et128x32_m128x32x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | external_id=151589: `Torch-Compiled Region: 4/2` {} |
| 3.01 | 406 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[97], [], []], "Input Strides": [[1], [], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.74 | 580 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x16x512_s5_et128x16_m256x16x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[3], [3], []], "Input Strides": [[1], [1], []], "Input type": ["long unsigned int", "long unsigned int", "Scalar"]} |
| 2.61 | 3587 | gemm | ok | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK21111000_PermutationMNK____MMAAtom_ThrID2_0` | external_id=141281: `Torch-Compiled Region: 4/1` {} |
| 2.54 | 522 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x32x512_s4_et128x32_m256x32x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | external_id=151589: `Torch-Compiled Region: 4/2` {} |
| 2.47 | 4392 | other | missing | True | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` | external_id=141281: `Torch-Compiled Region: 4/1` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
