# Kernel Shape Inventory — sharegpt_mid

- Model: `Qwen/Qwen3-Coder-Next`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `708.5 ms`
- Trace files: `2`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 26.14 | 1520 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 2, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=117817: `aten::t` {"Concrete Inputs": [""], "Input Dims": [[512, 2048]], "Input Strides": [[2048, 1]], "Input type": ["c10::BFloat16"]} |
| 6.98 | 360 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_1x2_h_bz_TNT` | external_id=117461: `aten::reshape` {"Concrete Inputs": ["", "[262, -1]"], "Input Dims": [[262, 16, 128], []], "Input Strides": [[2048, 128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 6.94 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=95589: `aten::view` {"Concrete Inputs": ["", "[-1]"], "Input Dims": [[17, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 4.83 | 72 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` | external_id=98660: `aten::view` {"Concrete Inputs": ["", "[-1]"], "Input Dims": [[17, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 3.80 | 96 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[129600, 2048]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sc... |
| 2.50 | 96 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `nccl:all_reduce` {"Concrete Inputs": [""], "Input Dims": [[9739, 2048]], "Input Strides": [[2048, 1]], "Input type": ["c10::BFloat16"]} |
| 2.42 | 336 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[32, 151936]", "[151936, 1]", "0"], "Input Dims": [[32, 151936], [], [], []], "Input Strides": [[151936, 1], [], [], []], "Input type": ["float", "Scal... |
| 2.42 | 336 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[32, 1]", "[1, 0]", ""], "Input Dims": [[32], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
