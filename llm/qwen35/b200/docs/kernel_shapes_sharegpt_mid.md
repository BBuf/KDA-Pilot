# Kernel Shape Inventory — sharegpt_mid

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2062.4 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 30.38 | 3808 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=109465: `aten::empty_like` {"Concrete Inputs": ["", "", "", "", "False", ""], "Input Dims": [[17, 4096], [], [], [], [], []], "Input Strides": [[4096, 1], [], [], [], [], []], "Input type": ["c10::BFloat1... |
| 7.21 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=109483: `aten::as_strided` {"Concrete Inputs": ["", "[4096, 32]", "[1, 4096]", ""], "Input Dims": [[32, 4096], [], [], []], "Input Strides": [[4096, 1], [], [], []], "Input type": ["c10::BFloat16", "Scala... |
| 5.40 | 180 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` | external_id=104579: `detach_` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["int"]} |
| 4.92 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_1x2_h_bz_TNT` | external_id=135304: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[267, 4096], [4096, 512]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.99 | 240 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=122502: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[10501, 4096], [4096, 5120]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.85 | 240 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x128x256_s6_et128x128_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `c10d::allreduce_` {"Concrete Inputs": ["", "", "", "", "False", "-1"], "Input Dims": [[[10501, 4096]], [], [], [], [], []], "Input Strides": [[[4096, 1]], [], [], [], [], []], "Input type": ["Ten... |
| 2.32 | 480 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[10501, 4096]"], "Input Dims": [[10501, 4096], []], "Input Strides": [[4096, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.19 | 240 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | timestamp_enclosure: `nccl:_all_gather_base` {"Concrete Inputs": [""], "Input Dims": [[31, 62080]], "Input Strides": [[62080, 1]], "Input type": ["c10::BFloat16"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
