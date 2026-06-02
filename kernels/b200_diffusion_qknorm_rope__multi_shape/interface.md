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
src/register.py   # thin, export-safe forwarder + EXPORTS
src/wrapper.py    # implementation (lean custom-op-free dispatch + load_jit build + rare fallback)
```

`src/register.py` is a thin, import-light forwarder: `optimized_wrapper(*args, **kwargs)`
lazily imports the implementation from `src/wrapper.py` under a **slug-specific** module name
(via `importlib`, never a generic `wrapper` that another task could shadow), `register()` returns
`{name, op_type, callable, version, source}`, and `EXPORTS =
{"fused_inplace_qknorm_rope": optimized_wrapper}` is read (keys only) by
`scripts/export_kda_kernels/export.py`. `Path(__file__)` is `try/except NameError`-guarded so
`read_exports()` can `exec` the file in a bare namespace. (Mirrors the promoted h200 PR #19 layout.)

`src/wrapper.py` holds the real op as a **lean, custom-op-free dispatcher**. A minimal guard —
`_fast_supported(head_dim, rope_dim, is_neox, dtype)` (an `lru_cache` template check) + `q`/`k`
contiguous — routes DIRECTLY to one of two workspace-owned kernels in
`src/qknorm_rope_candidate.cuh`, built via SGLang `load_jit`/`make_cpp_args`/`cache_once`
(relpath to `KERNEL_PATH/csrc` + content-hash cache marker + opt-in `KDA_LINEINFO=1`; no
`--use_fast_math`; no `torch.utils.cpp_extension`):
- exact production-large signature (`head_dim=128, rope_dim=128, is_neox=False`, int64 positions,
  captured `(tokens,heads,eps)`) → `QKNormRopeStagedKernel` (CTA-per-token cos/sin staging — the
  device win);
- any other template-supported contiguous signature → `QKNormRopeKernel` (warp-per-(token,head)
  faithful port, byte-identical to the SGLang baseline).
The common path does **not** go through torch `register_custom_op` (that is what makes the
installed overlay faster than the baseline — see Performance). The public callable reads **no
environment variables**. Only non-contiguous / out-of-template / non-bf16 inputs (never produced
by the production shapes or the CI grid) take a **rare fallback** to the SGLang baseline
**captured at import time** (pre-swap, before `kda_kernels.install()` monkey-patches the symbol),
recursion-safe via an identity/`__module__` check, with a PyTorch `semantic_reference_inplace`
net.

**Round 4 candidate status (cand_faithful_port_r4):** the `.cuh` is currently a
faithful port of the SGLang baseline, so the device kernel is identical. The workspace
`load_jit` build path is validated on B200 and production correctness passes. The
isolated benchmark's 1.29–1.40x is an **asymmetric-call-path artifact** (the candidate
skips the baseline's `register_custom_op` ~6–8µs layer) plus shared-box variance — NOT
a device win (decomposition: candidate-direct ≈ 0.79–0.95x vs baseline-direct). A real
device comparison must use the **integrated install path** (same wrapper for both).

**Round 5 candidate (cand_staged_r5) — real large-bucket device win.** Added a second
variant `QKNormRopeStagedKernel` (`fused_qknorm_rope_cta_token`): one CTA per token,
cos/sin staged once into shared memory and reused across the token's heads
(`KDA_CAND_VARIANT=staged`). Production correctness PASSES. A **device-fair interleaved**
benchmark (both kernels timed through their direct JIT modules, symmetric) gives geomean
**1.0787x** — large shapes **1.10–1.26x**, small ~1.0x — with the warp variant as a
**0.9994x** fairness sanity. NCU before/after on B8424: device 109.6→88.1 µs,
`long_scoreboard` 11.9→9.29 (`profile/staged_b200/REPORT.md`). Evidence justifies a
per-bucket dispatcher (large → staged, small → warp). **(Final: the literal
`kda_kernels.install()` path is a net WIN — geomean ~1.22x, all 10 shapes 1.18–1.28x. An interim
Round-8 heavy wrapper measured 0.93x, but that was an artifact of falling back into the
custom-op baseline; the lean custom-op-free dispatch reverses it. See "Performance (final)";
device-fair 1.07x is the device-only diagnostic.)**

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
- The PRODUCTION claim is the LITERAL install path: `benchmark.py --integrated` runs
  `kda_kernels.install()` (after `export.py`) and times the original baseline custom-op vs
  the INSTALLED public symbol, interleaved. `--device-fair` is a device-only diagnostic. On this
  workload the literal install path is the arbiter, and it shows a net **~1.22x win** (the
  installed overlay's plain dispatch is genuinely leaner than the baseline's `register_custom_op`;
  see Performance below).

## Frozen Baseline (Round 3 refreeze, symmetric timing, NVIDIA B200)

- Host `innomatrix-us-adc-smb200-0003`, physical GPU 4 (NVIDIA B200, idle 0% util),
  container `sglang_bbuf`, local commit `68a32061` (resolves the asymmetric-baseline
  timing of the Round 2 freeze: the direct fused-baseline callable is resolved once
  before timing, symmetric with the candidate path).
- Command: `CUDA_VISIBLE_DEVICES=4 KDA_GIT_COMMIT=68a32061 python benchmark.py`
  (correctness gate first: `CUDA_VISIBLE_DEVICES=4 KDA_RUN_CORRECTNESS=1 pytest
  tests/test_correctness.py` — 10 production + 2400 CI-grid + 3 negative tests PASS;
  logs `correctness_prod.log` / `cigrid_full.log` / `sanity.log` / `benchmark.log` in
  `REMOTE_KDA_DIR`).
- Latency formula: per-call CUDA-event median over `iters` (warmup excluded), no CUDA graph.
- Fused-baseline median latency (µs): joyai-edit B7904/H32 = 89.2; qwen B4096/H24 = 59.3;
  qwen-edit B8424/H24 = 95.6; zimage B4096/H30 = 73.6; zimage B4128/H30 = 74.0;
  qwen B19/H24 = 60.7; qwen B47/H24 = 60.8; qwen-edit B195/H24 = 61.2;
  qwen-edit B189/H24 = 61.2; zimage B32/H30 = 61.5.
- Candidate (routes to baseline) geomean = 0.9957x (≈1.0x; slightly <1 reflects the
  candidate's honest extra wrapper frame now that the baseline timing is symmetric).
- Run-to-run variance on the shared box is real (e.g. qwen B4096 read 45µs in Round 2,
  59µs here); treat frozen numbers as a per-run snapshot tied to the recorded commit/GPU.
- NCU named bounds (`profile/baseline_b200/REPORT.md`): small shapes are
  launch/dispatch-bound (device 7.55µs vs 60.7µs end-to-end, ~88% host dispatch); large
  shapes are memory-latency-bound, NOT DRAM-bandwidth-bound (~13% DRAM peak,
  long_scoreboard dominant, 89% occupancy). Full per-row stats + provenance + per-row
  idle snapshots are in `benchmark.csv`.

## Dispatch table (final)

`optimized_wrapper` is a **lean, custom-op-free dispatcher** — no env vars. Full per-shape table
+ evidence in `docs/dispatch.md`:
- exact production-large signature (`head_dim=128, rope_dim=128, is_neox=False`, int64 positions,
  captured `(num_tokens, num_heads, eps)`) → `QKNormRopeStagedKernel` (device win);
- any other template-supported (`head_dim∈{64,128,256}`, bf16, valid rope_dim/neox) contiguous
  signature → `QKNormRopeKernel` (warp faithful port; byte-identical to the baseline);
- non-contiguous / non-bf16 / out-of-template (never in production or the CI grid) → rare
  fallback to the captured SGLang baseline (recursion-safe) / PyTorch reference.
The common path never goes through torch `register_custom_op`. Correctness: **10 passed**
(`-k "not ci_grid"`: production + negatives + `_fast_supported` gate + staged/warp routing +
non-contiguous→fallback + the literal `kda_kernels.install()` drop-in/no-recursion test) and the
full **2400-case CI grid** (now routed through the warp faithful-port kernel across the whole
template space). `correctness_lean.log` / `cigrid_lean.log`.

## Performance (final) — NET WIN (PROMOTED)

Installing the overlay makes the 10 production shapes **~1.22x faster** on the literal
`kda_kernels.install()` path. Full write-up: `docs/sglang_jit_export.md`.

- **Literal install path** (`kda_kernels.install()`; baseline custom-op vs the INSTALLED public
  symbol, interleaved; idle B200): geomean **1.2199x / 1.2164x** (two runs) — **all 10 shapes
  win**: large (staged) 1.19–1.28x, small (warp) 1.20–1.23x. Rows in `benchmark.csv`
  (`*__install` + `GEOMEAN_install`).
- **Why:** (1) after install the public symbol is a plain dispatcher, so routing straight to the
  tvm-ffi kernel removes the baseline's per-call torch `register_custom_op` (~10 µs) for every
  shape — this alone wins ~1.2x on the dispatch-bound small shapes (whose `warp` device kernel is
  byte-identical to the baseline); (2) `QKNormRopeStagedKernel`'s cos/sin staging adds a device
  win on the large shapes (NCU B8424 109.6→88.1 µs, `long_scoreboard` 11.9→9.29) that compounds.
- Device-fair (symmetric direct JIT modules; **diagnostic, device-only**): geomean **1.0679x**,
  large 1.10–1.26x, small 0.98–1.00x; warp faithful-port sanity **0.9999x**. It is smaller than
  the install win because it removes the custom-op layer from both sides (measures only the
  device delta); the literal install path additionally captures the host custom-op saving.
- **Scope caveat:** the win includes removing `register_custom_op` on the common path — valid for
  this eager, single-op, no-CUDA-graph task and the overlay contract (patch the public Python
  symbol). Under `torch.compile` / CUDA graphs / `torch.ops` invocation the custom-op semantics
  may matter; re-validate the host portion there. The device-side staging win holds regardless.
- History: an interim Round-8 heavy wrapper (25-check gate + fallback that re-entered the
  custom-op baseline for small shapes) measured 0.93x and was held as a no-go; the lean design
  above reverses it. `GEOMEAN_production` 0.9957x (baseline-vs-baseline) is retained as the
  frozen reference.

## Source lineage
`src/qknorm_rope_candidate.cuh` ported from sglang `csrc/diffusion/qknorm_rope.cuh`
@`6965fe0ee`; `QKNormRopeStagedKernel` (CTA-per-token cos/sin staging) added in-workspace.
Tolerance = SGLang split-path oracle, ATOL=8e-2/RTOL=1e-2. Tooling commits:
`e2b54594a`, `69ae5b366`, `56997201e`, `a304b8eac`.

## Promotion status — PROMOTED (AC-8 complete, net win)
- AC-8 export + drop-in is DONE and the candidate is **promoted**
  (`KDA_OPTIMIZED_fused_inplace_qknorm_rope = True`). The repo export path
  (`scripts/export_kda_kernels/export.py` → `kda_kernels.install()`) was exercised end-to-end:
  drop-in correctness + 2400 CI grid + no-recursion all PASS, and the literal install path is a
  net **~1.22x** win, so the overlay ships the b200 impl. Details: `docs/sglang_jit_export.md`.
- (The plan's AC-8 wording referenced `python/sglang/jit_kernel/csrc/...`; this project's actual
  integrated path is the `kda_kernels` overlay — see `docs/sglang_jit_export.md`.)

(Frozen baseline numbers + exact command + selected GPU id/model are recorded above
in "Frozen Baseline (Round 3 refreeze)".)
