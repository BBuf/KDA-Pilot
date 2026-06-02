# Dispatch decision table — b200_diffusion_qknorm_rope__multi_shape

`optimized_wrapper` (in `src/wrapper.py`, forwarded by `src/register.py`) is a **lean,
custom-op-free dispatcher**. It reads no environment variables. The common path is a few cheap
comparisons + a direct tvm-ffi kernel call — it does **not** go through torch
`register_custom_op`.

## Routing

Per call: `head_dim`/`rope_dim` default from the tensors, then a minimal guard
`_fast_supported(head_dim, rope_dim, is_neox, dtype)` (cached) + `q`/`k` contiguous:

| condition | route | device kernel |
|-----------|-------|---------------|
| exact production-large signature: `head_dim=128, rope_dim=128, is_neox=False`, **int64** positions, and `(num_tokens, num_heads, eps)` ∈ the 5 captured large rows | **staged** | `QKNormRopeStagedKernel` (CTA-per-token cos/sin staging — device win) |
| any other template-supported (`head_dim∈{64,128,256}`, bf16, valid rope_dim/neox) contiguous signature | **warp** | `QKNormRopeKernel` (warp-per-(token,head) faithful port; byte-identical to the SGLang baseline) |
| non-contiguous / non-bf16 / out-of-template (never produced by the 10 production shapes or the CI grid) | **fallback** | captured original SGLang baseline (recursion-safe) or PyTorch reference |

The 5 staged rows: `{(7904,32,1e-6), (4096,24,1e-6), (8424,24,1e-6), (4096,30,1e-5),
(4128,30,1e-5)}`.

## The bottom line: NET WIN on the production install path (promoted)

| metric (idle B200, GPU 4) | geomean | per-shape |
|---|---|---|
| **Literal install path** (`kda_kernels.install()`; baseline custom-op vs the INSTALLED symbol) | **1.2199x / 1.2164x** (2 runs) | large 1.19–1.28x; small 1.20–1.23x — **all 10 win** |
| Device-fair (symmetric direct-JIT, both kernels; diagnostic) | 1.0679x | large 1.10–1.26x; small 0.98–1.00x |

### Per-shape install-path detail (run 1, `benchmark.csv` `*__install` rows)
| shape | bucket | route | base µs | installed µs | install speedup |
|-------|--------|-------|---------|--------------|-----------------|
| joyai-edit B7904/H32 | large | staged | 91.3 | 71.1 | **1.28x** |
| qwen B4096/H24 | large | staged | 58.6 | 47.9 | **1.22x** |
| qwen-edit B8424/H24 | large | staged | 100.4 | 82.1 | **1.22x** |
| zimage B4096/H30 | large | staged | 75.0 | 62.9 | **1.19x** |
| zimage B4128/H30 | large | staged | 74.3 | 62.2 | **1.19x** |
| qwen B19/H24 | small | warp | 63.5 | 51.9 | **1.22x** |
| qwen B47/H24 | small | warp | 62.9 | 51.7 | **1.22x** |
| qwen-edit B195/H24 | small | warp | 63.0 | 52.2 | **1.21x** |
| qwen-edit B189/H24 | small | warp | 62.2 | 51.5 | **1.21x** |
| zimage B32/H30 | small | warp | 62.9 | 51.3 | **1.23x** |

### Why it wins (named effects)
Two compounding host/device effects:
1. **Host: no `register_custom_op`.** After `kda_kernels.install()` the public SGLang symbol is
   a plain dispatcher, so routing straight to the tvm-ffi kernel removes the baseline's per-call
   torch custom-op layer (~10µs) for **every** shape. This alone wins ~1.2x on the small,
   dispatch-bound shapes (whose `warp` device kernel is byte-identical to the baseline — no
   device change, pure host saving).
2. **Device: cos/sin staging on the large shapes.** `QKNormRopeStagedKernel` stages the float32
   cos/sin row once per token in shared memory and reuses it across heads, cutting the
   memory-latency stall (NCU B8424: device 109.6→88.1 µs, `long_scoreboard` 11.9→9.29). This
   compounds with effect (1) so the large shapes win on host **and** device.

The device-fair number (1.0679x, device-only) is smaller than the install win because device-fair
removes the custom-op layer from **both** sides, so it measures only the device-kernel delta; the
literal install path additionally captures the host custom-op saving.

### History (why this differs from the earlier no-go)
An earlier heavy wrapper (a 25-check fail-closed gate that fell **back into** the SGLang
`register_custom_op` baseline for small shapes) measured a net regression (0.93x): it paid its own
Python layer **on top of** the baseline's custom-op. The lean design here never re-enters
custom-op on the common path — it routes straight to the project's kernels — which is what turns
the device win into a net install-path win. See `solutions.jsonl` (`lean_overlay_win` supersedes
`export_r8`).

## Why small shapes use the warp kernel (not staged) — NCU
`profile/baseline_b200/REPORT.md`: small shapes are launch/dispatch-bound (device ~7.55µs vs
~60µs end-to-end), tiny grid. Staging needs more CTAs per token and does not help the device time
(device-fair ~1.0x). So small shapes use the byte-identical warp kernel; their win is purely the
host custom-op saving.

## Why large shapes use the staged kernel — NCU
`profile/staged_b200/REPORT.md`: large shapes are memory-latency bound (~13% DRAM peak,
`long_scoreboard` dominant); staging the per-head-reread float32 cos/sin row cuts that stall
(109.6→88.1 µs device on B8424).

## Reproduce
```bash
python3 scripts/export_kda_kernels/export.py b200_diffusion_qknorm_rope__multi_shape
CUDA_VISIBLE_DEVICES=4 PYTHONPATH=<repo-root> python benchmark.py --integrated   # literal install path (the claim)
CUDA_VISIBLE_DEVICES=4 PYTHONPATH=<repo-root> python benchmark.py --device-fair  # device-only diagnostic
```
