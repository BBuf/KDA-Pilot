# Kernel Shape Inventory — random_mid

- Model: `tencent/Hy3-preview`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5171.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.73 | 11744 | moe | ok | True | `fused_moe_kernel` | external_id=36059: `aten::as_strided` {"Concrete Inputs": ["", "[33056, 1, 64, 128]", "[8192, 128, 128, 1]", ""], "Input Dims": [[33056, 64, 1, 128], [], [], []], "Input Strides": [[8192, 128, 128, 1], [], [], []], ... |
| 24.47 | 10832 | memory_bound | ok | True | `void sglang::cross_device_reduce_2stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[128], [128], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 9.78 | 1312 | comm | ok | True | `ncclDevKernel_AllReduce_Sum_f16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` | external_id=29293: `sglang::inplace_all_reduce` {"Concrete Inputs": ["", ""], "Input Dims": [[11225, 4096], []], "Input Strides": [[4096, 1], []], "Input type": ["c10::Half", ""]} |
| 4.34 | 5232 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 4.08 | 640 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x128x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=36159: `aten::empty_like` {"Concrete Inputs": ["", "", "", "", "False", ""], "Input Dims": [[11225, 128], [], [], [], [], []], "Input Strides": [[1280, 1], [], [], [], [], []], "Input type": ["c10::Half"... |
| 2.78 | 640 | moe | ok | True | `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, long, long, long, long, long, at::OpMathType<c10::Half>::type)` | external_id=37644: `aten::matmul` {"Concrete Inputs": ["", ""], "Input Dims": [[11225, 4096], [4096, 192]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["float", "float"]} |
| 2.09 | 11888 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o409640961_tensorptrf16gmemalign128o409640961_tensorptrf16gmemalign16o_0` | timestamp_enclosure: `aten::empty_strided` {"Concrete Inputs": ["[11225, 4096]", "[4096, 1]", "5", "0", "", "True"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Scal... |

The CSV/JSON siblings contain full sample metadata and trace paths.
