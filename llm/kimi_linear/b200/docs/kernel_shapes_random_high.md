# Kernel Shape Inventory — random_high

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1383.6 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 25.03 | 1872 | moe | ok | True | `fused_moe_kernel` | external_id=106517: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "2.4460000000000002", "", "", "Fal... |
| 2.88 | 1008 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=101675: `aten::narrow` {"Concrete Inputs": ["", "0", "31", "1"], "Input Dims": [[47], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "Scalar"]} |
| 2.78 | 1100 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |
| 2.66 | 1728 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::to` {"Concrete Inputs": ["", "4", "0", "", "", "True", "False", ""], "Input Dims": [[35], [], [], [], [], [], [], []], "Input Strides": [[1], [], [], [], [], [], [], []], "Input typ... |
| 2.47 | 416 | moe | ok | True | `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, long, long, long, long, long, float)` | external_id=101865: `aten::as_strided` {"Concrete Inputs": ["", "[]", "[]", "9"], "Input Dims": [[1], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
