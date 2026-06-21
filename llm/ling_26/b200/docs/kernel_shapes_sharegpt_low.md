# Kernel Shape Inventory — sharegpt_low

- Model: `inclusionAI/Ling-2.6-flash`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `419.5 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 33.85 | 2340 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::sub` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 29.95 | 2304 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[44, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 9.27 | 2232 | moe | ok | True | `fused_moe_kernel` | external_id=46998: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "2.5", "", "", "False", ""], "Inpu... |
| 2.38 | 1888 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | timestamp_enclosure: `aten::index_put_` {"Concrete Inputs": ["", "", "", "False"], "Input Dims": [[704, 262148], [], [], []], "Input Strides": [[262148, 1], [], [], []], "Input type": ["int", "", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
