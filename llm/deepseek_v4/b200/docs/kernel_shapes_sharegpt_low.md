# Kernel Shape Inventory — sharegpt_low

- Model: `deepseek-ai/DeepSeek-V4-Flash`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1296.5 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 36.16 | 3432 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[1]"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["long int", "ScalarList"]} |
| 33.01 | 3296 | other | ok | True | `mhc_post_tilelang_kernel` | timestamp_enclosure: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[15, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 4.87 | 9196 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["int"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
