# Kernel Shape Inventory — sharegpt_low

- Model: `zai-org/GLM-5.1-FP8`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `4467.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 36.29 | 11360 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=156594: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "True"], "Input Dims": [[16, 6144], [16, 6144], [6144], [], [], [], [], [], []], "Input ... |
| 18.18 | 5600 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | external_id=156611: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16, 6144], [6144, 256]], "Input Strides": [[6144, 1], [1, 6144]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.61 | 23960 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[4, 6144], [], []], "Input Strides": [[6144, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 2.26 | 544 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[4], [4], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
