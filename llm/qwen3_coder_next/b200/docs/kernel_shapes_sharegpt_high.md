# Kernel Shape Inventory — sharegpt_high

- Model: `Qwen/Qwen3-Coder-Next`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1354.4 ms`
- Trace files: `2`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 21.49 | 1330 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 2, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=125335: `aten::reshape` {"Concrete Inputs": ["", "[272, 128]"], "Input Dims": [[272, 128], []], "Input Strides": [[128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 7.40 | 144 | other | ok | True | `_fwd_kernel` | timestamp_enclosure: `sglang::inplace_all_reduce` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", ""]} |
| 5.90 | 192 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[16384, 2048]"], "Input Dims": [[16384, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 4.51 | 576 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=143658: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], [2048, 6144]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.37 | 388 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=131294: `aten::to` {"Concrete Inputs": ["", "4", "False", "False", ""], "Input Dims": [[16384], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scala... |
| 4.01 | 192 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::empty` {"Concrete Inputs": ["[0]", "1", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "", "... |
| 3.82 | 288 | quant_gemm | ok | True | `nvjet_sm100_tst_64x64_64x16_2x1_2cta_v_bz_TNT` | external_id=176457: `aten::matmul` {"Concrete Inputs": ["", ""], "Input Dims": [[118, 2048], [2048, 512]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.29 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=125353: `aten::empty_strided` {"Concrete Inputs": ["[17, 2048]", "[2048, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Scala... |
| 2.82 | 768 | quant_gemm | ok | True | `nvjet_sm100_tst_8x64_64x16_4x1_v_bz_TNN` | external_id=176542: `aten::empty_like` {"Concrete Inputs": ["", "", "", "", "False", ""], "Input Dims": [[118, 2048], [], [], [], [], []], "Input Strides": [[2048, 1], [], [], [], [], []], "Input type": ["c10::BFloat... |
| 2.31 | 288 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | timestamp_enclosure: `ChunkGatedDeltaRuleFunction` {"Concrete Inputs": ["", "", "", "", "", "0.088388347648318447", "", "", "", "True"], "Input Dims": [[1, 16384, 8, 128], [1, 16384, 8, 128], [1, 16384, 16, 128], [1, 16384, 16],... |
| 2.15 | 72 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` | external_id=127790: `aten::empty_like` {"Concrete Inputs": ["", "", "", "", "False", ""], "Input Dims": [[17, 2048], [], [], [], [], []], "Input Strides": [[2048, 1], [], [], [], [], []], "Input type": ["c10::BFloat1... |

The CSV/JSON siblings contain full sample metadata and trace paths.
