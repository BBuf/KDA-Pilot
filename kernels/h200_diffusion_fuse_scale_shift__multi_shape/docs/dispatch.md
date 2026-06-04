# Dispatcher Decision Table (final candidate: cuda-flat-v5)

Dispatcher: `solution/dispatch.py` (public callables re-exported by
`src/register.py`). Route observability: `consume_last_route()`. Env:
`KDA_NATIVE=0` forces fallback-only; `KDA_PDL=1` enables PDL (off by default —
not validated as a win on this workload).

## Native eligibility predicates

Family A `fuse_scale_shift_kernel` (kernel `fused_scale_shift_elementwise`):
- x: CUDA, 3D (B, L, C), contiguous, dtype in {bf16, fp16, fp32}, 16B-aligned,
  C % (16B / x-elemsize) == 0, B*L <= 65535 (grid.y), numel > 0 (empty returns
  `empty_like` directly).
- scale/shift: any float dtype in {bf16, fp16, fp32} with element size >= the
  x element size (independently of each other — covers the wan
  fp32-scale/bf16-shift rows; fp32 x with a NARROWER bf16/fp16 modulation
  declines to the baseline, since the 16-byte packet loader converts whole
  modulation packets per x packet). Accepted layouts, mirroring the baseline
  wrapper's resolution:
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

Local bare-ABI numbers, tag `cuda-flat-v5` (centered-variance build):

| row | op | native variant | v5 device | v5 sync_wall |
|---|---|---|---|---|
| prod00 firered 8424x3072 rowwise(1,1,C) | scale_shift | elementwise:ss (strided/strided) | 1.040x | 1.195x |
| prod01 hunyuan 27030x3072 (1,C) | scale_shift | elementwise:ss | 1.061x | 1.122x |
| prod02 hunyuan 55x3072 | scale_shift | elementwise:ss | 1.377x | 1.405x |
| prod03 hunyuan 27085x3072 | scale_shift | elementwise:ss | 1.054x | 1.121x |
| prod04 qwen 4096x3072 | scale_shift | elementwise:ss | 1.469x | 1.325x |
| prod05 qwen 19x3072 | scale_shift | elementwise:ss | 1.437x | 1.482x |
| prod06 qwen 47x3072 | scale_shift | elementwise:ss | 1.441x | 1.477x |
| prod07 qwen-edit select01 8424x3072 | select01 | ln_select01 (int32) | 0.933x | 1.114x |
| prod08 qwen-edit residual 8424x3072 | residual_select01 | ln_select01_residual | 0.979x | 1.138x |
| prod09 qwen-edit per-token 8424x3072 | scale_shift | elementwise:ss | 1.035x | 1.154x |
| prod10 qwen-edit 195x3072 | scale_shift | elementwise:ss | 1.450x | 1.479x |
| prod11 qwen-edit 189x3072 | scale_shift | elementwise:ss | 1.439x | 1.472x |
| prod12 wan-i2v 37044x5120 fp32-scale | scale_shift | elementwise:ss (mixed dtype) | 1.419x | 1.424x |
| prod13 wan-t2v 37800x5120 fp32-scale | scale_shift | elementwise:ss (mixed dtype) | 1.419x | 1.426x |
| prod14 wan-ti2v 18144x3072 NC fp32-scale | scale_shift | elementwise:ss (strided, no copy) | 1.070x | 1.121x |

DEC-1 note (RESOLVED by the in-tree arbiter, docs/sglang_jit_export.md): the
two Family B rows — 0.933x/0.979x on the bare-kernel device view with the
centered-variance build — win 1.139x/1.154x sync and 1.162x/1.169x
stream-span through their REAL production callsite (the registered CustomOp
layer, validation run r3), as does every other row through its direct public
function (all rows positive, min 1.1258x sync).
`PERF_FALLBACK` stays EMPTY; DEC-1 perf-fallback was never needed.

## Regression-grid routing

Full canonical grid (2418 non-negative cases, incl. the offset-data
LayerNorm cases) routes native (verified by the route assertions in
`bench/correctness.py`; run r5: 2428/2428 pass, routes = 2418 native + 10
fallback, the 10 being the negative-parity suite incl. the
fp32-x/bf16-modulation decline case).
