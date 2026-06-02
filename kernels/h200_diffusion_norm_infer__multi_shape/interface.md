# Interface: h200_diffusion_norm_infer__multi_shape

- Kernel slug: `h200_diffusion_norm_infer__multi_shape`
- Op type: `layer_or_rms_norm_infer`
- Target GPU: NVIDIA H200
- Wrapped SGLang entry points:
- `sglang.jit_kernel.diffusion.triton.norm:norm_infer`
- `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm`

## Export

Provide:

```text
src/register.py
```

with:

```python
KERNEL_SLUG = "h200_diffusion_norm_infer__multi_shape"
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

`optimized_wrapper` must preserve the recovered SGLang callsite contract
for every wrapped entry point. It must fall back to the baseline
implementation for any shape, dtype, layout, device, normalization type,
or feature flag that is not part of the configured shape table.

## Recovered Baseline Contract

Recovered from the SGLang checkout at
`/Users/bbuf/工作目录/Common/sglang` (read-only reference):

- `python/sglang/jit_kernel/diffusion/triton/norm.py` -> `norm_infer`
- `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` -> `triton_one_pass_rms_norm`

### `norm_infer`

```python
def norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None) -> Tensor
```

- Positional: `x` (2D `[M, N]`), `weight` (`[N]` or `None`), `bias` (`[N]` or `None`), `eps` (float).
- `is_rms_norm` and `out` are keyword-or-positional; the helios capture passes
  `eps=1e-6, is_rms_norm=False` as keywords.
- Behavior (one program per row, all math in fp32, output cast to `x.dtype`):
  - LayerNorm (`is_rms_norm=False`): `mean = sum(x)/N`, `var = sum((x-mean)^2)/N`,
    `rstd = 1/sqrt(var+eps)`, `y = (x-mean)*rstd`.
  - RMSNorm (`is_rms_norm=True`): `var = sum(x^2)/N`, `rstd = 1/sqrt(var+eps)`,
    `y = x*rstd`.
  - Then `y = y*weight` if `weight is not None`, `y += bias` if `bias is not None`
    (weight defaults to 1.0, bias to 0.0 when absent).
- Asserts: `weight.shape == (N,)` and `weight.stride(-1) == 1` (same for `bias`);
  `x` is made contiguous internally (`x = x.contiguous()`); `out` defaults to
  `empty_like(x)`; raises `RuntimeError` if `N * x.element_size() >= 64 KiB`.
- Returns the output tensor (same shape/dtype as `x`).
- helios target: `x=[8640,5120] fp32`, `weight=[5120] fp32`, `bias=[5120] fp32`,
  `eps=1e-6`, `is_rms_norm=False`.

### `triton_one_pass_rms_norm`

```python
def triton_one_pass_rms_norm(x, w, eps=1e-6) -> Tensor
```

- Positional: `x` (last dim `D`), `w` (`[D]`), `eps` (float, 3rd positional; the
  captures pass `eps` positionally as `arg2=1e-6`).
- RMSNorm only, **no bias**: reshape to `[S, D]`, `mean_square = sum(x^2)/D`,
  `rstd = rsqrt(mean_square+eps)`, `y = x*rstd*w`; math in fp32, output cast to
  `x.dtype`. `x` is made contiguous internally; returns `y` (same shape/dtype).
- RMS targets: `x in {[648720,128],[1320,128],[650040,128],[16384,128],[4096,128]}`
  bf16, `w=[128] bf16`, `eps=1e-6`.

## Dispatch + Fallback Set

The dispatcher preserves both public names and routes only the exact captured
buckets to the native-CUDA specializations; everything else falls back to the
SGLang baseline:

- `norm_infer` -> LayerNorm-fp32 specialization only when: CUDA tensor, dtype
  `float32`, `is_rms_norm=False`, `out is None`, fully contiguous (`x.is_contiguous()`),
  `N == 5120`, weight and bias both present and shape `(N,)` and contiguous.
  Otherwise fall back to baseline.
- `triton_one_pass_rms_norm` -> RMSNorm-bf16 specialization only when: CUDA
  tensor, dtype `bfloat16`, fully contiguous (`x.is_contiguous()`), `D == 128`,
  `w` shape `(D,)` and contiguous. Otherwise fall back to baseline.
- Full `x.is_contiguous()` (not merely a contiguous last dim) is required so the
  internal `reshape(-1, D)` and the fresh `empty_like(x)` output are kernel-writable
  views; any non-contiguous layout (e.g. a transposed higher-rank tensor with a
  contiguous last dim) falls back.
- Always fall back for: CPU/MPS/non-CUDA device, any non-contiguous layout,
  unsupported dtype (incl. fp16 RMS), `is_rms_norm=True` on `norm_infer`, `out`
  provided, `N != 5120` / `D != 128`, missing weight/bias for the specialization.
  Fallback output must equal the baseline output exactly (same call delegated to
  the SGLang baseline).

## Evidence (normv5 — promoted)

- **Wrapper signatures (preserved):** `triton_one_pass_rms_norm(x, w, eps=1e-6) -> Tensor`
  and `norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None) -> Tensor`
  (`src/norm_dispatch.py`, re-exported via `src/register.py`).
- **Dispatch table + per-bucket promote/no-go:** see `docs/dispatch.md`. RMS **bf16-only**
  D=128 → `rms_norm_warp<128,false,bf16_t>` (`src/rms_norm_d128.cuh`, 2-rows-per-warp
  128-bit); LN fp32 N=5120 +weight+bias → `layer_norm_block<5120,true,false,float>`
  (`src/layer_norm_n5120.cuh`, one-CTA-per-row exact tiling).
- **Fallback:** any other dtype (incl. fp16 RMS) / N / D / device / non-contiguous layout /
  `is_rms_norm=True` on norm_infer / `out` provided / missing weight|bias → SGLang baseline
  (output verified == baseline; non-contiguous higher-rank fallback is regression-tested).
- **Tolerance methodology:** candidate vs SGLang baseline AND vs a PyTorch FP32 reference;
  fixed SGLang tolerances (fp32 1e-5, bf16/fp16 5e-2) + a dynamic guard
  (candidate-vs-fp32 error ≤ 4× baseline-vs-fp32 error); explicit NaN/Inf checks.
  Result: 201/201 cases (full regression grid incl. odd M, + select01 oracle); helios
  LN abs err 2.86e-6 (== baseline's own error vs fp32).
- **Benchmark command:** inside `sglang_bbuf` on an idle H200,
  `KDA_RUN_CORRECTNESS=1 CUDA_VISIBLE_DEVICES=<idle> python benchmark.py --lock` (once),
  then `... python benchmark.py --candidate-version <ver>`. Latency = median of warmup +
  repeated wall-clock samples (cuda-synced), timed region excludes JIT/setup/copy; per-shape
  speedup = baseline_median / candidate_median; final = geomean across the 6 shapes.
  Result: **geomean 1.4223x** (helios 1.067x; huge RMS 1.041/1.046x; small RMS 1.91-1.94x),
  ion8-h200 GPU7 (NVIDIA H200), sglang c47f0e7cd. Bound analysis: `profile/ncu_normv2/REPORT.md`.
- **Source lineage:** kernel structure (params struct, templated `Kernel<...>::run`,
  `TensorMatcher`/`SymbolicSize`, `LaunchKernel`, packed `cast<fp32x2_t>` vectorization,
  `warp::reduce_sum`) mirrors `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`;
  2-rows-per-warp 128-bit lever from KernelWiki (pytorch#150705, vllm#27931). No
  `torch.utils.cpp_extension`; no `--use_fast_math`.
- **Export / install (done):** promoted into the `kda_kernels` overlay via
  `scripts/export_kda_kernels/export.py` (`src/register.py` `EXPORTS` + `src/wrapper.py`);
  `kda_kernels.install(strict=True)` swaps both public SGLang symbols to the native-CUDA
  dispatcher; the `.cuh` compile via `load_jit` from `kda_kernels/.../_impls/h200/`. Installed-path
  correctness (6 shapes + select01 oracle + fallback) and smoke benchmark validated on ion8-h200
  GPU7. Full detail: `docs/sglang_jit_export.md`.
