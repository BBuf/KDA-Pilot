# kda_kernels promotion status — qknorm_rope / b200

| Field | Value |
|---|---|
| Task slug | `b200_diffusion_qknorm_rope__multi_shape` |
| Arch | `b200` |
| CUDA capability | `(10, 0)` |
| Commit (kernel-pilot) | `2b2f8dd522f5782e799e1f2e0c44a08ac1039c41` |
| Promotion date | 2026-06-02 |
| Reported geomean speedup | **1.22x** (literal `kda_kernels.install()` path, B200; 1.2199x / 1.2164x over 2 idle runs; all 10 production shapes 1.18–1.28x) |
| Promoted functions | fused_inplace_qknorm_rope |

## Files

- `__init__.py`
- `qknorm_rope_candidate.cuh`
- `register.py`
- `wrapper.py`
