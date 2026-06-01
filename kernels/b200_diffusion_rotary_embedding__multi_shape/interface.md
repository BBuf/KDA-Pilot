# Interface: b200_diffusion_rotary_embedding__multi_shape

- Kernel slug: `b200_diffusion_rotary_embedding__multi_shape`
- Op type: `rotary_embedding`
- Target GPU: NVIDIA B200 (SM100)
- Wrapped SGLang entry points:
  - `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`
  - `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb`

## Pinned baseline source (recovered Round 0)

- Remote: host `ion-b200` (`innomatrix-us-adc-smb200-0003`), Docker container `sglang_bbuf`, repo `/home/sglang-omni/bbuf/repos/sglang`.
- SGLang commit (authoritative for this task): `0b65588c180a519427867d53cc4ed6e9e2610890` (branch `main`, `git describe` = `gateway-v0.3.1-4340-g0b65588c1`, editable install version `0.5.12.dev472`).
- The three baseline files are **clean at HEAD** (the repo has 17 unrelated dirty files, none of them the RoPE sources or the test):
  - `python/sglang/jit_kernel/diffusion/triton/rotary.py`
  - `python/sglang/jit_kernel/diffusion/triton/ltx2_rotary.py`
  - `python/sglang/jit_kernel/tests/test_rope.py`

## Entry point 1 — `apply_rotary_embedding`

**Signature** (recovered): `apply_rotary_embedding(x, cos, sin, interleaved: bool = False) -> torch.Tensor`
- The 4th positional arg is **`interleaved`** (NOT `is_neox`). The captured production callsite passes `arg3 = False`.
- **Mutation contract: OUT-OF-PLACE.** Allocates `output = torch.empty_like(x)` and returns it; `x` is not modified.

**Tensor contract** (captured production signature — HunyuanVideo):
- `x`: `[1, 27030, 24, 128]` bf16, contiguous, layout `(B, S, H, D)` (also accepts 3D `(S, H, D)` → `bsz=1`). Strides `[83036160, 3072, 128, 1]`.
- `cos`, `sin`: `[27030, 64]` fp32, contiguous (`[num_tokens, head_size/2]`). Strides `[64, 1]`. **Token-shared across all heads** (indexed by token only; for `bsz>1` also shared across batch via `token_idx = bt_idx % num_tokens`).
- Returns: `[1, 27030, 24, 128]` bf16 (new tensor).

**Rotation semantics** (`_rotary_embedding_kernel`, Triton, autotuned over BLOCK_HEADS∈{1,2,4,8}/BLOCK_HS_HALF∈{32,64}):
- The kernel **always pairs ADJACENT elements** `(x[2i], x[2i+1])` for `i ∈ [0, head_size/2)` (GPT-J / "interleaved"-style rotation):
  - `o1 = x1*cos_i - x2*sin_i`  (computed `tl.fma(-x2, sin, x1*cos)`)
  - `o2 = x1*sin_i + x2*cos_i`  (computed `tl.fma(x1, sin, x2*cos)`)
  - Inputs cast to fp32, computed in fp32, stored back as `x.dtype` (bf16).
- The `interleaved` flag only controls cos/sin width interpretation in the Python wrapper:
  - `interleaved=True` AND `cos.shape[-1]==head_size` → `cos=cos[...,::2]; sin=sin[...,::2]` (downsample full-width cos/sin to half).
  - else → `cos=cos.contiguous(); sin=sin.contiguous()` (use as half-width).
  - Captured case (`interleaved=False`, `cos` width `64 = head_size/2`) → uses cos/sin directly; adjacent-pair rotation with `cos[token, i]`.
- Platform fallback: at import, `apply_rotary_embedding` is replaced by a native impl on NPU/MPS/CPU; on CUDA the Triton kernel above is used.

## Entry point 2 — `apply_ltx2_split_rotary_emb`

**Signature** (recovered): `apply_ltx2_split_rotary_emb(x, cos, sin) -> torch.Tensor` (no flags).
- **Mutation contract: OUT-OF-PLACE.** Allocates `out = torch.empty_like(x)` and returns it.

