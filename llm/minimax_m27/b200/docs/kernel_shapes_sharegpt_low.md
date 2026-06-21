# Kernel Shape Inventory — sharegpt_low

- Model: `MiniMaxAI/MiniMax-M2.7`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `640.9 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 18.24 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=31570: `Torch-Compiled Region: 5/3` {} |
| 15.36 | 9000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 12.55 | 7936 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 8.12 | 8928 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[640], [640], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 4.69 | 3968 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[64], [576]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.59 | 4464 | moe | missing | True | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` | external_id=31570: `Torch-Compiled Region: 5/3` {} |
| 2.96 | 4464 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | timestamp_enclosure: `detach_` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.45 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __nv_bfloat16, __nv_fp8_e4m3, false, false, false, true, float>(__nv_bfloat16 const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[640], [59]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 2.36 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __nv_bfloat16, __nv_fp8_e4m3, true, true, false, true, unsigned int>(__nv_bfloat16 const*, __nv_fp8_e4m3*, unsigned int*, int const*, int, int, int, int, int)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[640], [640], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 2.33 | 496 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=31570: `Torch-Compiled Region: 5/3` {} |
| 2.33 | 992 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=31546: `aten::to` {"Concrete Inputs": ["", "3", "False", "False", ""], "Input Dims": [[1], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", ... |

The CSV/JSON siblings contain full sample metadata and trace paths.
