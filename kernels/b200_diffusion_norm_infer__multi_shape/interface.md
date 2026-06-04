# Interface: b200_diffusion_norm_infer__multi_shape

- Kernel slug: `b200_diffusion_norm_infer__multi_shape`
- Op type: `layer_or_rms_norm_infer`
- Target GPU: NVIDIA B200 (sm_100)
- Wrapped SGLang entry points:
  - `sglang.jit_kernel.diffusion.triton.norm:norm_infer`
  - `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm`

## Recovered Baseline Contracts (from SGLang source)

Source checkout: `/Users/bbuf/工作目录/Common/sglang` (record exact commit in `solutions.jsonl` before remote builds).

### 1. `norm_infer` — `python/sglang/jit_kernel/diffusion/triton/norm.py`

```python
def norm_infer(
    x: Tensor,                     # (M, N), 2D; x = x.contiguous() applied internally
    weight: Optional[Tensor],      # (N,) or None; asserts shape==(N,), stride(-1)==1
    bias: Optional[Tensor],        # (N,) or None; asserts shape==(N,), stride(-1)==1
    eps: float,                    # positional, REQUIRED (no default)
    is_rms_norm: bool = False,     # False = LayerNorm, True = RMSNorm
    out: Optional[Tensor] = None,  # if None -> torch.empty_like(x)
) -> Tensor                        # returns `out`, same shape & dtype as x
```

Kernel `_norm_infer_kernel` — **one Triton program per row** (`grid=(M,)`); the row is loaded once into registers and reduced twice (mean, then variance):
- `x` row loaded as **fp32** over `BLOCK_N` cols, `mask = cols < N`, `other=0`.
- LayerNorm (`is_rms_norm=False`): `mean = sum(x)/N`; `xbar = where(cols<N, x-mean, 0)`; `var = sum(xbar*xbar)/N` (population variance, post-mean — NOT Welford, NOT `E[x^2]-mean^2`).
- RMSNorm (`is_rms_norm=True`): `xbar = where(cols<N, x, 0)`; `var = sum(xbar*xbar)/N` (no mean subtraction).
- `rstd = 1/sqrt(var + eps)`.
- `x_hat = (x - mean)*rstd` (LN) or `x*rstd` (RMS).
- weight (loaded fp32, default 1.0): `y = x_hat * w`; bias (loaded fp32, default 0.0): `y += b`.
- store `y` masked, cast back to `x`'s dtype.

Launch shape guards (host side):
- `MAX_FUSED_SIZE = 65536 // x.element_size()`; `BLOCK_N = min(MAX_FUSED_SIZE, next_pow2(N))`.
- Raises `RuntimeError("This layer norm doesn't support feature dim >= 64KB.")` when `N > BLOCK_N`.
- `num_warps = min(max(BLOCK_N // 256, 1), 8)`.

Numerics: fp32 accumulation; output dtype = input dtype. **The CUDA port must reproduce the LN `sum((x-mean)^2)/N` formula and fp32 accumulation to hold the fp32 `1e-5` tolerance.**

Production case for this entry point:
- **helios**: `x=[8640,5120] fp32`, `weight=[5120] fp32`, `bias=[5120] fp32`, `eps=1e-6`, `is_rms_norm=False` → `BLOCK_N = min(16384, 8192) = 8192`, `num_warps=8`, `grid=(8640,)`.

### 2. `triton_one_pass_rms_norm` — `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py`

```python
def triton_one_pass_rms_norm(
    x: torch.Tensor,    # any shape; x = x.contiguous(); reshaped to (-1, D) -> (S, D)
    w: torch.Tensor,    # (D,)
    eps: float = 1e-6,  # positional / keyword, default 1e-6
) -> torch.Tensor       # returns y = empty_like(x), same shape & dtype as x
```

