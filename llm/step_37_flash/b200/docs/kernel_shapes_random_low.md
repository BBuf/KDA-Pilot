# Kernel Shape Inventory — random_low

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1229.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 36.73 | 6552 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 32.09 | 6480 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::movedim` {"Concrete Inputs": ["", "[0]", "[1]"], "Input Dims": [[8, 1, 16112], [], []], "Input Strides": [[16112, 16112, 1], [], []], "Input type": ["c10::BFloat16", "ScalarList", "Scala... |
| 2.60 | 5568 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.26 | 3024 | moe | ok | True | `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float const*)` | timestamp_enclosure: `aten::index` {"Concrete Inputs": ["", ""], "Input Dims": [[4097, 262148], []], "Input Strides": [[262148, 1], []], "Input type": ["int", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
