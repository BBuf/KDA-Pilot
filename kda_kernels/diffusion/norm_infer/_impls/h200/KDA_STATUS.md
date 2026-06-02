# kda_kernels promotion status — norm_infer / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_norm_infer__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `75d4a0ab8fbbaca3ca67b9ca2a979e5078cdd07f` (export-source; this commit's `_impls/h200/` tree matches this package) |
| Benchmarked commit | `b9dcb121e` (kernels byte-identical since `149392da2`; only export/wrapper/validation/metadata changed afterward) |
| Promotion date | 2026-06-02 |
| Reported geomean speedup | 1.4223x (measured on the candidate kernels, unchanged across the commits above) |
| Promoted functions | norm_infer, triton_one_pass_rms_norm |

## Files

- `__init__.py`
- `layer_norm_n5120.cuh`
- `norm_dispatch.py`
- `register.py`
- `rms_norm_d128.cuh`
- `wrapper.py`
