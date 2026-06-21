# Kernel Shape Inventory — sharegpt_high

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `8346.0 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 25.16 | 4560 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=123649: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[17, 2048], [17, 2048], [2048], [], [], [], [], [], []], "Input ... |
| 12.55 | 2688 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=123666: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 2048], [2048, 1536]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 10.72 | 760 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 8>, std::array<int, 8>)` | external_id=160474: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[785, 2048], [785, 2048], [2048], [], [], [], [], [], []], "Inpu... |
| 6.42 | 384 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=123603: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 2048], [2048, 128]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.29 | 8 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=153911: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[785, 2048], [], []], "Input Strides": [[2048, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
