# kda_kernels promotion status — group_norm_silu / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_group_norm_silu__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `187b4578141a34938bef1dc47cebf150d8b0fab0` (export-source HEAD; package source lands in the successor commit) |
| Benchmarked commit (perf anchor) | `4b2a6c258e9115e019daaf33add3024ef5479867` (canonical benchmark.csv, geomean 1.4487x, v5-dispatch-final) |
| Promotion date | 2026-06-02 |
| Reported geomean speedup | 1.4487x |
| Promoted functions | apply_group_norm_silu, triton_group_norm_silu |

## Files

- `__init__.py`
- `group_norm_dispatch.py`
- `group_norm_silu.cuh`
- `register.py`
- `wrapper.py`
