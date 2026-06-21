# Kernel Shape Inventory — random_mid

- Model: `deepseek-ai/DeepSeek-Math-V2`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `29160.3 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 5.81 | 26872 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 240u, 128u, 128u, 1u, 128u, 128u, 128u, 6u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=17787: `sglang::deep_gemm_fp8_fp8_bf16_nt` {"Concrete Inputs": ["", "", "", "", ""], "Input Dims": [[11101, 7168], [11101, 14], [4608, 7168], [4608, 14], [11101, 4608]], "Input Strides": [[7168, 1], [1, 11104], [7168, 1]... |

The CSV/JSON siblings contain full sample metadata and trace paths.
