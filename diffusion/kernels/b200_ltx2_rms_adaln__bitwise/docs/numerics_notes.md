# Numerics Notes — bf16 bit-exactness (task2, analyze via Codex)

The staged candidate must be bit-identical to PyTorch eager
`normed = F.rms_norm(x,(D,),eps); y = normed * (1 + scale) + shift` (bf16).

## Elementwise rounding
- PyTorch bf16 elementwise ops compute in fp32 opmath and store via
  `static_cast<at::BFloat16>(float)` → `c10::BFloat16(float)`, which on CUDA is
  round-to-nearest-**even** (NVIDIA device conversion; software fallback uses the
  explicit RNE bias `((bits>>16)&1)+0x7fff`).
- CUDA `__float2bfloat16_rn(float)` is documented RNE and **matches** that store,
  ties-to-even included. So each modulation stage matches eager:
  - `one_plus = __float2bfloat16_rn(1.0f + float(scale))`  ≡ bf16 `1 + scale`
  - `mul      = __float2bfloat16_rn(float(normed) * float(one_plus))` ≡ bf16 `normed*(1+scale)`
  - `y        = __float2bfloat16_rn(float(mul) + float(shift))` ≡ bf16 `+ shift`
- `1` is exactly representable; keep the operand order `1.0f + float(scale)`
  (commutative for finite values; preserves raw NaN payload/sign in the fragile
  case).

## RMS reduction order
- The staged candidate calls the **same** `at::rms_norm(x,{D},{},eps)` as the
  baseline, so the fp32 reduction order and the bf16 store of `normed` are
  identical **by construction** — no reduction-order reverse-engineering needed.
- Reduction-order analysis is required **only** before a fully-fused single-kernel
  attempt (task10); it gates that stretch, not the staged candidate.

## Edge cases / compile requirements
- Keep the modulation as three discrete bf16-rounded stages; do **not** fuse into
  an FMA or reorder. The intermediate `__float2bfloat16_rn` rounds act as barriers,
  so `a*b` and `+c` cannot be contracted (no unbroken `a*b+c` expression exists).
- Do **not** pass `--use_fast_math` / FTZ (we don't): bf16 subnormals must round
  normally to match eager.
- signed zero (+0/-0), inf: match when the exact rounded sequence is preserved.
- NaN: device conversion path matches; payload/sign is the fragile case — do not
  canonicalize. A targeted NaN-payload row would be added only if NaNs were in
  scope (production rows are finite; `correctness.py` rejects any NaN/Inf output).

Source: Codex (gpt-5.5:high) analysis; NVIDIA CUDA Math API bf16 docs; PyTorch
`torch/headeronly/util/BFloat16.h`.
