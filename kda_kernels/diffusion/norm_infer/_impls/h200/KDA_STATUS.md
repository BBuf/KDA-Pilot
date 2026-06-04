# kda_kernels promotion status — norm_infer / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_norm_infer__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `76cd0a0de3ed29306d774ebc9921359e2d573974` (export-source: git HEAD at export; the exported `src/` lands in the SUCCESSOR commit, so this stamp marks the generation point) |
| Benchmarked commit | `b4f9b43aa` (perf anchor: contains the exact benchmarked kernel bytes + arbiter evidence; wall geomean 1.4458x via the in-SGLang dispatch-symmetric env-toggle A/B @ sglang 84e1108312) |
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
