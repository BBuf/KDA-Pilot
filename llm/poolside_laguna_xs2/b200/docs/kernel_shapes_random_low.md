# Kernel Shape Inventory — random_low

- Model: `poolside/Laguna-XS.2-FP8`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `219.1 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 11.76 | 2808 | moe | ok | True | `fused_moe_kernel` | external_id=392: `aten::as_strided` {"Concrete Inputs": ["", "[4097, 38]", "[262148, 1]", "0"], "Input Dims": [[4097, 262148], [], [], []], "Input Strides": [[262148, 1], [], [], []], "Input type": ["int", "Scalar... |
| 9.03 | 2916 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=392: `aten::as_strided` {"Concrete Inputs": ["", "[4097, 38]", "[262148, 1]", "0"], "Input Dims": [[4097, 262148], [], [], []], "Input Strides": [[262148, 1], [], [], []], "Input type": ["int", "Scalar... |
| 6.64 | 2880 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `aten::index_put_` {"Concrete Inputs": ["", "", "", "False"], "Input Dims": [[4097, 262148], [], [], []], "Input Strides": [[262148, 1], [], [], []], "Input type": ["int", "", "int", "Scalar"]} |
| 5.85 | 2560 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[4096, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 5.80 | 1800 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.93 | 960 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64MultiCtasKvCgaVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[4097, 262148], [], [], [], []], "Input Strides": [[262148, 1], [], [], [], []], "Input type": ["int", "", "in... |
| 2.75 | 960 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | external_id=4236: `aten::view` {"Concrete Inputs": ["", "[-1]"], "Input Dims": [[1, 1], []], "Input Strides": [[1, 1], []], "Input type": ["int", "ScalarList"]} |
| 2.20 | 320 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=392: `aten::as_strided` {"Concrete Inputs": ["", "[4097, 38]", "[262148, 1]", "0"], "Input Dims": [[4097, 262148], [], [], []], "Input Strides": [[262148, 1], [], [], []], "Input type": ["int", "Scalar... |

The CSV/JSON siblings contain full sample metadata and trace paths.
