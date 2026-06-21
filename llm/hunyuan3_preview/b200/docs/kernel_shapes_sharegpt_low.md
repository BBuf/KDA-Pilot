# Kernel Shape Inventory — sharegpt_low

- Model: `tencent/Hy3-preview`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2064.2 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 59.51 | 12192 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "0", "15", "1"], "Input Dims": [[15], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "Scal... |
| 12.37 | 11776 | moe | ok | True | `fused_moe_kernel` | external_id=87899: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False"], "Input Dims"... |
| 2.81 | 5760 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::_local_scalar_dense` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.70 | 10560 | quant_gemm | ok | True | `nvjet_hsh_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[4], [4], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.47 | 5120 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ32Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
