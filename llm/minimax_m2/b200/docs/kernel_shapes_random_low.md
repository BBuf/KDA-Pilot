# Kernel Shape Inventory — random_low

- Model: `MiniMaxAI/MiniMax-M2`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `326.5 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 23.61 | 4464 | moe | ok | True | `fused_moe_kernel` | external_id=244: `Torch-Compiled Region: 5/3` {} |
| 23.36 | 4464 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 7.54 | 4500 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=244: `Torch-Compiled Region: 5/3` {} |
| 6.18 | 3968 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | external_id=4300: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 200064], [], []], "Input Strides": [[200064, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 4.72 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 4.53 | 1984 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `c10d::broadcast_` {"Concrete Inputs": ["", "", "0", "0", "False", "-1"], "Input Dims": [[[1]], [], [], [], [], []], "Input Strides": [[[1]], [], [], [], [], []], "Input type": ["TensorList", "", ... |
| 2.73 | 2232 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=244: `Torch-Compiled Region: 5/3` {} |
| 2.15 | 248 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=236: `aten::empty` {"Concrete Inputs": ["[2]", "3", "0", "", "", "0"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "Sc... |

The CSV/JSON siblings contain full sample metadata and trace paths.
