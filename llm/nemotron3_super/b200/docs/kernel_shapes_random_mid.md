# Kernel Shape Inventory — random_mid

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1712.1 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 8.01 | 356 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 7.62 | 2492 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=13380: `aten::as_strided` {"Concrete Inputs": ["", "[38, 32]", "[4640, 1]", "4608"], "Input Dims": [[38, 32], [], [], []], "Input Strides": [[4640, 1], [], [], []], "Input type": ["c10::BFloat16", "Scala... |
| 6.96 | 480 | other | ok | True | `_chunk_scan_fwd_kernel` | external_id=19001: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "71"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 6.93 | 356 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=22919: `aten::as_strided` {"Concrete Inputs": ["", "[2, 1, 1]", "[1, 1, 1]", ""], "Input Dims": [[2, 1], [], [], []], "Input Strides": [[1, 1], [], [], []], "Input type": ["bool", "ScalarList", "ScalarLi... |
| 6.78 | 480 | other | ok | True | `_chunk_state_fwd_kernel` | external_id=19106: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "73"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 6.21 | 160 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_relu2_bN_tma_tmaSf_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[30], [30], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 5.78 | 160 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=16016: `aten::empty` {"Concrete Inputs": ["[1, 128, 2, 128, 128]", "6", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Scala... |
| 4.38 | 480 | other | ok | True | `_state_passing_fwd_kernel` | external_id=19106: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "73"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 4.14 | 1056 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=9987: `aten::empty` {"Concrete Inputs": ["[38, 2048]", "15", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "S... |
| 3.48 | 160 | quant_gemm | ok | True | `nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_TNN` | external_id=18513: `aten::index_put_` {"Concrete Inputs": ["", "", "", "False"], "Input Dims": [[1025, 32, 64, 128], [], [30, 32, 64, 128], []], "Input Strides": [[262144, 8192, 128, 1], [], [262144, 8192, 128, 1], ... |
| 3.29 | 512 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=19203: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], [2048, 4096]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.27 | 720 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128_s5_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::_to_copy` {"Concrete Inputs": ["", "4", "0", "", "", "False", ""], "Input Dims": [[32], [], [], [], [], [], []], "Input Strides": [[1], [], [], [], [], [], []], "Input type": ["long int",... |
| 2.34 | 480 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128_s4_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_relu2_bN_ldgsts_ldgstsSf_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[32, 131072], [], []], "Input Strides": [[131072, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
