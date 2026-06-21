# Kernel Shape Inventory — random_mid

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3350.0 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 19.65 | 1936 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=39991: `aten::as_strided` {"Concrete Inputs": ["", "[7168]", "[1]", "0"], "Input Dims": [[8192], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "S... |
| 11.97 | 4104 | quant_gemm | missing | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=40074: `Torch-Compiled Region: 5/2` {} |
| 11.68 | 2880 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=22153: `Torch-Compiled Region: 5/4` {} |
| 10.58 | 6776 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[0]", "3", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", ... |
| 9.80 | 4104 | quant_gemm | missing | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=40074: `Torch-Compiled Region: 5/2` {} |
| 6.87 | 9072 | quant_gemm | missing | True | `_mxfp8_block_scaled_matmul_kernel` | external_id=40074: `Torch-Compiled Region: 5/2` {} |
| 2.78 | 4104 | gemm | ok | True | `post_reorder_deepgemm_triton_kernel` | external_id=40074: `Torch-Compiled Region: 5/2` {} |
| 2.06 | 4104 | quant_gemm | missing | True | `void (anonymous namespace)::per_token_quant_ue8m0_scatter_kernel<32u, 5u, true>((anonymous namespace)::PerTokenQuantUe8m0ScatterParams)` | external_id=40074: `Torch-Compiled Region: 5/2` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
