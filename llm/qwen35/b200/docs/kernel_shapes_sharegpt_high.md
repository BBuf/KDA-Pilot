# Kernel Shape Inventory — sharegpt_high

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5837.5 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 9.38 | 2856 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=149138: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[17, 4096], [17, 4096], [4096], [], [], [], [], [], []], "Input ... |
| 5.72 | 476 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 4>, std::array<int, 4>)` | external_id=193973: `aten::reshape` {"Concrete Inputs": ["", "[1110, 2048]"], "Input Dims": [[1110, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["unsigned char", "ScalarList"]} |
| 3.16 | 1200 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=166951: `aten::empty_like` {"Concrete Inputs": ["", "15", "", "", "False", ""], "Input Dims": [[20968, 8, 256], [], [], [], [], []], "Input Strides": [[2048, 256, 1], [], [], [], [], []], "Input type": ["... |
| 2.96 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16tokFp32_t128x128x256_s6_et128x128_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[20968, 2048], [2048, 4096]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.83 | 1920 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1, 20968, 16, 128]", "15", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Scalar... |
| 2.74 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=146796: `aten::to` {"Concrete Inputs": ["", "6", "False", "False", ""], "Input Dims": [[], [], [], [], []], "Input Strides": [[], [], [], [], []], "Input type": ["float", "Scalar", "Scalar", "Scal... |
| 2.25 | 480 | quant_gemm | ok | True | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512u2_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_fCp_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_lbW4_lsfbW4_dynB_sm100f` | timestamp_enclosure: `ChunkGatedDeltaRuleFunction` {"Concrete Inputs": ["", "", "", "", "", "0.088388347648318447", "", "", "", "True"], "Input Dims": [[1, 20968, 4, 128], [1, 20968, 4, 128], [1, 20968, 16, 128], [1, 20968, 16],... |
| 2.10 | 180 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` | external_id=149893: `aten::empty` {"Concrete Inputs": ["[1, 17, 4, 128]", "15", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList... |
| 2.03 | 240 | quant_gemm | ok | True | `nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_TNT` | external_id=159589: `aten::view` {"Concrete Inputs": ["", "[-1, 128]"], "Input Dims": [[1, 20968, 16, 128], []], "Input Strides": [[42942464, 2048, 128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
