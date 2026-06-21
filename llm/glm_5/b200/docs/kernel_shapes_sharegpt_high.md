# Kernel Shape Inventory — sharegpt_high

- Model: `nvidia/GLM-5-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5074.2 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 13.10 | 2496 | attention | ok | True | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[20784, 16, 576]"], "Input Dims": [[20784, 1, 16, 576], []], "Input Strides": [[9216, 9216, 576, 1], []], "Input type": ["c10::Float8_e4m3fn", "ScalarL... |
| 10.15 | 1872 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=199415: `aten::transpose` {"Concrete Inputs": ["", "0", "1"], "Input Dims": [[20784, 16, 256], [], []], "Input Strides": [[4096, 256, 1], [], []], "Input type": ["c10::BFloat16", "Scalar", "Scalar"]} |
| 6.45 | 600 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[20784, 6144], [6144, 128]], "Input Strides": [[6144, 1], [1, 6144]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.12 | 600 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x128x256u2_s6_et128x128_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::sum` {"Concrete Inputs": ["", "[]", "False", ""], "Input Dims": [[60], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "Scalar", ""]} |
| 3.73 | 5616 | other | ok | True | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamardKernelTraits<16, 7, __nv_bfloat16> >(HadamardParamsBase)` | external_id=213671: `sglang::hadamard_transform` {"Concrete Inputs": ["", "0.088388347648318447"], "Input Dims": [[20784, 32, 128], []], "Input Strides": [[4096, 128, 1], []], "Input type": ["c10::BFloat16", "Scalar"]} |
| 3.57 | 4340 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=152077: `Torch-Compiled Region: 4/3` {} |
| 3.50 | 2400 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | timestamp_enclosure: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |
| 3.03 | 1272 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign_0` | timestamp_enclosure: `sgl_kernel::fast_topk_transform_fused` {"Concrete Inputs": ["", "", "", "", "", ""], "Input Dims": [[20784, 20784], [20784], [20784, 2048], [60, 2896], [61], [20784]], "Input Strides": [[21040, 1], [1], [2048, 1], [2... |
| 2.62 | 312 | quant_gemm | ok | True | `nvjet_sm100_tst_192x288_64x5_2x1_2cta_v_bz_TNT` | external_id=186891: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[20784, 6144], [6144, 2624]], "Input Strides": [[6144, 1], [1, 6144]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.51 | 612 | quant_gemm | missing | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | external_id=152077: `Torch-Compiled Region: 4/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
