# kda_kernels promotion status — rotary_embedding

| Field | Value |
|---|---|
| Task slug | `b200_diffusion_rotary_embedding__multi_shape` |
| Kernel-source commit (kernel-pilot) | `fb74277933d3d04d6fe48d9f2b4650a52467ab09` (candidate `cuda-v1`; restricted guards in `aaa8d0642`; evidence in `93af8df91`) |
| Promotion date | 2026-05-31 |
| Reported geomean speedup | 1.3676x (11 unique captured signatures; standard 1.77x, LTX-2 1.06–1.54x) — B200 GPU3 idle-gated |
| Promoted functions | apply_ltx2_split_rotary_emb, apply_rotary_embedding |

## Files

- `csrc`
- `register.py`
- `wrapper.py`
