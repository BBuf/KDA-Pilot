# Kernel Shape Inventory — sharegpt_mid

- Model: `tencent/Hy3-preview`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5306.5 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 44.46 | 3936 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | external_id=136597: `sgl_kernel::all_reduce` {"Concrete Inputs": ["434645568", "", "", "139898115850240", "8388608"], "Input Dims": [[], [6, 4096], [6, 4096], [], []], "Input Strides": [[], [4096, 1], [4096, 1], [], []], "... |
| 21.16 | 11680 | moe | ok | True | `fused_moe_kernel` | external_id=126074: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False"], "Input Dims"... |
| 7.90 | 6800 | memory_bound | ok | True | `void sglang::cross_device_reduce_2stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32, 37], [32, 37], []], "Input Strides": [[4096, 1], [37, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 3.13 | 5200 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1, 5]", "3", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", ""... |
| 2.02 | 640 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x128x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=124920: `sglang::inplace_all_reduce` {"Concrete Inputs": ["", ""], "Input Dims": [[5067, 4096], []], "Input Strides": [[4096, 1], []], "Input type": ["c10::Half", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
