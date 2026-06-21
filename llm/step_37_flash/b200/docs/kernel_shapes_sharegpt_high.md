# Kernel Shape Inventory — sharegpt_high

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `4131.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 27.51 | 1456 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=124383: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[49, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 27.24 | 6480 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[49, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 13.46 | 4368 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=116187: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[600, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