**Tensor contract** (captured production signatures — LTX-2):
- `x`: `[B, S, inner_dim]` bf16, contiguous (3D). `inner_dim = num_heads * head_dim`. Viewed internally as `[B, S, num_heads, head_dim]` contiguous (the kernel uses computed flat offsets, so x must be contiguous).
- `cos`, `sin`: `[B, num_heads, S, half_dim]` bf16, **non-contiguous** — stored `[B, S, H, half]`-contiguous, viewed `[B, H, S, half]` (e.g. shape `[1,32,1536,64]`, strides `[3145728, 64, 2048, 1]`). Innermost `half_dim` is contiguous (stride 1); the per-token `[H, half]` block is contiguous in memory. **Per-`(B, head, token)`** — NOT shared across heads.
- Derived: `num_heads = cos.shape[1]` (=32), `half_dim = cos.shape[3]`, `head_dim = 2*half_dim`. Captured: `head_dim ∈ {64,128}`, `half_dim ∈ {32,64}`, `B ∈ {1,2}`, `S ∈ {126,1536,6144,24576}`.
- **Exception behavior**: raises `ValueError` if `cos.shape[0]!=B`, `cos.shape[2]!=S`, `inner_dim != num_heads*head_dim`, or `sin.shape != cos.shape`.

**Rotation semantics** (`_ltx2_split_rotary_kernel`, Triton; grid `(B*S, cdiv(num_heads, block_heads))`, `block_heads=min(16,next_pow2(H))`, `block_half=next_pow2(half_dim)`):
- **Split-half rotation**: pairs `(x[i], x[i+half_dim])` for `i ∈ [0, half_dim)` (rotate-half / neox-style), per head:
  - `x_first = x[..., 0:half_dim]`, `x_second = x[..., half_dim:2*half_dim]`.
  - **Exact numeric order (must be matched by the CUDA candidate to bit-track the baseline):**
    - `out_first  = bf16(x_first  * cos) -> fp32  +  (-x_second(fp32) * sin(fp32))`
    - `out_second = bf16(x_second * cos) -> fp32  +  ( x_first(fp32)  * sin(fp32))`
    - i.e. the `x*cos` product is **rounded to bf16 first**, re-widened to fp32, then the sine term is added in fp32; the final result is stored as bf16. (Comment in source: "Match the original PyTorch order: x*cos written as BF16 first, then addcmul_ in FP32 before the final BF16 store.")
  - `cos`/`sin` indexed via explicit `(batch, head, token)` strides; innermost `half_dim` contiguous.

## CUDA fast-path support gates (to implement in `src/wrapper.py`)

Route to the native CUDA kernel ONLY for the **captured production signatures** (the fixed table); fall back to the SGLang Triton baseline for everything else (baselines bound at import for recursion safety). The kernels are mathematically correct for the broader signature class, but the guard is intentionally restricted to profiled/benchmarked shapes so a promoted wrapper never silently intercepts an unmeasured shape (plan fixed-shape contract).

- `_supported_standard(x, cos, sin, interleaved)`: `interleaved is False`; `x` CUDA bf16 contiguous, rank 3 `(S,H,D)` or rank 4 `(1,S,H,D)` (batch==1 if 4D); `(num_tokens, num_heads, head_dim) == (27030, 24, 128)`; `cos`/`sin` CUDA fp32 contiguous `(27030, 64)`; same device. Else → baseline.
- `_supported_ltx2(x, cos, sin)`: `x` CUDA bf16 contiguous 3D; `cos`/`sin` CUDA bf16 4D `(B,32,S,half)`, equal shapes, innermost stride 1, `(b,h,t)` strides multiples of 8; `num_heads==32`, `half ∈ {32,64}`, `(B,S,half)` in the 10 captured tuples; `inner_dim==32*2*half`; same device. Else → baseline.

## Correctness oracle methodology

