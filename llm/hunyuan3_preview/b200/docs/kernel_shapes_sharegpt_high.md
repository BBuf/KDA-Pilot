# Kernel Shape Inventory — sharegpt_high

- Model: `tencent/Hy3-preview`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5536.0 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 30.75 | 2616 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | external_id=185392: `aten::linear` {"Concrete Inputs": ["", "", ""], "Input Dims": [[31, 1024], [4096, 1024], []], "Input Strides": [[1024, 1], [1024, 1], []], "Input type": ["c10::Half", "c10::Half", ""]} |
| 18.92 | 11680 | moe | ok | True | `fused_moe_kernel` | external_id=168001: `aten::linear` {"Concrete Inputs": ["", "", ""], "Input Dims": [[1220, 4096], [384, 4096], []], "Input Strides": [[4096, 1], [4096, 1], []], "Input type": ["c10::Half", "c10::Half", ""]} |
| 15.77 | 8112 | memory_bound | ok | True | `void sglang::cross_device_reduce_2stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[256]", "[1]", "0"], "Input Dims": [[256], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |
| 6.91 | 5200 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "0", "31", "1"], "Input Dims": [[31, 8], [], [], [], []], "Input Strides": [[8, 1], [], [], [], []], "Input type": ["int", "Scalar", "Scalar", "Sca... |

The CSV/JSON siblings contain full sample metadata and trace paths.
