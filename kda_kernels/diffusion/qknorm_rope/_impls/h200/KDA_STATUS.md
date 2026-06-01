# kda_kernels promotion status — qknorm_rope / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_qknorm_rope__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `93ab0645a679bbb2ae4c60fc5bb605a6cbe71ea0` |
| Promotion date | 2026-06-01 |
| Reported geomean speedup (kernel) | ~1.11x (run-to-run 1.09-1.13; committed runs 1.0965/1.1258/1.0883; large shapes stable ~1.14-1.16x) |
| Integrated-overlay geomean (through install()) | 1.0846x over 9 shapes on idle H200; every shape >= 1.03x; correctness PASS vs oracle. See `kernels/h200_diffusion_qknorm_rope__multi_shape/profile/integration/REPORT.md` |
| Promoted functions | fused_inplace_qknorm_rope |

## Files

- `__init__.py`
- `csrc`
- `register.py`
- `wrapper.py`
