# Kernel Shape Inventory — sharegpt_low

- Model: `Qwen/Qwen3-Coder-Next`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `141.1 ms`
- Trace files: `2`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 20.73 | 1710 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 2, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=90127: `aten::empty` {"Concrete Inputs": ["[1360, 256]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scala... |
| 6.87 | 1536 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 6.13 | 1536 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 151936]", "[151936, 1]", "0"], "Input Dims": [[1, 151936], [], [], []], "Input Strides": [[151936, 1], [], [], []], "Input type": ["float", "Scalar... |
| 5.89 | 768 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 5.08 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=90081: `aten::view` {"Concrete Inputs": ["", "[-1, 2048]"], "Input Dims": [[17, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 3.41 | 432 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s4_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1360, 2048]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scal... |
| 3.25 | 864 | moe | ok | True | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 2, true>)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1360, 2048]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scal... |
| 3.05 | 72 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` | external_id=90144: `aten::view` {"Concrete Inputs": ["", "[-1]"], "Input Dims": [[17, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.62 | 768 | moe | ok | True | `void moe::dev::routing::routingCustom::routingIndicesBlockKernel<moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 512, 16, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> > >(moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 512, 16, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> >)` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.33 | 384 | other | ok | True | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schedS_biasBfloat16Mn_bN_ldgsts_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 151936]", "[151936, 1]", "0"], "Input Dims": [[1, 151936], [], [], []], "Input Strides": [[151936, 1], [], [], []], "Input type": ["float", "Scalar... |

The CSV/JSON siblings contain full sample metadata and trace paths.
