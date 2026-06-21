# Kernel Shape Inventory — random_high

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `8482.7 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 29.99 | 4560 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=41068: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[38, 2048], [38, 2048], [2048], [], [], [], [], [], []], "Input ... |
| 25.37 | 384 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=41086: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 2048], [2048, 128]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.04 | 1152 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | external_id=41311: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 2048], [2048, 1536]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.99 | 1152 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `nccl:all_reduce` {"Concrete Inputs": [""], "Input Dims": [[16384, 2048]], "Input Strides": [[2048, 1]], "Input type": ["c10::BFloat16"]} |
| 2.90 | 1152 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[196096, 2048]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sc... |
| 2.07 | 1152 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[15303, 4]", "[4, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarLi... |

The CSV/JSON siblings contain full sample metadata and trace paths.
