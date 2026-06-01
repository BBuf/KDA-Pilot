# Interface: b200_diffusion_qknorm_rope__multi_shape

- Kernel slug: `b200_diffusion_qknorm_rope__multi_shape`
- Op type: `qknorm_rope_inplace`
- Target GPU: NVIDIA B200 (SM100)
- Wrapped SGLang entry point:
  - `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope`

## Recovered Callsite Contract

```python
fused_inplace_qknorm_rope(
    q,                # [num_tokens, num_heads, head_dim], bf16, contiguous (mutated in place)
    k,                # [num_tokens, num_kv_heads, head_dim], bf16, contiguous (mutated in place)
    q_weight,         # [head_dim], bf16
    k_weight,         # [head_dim], bf16
    cos_sin_cache,    # [*, rope_dim], float32  (concat(cos, sin) halves)
    positions,        # [num_tokens], int32 or int64
    *,
    is_neox: bool,
    eps: float = 1e-6,
    head_dim: int = 0,   # defaults to q.size(-1)
    rope_dim: int = 0,   # defaults to cos_sin_cache.size(-1)
) -> None
```

- Semantics: per-head RMS normalization of `q`/`k` (sum-of-squares over `head_dim`,
  `rsqrt(mean + eps)`, multiply by `q_weight`/`k_weight`), then RoPE rotation using
  `cos_sin_cache[positions[token]]`. Writes back **in place**; returns `None`.
- Device kernel `QKNormRopeKernel<head_dim, rope_dim, is_neox, use_pdl, dtype>::run(...)`
  is templated; one warp processes one `(token, head)`; q and k are fused into a single
  launch over `(num_qo_heads + num_kv_heads) * num_tokens` work items.
- Support gate: `can_use_fused_inplace_qknorm_rope(head_dim, rope_dim, is_neox, dtype)`
  requires `head_dim ∈ {64,128,256}`, `0 < rope_dim ≤ head_dim`,
  `rope_dim % (head_dim // 32) == 0`, and (for `is_neox`) a power-of-two rotary-lane
  count `rope_dim // (head_dim // 32)`.
- On B200, `is_arch_support_pdl()` is true (SM ≥ 9), so the baseline is built with
  **PDL on**; a PDL-off candidate variant is therefore a legitimate A/B.

## Candidate Wrapper

```text
src/register.py
```

`optimized_wrapper(*args, **kwargs)` preserves the contract above. Currently it routes
to the SGLang baseline (correct-by-construction starting point + fallback target). The
specialized B200 kernel will be wired in behind a shape gate, falling back to the
baseline for any shape, dtype, layout, device, or feature flag it does not support.

`register()` returns `{name, op_type, callable, version, source}`.

## Correctness Methodology

- Oracle: SGLang split path — `sglang.jit_kernel.norm.fused_inplace_qknorm` (with the
  per-case `eps`) followed by `flashinfer.rope.apply_rope_with_cos_sin_cache_inplace`.
- Tolerance: `ATOL=8e-2, RTOL=1e-2` (matches `tests/diffusion/test_qknorm_rope.py`).
- Comparison is on the in-place-mutated `q`/`k` (inputs cloned per run via a seeded,
  deterministic generator so oracle and candidate see identical data); every validator
  runs NaN/Inf checks.
- Inputs follow the SGLang test/benchmark convention: `cos_sin_cache` is
  `[MAX_SEQ_LEN=131072, rope_dim]` and `positions` are randomized in
  `[0, MAX_SEQ_LEN)` (exercises arbitrary RoPE positions; immaterial cache-size
  difference from the captured `[num_tokens, rope_dim]`, consistent with SGLang's own
  harnesses).

## Benchmark Methodology

- `benchmark.py` on a verified-idle B200 inside `sglang_bbuf` via the `ion-b200` skill.
- CUDA-event timing (no CUDA graph); inputs built once per case; report
  median/mean/std/min/p10/p90 per shape; primary metric = equal-weight geomean of
  per-shape median-latency speedups over the baseline across the 10 production rows.
- Small-shape wins (19–195 tokens) are additionally validated on the integrated SGLang
  install path (`kda_kernels.install()` + zero-overhead dispatcher).

## Frozen Baseline (Round 2, NVIDIA B200)

- Host `innomatrix-us-adc-smb200-0003`, physical GPU 4 (NVIDIA B200, idle 0% util),
  container `sglang_bbuf`, local commit `43a8fd164`.
- Command: `CUDA_VISIBLE_DEVICES=4 KDA_GIT_COMMIT=43a8fd164 python benchmark.py`
  (correctness gate first: `CUDA_VISIBLE_DEVICES=4 KDA_RUN_CORRECTNESS=1 pytest
  tests/test_correctness.py` — 10 production + 2400 CI-grid + 3 negative tests PASS).
- Latency formula: per-call CUDA-event median over `iters` (warmup excluded), no CUDA graph.
- Fused-baseline median latency (µs): joyai-edit B7904/H32 = 89.5; qwen B4096/H24 = 45.1;
  qwen-edit B8424/H24 = 98.0; zimage B4096/H30 = 76.1; zimage B4128/H30 = 76.5;
  qwen B19/H24 = 64.2; qwen B47/H24 = 64.0; qwen-edit B195/H24 = 64.1;
  qwen-edit B189/H24 = 64.3; zimage B32/H30 = 64.9.
- Candidate (routes to baseline) geomean = 1.0149x (≈1.0x, validates methodology).
- Signal: small shapes (19–195 tok) are flat ~64µs — a fixed per-call dispatch/launch
  floor that exceeds the 4096-tok large shape (45µs); large shapes scale with size.
  Full per-row stats + provenance + idle snapshots are in `benchmark.csv`.

## To Be Filled Before Promotion

- final wrapper signature once the specialized kernel is wired in;
- per-shape dispatch table (which candidate handles which bucket);
- confirmed fallback cases;
- frozen baseline numbers + exact benchmark command + selected GPU id/model;
- source lineage for any ported/adapted helper code.
