# kda_kernels promotion status — rotary_embedding / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_rotary_embedding__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `4e4229fd7f442773bf54753a6a3845c077f2f01c` |
| Promotion date | 2026-06-02 |
| Reported geomean speedup | 1.295504x |
| Promoted functions | apply_ltx2_split_rotary_emb, apply_rotary_embedding |

## Files

- `__init__.py`
- `csrc`
- `reference.py`
- `register.py`
- `wrapper.py`

## Benchmarked / validated (lag-proof lineage)

- **Benchmarked commit**: `be7bb20f1` (+ harness-fairness fix `5d85066bd`) — the commit whose
  `benchmark.csv` numbers stand; the `.cuh` `src_hash` is `e6588f9edfe7` (a later comment-only
  scrub; compiled kernel byte-identical to the benchmarked `be7bb20f1` `.cuh`). `KDA_COMMIT`
  above is the export-source HEAD (`4e4229fd7`); the `_impls/` tree is committed in its successor.
- **Thin task benchmark** (`kernels/h200_diffusion_rotary_embedding__multi_shape/benchmark.csv`,
  times `optimized_wrapper`): geomean **1.295504×** (the `KDA_SPEEDUP` stamp).
- **Integrated `install()` overlay** (`profile/integration/REPORT.md`, times the swapped public
  SGLang symbol on GPU 7 / `ion-h200-8` / sglang `c47f0e7cd`): geomean **1.3032×** over the 6
  production shapes, correctness PASS (6/6 `cuda` route, matches baseline within `1e-2`,
  functional new-tensor contract). The two geomeans agree → the memoized dispatcher adds no
  measurable per-call tax.
- `scripts/export_kda_kernels/verify.py`: `installed: 2 swaps` (both rotary functions); all other
  families `skipped: not optimized`.
