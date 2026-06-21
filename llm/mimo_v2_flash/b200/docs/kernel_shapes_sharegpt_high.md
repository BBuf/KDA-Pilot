# Kernel Shape Inventory — sharegpt_high

- Model: `XiaomiMiMo/MiMo-V2-Flash`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `6144.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 92.61 | 6984 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)` | external_id=3695541: `sgl_kernel::all_reduce` {"Concrete Inputs": ["1284723296", "", "", "139933616439296", "8388608"], "Input Dims": [[], [4, 4096], [4, 4096], [], []], "Input Strides": [[], [4096, 1], [4096, 1], [], []], ... |

The CSV/JSON siblings contain full sample metadata and trace paths.
