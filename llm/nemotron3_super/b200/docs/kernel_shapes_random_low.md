# Kernel Shape Inventory — random_low

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `370.7 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 32.11 | 3204 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=4704: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[38, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 8.85 | 352 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[38, 1024], [38, 1024], []], "Input Strides": [[1024, 1], [1024, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", ... |
| 8.03 | 4096 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 5.16 | 2816 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 131072]", "[131072, 1]", "0"], "Input Dims": [[1, 131072], [], [], []], "Input Strides": [[131072, 1], [], [], []], "Input type": ["float", "Scalar... |
| 3.57 | 2816 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 1]", "[1, 0]", ""], "Input Dims": [[1], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", ""]} |
| 3.14 | 1280 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::to` {"Concrete Inputs": ["", "4", "False", "False", ""], "Input Dims": [[1], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", ... |
| 2.99 | 720 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s4_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=389: `aten::expand` {"Concrete Inputs": ["", "[38]", "False"], "Input Dims": [[38], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "ScalarList", "Scalar"]} |
| 2.95 | 1280 | moe | ok | True | `void moe::dev::routing::routingCustom::routingIndicesBlockKernel<moe::dev::routing::routingCustom::KernelParams<float, __nv_bfloat16, 512, 22, moe::dev::routing::TopKExpertSelect<moe::dev::routing::SigmoidBiasPreprocess, moe::dev::routing::ScaledSumNormalizePostprocess> > >(moe::dev::routing::routingCustom::KernelParams<float, __nv_bfloat16, 512, 22, moe::dev::routing::TopKExpertSelect<moe::dev::routing::SigmoidBiasPreprocess, moe::dev::routing::ScaledSumNormalizePostprocess> >)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 131072]", "[131072, 1]", "0"], "Input Dims": [[1, 131072], [], [], []], "Input Strides": [[131072, 1], [], [], []], "Input type": ["float", "Scalar... |
| 2.47 | 1440 | moe | ok | True | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | timestamp_enclosure: `sglang::nemotron_mamba2_with_output` {"Concrete Inputs": ["", "", "13"], "Input Dims": [[48, 4096], [48, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", "Sc... |
| 2.46 | 1280 | quant_gemm | ok | True | `nvjet_sm100_tss_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 131072]", "[131072, 1]", "0"], "Input Dims": [[1, 131072], [], [], []], "Input Strides": [[131072, 1], [], [], []], "Input type": ["float", "Scalar... |

The CSV/JSON siblings contain full sample metadata and trace paths.
