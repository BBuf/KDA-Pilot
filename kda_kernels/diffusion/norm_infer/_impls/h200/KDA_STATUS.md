# kda_kernels promotion status — norm_infer / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_norm_infer__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `76cd0a0de3ed29306d774ebc9921359e2d573974` |
| Promotion date | 2026-06-04 |
| Reported geomean speedup | 1.4458x |
| Promoted functions | norm_infer, triton_one_pass_rms_norm |

## Files

- `__init__.py`
- `layer_norm_n5120.cuh`
- `norm_dispatch.py`
- `register.py`
- `rms_norm_d128.cuh`
- `rms_norm_d128_tile16.cuh`
- `wrapper.py`
