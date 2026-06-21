# Kernel Shape Inventory — random_high

- Model: `poolside/Laguna-XS.2-FP8`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `408.8 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 15.89 | 2808 | moe | ok | True | `fused_moe_kernel` | external_id=21160: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[704]], []], "Input Strides": [[[1]], []], "Input type": ["TensorList", "Scalar"]} |
| 10.08 | 2592 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[104, 16], [104, 16], []], "Input Strides": [[4096, 1], [16, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 5.49 | 1248 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "320"], "Input Dims": [[64], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scal... |
| 4.19 | 1280 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=14168: `Torch-Compiled Region: 5/3` {} |
| 4.15 | 324 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=21160: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[704]], []], "Input Strides": [[[1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.77 | 480 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext` | external_id=22341: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "19", "", "", ""], "Input Dims": [[2560, 2048], [2560, 2, 128], [2560, 2, 128], [2560, 2048], [], [], [], [], []], "Input Strides": ... |
| 3.27 | 156 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=21160: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[704]], []], "Input Strides": [[[1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.09 | 1600 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[100], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 2.48 | 2060 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[100]"], "Input Dims": [[100], []], "Input Strides": [[1], []], "Input type": ["long int", "ScalarList"]} |
| 2.28 | 600 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | timestamp_enclosure: `aten::narrow` {"Concrete Inputs": ["", "0", "0", "192"], "Input Dims": [[192], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
