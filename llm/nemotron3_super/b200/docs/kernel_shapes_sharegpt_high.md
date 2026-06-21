# Kernel Shape Inventory — sharegpt_high

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3174.4 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 9.41 | 712 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[14375, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 7.13 | 480 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_relu2_bN_tma_tmaSf_rgTma_clmp_dynB_sm100f` | external_id=126940: `aten::item` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |
| 6.72 | 480 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "18"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 6.13 | 1068 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=136841: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[1884, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 5.74 | 1376 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=114968: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[14375, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.12 | 2112 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[18, 1024], [18, 1024], []], "Input Strides": [[1024, 1], [1024, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", ... |
| 2.10 | 320 | quant_gemm | ok | True | `nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_TNN` | external_id=127490: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 4096], [4096, 4640]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.08 | 800 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "20"], "Input Dims": [[16384, 4096], [16384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16... |
| 2.05 | 1424 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=109810: `aten::view` {"Concrete Inputs": ["", "[1, 18, -1, 64]"], "Input Dims": [[18, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
