# Kernel Shape Inventory — sharegpt_low

- Model: `poolside/Laguna-XS.2-FP8`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `221.9 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 11.02 | 2808 | moe | missing | True | `fused_moe_kernel` | external_id=27950: `Torch-Compiled Region: 5/3` {} |
| 10.00 | 2916 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=27432: `Torch-Compiled Region: 5/3` {} |
| 6.56 | 2880 | quant_gemm | ok | True | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u, 128u, 0u, 0u, 0u, 16u, 128u, 128u, 1u, 128u, 128u, 128u, 12u, 128u, 128u, 2u, true, 148u, true, (deep_gemm::GemmType)0, false, cutlass::float_e4m3_t, cutlass::float_e4m3_t, cutlass::bfloat16_t, deep_gemm::epilogue::transform::EpilogueIdentity>(int*, unsigned int, unsigned int, unsigned int, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st, CUtensorMap_st)` | timestamp_enclosure: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["long int", "long int", "Scalar"]} |
| 5.73 | 2560 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 5.23 | 1600 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.10 | 320 | norm | missing | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=27432: `Torch-Compiled Region: 5/3` {} |
| 3.02 | 1080 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::sub` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.89 | 960 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64MultiCtasKvCgaVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
