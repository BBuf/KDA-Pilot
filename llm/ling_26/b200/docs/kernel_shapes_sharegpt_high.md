# Kernel Shape Inventory — sharegpt_high

- Model: `inclusionAI/Ling-2.6-flash`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1350.6 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 26.01 | 1820 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=108457: `aten::view` {"Concrete Inputs": ["", "[-1, 512]"], "Input Dims": [[88, 512], []], "Input Strides": [[512, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 21.78 | 2304 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[11, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 18.55 | 2232 | moe | ok | True | `fused_moe_kernel` | external_id=91789: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "2.5", "", "", "False", ""], "Inpu... |
| 7.02 | 260 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=82116: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[1160, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 2.55 | 140 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x128x16_1x1x1_3_tnn_align1_bias_f32_relu` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[3], [3], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
