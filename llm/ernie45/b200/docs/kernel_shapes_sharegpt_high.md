# Kernel Shape Inventory — sharegpt_high

- Model: `baidu/ERNIE-4.5-21B-A3B-PT`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `97.6 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 64.82 | 486 | moe | missing | True | `fused_moe_kernel` | external_id=32395: `Torch-Compiled Region: 4/1` {} |
| 4.48 | 140 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=32397: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "0", "", "", "", "", "", "", ""], "Input Dims": [[2816, 2560], [2816, 4, 128], [2816, 4, 128], [2816, 2560], [], [], [], [], [], [],... |
| 3.33 | 112 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "0"], "Input Dims": [[0], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scalar"]} |
| 2.55 | 360 | quant_gemm | ok | True | `nvjet_sm100_tst_64x64_64x16_2x2_2cta_h_bz_TNT` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[100, 103424], [], []], "Input Strides": [[103424, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
