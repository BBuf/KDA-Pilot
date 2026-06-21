# Kernel Shape Inventory — sharegpt_high

- Model: `MiniMaxAI/MiniMax-M2.5`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1705.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 30.75 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=71306: `aten::view` {"Concrete Inputs": ["", "[-1, 128]"], "Input Dims": [[4150976, 1, 128], []], "Input Strides": [[128, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 9.33 | 8928 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=65534: `aten::slice` {"Concrete Inputs": ["", "0", "0", "264", "1"], "Input Dims": [[288, 768], [], [], [], []], "Input Strides": [[768, 1], [], [], [], []], "Input type": ["c10::Half", "Scalar", "S... |
| 8.28 | 5000 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=74327: `aten::permute` {"Concrete Inputs": ["", "[0, 2, 1, 3]"], "Input Dims": [[64859, 64, 1, 128], []], "Input Strides": [[8192, 128, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 5.94 | 1488 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=74327: `aten::permute` {"Concrete Inputs": ["", "[0, 2, 1, 3]"], "Input Dims": [[64859, 64, 1, 128], []], "Input Strides": [[8192, 128, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 5.20 | 2976 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=68431: `aten::slice` {"Concrete Inputs": ["", "0", "0", "497", "1"], "Input Dims": [[512, 768], [], [], [], []], "Input Strides": [[768, 1], [], [], [], []], "Input type": ["c10::Half", "Scalar", "S... |
| 3.99 | 4000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=59420: `Torch-Compiled Region: 5/3` {} |
| 3.49 | 1984 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "240259864"], "Input Dims": [[196612], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", ... |
| 2.97 | 2976 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[64]", "[1]", "128"], "Input Dims": [[192], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sc... |
| 2.62 | 17856 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=71306: `aten::view` {"Concrete Inputs": ["", "[-1, 128]"], "Input Dims": [[4150976, 1, 128], []], "Input Strides": [[128, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 2.19 | 5952 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=59420: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