- **Note (Round 0 finding):** `python/sglang/jit_kernel/tests/test_rope.py` tests a DIFFERENT function — `sglang.jit_kernel.rope.apply_rope_inplace` (LLM q/k RoPE with `cos_sin_cache`+`positions`+`is_neox`, in-place, FlashInfer `apply_rope_with_cos_sin_cache_inplace` oracle, tol 1e-2). It is the correctness-test **style** to adapt, not a direct oracle for the diffusion entry points here.
- **Primary oracle for BOTH diffusion functions**: the SGLang Triton baseline itself (same function, production numerics). The CUDA candidate must match it within a dynamic BF16-aware tolerance.
- **Cross-check**: a PyTorch FP32 reference implementing the exact rotation (adjacent-pair for standard `interleaved=False`; split-half with the bf16-rounding order for LTX-2).
- **Tolerance**: SGLang-style dynamic tolerance — candidate error vs FP32 reference must not exceed a small multiple of the baseline's own BF16 quantization error vs FP32; plus explicit NaN/Inf checks. Standard enumeration uses tol 1e-2 abs/rel (per test_rope.py).

## Export / registry contract

`src/register.py` must expose (read by `scripts/export_kda_kernels/export.py`, which already maps both `rotary_embedding` family swaps):

```python
KERNEL_SLUG = "b200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"

def optimized_wrapper(*args, **kwargs): ...   # registry callable (routes to apply_rotary_embedding)

def register() -> dict: ...                   # {name, op_type, callable, version, source}

EXPORTS = {
    "apply_rotary_embedding": apply_rotary_embedding,            # both keys; each independently
    "apply_ltx2_split_rotary_emb": apply_ltx2_split_rotary_emb,  # fallback-safe. Partial promotion OK.
}
```

`optimized_wrapper` and both exported functions preserve the recovered callsite contract (out-of-place return) and fall back to the SGLang baseline for any shape/dtype/layout/device/flag outside the captured table.

## Final result (RLCR Round 2)

- **Candidate**: `cuda-v1` (`src/csrc/rotary_embedding_kernel.cu`, kp_commit `fb7427793`). Final wrapper signatures: `apply_rotary_embedding(x, cos, sin, interleaved=False) -> Tensor` and `apply_ltx2_split_rotary_emb(x, cos, sin) -> Tensor` (both out-of-place).
- **Dispatch table**: `docs/dispatch.md` (per-bucket baseline/candidate/speedup/promote, matching the gates above).
- **Correctness**: candidate-vs-baseline 17/17 (LTX-2 bit-exact, standard within 1 ulp); pytest 7/7 (dispatch=cuda on captured only, fallback negatives, mutation, EXPORTS). Oracle = SGLang baseline + PyTorch FP32 cross-check; SGLang-style dynamic BF16-aware tolerance (`floor + k·bf16_quant_noise`).
- **Benchmark**: CUDA-event single-call timing, warmup excludes JIT/autotune, hard idle-gating (fail if non-idle before; settle util→0 after). `benchmark.csv` geomean **1.3676×** (standard 1.77×, LTX-2 1.06–1.54×) on idle B200 GPU3. Latency formula: median over 300 single-call CUDA-event samples per shape.
- **Active bound (AC-6)**: `profile/ncu-v1/REPORT.md` — LTX-2-large DRAM-bandwidth bound (85.7% SOL, near roofline); standard memory-leaning (60% SOL, headroom but wins 1.77×); LTX-2-small launch-bound.
- **Source lineage**: rotation semantics + numeric order ported from SGLang `rotary.py`/`ltx2_rotary.py` @ `0b65588c1`; wrapper/guard/`_LAST_DISPATCH`/EXPORTS pattern from the `b200_diffusion_qknorm_rope__multi_shape` sibling. No external (KernelWiki) PR ideas used.
- **Promotion**: see `kda_kernels/diffusion/rotary_embedding/` after `scripts/export_kda_kernels/export.py b200_diffusion_rotary_embedding__multi_shape` (both functions; install/uninstall/status + recursion-safe smoke verified).
