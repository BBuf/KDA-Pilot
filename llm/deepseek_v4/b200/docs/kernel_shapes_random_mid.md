# Kernel Shape Inventory — random_mid

- Model: `deepseek-ai/DeepSeek-V4-Flash`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `11807.8 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 8.18 | 17088 | quant_gemm | ok | True | `void deep_gemm::sm100_tf32_hc_prenorm_gemm_impl<24u, 16384u, 64u, 32u, 64u, 2u, 128u, 12u, 128u, 128u>(unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, float*)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[16384, 16384]", "[16384, 1]", "0"], "Input Dims": [[16384, 16384], [], [], []], "Input Strides": [[16384, 1], [], [], []], "Input type": ["c10::BFloat... |
| 7.74 | 17088 | quant_gemm | ok | True | `void deep_gemm::sm100_tf32_hc_prenorm_gemm_impl<24u, 16384u, 64u, 32u, 64u, 3u, 128u, 12u, 128u, 128u>(unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, float*)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[16384, 16384]", "[16384, 1]", "0"], "Input Dims": [[16384, 16384], [], [], []], "Input Strides": [[16384, 1], [], [], []], "Input type": ["c10::BFloat... |
| 4.23 | 3232 | other | ok | True | `mhc_post_tilelang_kernel` | timestamp_enclosure: `sglang::deep_gemm_fp8_fp8_bf16_nt` {"Concrete Inputs": ["", "", "", "", ""], "Input Dims": [[38, 4096], [38, 8], [1536, 4096], [1536, 8], [38, 1536]], "Input Strides": [[4096, 1], [1, 40], [4096, 1], [1, 1536], [... |
| 4.18 | 1896 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[128], [128], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
