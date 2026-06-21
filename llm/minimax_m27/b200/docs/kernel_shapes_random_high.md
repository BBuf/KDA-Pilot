# Kernel Shape Inventory — random_high

- Model: `MiniMaxAI/MiniMax-M2.7`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1636.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 32.52 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=24177: `Torch-Compiled Region: 5/1` {} |
| 7.47 | 7000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[104], [104], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 7.26 | 3968 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "384", "384", "1"], "Input Dims": [[388], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["int", "Scalar", "Scalar", "Scala... |
| 5.75 | 5952 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[100], [100], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 3.88 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=24177: `Torch-Compiled Region: 5/1` {} |
| 2.40 | 2976 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=18508: `aten::detach_` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.34 | 3472 | moe | ok | True | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "128", "131", "1"], "Input Dims": [[131], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "... |
| 2.07 | 1488 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=25652: `aten::view` {"Concrete Inputs": ["", "[-1, 64, 1, 128]"], "Input Dims": [[4148736, 1, 128], []], "Input Strides": [[128, 128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.00 | 2976 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[0], [14]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
