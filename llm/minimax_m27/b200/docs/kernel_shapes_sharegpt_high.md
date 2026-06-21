# Kernel Shape Inventory — sharegpt_high

- Model: `MiniMaxAI/MiniMax-M2.7`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1626.2 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 32.22 | 8928 | moe | missing | True | `fused_moe_kernel` | external_id=65216: `Torch-Compiled Region: 5/3` {} |
| 10.87 | 5000 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=65216: `Torch-Compiled Region: 5/3` {} |
| 5.38 | 2976 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=59538: `aten::as_strided` {"Concrete Inputs": ["", "[64824, 1, 64, 128]", "[8192, 128, 128, 1]", ""], "Input Dims": [[64824, 64, 1, 128], [], [], []], "Input Strides": [[8192, 128, 128, 1], [], [], []], ... |
| 4.60 | 2480 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "248427572"], "Input Dims": [[330], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "Sc... |
| 4.23 | 4000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=51659: `Torch-Compiled Region: 5/3` {} |
| 4.12 | 992 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=62291: `aten::empty_strided` {"Concrete Inputs": ["[707, 6, 128]", "[768, 128, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ... |
| 3.24 | 2976 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[0], [21]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 2.56 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=65416: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "6", "", "", "", "", "", "", ""], "Input Dims": [[1536, 768], [1536, 1, 128], [1536, 1, 128], [1536, 768], [], [], [], [], [], [], [... |
| 2.40 | 5952 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=51659: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
