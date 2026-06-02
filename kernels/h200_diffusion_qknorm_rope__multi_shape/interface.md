# Interface: h200_diffusion_qknorm_rope__multi_shape

- Kernel slug: `h200_diffusion_qknorm_rope__multi_shape`
- Op type: `qknorm_rope_inplace`
- Target GPU: NVIDIA H200 (Hopper, sm_90)
- Wrapped SGLang entry point: `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope`

## Recovered Baseline Contract

### Public callable (must be preserved)
```python
fused_inplace_qknorm_rope(
    q, k, q_weight, k_weight, cos_sin_cache, positions,
    *, is_neox: bool, eps: float = 1e-6, head_dim: int = 0, rope_dim: int = 0,
) -> None
```
- In place on `q` and `k`; returns `None`. `q_weight`, `k_weight`, `cos_sin_cache`, `positions` are read-only.
- `q`, `k`: `[num_tokens, num_heads, head_dim]` bf16, contiguous (innermost stride 1).
- `q_weight`, `k_weight`: `[head_dim]` bf16. `cos_sin_cache`: `[num_rows, rope_dim]` float32. `positions`: `[num_tokens]` int32 or int64.
- `head_dim` defaults to `q.size(-1)`; `rope_dim` defaults to `cos_sin_cache.size(-1)`.
- Upstream builds the kernel via `load_jit("qknorm_rope", *make_cpp_args(head_dim, rope_dim, is_neox, is_arch_support_pdl(), dtype), cuda_files=["diffusion/qknorm_rope.cuh"], cuda_wrappers=[("qknorm_rope", "QKNormRopeKernel<...>::run")])` and calls `module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)` (eps is the last positional arg; is_neox/head_dim/rope_dim/pdl/dtype are template args). Upstream itself does NOT fall back — the caller owns the gate + fallback.

### Support gate (`can_use_fused_inplace_qknorm_rope(head_dim, rope_dim, is_neox, dtype)`)
- `head_dim in {64, 128, 256}`
- `0 < rope_dim <= head_dim`
- `rope_dim % (head_dim // 32) == 0`
- if `is_neox`: `rotary_lanes = rope_dim // (head_dim // 32)` must be `>= 2` and a power of two
- plus a successful JIT compile of the module

