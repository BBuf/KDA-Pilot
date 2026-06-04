# Dispatch table (shipped configuration)

The dispatcher (`src/wrapper.py`) classifies each call by (entry point,
scale/shift class+dtype, gate class+dtype, weight/bias presence) and routes to
one of 10 native CUDA template instantiations, or falls back (fail-closed) to
the vendored baseline. Per-combo vector width is the one measured
specialization: combos touching any fp32 operand stream run 8 elems/thread
(kVecBytes=16, block=D/8) after NCU run r0v1 showed the 16-elem variant at 41%
occupancy / long_scoreboard 16.4 on fp32 streams; bf16-only combos run 16
elems/thread (kVecBytes=32, block=D/16).

Numbers: run_id=r6-final (idle-gated harness on B200 GPU1; committed
external before/after all-GPU snapshots in `bench/evidence/r6-final/`;
interleaved A/B, candidate behind the kda_nss custom-op layer = host stacks
identical; median of 100 iters; rows carry the current joint source hash
d0f645a016cb). Ranges below re-verified against r6-final (per-case deltas vs
the superseded r4/r5 runs are within run-to-run noise, <2%).

| Export | Combo | Vec | Covered signatures | device speedup | e2e speedup | Verdict |
|---|---|---|---|---|---|---|
| nss_row_bf16 | nss, scale/shift row-bcast bf16 (11D + 1D) | 32B | 17 sigs (qwen/hunyuan/joyai/firered/mova/qwen-edit/wan, D 1536..5120, S 19..176400) | 1.20-1.60x | 1.26-1.49x | promote |
| nss_row_fp32 | nss, row-bcast fp32 | 16B | wan-i2v/t2v 37044/37800x5120 | 1.12x | 1.16x | promote |
| nss_token_bf16 | nss, per-token bf16 | 32B | helios 8640x5120, wan-ti2v 18144x3072 | 1.37-1.63x | 1.28-1.29x | promote |
| nss_token_fp32 | nss, per-token fp32 | 16B | helios 11040x5120, wan-ti2v 18144x3072 | 0.98-1.00x (parity) | 1.11x | promote (host win; device at DRAM operand-stream bound, see results.md) |
| srnss_grow_bf16_row_bf16 | srnss, gate row bf16, sc row bf16 | 32B | qwen/hunyuan/firered/qwen-edit srnss rows (8 sigs) | 1.15-1.42x | 1.23-1.40x | promote |
| srnss_gnone_row_bf16 | srnss, no gate, sc row bf16 | 32B | mova 44100x5120, 101x1536 | 1.15-1.17x | 1.19-1.20x | promote |
| srnss_gnone_row_fp32 | srnss, no gate, sc row fp32 | 16B | wan 37044/37800x5120 | 1.05-1.06x | 1.10x | promote |
| srnss_gnone_token_fp32 | srnss, no gate, per-token fp32 | 16B | wan-ti2v 18144x3072 | 1.02x | 1.10x | promote (device at bound) |
| srnss_grow_fp32_wb_scalar_bf16 | srnss, gate row fp32, w/b [D] fp32, scalar sc bf16 | 16B | wan 37044/37800x5120 | 1.32-1.33x | 1.31x | promote |
| srnss_gtoken_fp32_wb_scalar_bf16 | srnss, gate per-token fp32, w/b fp32, scalar sc bf16 | 16B | wan-ti2v 18144x3072 | 1.21x | 1.22x | promote |

Cross-check: the in-SGLang drop-in smoke (`docs/sglang_jit_export.md`, same
public op A/B) reproduces these ranges on six representative buckets
(1.108x-1.448x).

Fallback routes (tested, baseline handles): fp16/fp32 activations, rms norm,
B>1 operand layouts (BD/B1D/BSD with B>1), 4-D BF1D frame mode, scalar
scale/shift without the wan affine pattern, non-contiguous/misaligned views,
non-CUDA or cross-device operands, D not in the native geometry (e.g. 256),
empty tensors, non-tensor scale/shift.

All 39 unique captured signatures dispatch native (zero fallbacks across 9399
calls in the final run); the regression grid exercises both routes.
