# Kernel Shape Inventory — sharegpt_high

- Model: `poolside/Laguna-XS.2-FP8`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `445.5 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 13.91 | 2808 | moe | ok | True | `fused_moe_kernel` | external_id=56384: `Torch-Compiled Region: 5/3` {} |
| 12.60 | 648 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=51125: `aten::narrow` {"Concrete Inputs": ["", "0", "320", "41"], "Input Dims": [[361], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "Scalar"]} |
| 8.85 | 2268 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=44346: `Torch-Compiled Region: 5/3` {} |
| 6.42 | 1920 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=44346: `Torch-Compiled Region: 5/3` {} |
| 4.88 | 468 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=51667: `Torch-Compiled Region: 5/3` {} |
| 3.44 | 720 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext` | external_id=55865: `aten::slice` {"Concrete Inputs": ["", "0", "0", "768", "1"], "Input Dims": [[768], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "Sc... |
| 3.10 | 780 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[99]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |

The CSV/JSON siblings contain full sample metadata and trace paths.
