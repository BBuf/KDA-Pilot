# Dispatch decision table — h200_diffusion_qknorm_rope__multi_shape

The candidate is a single native-CUDA `.cuh` (`src/csrc/qknorm_rope_kernel.cuh`) with a compile-time
path selection inside `QKNormRopeKernel<...>::run`, plus a lean Python gate in `src/wrapper.py`.

## Kernel-path selection (compile-time, by template params)

| Condition | Path | Layout |
|---|---|---|
| `head_dim == 128 && rope_dim == 128 && !is_neox` | `fused_qknorm_rope_warp2` (2 heads per warp, float4) | 16 lanes/head, 8 bf16/lane via one 128-bit load, 16-lane RMS reduction, GPT-J RoPE on all 128 dims |
| otherwise — incl. **`head_dim=128, rope_dim=64`**, head_dim ∈ {64,256}, or is_neox | `fused_qknorm_rope_warp` (baseline, 1 head per warp) | 32 lanes/head, 4 bf16/lane (64-bit), 32-lane reduction, rope_dim-aware (`lane_id < kRotaryLanes`) |

Rationale: all 9 captured production shapes are `head_dim=128, rope_dim=128, is_neox=False`, so they
take the warp2 path. The warp2 body rotates **all 128 dims** and indexes cos/sin as if `rope_dim==128`,
so it is gated to `rope_dim==128` (enforced by `static_assert(kRopeDim == 128)`); **`rope_dim=64` (and
all other points) use the rope_dim-aware baseline path** — the baseline guards rotation with
`lane_id < kRotaryLanes`. (Round-0 review caught a bug where warp2 was wrongly used for `rope_dim=64`
and rotated dims 64–127 / read past the cos/sin row; fixed by the `rope_dim==128` gate.)

## Wrapper dispatch (`optimized_wrapper`, runtime)

| Input class | Dispatch | Notes |
|---|---|---|
| bf16, CUDA, contiguous, 16B-aligned, non-aliased q/k, head_dim∈{64,128,256}, rope_dim gate | `"cuda"` (candidate kernel via load_jit) | static eligibility cached; minimal per-call checks |
| CPU / fp16 / non-contiguous / misaligned / aliased q/k / unsupported head_dim/rope_dim/is_neox/pos-dtype | `"fallback"` (PyTorch FP32 semantic reference) | never raises except the double-install guard |

## Per-bucket benchmark evidence

See `benchmark.csv` and `bench_summary_*.json` (ion8-h200 GPU7, idle, dual-level wrapper+module).

| Tag | What | Geomean (wrapper) | Geomean (module) | Notes |
|---|---|---|---|---|
| d0-clone | baseline clone, heavy wrapper | 0.9036x | 1.0003x | wrapper tax dominates tiny shapes |
| d0-leanwrap | baseline clone, lean wrapper | 1.0587x | 0.9948x | dispatch win on tiny (T≤195: 1.09–1.11x) |
| d2-warp2 (history) | 2-head float4 + lru_cache wrapper | 1.0992x | 1.0285x | round-0; superseded (warp2 over-gated for rope_dim=64; lru_cache wrapper) |
| **d3-final** | **2-head float4 + cache_once wrapper + rope_dim gate (FINAL, src 4f70cda7)** | **1.0723x** | **1.0268x** | kernel win on large (module 1.069–1.085x); lean dispatch on tiny (~1.05–1.09x wrapper) |

### Per-shape — d3-final (from benchmark.csv; module-level = kernel; wrapper-level = end-to-end)
| Shape | tokens | heads | module sp | wrapper sp | regime |
|---|---|---|---|---|---|
| qwen_t4096 | 4096 | 24 | 1.069x | 1.065x | large / memory-latency |
| qwen_t19 | 19 | 24 | 0.985x | 1.072x | tiny / launch-bound |
| qwen_t47 | 47 | 24 | 0.985x | 1.051x | tiny / launch-bound |
| qwenedit_t8424 | 8424 | 24 | 1.084x | 1.077x | large / memory-latency |
| qwenedit_t195 | 195 | 24 | 0.993x | 1.068x | tiny / launch-bound |
| qwenedit_t189 | 189 | 24 | 0.985x | 1.090x | tiny / launch-bound |
| zimage_t4096 | 4096 | 30 | 1.075x | 1.078x | large / memory-latency |
| zimage_t32 | 32 | 30 | 0.989x | 1.071x | tiny / launch-bound |
| zimage_t4128 | 4128 | 30 | 1.085x | 1.080x | large / memory-latency |

Bound (NCU, `profile/round_warp2/REPORT.md`): large = memory-latency-bound (long-scoreboard 58%, DRAM
40% of peak, occ 73%) near the attainable bound; tiny = launch/underfill-bound (occ 12%, 0.07 waves/SM)
→ kernel no-go, carried by lean dispatch. No 1-head-vs-2-head per-bucket split is needed: the universal
warp2 path wins or ties everywhere on head_dim=128, and head_dim 64/256 + neox keep the baseline path.
