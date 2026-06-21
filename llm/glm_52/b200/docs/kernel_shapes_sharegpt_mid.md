# Kernel Shape Inventory — sharegpt_mid

- Model: `zai-org/GLM-5.2-FP8`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `15341.2 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 11.47 | 1824 | moe_comm | ok | True | `void deep_ep::intranode::notify_dispatch<8>(int const*, int*, int const*, int*, int, int, int, bool const*, int*, int*, int, int, void**, int**, int)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[8, 10]", "3", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "... |
| 2.90 | 1824 | moe_comm | ok | True | `void deep_ep::intranode::combine<__nv_bfloat16, 8, 768, 4096>(__nv_bfloat16*, float*, __nv_bfloat16 const*, float const*, __nv_bfloat16 const*, __nv_bfloat16 const*, int const*, int const*, int const*, int*, int, int, int, int, void**, int, int, int)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[-1, 64, 512]"], "Input Dims": [[2128, 1, 64, 512], []], "Input Strides": [[32768, 32768, 512, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.38 | 3648 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 4096u, 6144u, 128u, 128u, 128u, 32u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `sglang::deep_gemm_fp8_fp8_bf16_nt` {"Concrete Inputs": ["", "", "", "", ""], "Input Dims": [[8, 16384], [8, 32], [6144, 16384], [6144, 32], [8, 6144]], "Input Strides": [[16384, 1], [1, 8], [16384, 1], [1, 6144],... |
| 2.35 | 1824 | moe_comm | ok | True | `void deep_ep::intranode::dispatch<8, 768, 8192>(int4*, float*, int*, long*, float*, int*, int*, int4 const*, float const*, long const*, float const*, bool const*, int const*, int, int, int, int, int, int, int, int, void**, int, int, int)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[5325, 12]", "3", "0", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar... |

The CSV/JSON siblings contain full sample metadata and trace paths.
