# Kernel Shape Inventory — random_low

- Model: `MiniMaxAI/MiniMax-M2.5`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `732.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 20.52 | 8928 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=253: `aten::as_strided` {"Concrete Inputs": ["", "[39, 1, 128]", "[1024, 128, 1]", "0"], "Input Dims": [[48, 1, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ["c10::Ha... |
| 15.14 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=253: `aten::as_strided` {"Concrete Inputs": ["", "[39, 1, 128]", "[1024, 128, 1]", "0"], "Input Dims": [[48, 1, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ["c10::Ha... |
| 13.92 | 9000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=4339: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[4097], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "", "long int", "S... |
| 10.79 | 7936 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.16 | 17856 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=4339: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[4097], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "", "long int", "S... |
| 3.98 | 3968 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | external_id=4339: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[4097], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "", "long int", "S... |
| 3.08 | 4464 | moe | ok | True | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` | external_id=253: `aten::as_strided` {"Concrete Inputs": ["", "[39, 1, 128]", "[1024, 128, 1]", "0"], "Input Dims": [[48, 1, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ["c10::Ha... |
| 2.61 | 4464 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=253: `aten::as_strided` {"Concrete Inputs": ["", "[39, 1, 128]", "[1024, 128, 1]", "0"], "Input Dims": [[48, 1, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ["c10::Ha... |
| 2.44 | 992 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=245: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
