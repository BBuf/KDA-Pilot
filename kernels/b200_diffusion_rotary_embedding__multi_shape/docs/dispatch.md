# Dispatcher decision table — b200_diffusion_rotary_embedding__multi_shape

`src/wrapper.py` exposes two out-of-place entry points, each routing to a native CUDA kernel for the
captured production signatures and to the SGLang Triton baseline for everything else. Candidate
`cuda-v1` (kp_commit `fb7427793`), B200 GPU3 idle, CUDA-event single-call timing (`benchmark.csv`).

## Routing gates (must match `wrapper.py::_supported_*` exactly)

### `apply_rotary_embedding` → `_supported_standard`  (CUDA iff ALL hold; else SGLang baseline)
- `interleaved == False`
- `x` CUDA bf16 contiguous, rank 3 `(S,H,D)` or rank 4 `(1,S,H,D)` (batch must be 1 if 4D)
- `(num_tokens, num_heads, head_dim) == (27030, 24, 128)`  ← the only captured standard signature
- `cos`, `sin` CUDA fp32 contiguous, shape `(27030, 64)`
- all tensors on the same device

### `apply_ltx2_split_rotary_emb` → `_supported_ltx2`  (CUDA iff ALL hold; else SGLang baseline)
- `x` CUDA bf16 contiguous 3D `(B, S, H*2*half)`
- `cos`, `sin` CUDA bf16, 4D `(B, 32, S, half)`, equal shapes, innermost stride 1, `(b,h,t)` strides multiples of 8
- `num_heads == 32`, `half ∈ {32,64}`, and `(B, S, half)` in the 10 captured tuples:
  `(1,1536,64) (1,126,32) (1,1536,32) (1,6144,64) (1,6144,32) (2,6144,64) (2,126,32) (2,6144,32) (1,24576,64) (1,24576,32)`
- all tensors on the same device

> Guards are intentionally restricted to the captured/benchmarked table (the kernels are correct for
> the broader class, but a promoted wrapper must never silently intercept an unprofiled shape). Widen
> only after capturing + benchmarking new shapes.

## Per-bucket decision (cuda-v1, idle B200 GPU3; medians from benchmark.csv)

| Bucket | Captured signature(s) | Path | Baseline µs | Cand µs | Speedup | Active bound (NCU/roofline) | Promote? |
|---|---|---|---|---|---|---|---|
| standard (HunyuanVideo) | `[1,27030,24,128]`, cos/sin `[27030,64]` | cuda | 133.9 | 75.5 | **1.77×** | memory-leaning 60% SOL (headroom, but wins big) | **yes** |
| LTX-2 small | `(1,126,32)`,`(2,126,32)` | cuda | 21.5–21.9 | 14.9 | 1.44–1.46× | launch/latency bound (~1.55MB) | **yes** |
| LTX-2 mid | `(1,1536,*)`,`(1,6144,*)`,`(2,6144,*)` | cuda | 22.8–62.1 | 15.1–56.0 | 1.11–1.54× | partial BW saturation | **yes** |
| LTX-2 large | `(1,24576,64)`,`(1,24576,32)` | cuda | 71.8–104.5 | 55.7–98.7 | 1.06–1.29× | **DRAM-BW bound, 85.7% SOL (near roofline)** | **yes** |
| geomean (11 unique sigs) | — | — | — | — | **1.3676×** | — | **PROMOTE** |

## Fallback bucket (correctness-only; NOT optimization shapes)

| Tuple | Path | Status |
|---|---|---|
| standard non-captured (e.g. `(4,8,128)`, any token count ≠ 27030, H ≠ 24) | fallback | correct vs oracle (baseline) |
| standard `interleaved=True` | fallback | correct vs oracle |
| standard head_dim ≠ 128 (e.g. 64) | fallback | correct vs oracle |
| LTX-2 `num_heads ≠ 32` (e.g. 16) | fallback | correct vs oracle |
| LTX-2 `(B,S,half)` not in captured set (e.g. `(2,1536,64)`, `S=512`) | fallback | correct vs oracle |
| LTX-2 `half ∉ {32,64}` | fallback | correct vs oracle |
| non-bf16 x / non-contiguous x / CPU / mismatched device / wrong cos dtype | fallback | correct vs oracle |

(Fallback routing + the above negatives are asserted in `tests/test_correctness.py::test_dispatch_gates_reject_unsupported`.)

## Promotion stance: PROMOTE (both entry points)

cuda-v1 is correct on every captured shape (candidate-vs-baseline 17/17; LTX-2 bit-exact, standard
within 1 ulp; pytest 7/7) and beats the SGLang baseline on **every** captured signature — geomean
**1.3676×** (standard **1.77×**, LTX-2 1.06–1.54×) — with an NCU/roofline-named active bound per bucket
and the wall-clock-dominant LTX-2-large bucket already near the DRAM roofline (85.7% SOL). Promote both
`apply_rotary_embedding` and `apply_ltx2_split_rotary_emb` via
`scripts/export_kda_kernels/export.py b200_diffusion_rotary_embedding__multi_shape`.
