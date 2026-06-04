# Interface: b200_diffusion_cutedsl_norm_scale_shift__multi_shape

- Kernel slug: `b200_diffusion_cutedsl_norm_scale_shift__multi_shape`
- Op type: `cutedsl_norm_scale_shift`
- Target GPU: NVIDIA B200 (sm_100, 148 SMs, 192 GB HBM3e)
- Wrapped SGLang entry points:
  - `sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_norm_scale_shift`
  - `sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_scale_residual_norm_scale_shift`
- Baseline provenance: SGLang commit `edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7`
  (see `docs/baseline_source.md`).

## Recovered Baseline Contract (pinned commit, authoritative)

### `fused_norm_scale_shift(x, weight, bias, scale, shift, norm_type, eps=1e-5) -> y`

`y = norm(x, weight, bias) * (1 + scale) + shift`, norm in {layer, rms}.

Positional/captured-arg mapping (matches the capture table directly):

| Captured | Parameter | Production values observed |
|---|---|---|
| arg0 | `x` | `[1, S, D]` bf16, S in 19..176400, D in {1536, 3072, 4096, 5120} |
| arg1 | `weight` | always `None` |
| arg2 | `bias` | always `None` |
| arg3 | `scale` | `[1,1,D]` / `[1,D]` bf16; `[1,1,D]` fp32; per-token `[1,S,D]` bf16/fp32 |
| arg4 | `shift` | same classes as `scale` |
| arg5 | `norm_type` | always `"layer"` |
| arg6 | `eps` | always `1e-06` (signature default is `1e-5`) |

### `fused_scale_residual_norm_scale_shift(residual, x, gate, weight, bias, scale, shift, norm_type, eps=1e-5) -> (y, res_out)`

`res_out = residual + gate * x` (`gate=None` -> `res_out = residual + x`);
`y = norm(res_out, weight, bias) * (1 + scale) + shift`.

**Capture-table label correction**: positional `arg0` is `residual` and `arg1` is
`x`. The capture table's "x shape" column labels arg0 as x; the two tensors have
identical `[B, S, D]` shapes/dtypes in every captured row, so the captured data is
unaffected, but implementation and harness must follow the source order above.
(With a non-trivial `gate`, swapping them changes results: `residual + gate*x` ≠
`x + gate*residual`.)

| Captured | Parameter | Production values observed |
|---|---|---|
| arg0 | `residual` | `[1, S, D]` bf16 |
| arg1 | `x` | `[1, S, D]` bf16 |
| arg2 | `gate` | `None`; `[1,1,D]` bf16; `[1,1,D]` fp32; per-token `[1,S,D]` fp32 |
| arg3 | `weight` | `None`; `[D]` fp32 (wan family) |
| arg4 | `bias` | `None`; `[D]` fp32 (wan family) |
| arg5 | `scale` | `[1,1,D]` / `[1,D]` bf16; `[1,1,D]` fp32; per-token `[1,S,D]` fp32; scalar `[1]` bf16 |
| arg6 | `shift` | same classes as `scale` |
| arg7 | `norm_type` | always `"layer"` |
| arg8 | `eps` | always `1e-06` |

### Validators (fail with `ValueError`, candidate must preserve)

- `x`/`residual`: shape `(B, S, D)`, dtype in {fp16, bf16, fp32}, `stride[-1] == 1`.
- `weight`/`bias`: `None` or shape `(D,)`, same dtype set, contiguous.
- `scale`/`shift`/`gate` (gate additionally accepts `None`): ndim 1 -> `[1]` or `[D]`;
  ndim 2 -> `[1|B, D]`; ndim 3 -> `[1|B, 1|S, D]`; ndim 4 -> `[B, F, 1, D]` with
  `S % F == 0` (else `"S(<S>) must be divisible by F(<F>)"`); `stride[-1] == 1`.
- `D % 256 == 0` and `D <= 8192` (else `"D=<D> not supported..."`).
- `norm_type` in {"layer", "rms"} (else `ValueError`).

### Host-side operand normalization (baseline behavior the dispatcher mirrors)

`broadcast_tensor_for_bsfd`: scalar `[1]` passes through unchanged; `[D]`, `[1,D]`,
`[B,D]`, and all 3-D forms are expanded (zero-copy, stride-0) to a `[B, S, D]`
view; `[B,F,1,D]` is kept 4-D and the kernel computes `frame_len = S // F`,
`frame_id = seq_id // frame_len` at runtime. `None` gate/weight/bias become scalar
placeholders (`gate=1`, `weight=1`, `bias=0`) that eliminate the corresponding
compute entirely at compile time (same for `ResOut=0, Residual=0, Gate=1` in the
non-residual entry point — both entry points share one kernel class).

Operand layout classes after normalization (the dispatch enum):
`absent (scalar placeholder)` | `scalar [1] tensor` | `broadcast row (strides
(0,0,1) or (D,0,1))` | `per-token [B,S,D] (real strides)` | `frame 4-D [B,F,1,D]`.

### Numerics contract (tolerance-relevant)

- Pre-norm accumulation `gate*x + residual` is computed and then **cast to
  x.dtype** before normalization (`res_out` stores that cast value; the norm
  consumes the cast value, not the fp32 intermediate).
- Norm statistics accumulate in **fp32**: rms uses sum of squares; layer uses
  **two-pass** mean then variance (`var = sum((x-mean)^2)/D`), both via
  warp-shuffle tree + smem CTA reduction; `factor = rsqrt(var_or_msq/D + eps)`.
- Norm output is cast to x.dtype, then `* (1 + scale) + shift` is applied with
  scale/shift in **their own dtype** (fp32 operands promote the arithmetic), and
  the final value is cast to y.dtype (= x.dtype).
- Outputs are freshly allocated (`torch.empty_like(x)`); no input mutation.

### Registration / integration contract

- Both entry points are `@torch.library.custom_op("sglang::<name>", mutates_args=())`
  with `@<op>.register_fake` shape functions. The shipping integration MUST keep
  this registration; outputs allocated inside the op.
- Launch: current torch CUDA stream; baseline grid `[B*S, 1, 1]`, CTA threads
  `(D // 256) * 32`, 8 elements/thread via 128-bit vectorized copies.
- Baseline compile cache key: `(norm_type, *(dtype, ndim, shape[-1]) per tensor,
  scalar placeholders verbatim)` — B and S are symbolic (one compile per
  (norm_type, dtype-mix, ndim-mix, D)).

## Export

Provide:

```text
src/register.py
```

with:

```python
KERNEL_SLUG = "b200_diffusion_cutedsl_norm_scale_shift__multi_shape"
OP_TYPE = "cutedsl_norm_scale_shift"

def optimized_wrapper(*args, **kwargs):
    ...

def register() -> dict:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }
```

`optimized_wrapper` must preserve the recovered SGLang callsite contract above
for both wrapped entry points (same positional order, same return structure,
same validator failures) and fall back to the `baseline/` copy for any shape,
dtype, layout, device, normalization type, or feature flag not on the verified
native path.

## Evidence Requirements

Before promotion, update this file with:

- final wrapper signature(s);
- per-shape dispatch table (which underlying candidate kernel handles which
  shape bucket);
- fallback cases;
- PyTorch-FP32 or `_reference()` tolerance methodology used in tests;
- benchmark command and latency formula;
- source lineage for copied or ported helper code.
