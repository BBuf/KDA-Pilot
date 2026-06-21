# Kernel Shape Inventory — random_mid

- Model: `Qwen/Qwen3-Coder-Next`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `589.6 ms`
- Trace files: `2`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 13.70 | 1520 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 2, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=17588: `aten::empty` {"Concrete Inputs": ["[3040, 256]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scala... |
| 6.79 | 96 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[16384, 10]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scala... |
| 5.20 | 288 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=21219: `aten::arange` {"Concrete Inputs": ["0", "14", "1", ""], "Input Dims": [[], [], [], [0]], "Input Strides": [[], [], [], [1]], "Input type": ["Scalar", "Scalar", "Scalar", "long int"]} |
| 4.59 | 96 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `sglang::inplace_all_reduce` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", ""]} |
| 4.14 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=17542: `aten::view` {"Concrete Inputs": ["", "[-1, 2048]"], "Input Dims": [[38, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 3.49 | 336 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[32, 151936]", "[151936, 1]", "0"], "Input Dims": [[32, 151936], [], [], []], "Input Strides": [[151936, 1], [], [], []], "Input type": ["float", "Scal... |
| 3.21 | 288 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 3.03 | 72 | quant_gemm | ok | True | `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT` | external_id=17753: `aten::alias` {"Concrete Inputs": [""], "Input Dims": [[38, 2048]], "Input Strides": [[2048, 1]], "Input type": ["c10::BFloat16"]} |
| 2.68 | 192 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | timestamp_enclosure: `aten::empty_like` {"Concrete Inputs": ["", "", "", "", "False", ""], "Input Dims": [[4096, 16384], [], [], [], [], []], "Input Strides": [[1, 4096], [], [], [], [], []], "Input type": ["c10::BFlo... |
| 2.15 | 96 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s6_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[10448, 2048]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sca... |

The CSV/JSON siblings contain full sample metadata and trace paths.
