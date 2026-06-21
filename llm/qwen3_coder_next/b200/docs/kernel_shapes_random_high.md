# Kernel Shape Inventory — random_high

- Model: `Qwen/Qwen3-Coder-Next`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1432.7 ms`
- Trace files: `2`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 10.58 | 1140 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 2, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=47806: `aten::matmul` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 2048], [2048, 6144]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 8.25 | 288 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[196096, 2048]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sc... |
| 6.21 | 768 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=60151: `aten::as_strided` {"Concrete Inputs": ["", "[16384, 4096]", "[4096, 1]", "0"], "Input Dims": [[16384, 4096], [], [], []], "Input Strides": [[4096, 1], [], [], []], "Input type": ["c10::BFloat16",... |
| 5.58 | 288 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], [2048, 32]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.29 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=47288: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 2048], [2048, 1]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.52 | 72 | quant_gemm | ok | True | `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT` | external_id=47823: `aten::gt` {"Concrete Inputs": ["", "0"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["int", "Scalar"]} |
| 3.46 | 96 | other | ok | True | `_fwd_kernel` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], [2048, 2048]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.06 | 288 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[16384, 2048]"], "Input Dims": [[16384, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
