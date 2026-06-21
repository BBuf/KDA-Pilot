# Kernel Shape Inventory — random_high

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3106.3 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 15.99 | 1936 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=115486: `Torch-Compiled Region: 5/2` {} |
| 14.68 | 4104 | quant_gemm | missing | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=115486: `Torch-Compiled Region: 5/2` {} |
| 11.08 | 2880 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=96400: `aten::lift_fresh` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 10.64 | 4104 | quant_gemm | missing | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=115486: `Torch-Compiled Region: 5/2` {} |
| 8.77 | 968 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=96400: `aten::lift_fresh` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 5.80 | 9072 | quant_gemm | ok | True | `_mxfp8_block_scaled_matmul_kernel` | external_id=114594: `aten::select` {"Concrete Inputs": ["", "0", "0"], "Input Dims": [[1, 1], [], []], "Input Strides": [[1, 1], [], []], "Input type": ["int", "Scalar", "Scalar"]} |
| 3.69 | 5808 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[0]", "3", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", ... |
| 3.38 | 2736 | attention | ok | True | `_gqa_share_sparse_decode_kernel` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[42]", "[1]", "256"], "Input Dims": [[298], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sc... |

The CSV/JSON siblings contain full sample metadata and trace paths.
