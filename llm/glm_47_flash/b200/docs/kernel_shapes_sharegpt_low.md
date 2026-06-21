# Kernel Shape Inventory — sharegpt_low

- Model: `zai-org/GLM-4.7-Flash`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `73.4 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 20.23 | 828 | moe | missing | True | `fused_moe_kernel` | external_id=40204: `Torch-Compiled Region: 5/1` {} |
| 6.51 | 47 | other | ok | True | `_fwd_kernel` | external_id=41451: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "43", "", "", "", "", "", "", ""], "Input Dims": [[4, 20, 576], [4, 1, 576], [4, 1, 512], [4, 10240], [], [], [], [], [], [], [], []... |
| 4.62 | 846 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | external_id=40204: `Torch-Compiled Region: 5/1` {} |
| 3.91 | 432 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.56 | 423 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.55 | 752 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.34 | 423 | quant_gemm | ok | True | `nvjet_sm100_tst_128x8_64x12_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
