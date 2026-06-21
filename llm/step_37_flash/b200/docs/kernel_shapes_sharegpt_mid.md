# Kernel Shape Inventory — sharegpt_mid

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3465.5 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 21.82 | 6480 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16, 4096], [4096, 1792]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 21.40 | 5096 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=69468: `aten::_reshape_alias` {"Concrete Inputs": ["", "[16, 128]", "[1280, 1]"], "Input Dims": [[16, 128], [], []], "Input Strides": [[1280, 1], [], []], "Input type": ["c10::BFloat16", "ScalarList", "Scala... |
| 16.15 | 728 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=87562: `aten::view` {"Concrete Inputs": ["", "[-1, 1, 128]"], "Input Dims": [[442, 128], []], "Input Strides": [[128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 4.48 | 336 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=75207: `aten::transpose` {"Concrete Inputs": ["", "0", "1"], "Input Dims": [[4096, 160], [], []], "Input Strides": [[160, 1], [], []], "Input type": ["c10::BFloat16", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
