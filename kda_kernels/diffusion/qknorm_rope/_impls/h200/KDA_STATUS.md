# kda_kernels promotion status — qknorm_rope / h200

| Field | Value |
|---|---|
| Task slug | `h200_diffusion_qknorm_rope__multi_shape` |
| Arch | `h200` |
| CUDA capability | `(9, 0)` |
| Commit (kernel-pilot) | `673217af69ce03f4c92237e37fd8aa70acaa2797` |
| Promotion date | 2026-06-02 |
| Reported geomean speedup | `1.015x` all-9 (integrated install() path vs SGLang baseline) |
| — large shapes (tokens ≥ 4096) | `1.06x` (memory-latency-bound regime — the real win) |
| — small shapes (tokens ≤ 195) | parity (`0.97–0.99x`; launch-bound, dispatcher-frame limited) |
| Promoted functions | fused_inplace_qknorm_rope |

> Speedup is the **integrated `install()` production path** (kda dispatcher → wrapper →
> jit_kernel candidate) vs the captured SGLang baseline, measured on an idle H200 (GPU 7),
> CUDA-event median of 200 iters, inputs restored outside the timed region, two consistent runs
> (all-9 geomean 1.012× / 1.018×). Correctness: all 9 captured shapes dispatch `cuda` and match the
> split oracle (sglang `fused_inplace_qknorm` + flashinfer RoPE) at 1 bf16 ulp (ATOL 8e-2/RTOL 1e-2);
> fp16 inputs fall back cleanly. See `../../../../kernels/h200_diffusion_qknorm_rope__multi_shape/profile/integration/REPORT.md`.

## Files

- `__init__.py`
- `csrc`
- `register.py`
- `wrapper.py`
