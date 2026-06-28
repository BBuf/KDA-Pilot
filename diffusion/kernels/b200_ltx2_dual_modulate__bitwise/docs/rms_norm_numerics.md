# Bit-Exact Numerics Spec — LTX2 Dual Modulation

Source: task3 (`analyze`) — Codex `gpt-5.5:high`, Round 0. This pins the exact
operation/rounding decomposition the candidate must reproduce for `torch.equal`
parity with the PyTorch eager baseline. Empirically re-verify on the B200 against
the installed torch build (bitwise parity is torch-version-sensitive).

## Design implication (decisive)
`F.rms_norm` on CUDA bf16 uses the **vectorized** `_fused_rms_norm` path: `vec_size=4`,
~128 logical threads/row, per-thread strided vec4 fp32 accumulation, warp-shuffle
tree reduction, then inter-warp shared-memory reduction. **A naive sequential fp32
`sum += x_i*x_i` will NOT reproduce ATen's `rstd` bit-for-bit.** Therefore:
- **Strategy A is the primary path:** obtain `normed` from the SAME normalization the
  baseline uses (ATen `F.rms_norm` / `aten._fused_rms_norm`) so it is bit-identical by
  construction, and implement only the **affine** in a fused CUDA kernel.
- **Strategy B (custom fused RMS reduction)** is gated: only pursue if an RMS-only
  `torch.equal` check (AC-4) passes after matching ATen's reduction tree exactly.

## RMS_NORM_DECOMP
For current CUDA fused bf16 RMSNorm on contiguous `[*, D]` (no weight):
1. Read `x` as bf16, convert to fp32 accumulator.
2. `ms = fp32_reduce(x_i * x_i) / float(D)`; `rstd = rsqrtf(ms + fp32(eps))` (eps in fp32).
3. `normed_i = bf16_rne(fp32(x_i) * rstd_fp32)` (single final multiply, no weight).
4. `F.rms_norm` returns bf16 (`empty_like(input)`); internal `rstd` is fp32.
5. Reduction order is the vectorized tree above — not index order. Use `rsqrtf`
   (not `1/sqrtf`). If mimicking ATen, also check whether its local `sum += x*x`
   compiled to FFMA vs separate MUL+ADD for the target wheel.

## AFFINE_BOUNDARIES
Eager `y = normed * (1 + scale) + shift` with bf16 tensors is three materialized
bf16-producing ops (fp32 opmath, bf16 store, round-to-nearest-even each):
```
t_i = bf16_rne(fp32(1.0) + fp32(scale_i))
p_i = bf16_rne(fp32(normed_i) * fp32(t_i))
y_i = bf16_rne(fp32(p_i)    + fp32(shift_i))
```
Do NOT collapse to `bf16_rne(fp32(normed)*(1+fp32(scale)) + fp32(shift))` (one
rounding instead of three → can differ by ≥1 bf16 ulp).

## CA_DERIVATION
`scale_shift_table.to(x.dtype).view(1,1,4,D) + temb.reshape(B,temb_seq,4,D)`:
- fp32 table → `table_bf16[k,d] = bf16_rne(table_fp32[k,d])` FIRST, then
  `scale_shift[k,d] = bf16_rne(fp32(table_bf16[k,d]) + fp32(temb_bf16[k,d]))`.
- bf16 table: `.to` is a no-op; bits unchanged.
- Broadcasting `[1,1,4,D]`→`[B,temb_seq,4,D]` changes strides only (no bit change).
- `unbind(dim=2)` order: `0→scale0, 1→shift0, 2→scale1, 3→shift1`.

## CUDA_REPRO_NOTES
```cpp
float s = __bfloat162float(scale);
__nv_bfloat16 t  = __float2bfloat16_rn(__fadd_rn(1.0f, s));
float p          = __fmul_rn(__bfloat162float(normed), __bfloat162float(t));
__nv_bfloat16 pb = __float2bfloat16_rn(p);
float y          = __fadd_rn(__bfloat162float(pb), __bfloat162float(shift));
__nv_bfloat16 yb = __float2bfloat16_rn(y);
```
- Use explicit `__float2bfloat16_rn`, `__fadd_rn`, `__fmul_rn`. Avoid overloaded
  `__nv_bfloat16` operators (may emit native bf16 ops, not fp32-opmath+bf16-store).
- Disable FMA contraction in the affine (separate mul→bf16→reload→add). No
  `--use_fast_math`.

## VERIFICATION_RECIPE
- Per D∈{2048,4096}: build bf16 inputs, compute eager reference, assert
  `torch.equal` on `normed`, `y0`, `y1` for both operations.
- Isolate RMS: `torch.equal(my_rms(x), F.rms_norm(x,(D,),eps))`.
- rstd ulp probe: `out, rstd = torch.ops.aten._fused_rms_norm.default(x,[D],None,eps)`;
  compare `rstd.view(torch.int32)` against the candidate's fp32 rstd (max abs ulp).
- Set `torch.backends.cuda.matmul.allow_tf32 = False`.

## RISKS
1. RMS reduction order (sequential fp32 sum ≠ ATen fused). → Strategy A avoids it.
2. torch version (2.4 vs 2.6/2.7 vs current fused differ). → pin + re-verify on B200.
3. Accidental affine fusion (must keep the three visible bf16 temporaries).
