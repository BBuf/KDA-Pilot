# Kernel Shape Inventory — sharegpt_low

- Model: `MiniMaxAI/MiniMax-M2`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `334.6 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 24.78 | 4464 | moe | ok | True | `fused_moe_kernel` | external_id=30080: `Torch-Compiled Region: 5/3` {} |
| 22.81 | 4464 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=30080: `Torch-Compiled Region: 5/3` {} |
| 7.37 | 4500 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=30080: `Torch-Compiled Region: 5/3` {} |
| 6.05 | 3968 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | nearest_preceding_shape_cpu_op: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 4.65 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 4.58 | 1984 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "160632644"], "Input Dims": [[699], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "Sc... |
| 2.65 | 2232 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=30046: `aten::as_strided` {"Concrete Inputs": ["", "[64]", "[1]", "0"], "Input Dims": [[16384], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sc... |
| 2.23 | 248 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=30080: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
