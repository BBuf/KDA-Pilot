# Interface: h200_diffusion_norm_infer__multi_shape

- Kernel slug: `h200_diffusion_norm_infer__multi_shape`
- Op type: `layer_or_rms_norm_infer`
- Target GPU: NVIDIA H200 (Hopper / SM90, capability 9.0)
- Wrapped SGLang entry points:
  - `sglang.jit_kernel.diffusion.triton.norm:norm_infer`
  - `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm`

## Recovered Baseline Contract

Recovered by reading the SGLang source on the remote H200 box (bind-mounted repo
`/home/sglang-omni/bbuf/repos/sglang`).

- Pinned SGLang commit: `c47f0e7cdde48ddc718e3c6ee8bc87bebee2e8ff` (`c47f0e7cd`, 2026-05-26).
- Source files:
  - `python/sglang/jit_kernel/diffusion/triton/norm.py` (`norm_infer`, Triton `_norm_infer_kernel`).
  - `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` (`triton_one_pass_rms_norm`, Triton `_rms_norm_tiled_onepass`).
- Both are pure-forward, inference-only, return a NEW tensor (out-of-place), call `.contiguous()` on `x` internally, and produce output with the SAME dtype as the input. Neither mutates its input in place. FP32 accumulation is used for the reductions; the output is cast to the input dtype on store.

### `norm_infer`

```python
def norm_infer(
    x: Tensor,                       # 2-D [M, N]; reductions over the last dim N
    weight: Optional[Tensor],        # shape (N,), stride(-1)==1; None allowed
    bias: Optional[Tensor],          # shape (N,), stride(-1)==1; None allowed
    eps: float,                      # positional, required
    is_rms_norm: bool = False,       # False => LayerNorm, True => RMSNorm
    out: Optional[Tensor] = None,    # if None -> torch.empty_like(x); returned
) -> Tensor                          # returns `out` (new tensor unless `out` given)
```

- Semantics (per row, all math in FP32):
  - LayerNorm (`is_rms_norm=False`): `mean = mean(x)`, `var = mean((x-mean)**2)` (BIASED, divide by N), `rstd = 1/sqrt(var+eps)`, `x_hat = (x-mean)*rstd`.
  - RMSNorm (`is_rms_norm=True`): `var = mean(x**2)`, `rstd = 1/sqrt(var+eps)`, `x_hat = x*rstd`.
  - Apply affine: `y = x_hat * weight` if weight else `x_hat`; then `y += bias` if bias. Masked weight load uses `other=1.0`, masked bias uses `other=0.0`.
- Output dtype = `x.dtype`. Grid is one Triton program per row; `BLOCK_N = next_pow2(N)` (must be < 64 KB / elem size), the whole row is loaded once.
- Captured signature (helios): `x=[8640,5120] float32`, `weight=[5120] float32`, `bias=[5120] float32`, `eps=1e-6`, `is_rms_norm=False`. LayerNorm with weight+bias, FP32.

### `triton_one_pass_rms_norm`

```python
def triton_one_pass_rms_norm(
    x: torch.Tensor,                 # reshaped internally to [-1, last_dim] = [S, D]
    w: torch.Tensor,                 # shape (D,) (= last dim); weight only, NO bias
    eps: float = 1e-6,
) -> torch.Tensor                    # new tensor, same dtype/shape as x (out-of-place)
```

- Semantics (per row, FP32 accumulation): `ms = mean(x**2)` over `D`, `rstd = rsqrt(ms + eps)`, `y = x * rstd * w`. No bias, no mean-subtraction (pure RMSNorm).
- Reshapes `x` to 2-D `[S, D]` where `D = x.shape[-1]`. Tiled kernel: `BLOCK_SIZE_DIM = next_pow2(D)`, `BLOCK_SIZE_SEQ = min(16, next_pow2(max(1, S//512)))`, grid `= cdiv(S, BLOCK_SIZE_SEQ)`.
- Output dtype = `x.dtype`.
- Captured signatures (hunyuanvideo, zimage): `x=[M,128] bfloat16`, `w=[128] bfloat16`, `eps=1e-6`, with `M in {1320, 4096, 16384, 648720, 650040}`. All `D = 128`.

### Captured production signatures (the ONLY signatures the CUDA fast path intercepts)

| Function | dtype | x shape | weight/bias | eps | is_rms_norm |
|---|---|---|---|---|---|
| `norm_infer` | float32 | `[8640, 5120]` | weight `[5120]`, bias `[5120]` | 1e-6 | False |
| `triton_one_pass_rms_norm` | bfloat16 | `[648720, 128]` | weight `[128]` | 1e-6 | n/a |
| `triton_one_pass_rms_norm` | bfloat16 | `[1320, 128]` | weight `[128]` | 1e-6 | n/a |
| `triton_one_pass_rms_norm` | bfloat16 | `[650040, 128]` | weight `[128]` | 1e-6 | n/a |
| `triton_one_pass_rms_norm` | bfloat16 | `[16384, 128]` | weight `[128]` | 1e-6 | n/a |
| `triton_one_pass_rms_norm` | bfloat16 | `[4096, 128]` | weight `[128]` | 1e-6 | n/a |

### Fallback policy (to be enforced by `src/register.py` wrapper)

