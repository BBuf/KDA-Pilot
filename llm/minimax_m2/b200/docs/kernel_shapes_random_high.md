# Kernel Shape Inventory — random_high

- Model: `MiniMaxAI/MiniMax-M2`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1080.9 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 48.15 | 4464 | moe | ok | True | `fused_moe_kernel` | external_id=22811: `aten::view` {"Concrete Inputs": ["", "[-1, 256]"], "Input Dims": [[2797, 2, 128], []], "Input Strides": [[2048, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 9.63 | 4464 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=22811: `aten::view` {"Concrete Inputs": ["", "[-1, 256]"], "Input Dims": [[2797, 2, 128], []], "Input Strides": [[2048, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 4.78 | 1736 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[7]", "[1]", "448"], "Input Dims": [[455], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |
| 3.18 | 3500 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[104], [104], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 3.08 | 500 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=19904: `aten::as_strided` {"Concrete Inputs": ["", "[352, 2, 128]", "[2048, 128, 1]", "0"], "Input Dims": [[352, 2, 128], [], [], []], "Input Strides": [[2048, 128, 1], [], [], []], "Input type": ["c10::... |
| 2.89 | 248 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=22811: `aten::view` {"Concrete Inputs": ["", "[-1, 256]"], "Input Dims": [[2797, 2, 128], []], "Input Strides": [[2048, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 2.57 | 2976 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "0"], "Input Dims": [[0], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scalar"]} |
| 2.36 | 1488 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[100]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.35 | 744 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=22813: `aten::view` {"Concrete Inputs": ["", "[-1, 256]"], "Input Dims": [[1622848, 2, 128], []], "Input Strides": [[256, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
