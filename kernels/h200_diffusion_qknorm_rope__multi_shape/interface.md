# Interface: h200_diffusion_qknorm_rope__multi_shape

- Kernel slug: `h200_diffusion_qknorm_rope__multi_shape`
- Op type: `qknorm_rope_inplace`
- Target GPU: NVIDIA H200 (SM90, Hopper)
- Wrapped SGLang entry point: `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope`

## Final wrapper signature (recovered, exact)

```python
def fused_inplace_qknorm_rope(
    q: torch.Tensor,            # [num_tokens, num_heads, head_dim] bf16, contiguous (mutated in place)
    k: torch.Tensor,            # [num_tokens, num_heads, head_dim] bf16, contiguous (mutated in place)
    q_weight: torch.Tensor,     # [head_dim] bf16
    k_weight: torch.Tensor,     # [head_dim] bf16
    cos_sin_cache: torch.Tensor,# [rows, rope_dim] float32 contiguous; cos=[:, :rope_dim/2], sin=[:, rope_dim/2:]
    positions: torch.Tensor,    # [num_tokens] int32 or int64
    *, is_neox: bool, eps: float = 1e-6, head_dim: int = 0, rope_dim: int = 0,
) -> None  # in place; returns None
```

`src/register.py` exposes `KERNEL_SLUG`, `OP_TYPE`, `optimized_wrapper`, `register()`, and
`EXPORTS = {"fused_inplace_qknorm_rope": optimized_wrapper}` (read by the export tool).
The runtime impl is in `src/wrapper.py`; the native kernel is `src/csrc/qknorm_rope_kernel.cu`.

## Dispatch table

| Signature | Path | Kernel |
|---|---|---|
| bf16, head_dim=128, rope_dim=128, is_neox=False, equal Q/K heads, contiguous, 16-byte-aligned, non-aliasing q/k, int32/int64 positions | native CUDA (`"cuda"`) | `fused_qknorm_rope` — 2-heads-per-warp (16 lanes/head, 8 bf16/lane, `float4`), fp32 RMSNorm warp reduce, interleaved (GPT-J) RoPE, occupancy-based grid-stride |
| unsupported but CUDA-safe layout: is_neox=True, head_dim/rope_dim outside the fast path (bf16, contiguous, 16-byte-aligned, non-aliased, same CUDA device, int32/int64 positions) | `"fallback"` -> SGLang baseline | SGLang `fused_inplace_qknorm_rope` (bound at import; recursion-safe) |
| anything the CUDA baseline cannot run: CPU, device-mismatched q/k, non-contiguous, 16-byte-misaligned, aliased q/k, fp16, non-int32/64 positions | `"fallback"` -> PyTorch reference | `_reference_qknorm_rope` — portable fp32 RMSNorm + RoPE in place, processed per output-tensor device |
| double-install (bound baseline resolves back into a KDA wrapper/dispatcher) | raises `RuntimeError` | recursion guard `_is_recursive_baseline` (identity + `kda_kernels.diffusion.qknorm_rope` module) |

A single universal 2-head kernel covers the whole captured regime; the 1-head variant
(`fused_qknorm_rope_1head`, A/B benchmarking only) is 1.20–1.22× slower on large shapes
and ties on tiny, so no per-bucket dispatch is used. See `docs/dispatch.md`.

## Fallback cases (two routes, both recorded as `"fallback"`)

Any signature outside the fast-path domain routes to one of two safe fallbacks (never raises
for a well-formed call):

- **SGLang CUDA baseline** — when the input is still a layout the baseline can safely run
  (bf16, contiguous, 16-byte-aligned, non-aliased q/k, same CUDA device, int32/int64 positions)
  but outside the fast-path shape/flag domain: `is_neox=True`, `head_dim != 128`,
  `rope_dim != 128`, unequal Q/K head counts.
- **PyTorch in-place reference** (`_reference_qknorm_rope`) — for anything the CUDA baseline
  cannot run without raising/crashing: CPU tensors, device-mismatched q/k (each output is
  computed on its own device), non-contiguous q/k/weights/cache, 16-byte-misaligned base
  pointers (the baseline issues vectorized loads and would async-crash), overlapping/aliased
  q and k, non-bf16 (e.g. fp16) q/k, non-float32 / non-2-D cos_sin_cache, position dtype not
  in {int32, int64}. The reference matches the oracle math (fp32 RMSNorm + interleaved/neox
  RoPE).