`optimized_wrapper` must preserve each recovered callsite contract above and fall
back to the SGLang baseline for any input that is not an exact captured signature:
different shape, dtype, device (non-CUDA / non-H200), non-contiguous layout,
base-pointer misalignment (for 128-bit vectorized loads), `is_rms_norm` mismatch,
or missing/extra optional tensors. The CUDA fast path intercepts ONLY the captured
signatures (the repo's rotary/qknorm precedent).

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

# Read by scripts/export_kda_kernels/export.py (keys drive promotion):
EXPORTS = {
    "norm_infer": norm_infer,
    "triton_one_pass_rms_norm": triton_one_pass_rms_norm,
}
```

`optimized_wrapper` must preserve the recovered SGLang callsite contract for every
wrapped entry point. It must fall back to the baseline implementation for any
shape, dtype, layout, device, normalization type, or feature flag that is not part
of the configured (captured) shape table.

## Evidence Requirements (filled at promotion — round 0)

### Final wrapper signatures (src/register.py -> src/wrapper.py)
- `norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None) -> Tensor` (out-of-place; preserves baseline).
- `triton_one_pass_rms_norm(x, w, eps=1e-6) -> Tensor` (out-of-place; preserves baseline).
- `EXPORTS = {"norm_infer": ..., "triton_one_pass_rms_norm": ...}` (both promoted).

### Per-shape dispatch table (CUDA fast path vs fallback)
| Signature | Kernel | Path |
|---|---|---|
| `norm_infer` LayerNorm, fp32, `[8640,5120]`, weight+bias `[5120]`, eps=1e-6, is_rms_norm=False | `layer_norm_fp32` (1 CTA/row, 256 thr, 5 float4/thr, registers, 1/sqrtf) | CUDA |
| `triton_one_pass_rms_norm`, bf16, `[M,128]`, w `[128]`, eps=1e-6, M∈{1320,4096,16384,648720,650040} | `rms_norm_bf16_n128` (16 lanes/row, 2 rows/warp, uint4, FP32 accum, rsqrtf) | CUDA |
| anything else (other M/N/dtype/eps, non-contiguous, unaligned, non-H200 (cap≠9.0), CPU, is_rms_norm=True for norm_infer, missing weight/bias, `out` given) | — | fallback to SGLang baseline |

Dispatch is enforced by `supported_norm_infer` / `supported_rms` in `src/wrapper.py`
and recorded by `last_dispatch()` (tests assert the CUDA path actually ran).

### Tolerance methodology (tests/test_correctness.py)
- Oracle: the SGLang baseline (pinned `c47f0e7cd`). High-precision reference: FP64 torch.
- Dynamic bound: `err(candidate) <= tol_mult * err(baseline) + tol_abs`, where `err(t)=max|t.double()-fp64_ref|`. `tol_mult` 3 (bf16) / 4 (fp32); `tol_abs` ≈ 1 bf16 ULP / 2e-6 fp32.
- fp32 hard ceiling: `err(candidate) <= 1e-5` for ALL fp32 LayerNorm cases including adversarial (near-constant / tiny-variance). The kernel computes mean/variance/normalize in double internally, so it meets 1e-5 even on ill-conditioned rows where the fp32-accumulating baseline does not.
- NaN/Inf checks; shape/dtype/device preserved. Result: 33/33 pass; RMS bf16 bitwise-identical to baseline; fp32 LN err 2.26e-6.

### Benchmark command and latency formula
```
KDA_RUN_CORRECTNESS=1 CUDA_VISIBLE_DEVICES=<idle> \
  PYTHONPATH=<sglang>/python:tests KDA_HOST=<host> KDA_GPU_ID=<idle> KDA_COMMIT=<hash> \
  python benchmark.py
```
Latency = per-call median of (`perf_counter` delta with `cudaDeviceSynchronize`), warmup 25 / iters 100, inputs built once, CUDA extension warm-built (JIT excluded). Speedup = baseline_median / candidate_median; final claim = geometric mean of per-shape speedups.

### Results (round 5, commit `6aaec1397`; ion-h200-8, GPU 7, NVIDIA H200; idle_before util 0% / mem 100 MiB / procs 0 AND idle_after util 0% / mem 717 MiB / procs 1 — both validated clean by benchmark.py, which aborts without writing on a busy/unavailable snapshot)
- Per-shape median speedup: helios LN 1.014×; RMS 648720 1.098×; RMS 650040 1.100×; RMS 1320 2.124×; RMS 16384 2.101×; RMS 4096 2.103×.
- **Geomean (all 6 captured shapes): 1.502×.** No per-shape regression. (Rounds 4-5 added a multi-GPU `CUDAGuard` and registry-callable routing — both benchmark-inert; the kernels are byte-identical, so per-shape numbers shift only by run-to-run variance, ~1.49-1.54×.)
- NCU active bound: huge-M RMS DRAM 75.7% peak (~3.6 TB/s); fp32 LN (double) mixed memory/compute (DRAM 62.7% / SM 56.7%); tiny-M RMS launch-bound (0.08 waves). The fp32 LN uses double-precision internal math to meet the strict 1e-5 ceiling on adversarial rows (round-0 fp32-fast was 1.119× but failed adversarial 1e-5). See `profile/ncu_round0/REPORT.md` (+ `analysis/metrics.md`, source-counter reports), `benchmark.csv`, `solutions.jsonl`.

### Source lineage
- SGLang baseline `norm.py` + `rmsnorm_onepass.py` @ `c47f0e7cd` (semantics, biased variance, FP32 accumulation, weight/bias handling).
- `kda_kernels/diffusion/rotary_embedding/_impls/b200/wrapper.py` (JIT-build + strict dispatch gate + import-time baseline binding + dispatch-path recorder pattern).
- Direction ranking: Codex gpt-5.5:high consult; KernelWiki `patterns/memory-bound.md`, `techniques/vectorized-loads.md`.
