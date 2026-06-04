# Dispatcher Decision Table (final candidate: cuda-flat-v4)

Dispatcher: `solution/dispatch.py` (public callables re-exported by
`src/register.py`). Route observability: `consume_last_route()`. Env:
`KDA_NATIVE=0` forces fallback-only; `KDA_PDL=1` enables PDL (off by default —
not validated as a win on this workload).

## Native eligibility predicates

Family A `fuse_scale_shift_kernel` (kernel `fused_scale_shift_elementwise`):
- x: CUDA, 3D (B, L, C), contiguous, dtype in {bf16, fp16, fp32}, 16B-aligned,
  C % (16B / x-elemsize) == 0, B*L <= 65535 (grid.y), numel > 0 (empty returns
  `empty_like` directly).
- scale/shift: any float dtype in {bf16, fp16, fp32} (independently of x —
  covers the wan fp32-scale/bf16-shift rows). Accepted layouts, mirroring the
  baseline wrapper's resolution:
  - scalar (0D / 1-element) -> splat template path;
  - 2D (B,C)/(1,C), 3D (B,L,C) + broadcastable variants -> expand() view with
    c-stride 1 and 16B-aligned b/l strides (zero strides included; the
    non-contiguous fp32 production scale passes through WITHOUT a copy);
  - 4D (B,F,1,C) contiguous with L % F == 0 -> per-frame path (shift must be
    per-token reshapeable, as in the baseline).
- BOTH-scalar calls replicate the baseline wrapper exactly (including its
  zero-check host sync and copy short-circuit) before entering the splat
  kernel, preserving bug-for-bug wrapper semantics.

Family B select01 / residual (kernel `fused_ln_select01`):
- x (and residual/residual_gate for the residual op): CUDA, 3D, contiguous,
  same dtype, 16B-aligned; C % vec == 0 and C <= 256 * vec * 4 (register tile).
- six modulation tensors: 2D (B, C), x dtype, c-stride 1, one SHARED row
  stride (production: the padded 18432-element adaLN chunk stride), aligned.
- weight/bias: None or 1D [C] contiguous in x dtype.
- index: 2D (B, L) int32/int64 (bool is cast to int32 — tiny copy, same !=0
  selection semantics); values contract {0, 1}.
- eps: runtime float.

Anything else -> vendored Triton baseline (`baseline/`), so out-of-contract
inputs inherit the baseline's exact error behavior (verified by the
negative-parity suite).

## Production routing (15/15 rows native; PERF_FALLBACK empty — DEC-1 unused)

| row | op | native variant | v4 device | v4 sync_wall |
|---|---|---|---|---|
| prod00 firered 8424x3072 rowwise(1,1,C) | scale_shift | elementwise:ss (strided/strided) | 1.039x | 1.199x |
| prod01 hunyuan 27030x3072 (1,C) | scale_shift | elementwise:ss | 1.060x | 1.122x |
| prod02 hunyuan 55x3072 | scale_shift | elementwise:ss | 1.391x | 1.403x |
| prod03 hunyuan 27085x3072 | scale_shift | elementwise:ss | 1.055x | 1.121x |
| prod04 qwen 4096x3072 | scale_shift | elementwise:ss | 1.476x | 1.327x |
| prod05 qwen 19x3072 | scale_shift | elementwise:ss | 1.434x | 1.470x |
| prod06 qwen 47x3072 | scale_shift | elementwise:ss | 1.443x | 1.474x |
| prod07 qwen-edit select01 8424x3072 | select01 | ln_select01 (int32) | 0.954x | 1.122x |
| prod08 qwen-edit residual 8424x3072 | residual_select01 | ln_select01_residual | 0.982x | 1.131x |
| prod09 qwen-edit per-token 8424x3072 | scale_shift | elementwise:ss | 1.037x | 1.157x |
| prod10 qwen-edit 195x3072 | scale_shift | elementwise:ss | 1.445x | 1.468x |
| prod11 qwen-edit 189x3072 | scale_shift | elementwise:ss | 1.443x | 1.470x |
| prod12 wan-i2v 37044x5120 fp32-scale | scale_shift | elementwise:ss (mixed dtype) | 1.420x | 1.429x |
| prod13 wan-t2v 37800x5120 fp32-scale | scale_shift | elementwise:ss (mixed dtype) | 1.420x | 1.428x |
| prod14 wan-ti2v 18144x3072 NC fp32-scale | scale_shift | elementwise:ss (strided, no copy) | 1.071x | 1.126x |

DEC-1 note (RESOLVED by the in-tree arbiter, docs/sglang_jit_export.md): the
two Family B rows — 0.954x/0.982x on the bare-kernel device view — win
1.149x/1.151x sync and 1.181x/1.168x stream-span through the real SGLang
public wrapper, as does every other row (min 1.125x). `PERF_FALLBACK` stays
EMPTY; DEC-1 perf-fallback was never needed.

## Regression-grid routing

Full canonical grid (2415 non-negative cases) routes native (verified by the
route assertions in `bench/correctness.py`; run r4: 2424/2424 pass, routes =
2415 native + 9 fallback, the 9 being the negative-parity suite).