### Correctness oracle (split baseline)
On cloned inputs, per shape (pass the shape's eps to BOTH stages):
```python
from sglang.jit_kernel.norm import fused_inplace_qknorm
from flashinfer.rope import apply_rope_with_cos_sin_cache_inplace
fused_inplace_qknorm(q, k, q_weight, k_weight, eps)        # RMS-norm per (token, head), in place
apply_rope_with_cos_sin_cache_inplace(
    positions=positions.long(), query=q.view(N, -1), key=k.view(N, -1),
    head_size=head_dim, cos_sin_cache=cos_sin_cache, is_neox=is_neox)
```
- Tolerance: `ATOL=8e-2, RTOL=1e-2` (BF16; the split path differs from the fused path by ~1 BF16 rounding step).
- The upstream test only exercises `eps=1e-6`; the **zimage** shapes use `eps=1e-5`, so the harness must pass per-shape eps.

### `cos_sin_cache` convention
```python
inv_freq = 1.0 / (10000.0 ** (arange(0, rope_dim, 2).float() / rope_dim))   # length rope_dim/2
freqs    = outer(arange(num_rows).float(), inv_freq)                        # [num_rows, rope_dim/2]
cos_sin_cache = cat([freqs.cos(), freqs.sin()], dim=-1)                      # [num_rows, rope_dim]
```
Row `p`: first `rope_dim/2` are cos, last `rope_dim/2` are sin. RoPE rotates only `[..., :rope_dim]`; lanes `[rope_dim, head_dim)` keep the normalized value. The captured shapes size `cos_sin_cache` to `[num_tokens, 128]`, so positions live in `[0, num_tokens)`; do NOT assume `positions[i] == i` (test shuffled/repeat/zero too).

## PyTorch FP32 Semantic Reference (oracle cross-check + CPU/fp16/fallback)
Validated math (device/dtype/layout-agnostic; FP32 compute then cast to input dtype, with an intermediate cast after QK-norm to mirror the split oracle's BF16 rounding):
- RMS-norm: `var = x.float().square().sum(-1, keepdim=True) / head_dim; out = x.float() * rsqrt(var + eps) * weight.float()`; cast to dtype.
- RoPE: `cos = row[:rope_dim/2]`, `sin = row[rope_dim/2:]`.
  - `is_neox=False` (GPT-J/interleaved): pairs `(x[2i], x[2i+1])` → `(x0*cos - x1*sin, x1*cos + x0*sin)`.
  - `is_neox=True` (rotate-half): pairs `(x[i], x[i+rope_dim/2])` → `(x0*cos - x1*sin, x1*cos + x0*sin)`.

## Fallback Policy (DEC-3)
`optimized_wrapper` dispatches:
- **Supported** (CUDA, bf16, contiguous, 16-byte aligned, non-aliased q/k, head_dim/rope_dim/is_neox/pos-dtype within the gate) → the candidate native-CUDA jit_kernel module. Dispatch tag `"cuda"`.
- **Unsupported** (CPU, fp16, non-contiguous, misaligned, aliased q/k, out-of-gate head_dim/rope_dim/is_neox, unsupported position dtype) → the PyTorch FP32 semantic reference, in place. Dispatch tag `"fallback"`. Never raises **except** a double-install / re-entrancy guard (raises a clear `RuntimeError`).

## Benchmark Methodology (DEC-4)
- Two levels, applied identically to baseline and candidate:
  - **wrapper** (primary): end-to-end `optimized_wrapper` / SGLang public callable.
  - **module**: direct tvm-ffi `module.qknorm_rope(...)` call.
- Interleave baseline/candidate on the SAME idle H200; reset q/k from pristine copies BEFORE each timed call, OUTSIDE the timed region; exclude first-call JIT compile / cache warmup (warm each path separately).
- Report per shape: median, mean, std, min, p10, p90. Headline = geomean of per-shape median-latency speedups across all 9 shapes (AC-8). Record host, GPU id, GPU model, and before/after idle state per row (AC-7).

## Workload (9 captured shapes; verbatim — see `docs/captured_shapes_h200.jsonl`)
All bf16, is_neox=False, head_dim=128, rope_dim=128, `q=k=[tokens, heads, 128]`, `cos_sin_cache=[tokens, 128]` f32, `positions=[tokens]` int64.
- qwen (eps=1e-6): tokens ∈ {4096, 19, 47}, heads=24
- qwen-edit (eps=1e-6): tokens ∈ {8424, 195, 189}, heads=24
- zimage (eps=1e-5): tokens ∈ {4096, 32, 4128}, heads=30

## Build Policy
- Build via SGLang `load_jit` / `make_cpp_args` / `cache_once` over a task-owned `.cu`/`.cuh` (under `src/csrc/`), referenced through `cuda_files` + `extra_include_paths`. NO `torch.utils.cpp_extension`, NO `EXPORTS`, NO `--use_fast_math`. Compile flags match the diffusion baseline (`-std=c++20 -O3 --expt-relaxed-constexpr` + arch). PDL only as a measured variant.

## Evidence (final, ion8-h200 GPU7, sglang c47f0e7cd, bf16)
- **Wrapper signature**: `optimized_wrapper(q, k, q_weight, k_weight, cos_sin_cache, positions, *, is_neox, eps=1e-6, head_dim=0, rope_dim=0) -> None` (preserves the SGLang callsite; in place on q,k).
- **Dispatch table**: head_dim=128 & **rope_dim=128** & !is_neox → `fused_qknorm_rope_warp2` (2-heads-per-warp float4, `static_assert(kRopeDim==128)`); everything else — incl. **head_dim=128 rope_dim=64**, head_dim∈{64,256}, is_neox — → baseline `fused_qknorm_rope_warp` (rope_dim-aware); unsupported / malformed (CPU/fp16/non-contig/misaligned/aliased/wrong-weight-shape/out-of-gate) → PyTorch FP32 semantic fallback (never raises except double-install guard). See `docs/dispatch.md`.
- **Correctness**: 73 captured-shape tests + 144 regression-grid tests pass vs the split SGLang oracle (`fused_inplace_qknorm` + FlashInfer RoPE), ATOL=8e-2/RTOL=1e-2; FP32 reference cross-checked vs the GPU oracle (both neox); no NaN/Inf.
- **Benchmark** (d3-final; dual-level, CUDA-event timing, q/k reset outside the timed region, JIT excluded, iters=300, GPU7 external idle util=0% mem=70MiB before+after): all-9 geomean **wrapper 1.0723× / module 1.0268×** (src `4f70cda745940c96`). Latency formula: per-shape median over `iters`; speedup = baseline_median / candidate_median; headline = geomean of per-shape speedups across all 9 shapes. Command (recorded per row in `benchmark.csv`): `CUDA_VISIBLE_DEVICES=7 KDA_TAG=d3-final KDA_ITERS=300 PYTHONPATH=<repos/sglang>/python python bench_remote.py`. (Round-0 d2 measured 1.0992×/1.0285× with an lru_cache wrapper — superseded.)
- **Bound** (`profile/round_warp2/REPORT.md`, `docs/perf_analysis.md`): large shapes memory-latency-bound (long-scoreboard 58%, DRAM 40% of peak, occ 73%) near attainable bound; tiny shapes launch/underfill-bound (occ 12%) → kernel no-go, carried by lean dispatch.
- **Source lineage** (`solutions.jsonl`): d0 baseline clone of sglang qknorm_rope.cuh @ c47f0e7cd → d1 lean dispatch → d2 2-head float4 (history/superseded; Codex D1 design) → **d3-final-corrected** (the FINAL candidate, src `4f70cda745940c96`: warp2 rope_dim==128 gate + cache_once + weight gate) → **export-real-in-sglang** (the AC-13 real in-tree placement + replacement test).

## Source Lineage (recovered from local SGLang checkout)
- `sglang/jit_kernel/diffusion/qknorm_rope.py` — wrapper, gate, jit module.
- `sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` — baseline kernel (`QKNormRopeKernel<...>::run`); 256 thr/CTA, 8 warps, one warp per (token,head), grid-stride over `(q_heads+k_heads)*tokens`, 128-bit vectorized, FP32 RMS accum.
- `sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py` — oracle + regression grid + tolerances.
- `sglang/jit_kernel/norm.py` — `fused_inplace_qknorm(q,k,q_weight,k_weight,eps=1e-6,*,head_dim=0)`.
- `sglang/jit_kernel/benchmark/diffusion/bench_qknorm_rope.py` — benchmark reference (note: reuses q/k across iters; we reset outside the timed region).
- `sglang/jit_kernel/csrc/elementwise/rmsnorm.cuh` + `norm.py` — sibling `Kernel<...>::run` + `load_jit` + `TensorMatcher`/`SymbolicSize`/`LaunchKernel` + PDL template pattern.
