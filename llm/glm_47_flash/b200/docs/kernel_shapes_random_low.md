# Kernel Shape Inventory — random_low

- Model: `zai-org/GLM-4.7-Flash`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `67.3 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 21.80 | 828 | moe | missing | True | `fused_moe_kernel` | external_id=241: `Torch-Compiled Region: 5/1` {} |
| 5.01 | 846 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | timestamp_enclosure: `aten::any` {"Concrete Inputs": [""], "Input Dims": [[1, 154880]], "Input Strides": [[154880, 1]], "Input type": ["bool"]} |
| 4.21 | 432 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.87 | 423 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 2.80 | 752 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.55 | 423 | quant_gemm | ok | True | `nvjet_sm100_tst_128x8_64x12_4x1_v_bz_TNT` | external_id=241: `Torch-Compiled Region: 5/1` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
