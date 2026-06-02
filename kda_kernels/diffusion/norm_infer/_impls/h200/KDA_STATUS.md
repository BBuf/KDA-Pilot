# kda_kernels promotion status — norm_infer / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_norm_infer__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `613f780dd77eb5356379bfbd43c3f96009b4ca6f` (export-source: git HEAD when the export ran; the exported `src/` in this package is committed in the SUCCESSOR commit, so this stamp marks the generation point, not a byte-match of the package tree) |
| Benchmarked commit | `b9dcb121ea4c9a1eaf153442548972f5da4704f1` (perf reproducibility anchor; candidate kernels byte-identical since `149392da2`) |
| Promotion date | 2026-06-02 |
| Reported geomean speedup | 1.4223x |
| Promoted functions | norm_infer, triton_one_pass_rms_norm |

## Files

- `__init__.py`
- `layer_norm_n5120.cuh`
- `norm_dispatch.py`
- `register.py`
- `rms_norm_d128.cuh`
- `wrapper.py`
