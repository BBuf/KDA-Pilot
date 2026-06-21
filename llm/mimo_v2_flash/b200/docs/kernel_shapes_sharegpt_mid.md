# Kernel Shape Inventory — sharegpt_mid

- Model: `XiaomiMiMo/MiMo-V2-Flash`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `7420.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 93.86 | 6984 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)` | external_id=3394808: `sgl_kernel::all_reduce` {"Concrete Inputs": ["662564240", "", "", "139781910560768", "8388608"], "Input Dims": [[], [4, 4096], [4, 4096], [], []], "Input Strides": [[], [4096, 1], [4096, 1], [], []], "... |

The CSV/JSON siblings contain full sample metadata and trace paths.
