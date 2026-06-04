# kda_kernels promotion status — rotary_embedding / b200

| Field | Value |
|---|---|
| Task slug | `b200_diffusion_rotary_embedding__multi_shape` |
| Arch | `b200` |
| CUDA capability | `(10, 0)` |
| Commit (kernel-pilot) | `afb416adff0765da3bf610826631b6d5704d5381` |
| Promotion date | 2026-06-04 |
| Reported geomean speedup | 1.466x vs sglang main 8933ec877 (measured geomean over the 11 captured signatures, 3 idle-gated sessions; standard 1.92x, LTX-2 1.00-1.67x; replacement gate vs prior promoted cuda-v4: standard 1.071x) |
| Promoted functions | apply_ltx2_split_rotary_emb, apply_rotary_embedding |

## Files

- `__init__.py`
- `csrc`
- `register.py`
- `wrapper.py`
