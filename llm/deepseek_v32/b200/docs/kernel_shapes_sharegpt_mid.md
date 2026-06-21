# Kernel Shape Inventory — sharegpt_mid

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2000.2 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 15.00 | 492 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=95057: `aten::clone` {"Concrete Inputs": ["", ""], "Input Dims": [[552320], []], "Input Strides": [[1], []], "Input type": ["float", ""]} |
| 8.84 | 488 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ32Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[8630, 32, 576]"], "Input Dims": [[8630, 1, 32, 576], []], "Input Strides": [[18432, 18432, 576, 1], []], "Input type": ["c10::Float8_e4m3fn", "ScalarL... |
| 7.45 | 3872 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=83568: `Torch-Compiled Region: 4/3` {} |
| 4.17 | 232 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | timestamp_enclosure: `aten::numpy_T` {"Concrete Inputs": [""], "Input Dims": [[448, 1024]], "Input Strides": [[1, 448]], "Input type": ["c10::Float8_e4m3fn"]} |
| 4.04 | 4392 | other | ok | True | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` | external_id=109568: `sglang::hadamard_transform` {"Concrete Inputs": ["", "0.088388347648318447"], "Input Dims": [[8630, 64, 128], []], "Input Strides": [[8192, 128, 1], []], "Input type": ["c10::BFloat16", "Scalar"]} |
| 3.58 | 232 | gemm | missing | True | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` | external_id=83568: `Torch-Compiled Region: 4/3` {} |
| 3.57 | 4211 | gemm | ok | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID1_0` | external_id=95081: `PythonDispatchMode` {"Concrete Inputs": [""], "Input Dims": [[33161216]], "Input Strides": [[1]], "Input type": ["int"]} |
| 3.44 | 232 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x128x256u2_s6_et128x128_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[-1, 1]"], "Input Dims": [[8630, 64, 1], []], "Input Strides": [[64, 1, 1], []], "Input type": ["float", "ScalarList"]} |
| 3.21 | 812 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x8x512u2_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[5092]], "Input Strides": [[1]], "Input type": ["unsigned char"]} |
| 2.56 | 1160 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[32], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 2.17 | 244 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x4_1x2_h_bz_TNT` | external_id=106472: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[8630, 7168], [7168, 2112]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.11 | 464 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | timestamp_enclosure: `sglang::flashinfer_fp4_quantize` {"Concrete Inputs": ["", "", "16", "False", "True", "False", ""], "Input Dims": [[8630, 4096], [], [], [], [], [], []], "Input Strides": [[4096, 1], [], [], [], [], [], []], "In... |

The CSV/JSON siblings contain full sample metadata and trace paths.
