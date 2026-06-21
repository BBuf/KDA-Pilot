# Kernel Shape Inventory — random_low

- Model: `MiniMaxAI/MiniMax-M2.7`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `662.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 17.19 | 9000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=4358: `aten::empty_strided` {"Concrete Inputs": ["[]", "[]", "3", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "ScalarL... |
| 16.64 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=264: `Torch-Compiled Region: 5/3` {} |
| 12.36 | 7936 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign_0` | external_id=4358: `aten::empty_strided` {"Concrete Inputs": ["[]", "[]", "3", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "ScalarL... |
| 7.86 | 8928 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | external_id=4358: `aten::empty_strided` {"Concrete Inputs": ["[]", "[]", "3", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "ScalarL... |
| 4.42 | 3968 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::to` {"Concrete Inputs": ["", "", "4", "False", "False", ""], "Input Dims": [[1], [], [], [], [], []], "Input Strides": [[1], [], [], [], [], []], "Input type": ["long int", "", "Sca... |
| 3.90 | 992 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=264: `Torch-Compiled Region: 5/3` {} |
| 3.39 | 4464 | moe | missing | True | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` | external_id=264: `Torch-Compiled Region: 5/3` {} |
| 2.88 | 4464 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=264: `Torch-Compiled Region: 5/3` {} |
| 2.37 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __nv_bfloat16, __nv_fp8_e4m3, false, false, false, true, float>(__nv_bfloat16 const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=4358: `aten::empty_strided` {"Concrete Inputs": ["[]", "[]", "3", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "ScalarL... |
| 2.25 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __nv_bfloat16, __nv_fp8_e4m3, true, true, false, true, unsigned int>(__nv_bfloat16 const*, __nv_fp8_e4m3*, unsigned int*, int const*, int, int, int, int, int)` | nearest_preceding_shape_cpu_op: `detach_` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.12 | 496 | gemm | missing | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=264: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
