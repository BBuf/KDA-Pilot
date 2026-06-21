# Kernel Shape Inventory — sharegpt_mid

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3053.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 14.72 | 968 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=229601: `Torch-Compiled Region: 5/2` {} |
| 12.10 | 6776 | comm | missing | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=216206: `Torch-Compiled Region: 5/4` {} |
| 12.08 | 2880 | norm | missing | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=216206: `Torch-Compiled Region: 5/4` {} |
| 10.59 | 4104 | quant_gemm | missing | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 768u, 6144u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=229601: `Torch-Compiled Region: 5/2` {} |
| 8.52 | 968 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=269759: `Torch-Compiled Region: 5/4` {} |
| 8.05 | 4104 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u, 32u, 0u, 6144u, 384u, 128u, 128u, 128u, 129u, 128u, 128u, 128u, 8u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)2, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=229601: `Torch-Compiled Region: 5/2` {} |
| 5.85 | 9072 | quant_gemm | ok | True | `_mxfp8_block_scaled_matmul_kernel` | external_id=229601: `Torch-Compiled Region: 5/2` {} |
| 2.09 | 5760 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign128o614461441_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[0], [13]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
