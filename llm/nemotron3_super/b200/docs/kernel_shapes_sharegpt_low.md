# Kernel Shape Inventory — sharegpt_low

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `384.3 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 35.59 | 3204 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "0"], "Input Dims": [[20, 4096], [20, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", "Sca... |
| 8.42 | 352 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | nearest_preceding_shape_cpu_op: `aten::fill_` {"Concrete Inputs": ["", "0"], "Input Dims": [[2, 4096], []], "Input Strides": [[4096, 1], []], "Input type": ["c10::BFloat16", "Scalar"]} |
| 7.75 | 4096 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.97 | 2816 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 131072], [], []], "Input Strides": [[131072, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 3.45 | 2816 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 131072], [], []], "Input Strides": [[131072, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 3.02 | 1280 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 1]", "[1, 0]", ""], "Input Dims": [[1], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", ""]} |
| 2.85 | 1280 | moe | ok | True | `void moe::dev::routing::routingCustom::routingIndicesBlockKernel<moe::dev::routing::routingCustom::KernelParams<float, __nv_bfloat16, 512, 22, moe::dev::routing::TopKExpertSelect<moe::dev::routing::SigmoidBiasPreprocess, moe::dev::routing::ScaledSumNormalizePostprocess> > >(moe::dev::routing::routingCustom::KernelParams<float, __nv_bfloat16, 512, 22, moe::dev::routing::TopKExpertSelect<moe::dev::routing::SigmoidBiasPreprocess, moe::dev::routing::ScaledSumNormalizePostprocess> >)` | timestamp_enclosure: `aten::view` {"Concrete Inputs": ["", "[]"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["long int", "ScalarList"]} |
| 2.38 | 1280 | quant_gemm | ok | True | `nvjet_sm100_tss_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 131072]", "[131072, 1]", "0"], "Input Dims": [[1, 131072], [], [], []], "Input Strides": [[131072, 1], [], [], []], "Input type": ["float", "Scalar... |
| 2.37 | 1440 | moe | ok | True | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | timestamp_enclosure: `aten::empty_strided` {"Concrete Inputs": ["[1]", "[1]", "4", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scala... |
| 2.18 | 680 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "2"], "Input Dims": [[20, 4096], [20, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", "Sca... |

The CSV/JSON siblings contain full sample metadata and trace paths.
