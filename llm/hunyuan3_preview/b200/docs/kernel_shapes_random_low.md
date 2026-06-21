# Kernel Shape Inventory — random_low

- Model: `tencent/Hy3-preview`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1809.7 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 38.47 | 1312 | memory_bound | ok | True | `void sglang::cross_device_reduce_2stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | external_id=245: `sgl_kernel::all_reduce` {"Concrete Inputs": ["597603008", "", "", "140569036718080", "8388608"], "Input Dims": [[], [38, 4096], [38, 4096], [], []], "Input Strides": [[], [4096, 1], [4096, 1], [], []],... |
| 15.84 | 11776 | moe | ok | True | `fused_moe_kernel` | external_id=9354: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False"], "Input Dims"... |
| 12.74 | 10880 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __half*, int, int)` | timestamp_enclosure: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False"], "Input Dims"... |
| 3.88 | 5760 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=6814: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 4096], [4096, 192]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["float", "float"]} |
| 3.08 | 10560 | quant_gemm | ok | True | `nvjet_hsh_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `sgl_kernel::build_tree_kernel_efficient` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "1", "3", "4", "0"], "Input Dims": [[1, 3], [1, 3], [1], [248], [4], [1, 4], [1, 4], [1, 4], [], [], [], []], "Input Strides... |
| 2.84 | 5120 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ32Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.24 | 11920 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o409640961_tensorptrf16gmemalign128o409640961_tensorptrf16gmemalign16o_0` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[1]", "[1]", "3", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scala... |

The CSV/JSON siblings contain full sample metadata and trace paths.
