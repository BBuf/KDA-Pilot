# Kernel Shape Inventory — sharegpt_mid

- Model: `nvidia/GLM-5-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2350.3 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 14.65 | 628 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=124329: `record_param_comms` {"Concrete Inputs": ["", "", "", "3", "", "[]", "[]", "0", "1", "4"], "Input Dims": [[[9962, 6144]], [], [], [], [], [], [], [], [], []], "Input Strides": [[[6144, 1]], [], [], ... |
| 10.00 | 1560 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=146393: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[9962, 4096], [4096, 6144]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 8.39 | 312 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128PersistentSwapsAbForGen` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[201]], "Input Strides": [[1]], "Input type": ["unsigned char"]} |
| 6.67 | 4960 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=109949: `Torch-Compiled Region: 4/3` {} |
| 5.96 | 4896 | quant_gemm | missing | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | external_id=109949: `Torch-Compiled Region: 4/3` {} |
| 4.56 | 300 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[201]], "Input Strides": [[1]], "Input type": ["unsigned char"]} |
| 3.66 | 300 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x128x256u2_s6_et128x128_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[201]], "Input Strides": [[1]], "Input type": ["unsigned char"]} |
| 3.37 | 1125 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x16x512u2_s5_et128x16_m128x16x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[31], [31], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 3.29 | 1050 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512u2_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[31], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 2.73 | 5616 | other | ok | True | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` | external_id=146889: `sglang::hadamard_transform` {"Concrete Inputs": ["", "0.088388347648318447"], "Input Dims": [[9962, 32, 128], []], "Input Strides": [[4096, 128, 1], []], "Input type": ["c10::BFloat16", "Scalar"]} |
| 2.17 | 300 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.03 | 652 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[-1, 1]"], "Input Dims": [[9962, 32, 1], []], "Input Strides": [[32, 1, 1], []], "Input type": ["float", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
