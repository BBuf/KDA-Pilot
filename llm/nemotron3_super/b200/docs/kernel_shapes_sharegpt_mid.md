# Kernel Shape Inventory — sharegpt_mid

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1385.9 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 9.25 | 480 | other | ok | True | `_chunk_scan_fwd_kernel` | external_id=95096: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "75"], "Input Dims": [[10240, 4096], [10240, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 7.80 | 2492 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=86102: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[18, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 6.24 | 356 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=89733: `aten::remainder` {"Concrete Inputs": ["", "128"], "Input Dims": [[], []], "Input Strides": [[], []], "Input type": ["int", "Scalar"]} |
| 6.12 | 356 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=101431: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[262, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 5.51 | 704 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=90273: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[10111, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.10 | 480 | other | ok | True | `_chunk_state_fwd_kernel` | external_id=94521: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "66"], "Input Dims": [[10240, 4096], [10240, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 4.97 | 160 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_relu2_bN_tma_tmaSf_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[31], [31], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.73 | 160 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "11"], "Input Dims": [[10240, 4096], [10240, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 4.51 | 840 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128_s5_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.10 | 480 | other | ok | True | `_state_passing_fwd_kernel` | external_id=94705: `aten::unsqueeze` {"Concrete Inputs": ["", "3"], "Input Dims": [[31, 1, 1], []], "Input Strides": [[1, 1, 1], []], "Input type": ["bool", "Scalar"]} |
| 3.62 | 1056 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "80"], "Input Dims": [[20, 4096], [20, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", "Sc... |
| 3.22 | 560 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128_s4_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_relu2_bN_ldgsts_ldgstsSf_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[32, 131072], [], []], "Input Strides": [[131072, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
