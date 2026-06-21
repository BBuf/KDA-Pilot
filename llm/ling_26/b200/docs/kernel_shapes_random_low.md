# Kernel Shape Inventory — random_low

- Model: `inclusionAI/Ling-2.6-flash`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `391.3 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 33.75 | 2340 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=1785: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[39, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 28.14 | 2304 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | external_id=2366: `aten::empty` {"Concrete Inputs": ["[312, 256]", "15", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "S... |
| 9.39 | 2232 | moe | ok | True | `fused_moe_kernel` | external_id=1979: `sgl_kernel::moe_sum_reduce` {"Concrete Inputs": ["", "", "2.5"], "Input Dims": [[39, 8, 4096], [39, 4096], []], "Input Strides": [[32768, 4096, 1], [4096, 1], []], "Input type": ["c10::BFloat16", "c10::BFl... |
| 2.55 | 1888 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