A **double-install** where the bound baseline resolves back into a KDA wrapper/dispatcher is
detected (`_is_recursive_baseline`) and raises a clear `RuntimeError` rather than recursing.
`last_dispatch_path()` records `"cuda"` or `"fallback"` for the most recent call (tests assert it).

Scope note: these two fallback routes + the recursion guard live in the **wrapper**
(`optimized_wrapper` / the promoted `_impls/h200/wrapper.py`); the post-export smoke exercises
them by calling that wrapper directly. The installed `kda_kernels` **dispatcher** selects an arch
by CUDA capability, so an all-CPU call (no CUDA tensor) routes straight to the SGLang baseline by
design (CPU is not a promoted-arch path) — it does not pass through the H200 wrapper's CPU
reference. The wrapper-level CPU reference is what the AC-2/AC-3 negative tests and the smoke
validate.

## Tolerance methodology

Oracle (matches SGLang's `test_qknorm_rope.py`): `sglang.jit_kernel.norm.fused_inplace_qknorm`
then `flashinfer.rope.apply_rope_with_cos_sin_cache_inplace`. Correctness compares the
MUTATED q,k against the oracle with `torch.testing.assert_close(atol=8e-2, rtol=1e-2)` plus
NaN/Inf checks; observed `max_abs_err ≤ 0.0625` (≈ one bf16 quantum) on all captured shapes.
Math: fp32 RMS accumulation + fp32 RoPE arithmetic + bf16 writeback.

## Benchmark command and latency formula

Exact command (GPU 7 = the idle card; `run_bench.sh` records `nvidia-smi` before/after into
`profile/round0_ncu/gpu_state.md` and then invokes `benchmark.py`, which stamps this same
command into every `benchmark.csv` row):

```bash
ssh ion8-h200 'docker exec sglang_omni_bbuf_kda env CUDA_VISIBLE_DEVICES=7 KDA_HOST=ion8-h200 KDA_GPU_ID=7 KDA_CONTAINER=sglang_omni_bbuf_kda KDA_REMOTE_WORKDIR=/home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/round0-20260601-145601/cand PYTHONPATH=/home/sglang-omni/bbuf/repos/sglang/python bash -lc "cd /home/sglang-omni/bbuf/kda_runs/h200_diffusion_qknorm_rope__multi_shape/round0-20260601-145601/cand && bash profile/round0_ncu/run_bench.sh"'
```

Per shape: pristine q,k restored (`copy_`) before each timed sample; CUDA-event median over
200 iters (30 warmup, build excluded). speedup = baseline_median_us / candidate_median_us.
Headline = geometric mean of per-shape speedups. Result: **geomean ~1.11× over the SGLang
baseline** across the 9 captured shapes — run-to-run ~1.09–1.13 (3 committed idle-GPU runs:
1.0965 / 1.1258 / 1.0883). The all-9 geomean is noisy because the launch-bound tiny shapes
(T≤195, ~1.0–1.1×) dominate it; the large shapes (≥4096 tokens) are stable at ~1.14–1.16×.
This is the end-to-end speedup through the wrapper safety gate. Every `benchmark.csv` row
records the exact `run_bench.sh` command; per-run GPU-7 before/after idleness is in
`profile/round0_ncu/gpu_state.md`.

## Source lineage

- Kernel ported from the promoted sibling B200 impl
  `kda_kernels/diffusion/qknorm_rope/_impls/b200/csrc/qknorm_rope_kernel.cu` (geomean 1.1113×
  on B200); SM-agnostic, rebuilt for sm_90 with `-O3 --use_fast_math -lineinfo` (auto-detected
  arch). Wrapper/gate/telemetry/fallback patterns from `_impls/b200/wrapper.py`.
- Evidence: `benchmark.csv`, `solutions.jsonl`, `profile/round0_ncu/REPORT.md`,
  `docs/perf_analysis.md`, `docs/dispatch.md`. Active bound: memory-latency on large shapes
  (near-bound), launch/underfill on tiny.
