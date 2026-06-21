# Kernel Shape Inventory — random_high

- Model: `inclusionAI/Ling-2.6-flash`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `628.4 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 20.78 | 2080 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=32339: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[39, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 18.60 | 2232 | moe | ok | True | `fused_moe_kernel` | external_id=36797: `aten::zero_` {"Concrete Inputs": [""], "Input Dims": [[64]], "Input Strides": [[1]], "Input type": ["float"]} |
| 18.50 | 260 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=42584: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[334, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 17.97 | 2304 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[-1, 4096]"], "Input Dims": [[39, 4096], []], "Input Strides": [[4096, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.13 | 1680 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x2_h_bz_TNT` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[107], [107], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 2.06 | 992 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=32169: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[39, 4096], [4096, 256]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["float", "float"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
