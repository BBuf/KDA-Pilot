# Kernel Shape Inventory — random_high

- Model: `baidu/ERNIE-4.5-21B-A3B-PT`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `98.1 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 64.96 | 486 | moe | missing | True | `fused_moe_kernel` | external_id=13111: `Torch-Compiled Region: 4/1` {} |
| 4.39 | 112 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=13113: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "0", "", "", "", "", "", "", ""], "Input Dims": [[2816, 2560], [2816, 4, 128], [2816, 4, 128], [2816, 2560], [], [], [], [], [], [],... |
| 3.63 | 140 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[100]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.90 | 415 | quant_gemm | ok | True | `nvjet_sm100_tst_64x64_64x16_2x2_2cta_h_bz_TNT` | timestamp_enclosure: `aten::_to_copy` {"Concrete Inputs": ["", "4", "", "", "", "False", ""], "Input Dims": [[256], [], [], [], [], [], []], "Input Strides": [[1], [], [], [], [], [], []], "Input type": ["int", "Sca... |

The CSV/JSON siblings contain full sample metadata and trace paths.
