# Kernel Shape Inventory — sharegpt_high

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1029.3 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 26.35 | 1872 | moe | ok | True | `fused_moe_kernel` | external_id=145613: `aten::select` {"Concrete Inputs": ["", "0", "16"], "Input Dims": [[55], [], []], "Input Strides": [[1], [], []], "Input type": ["long int", "Scalar", "Scalar"]} |
| 3.05 | 220 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1075, 8, 128], [1, 1075, 8, 128], []], "Input Strides": [[1310720, 1024, 128, 1], [1100800, 1024, 128, 1], []], "Input ... |
| 2.85 | 1100 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |
| 2.79 | 400 | other | ok | True | `chunk_gated_delta_rule_fwd_kernel_h_blockdim64` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[1, 9135, 8, 128]", "[9354240, 1024, 128, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], ... |
| 2.73 | 632 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=143753: `aten::as_strided` {"Concrete Inputs": ["", "[3072, 16384]", "[1, 3336]", ""], "Input Dims": [[16384, 3072], [], [], []], "Input Strides": [[3336, 1], [], [], []], "Input type": ["c10::BFloat16", ... |
| 2.64 | 1512 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 1024], [1024, 2304]], "Input Strides": [[1024, 1], [1, 1024]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.35 | 416 | moe | ok | True | `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, long, long, long, long, long, float)` | external_id=148757: `sgl_kernel::moe_sum_reduce` {"Concrete Inputs": ["", "", "2.4460000000000002"], "Input Dims": [[16384, 8, 2304], [16384, 2304], []], "Input Strides": [[18432, 2304, 1], [2304, 1], []], "Input type": ["c10:... |
| 2.27 | 1200 | other | ok | True | `_causal_conv1d_fwd_kernel` | timestamp_enclosure: `LayerNormGatedFunction` {"Concrete Inputs": ["", "", "", "", "", "1.0000000000000001e-05", "False", "False", "True"], "Input Dims": [[1, 16384, 8, 128], [16384, 8, 128], [128], [], [], [], [], [], []],... |

The CSV/JSON siblings contain full sample metadata and trace paths.
