# Kernel Shape Inventory — random_low

- Model: `XiaomiMiMo/MiMo-V2-Flash`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `9858.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 60.19 | 6216 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)` | external_id=1252353: `sgl_kernel::all_reduce` {"Concrete Inputs": ["892916160", "", "", "140122326564864", "8388608"], "Input Dims": [[], [4, 4096], [4, 4096], [], []], "Input Strides": [[], [4096, 1], [4096, 1], [], []], "... |
| 34.97 | 768 | memory_bound | ok | True | `void sglang::cross_device_reduce_2stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)` | external_id=1216446: `aten::lift_fresh` {"Concrete Inputs": [""], "Input Dims": [[0]], "Input Strides": [[1]], "Input type": ["float"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
