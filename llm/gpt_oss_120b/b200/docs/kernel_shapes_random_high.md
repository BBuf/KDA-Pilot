# Kernel Shape Inventory — random_high

- Model: `openai/gpt-oss-120b`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `526.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 27.69 | 5112 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=16730: `Torch-Compiled Region: 1/3` {} |
| 10.49 | 576 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x2_2cta_h_bz_splitK_bias_TNN` | external_id=16730: `Torch-Compiled Region: 1/3` {} |
| 8.01 | 288 | quant_gemm | missing | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_bias_TNT` | external_id=14146: `Torch-Compiled Region: 1/3` {} |
| 4.68 | 1404 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x8x512u2_s3_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[18]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 4.19 | 1728 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_bias_TNT` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[128], [2]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.94 | 1512 | quant_gemm | ok | True | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x8x256u2_s4_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.74 | 1728 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_bias_TNT` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[128]], []], "Input Strides": [[[1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.18 | 576 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x16x256u2_s6_et128x16_m256x16x32_c2x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | external_id=18364: `Torch-Compiled Region: 1/3` {} |
| 2.85 | 2592 | moe | ok | True | `void moe::dev::routing::routingCustom::routingIndicesClusterKernel<moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 128, 4, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> > >(moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 128, 4, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> >)` | timestamp_enclosure: `aten::_to_copy` {"Concrete Inputs": ["", "4", "", "", "", "False", ""], "Input Dims": [[128], [], [], [], [], [], []], "Input Strides": [[1], [], [], [], [], [], []], "Input type": ["int", "Sca... |
| 2.21 | 612 | quant_gemm | ok | True | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x16x256_s4_et128x16_m128x16x32_c1x1x1_rM_TN_transOut_schPd2x1x2x3_biasFp32M_bN_rgTma_clmp_dynB_sm100f` | external_id=18364: `Torch-Compiled Region: 1/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
