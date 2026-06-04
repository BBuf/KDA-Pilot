# kda_kernels promotion status — rotary_embedding / b200

| Field | Value |
|---|---|
| Task slug | `b200_diffusion_rotary_embedding__multi_shape` |
| Arch | `b200` |
| CUDA capability | `(10, 0)` |
| Commit (kernel-pilot) | `ec7b6459c21fd18a90cd50bc618dffd4349c35ee` |
| Promotion date | 2026-06-04 |
| Reported geomean speedup | ~1.46x like-for-like (geomean over 11 captured signatures vs the 2026-06-01 baseline env; 3.17x vs the current container baseline whose LTX-2 Triton lacks PR #24732; replacement gate vs prior promoted cuda-v4: 1.0038-1.0066x, standard bucket 1.071x) |
| Promoted functions | apply_ltx2_split_rotary_emb, apply_rotary_embedding |

## Files

- `__init__.py`
- `csrc`
- `register.py`
- `wrapper.py`
