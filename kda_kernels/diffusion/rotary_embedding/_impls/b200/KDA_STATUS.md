# kda_kernels promotion status — rotary_embedding / b200

| Field | Value |
|---|---|
| Task slug | `b200_diffusion_rotary_embedding__multi_shape` |
| Arch | `b200` |
| CUDA capability | `(10, 0)` |
| Commit (kernel-pilot) | `afb416adff0765da3bf610826631b6d5704d5381` |
| Promotion date | 2026-06-04 |
| Reported geomean speedup | ~1.46x like-for-like (env-shift annotated; gate vs prior promoted cuda-v4: fresh pair geomeans 1.0018-1.0050x, standard bucket 1.071x) |
| Promoted functions | apply_ltx2_split_rotary_emb, apply_rotary_embedding |

## Files

- `__init__.py`
- `csrc`
- `register.py`
- `wrapper.py`
