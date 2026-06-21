# Kernel Shape Inventory — random_high

- Model: `deepseek-ai/DeepSeek-V4-Flash`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `10071.7 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 17.09 | 1800 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=159357: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[1995, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 9.51 | 17440 | quant_gemm | ok | True | `void deep_gemm::sm100_tf32_hc_prenorm_gemm_impl<24u, 16384u, 64u, 32u, 64u, 4u, 128u, 12u, 128u, 128u>(unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, float*)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[16384, 16384]", "[16384, 1]", "0"], "Input Dims": [[16384, 16384], [], [], []], "Input Strides": [[16384, 1], [], [], []], "Input type": ["c10::BFloat... |
| 4.51 | 384 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[400]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar"... |

The CSV/JSON siblings contain full sample metadata and trace paths.
