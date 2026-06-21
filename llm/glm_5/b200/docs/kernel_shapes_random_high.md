# Kernel Shape Inventory — random_high

- Model: `nvidia/GLM-5-NVFP4`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5272.1 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 18.55 | 2496 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=86176: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[30796, 4096], [4096, 6144]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 9.95 | 900 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | timestamp_enclosure: `aten::split_with_sizes` {"Concrete Inputs": ["", "[192, 64]", "-1"], "Input Dims": [[30796, 16, 256], [], []], "Input Strides": [[4096, 256, 1], [], []], "Input type": ["c10::BFloat16", "ScalarList", "... |
| 7.75 | 900 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x128x256u2_s6_et128x128_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::empty` {"Concrete Inputs": ["[256]", "3", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "",... |
| 4.88 | 2700 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | nearest_preceding_shape_cpu_op: `nccl:all_reduce` {"Concrete Inputs": [""], "Input Dims": [[30796, 6144]], "Input Strides": [[6144, 1]], "Input type": ["c10::BFloat16"]} |
| 4.13 | 1268 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1]", "3", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "", "... |
| 2.62 | 624 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256SeparateQkvCausalVarSeqQ128Kv128PersistentContext` | timestamp_enclosure: `sglang::fp4_gemm` {"Concrete Inputs": ["", "", "", "", "", "15", "1024"], "Input Dims": [[30796, 3072], [3072, 1024], [30848, 384], [384, 1024], [], [], []], "Input Strides": [[3072, 1], [1, 3072... |
| 2.26 | 3063 | gemm | ok | True | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersistentDenseGemmKernel_object_at__TiledMMA_ThrLayoutVMNK11110000_PermutationMNK____MMAAtom_ThrID1_0` | external_id=71714: `sglang::fp4_gemm` {"Concrete Inputs": ["", "", "", "", "", "15", "6144"], "Input Dims": [[30796, 3072], [3072, 6144], [30848, 384], [384, 6144], [], [], []], "Input Strides": [[3072, 1], [1, 3072... |
| 2.02 | 1240 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 4>, std::array<int, 4>)` | external_id=90626: `Torch-Compiled Region: 4/2` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