Registered as custom op `triton_one_pass_rms_norm_cuda` (`out_shape="x"`). Kernel `_rms_norm_tiled_onepass` — **tiled over rows**, one pass:
- `x.contiguous()`, `y = empty_like(x)`, reshape to `(S, D)`.
- `block_size_seq = min(16, next_pow2(max(1, S // 512)))`; `grid = (cdiv(S, block_size_seq),)`; `BLOCK_SIZE_DIM = next_pow2(D)`.
- Per block: load `(BLOCK_SIZE_SEQ × BLOCK_SIZE_DIM)` tile as **fp32**; `mean_square = sum(x*x, axis=1)/D`; `rstd = rsqrt(mean_square + eps)`; `w` loaded in native dtype (no explicit fp32 cast); `y = x * rstd * w`; store (cast to `y` dtype).
- No bias, no mean subtraction (pure RMS). No `is_rms_norm` flag.

Production cases for this entry point (all `D=128`, `bf16`, `w=[128]`, `eps=1e-6`):

| Preset | S (rows) | block_size_seq | grid blocks | BLOCK_SIZE_DIM |
|---|---|---|---|---|
| hunyuanvideo | 648720 | 16 | 40545 | 128 |
| hunyuanvideo | 1320 | 2 | 660 | 128 |
| hunyuanvideo | 650040 | 16 | 40628 | 128 |
| zimage | 16384 | 16 | 1024 | 128 |
| zimage | 4096 | 8 | 512 | 128 |

### Shared note — the `.contiguous()` copy

Both baselines call `x = x.contiguous()`. For the six captured shapes the inputs are already contiguous (`...C` in the capture), so this is a no-op. For genuinely non-contiguous (e.g. channels-last) inputs the baseline pays a copy that a strided-read CUDA kernel could skip via `TensorMatcher.with_strides` — a candidate optimization *lever*, but OUT of scope for the six contiguous production shapes (do not broaden the shape set to chase it).

## Export

Provide:

```text
src/register.py
```

with:

```python
KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"

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

`optimized_wrapper` must preserve the recovered SGLang callsite contract for BOTH wrapped entry points (dispatch on which underlying callable + shape/dtype) and fall back to the baseline implementation for any shape, dtype, layout, device, normalization type, or feature flag outside the configured shape table. A `*, dispatcher_hint=` keyword may be accepted for dispatcher overrides.

## Evidence Requirements (fill before promotion)

- final wrapper signature(s);
- per-shape dispatch table (which underlying candidate kernel handles which shape bucket);
- fallback cases;
- PyTorch-FP32 / `_reference()` tolerance methodology used in tests (fp32 `atol=rtol=1e-5`; bf16/fp16 `atol=rtol=5e-2`);
- benchmark command and latency formula (PRIMARY = wrapper-inclusive wall-clock; kernel-only CUDA-event time secondary);
- source lineage for copied or ported helper code (record in `solutions.jsonl`).
## Round-2 routing addendum (2026-06-04)

`optimized_wrapper` routing after the round-2 large-S reopen (evidence:
`docs/dispatch.md`, `docs/results.md`):

- `norm_infer` → CUDA `LayerNormInferKernel<fp32_t>` for allowlisted fp32 2-D
  shapes (unchanged from round 1).
- `triton_one_pass_rms_norm` → CUDA, with an in-route split:
  - `S < 100000`: `RmsNormOnepassKernel<128,1,bf16_t>` (one warp per row);
  - `S ≥ 100000` (allowlisted: 648720, 650040): `RmsNormTiledKernel<128,32,bf16_t>`
    with the persistent whole-wave grid (`scheduling=1`); requires a 16-byte-aligned
    base (the tile kernel uses 16-byte vector accesses) — 8-byte-aligned-only views
    fall back to the baseline.
- Everything outside the allowlists falls back to the SGLang Triton baseline
  (semantics unchanged; 15 fallback-routing cases re-verified).
- Direct harness entry (not routed by `optimized_wrapper`):
  `src/register.py::tiled_rms_onepass(x, w, eps, *, rows_per_cta, scheduling)` —
  raises on out-of-contract inputs instead of falling back.
