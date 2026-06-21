# Kernel Shape Inventory — random_high

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3841.7 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 12.59 | 800 | other | ok | True | `_chunk_scan_fwd_kernel` | external_id=51821: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "82"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 10.41 | 1068 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=46226: `aten::item` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |
| 8.40 | 800 | other | ok | True | `_chunk_state_fwd_kernel` | external_id=51950: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "84"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 8.07 | 480 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_relu2_bN_tma_tmaSf_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[34], [34], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 7.54 | 480 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "0", "16384", "1"], "Input Dims": [[16384, 4096], [], [], [], []], "Input Strides": [[4096, 1], [], [], [], []], "Input type": ["c10::BFloat16", "S... |
| 6.26 | 800 | other | ok | True | `_state_passing_fwd_kernel` | external_id=60085: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "38"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 6.24 | 1888 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=37199: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[14599, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.57 | 1760 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.54 | 1780 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |
| 3.10 | 320 | quant_gemm | ok | True | `nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_TNN` | external_id=46778: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.60 | 356 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=68932: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[694, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 2.38 | 800 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s6_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::unsqueeze` {"Concrete Inputs": ["", "-3"], "Input Dims": [[11821680, 1, 128], []], "Input Strides": [[128, 128, 1], []], "Input type": ["c10::BFloat16", "Scalar"]} |
| 2.24 | 640 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "15"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |

The CSV/JSON siblings contain full sample metadata and trace paths.
