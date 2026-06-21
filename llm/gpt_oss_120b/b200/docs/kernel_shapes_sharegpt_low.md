# Kernel Shape Inventory — sharegpt_low

- Model: `openai/gpt-oss-120b`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `292.5 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 27.11 | 5184 | quant_gemm | missing | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` | external_id=22290: `Torch-Compiled Region: 1/3` {} |
| 24.00 | 5112 | comm | missing | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=22290: `Torch-Compiled Region: 1/3` {} |
| 3.08 | 2592 | quant_gemm | missing | True | `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantizationType)2, __nv_bfloat16, 32, true, false, false, false, std::integral_constant<bool, false> >(int, int, int, int, __nv_bfloat16 const*, float const*, void*, unsigned int*, flashinfer::QuantizationSFLayout)` | external_id=22290: `Torch-Compiled Region: 1/3` {} |
| 2.99 | 2592 | moe | missing | True | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true> >(moe::dev::finalize::KernelParams<cutlass::bfloat16_t, cutlass::bfloat16_t, 4, true>)` | external_id=22290: `Torch-Compiled Region: 1/3` {} |
| 2.96 | 1152 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x16x256u2_s6_et128x16_m256x16x32_c2x1x1_rM_TN_transOut_schedS_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.93 | 1152 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[0], [15]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 2.68 | 2016 | quant_gemm | ok | True | `nvjet_sm100_tst_24x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.61 | 2304 | moe | ok | True | `void moe::dev::routing::routingCustom::routingIndicesBlockKernel<moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 128, 4, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> > >(moe::dev::routing::routingCustom::KernelParams<__nv_bfloat16, __nv_bfloat16, 128, 4, moe::dev::routing::TopKExpertSelect<moe::dev::routing::NoOpPreprocess, moe::dev::routing::SoftmaxPostprocess> >)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[]"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["long int", "ScalarList"]} |
| 2.42 | 1152 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 201088], [], []], "Input Strides": [[201088, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 2.41 | 2592 | rope | missing | True | `void (anonymous namespace)::fused_rope_kernel<true, 64l, true, __nv_bfloat16, long, 8u>((anonymous namespace)::FusedRopeParams)` | external_id=22290: `Torch-Compiled Region: 1/3` {} |
| 2.26 | 864 | quant_gemm | ok | True | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x16x256_s5_et128x16_m256x16x32_c2x1x1_rM_TN_transOut_schedS_biasFp32M_bN_tma_ldgstsSf_rgTma_clmp_swiGlu_dynB_sm100f` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 201088], [], []], "Input Strides": [[201088, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
