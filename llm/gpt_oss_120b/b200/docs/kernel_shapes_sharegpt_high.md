# Kernel Shape Inventory — sharegpt_high

- Model: `openai/gpt-oss-120b`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `670.2 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 21.40 | 4544 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=41373: `aten::as_strided` {"Concrete Inputs": ["", "[192, 1, 64]", "[640, 64, 1]", "0"], "Input Dims": [[192, 1, 64], [], [], []], "Input Strides": [[640, 64, 1], [], [], []], "Input type": ["c10::BFloat... |
| 8.07 | 616 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=43327: `Torch-Compiled Region: 1/2` {} |
| 5.65 | 576 | quant_gemm | missing | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` | external_id=37154: `Torch-Compiled Region: 1/3` {} |
| 4.32 | 1440 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_bias_TNT` | timestamp_enclosure: `aten::_unique2` {"Concrete Inputs": ["", "True", "False", "False"], "Input Dims": [[60], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "Scalar", "Scalar", "Scalar"]} |
| 3.88 | 1440 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x2_h_bz_bias_TNT` | timestamp_enclosure: `aten::gt` {"Concrete Inputs": ["", "0"], "Input Dims": [[93], []], "Input Strides": [[1], []], "Input type": ["long int", "Scalar"]} |
| 3.80 | 288 | quant_gemm | ok | True | `nvjet_sm100_tst_64x32_64x16_2x4_2cta_h_bz_splitK_bias_TNT` | external_id=41373: `aten::as_strided` {"Concrete Inputs": ["", "[192, 1, 64]", "[640, 64, 1]", "0"], "Input Dims": [[192, 1, 64], [], [], []], "Input Strides": [[640, 64, 1], [], [], []], "Input type": ["c10::BFloat... |
| 3.75 | 1368 | quant_gemm | ok | True | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x8x256_s4_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[384], [384], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 3.05 | 288 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x2_2cta_h_bz_splitK_bias_TNN` | external_id=39245: `Torch-Compiled Region: 1/3` {} |
| 2.77 | 792 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x8x512_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[5]", "[1]", "152310568"], "Input Dims": [[261], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "Sc... |
| 2.55 | 576 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=43902: `aten::view` {"Concrete Inputs": ["", "[-1, 64]"], "Input Dims": [[2373, 1, 64], []], "Input Strides": [[640, 64, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.31 | 576 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[5]", "[1]", "152310568"], "Input Dims": [[261], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "Sc... |
| 2.18 | 2304 | moe | ok | True | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | external_id=43867: `aten::as_strided` {"Concrete Inputs": ["", "[2373, 512]", "[512, 1]", "0"], "Input Dims": [[2560, 512], [], [], []], "Input Strides": [[512, 1], [], [], []], "Input type": ["c10::BFloat16", "Scal... |

The CSV/JSON siblings contain full sample metadata and trace paths.
