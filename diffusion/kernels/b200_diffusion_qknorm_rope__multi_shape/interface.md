# Interface: b200_diffusion_qknorm_rope__multi_shape

- Kernel slug: `b200_diffusion_qknorm_rope__multi_shape`
- Op type: `qknorm_rope_inplace`
- Target GPU: NVIDIA B200 (SM100)
- Wrapped SGLang entry point:
  - `sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope`

> **Continuation round (2026-06-04) — ACTIVE.** This round re-baselines on the SGLang
> `jit_kernel`/tvm-ffi stack (per `../../docs/tvm_ffi_benchmark_status.md`, the task is
> "Blocked" until the candidate is ported into the SGLang checkout). The promotion arbiter is
> the **in-tree drop-in** (candidate `.cuh` under SGLang's own
> `csrc/diffusion/qknorm_rope.cuh`, `register_custom_op` byte-unchanged) measured via
> `profile/in_sglang/validate_in_tree.py`; `benchmark.py --integrated` (the `kda_kernels`
> overlay) is retired and kept only as a negative control. All performance numbers below this
> banner are the **prior-round record** — fresh same-commit numbers land in `benchmark.csv`
> during this round. Active-round context: `docs/draft.md` (top section).
>
> **r9 outcome: ARBITER PASS.** In-SGLang in-tree drop-in at `0b65588c1`: device geomean
> **1.0970x** (large 1.141–1.271x, small ≥0.973 within the 3% materiality gate,
> run1-confirmed), correctness 10/10 ×4 runs, torch.compile fullgraph smoke PASS both sides,
> SGLang's own full grid 1248 passed in the candidate worktree. Loop-lane device-fair
> 1.0648–1.0691x; PDL kept at arch default (A/B sub-materiality). Evidence:
> `benchmark.csv` (`GEOMEAN_intree_r9`), `docs/sglang_jit_export.md` (r9 section),
> `profile/r9_staged_b200/REPORT.md`, `profile/in_sglang/r9/`.

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
src/wrapper.py    # implementation (gate, load_jit build, dispatch, recursion-safe fallback)
```

`src/register.py` is a thin, import-light forwarder: `optimized_wrapper(*args, **kwargs)`
lazily imports the implementation from `src/wrapper.py`, `register()` returns
`{name, op_type, callable, version, source}`, and `EXPORTS =
{"fused_inplace_qknorm_rope": optimized_wrapper}` names the task's public callables per the
interface contract (historically consumed by `scripts/export_kda_kernels/export.py` for the
retired overlay). `Path(__file__)` is `try/except NameError`-guarded so the file can be
`exec`ed in a bare namespace. (This mirrors the promoted h200 PR #19 tvm-ffi layout.)

`src/wrapper.py` holds the real op. For the exact captured-large production signature it
builds and calls the workspace-owned `src/qknorm_rope_candidate.cuh`
(`QKNormRopeStagedKernel<...>::run`) through SGLang `load_jit`/`make_cpp_args`/`cache_once`
(relative `cuda_files` to `KERNEL_PATH/csrc` + content-hash JIT cache marker + an opt-in
`KDA_LINEINFO=1` profiling build; no `--use_fast_math`; no `torch.utils.cpp_extension`). The
public callable reads **no environment variables**. Any other signature falls back to the
SGLang baseline. On the installed overlay the fallback calls the SGLang baseline **captured
at import time** (before `kda_kernels.install()` monkey-patches the symbol), guarded by a
thread-local re-entrancy check + an identity/`__module__` recursion check + a PyTorch
`semantic_reference_inplace` safety net — so the fallback never recurses into the swapped
KDA symbol.

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
per-bucket dispatcher (large → staged, small → warp/baseline); production claim pending
integrated install-path validation. **(Round 8 update: that validation, run on the literal
`kda_kernels.install()` path, returned a net regression (0.9301x) — the device win does not
survive the overlay dispatch tax. See "Performance (final)" below; the device-fair number
here is a diagnostic, not the production result.)**

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
- The PRODUCTION claim comes from the IN-TREE drop-in lane
  (`profile/in_sglang/validate_in_tree.py`): the candidate `.cuh` replaces SGLang's own
  `csrc/diffusion/qknorm_rope.cuh` in an isolated worktree so both sides go through the
  identical `register_custom_op` public op, interleaved/warm. The plain isolated mode and
  `--device-fair` are diagnostics (the isolated candidate path bypasses the baseline's
  `register_custom_op`, a known asymmetry). `benchmark.py --integrated` (the retired
  `kda_kernels.install()` overlay lane) is a negative control only — in the prior round it
  showed a net regression and it drops `register_custom_op` (see Performance below).

## Frozen Baseline (Round 3 refreeze, symmetric timing, NVIDIA B200)

- Host `ion-b200`, physical GPU 4 (NVIDIA B200, idle 0% util),
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

`optimized_wrapper` is an EXACT-shape, fail-closed dispatcher — it reads no environment
variables. Full per-shape table + evidence in `docs/dispatch.md`:
- the 5 large captured `(num_tokens, num_heads)` rows AND the full production contract
  (`head_dim=128, rope_dim=128, is_neox=False`; q/k/weights bf16; `cos_sin_cache` float32;
  `positions` int64; contiguous q/k) → `QKNormRopeStagedKernel`;
- everything else — the 5 small captured rows, any non-captured `(tokens, heads)`,
  non-production dtype/dim/flag, or non-contiguous layout → SGLang baseline fallback
  (explicit, before the C++ `TensorMatcher`).
Correctness re-validated with the dispatcher active (Round 8): **10 passed** (production
routes + negatives + exact-shape routing + fail-closed gate + fallback-correctness +
wrong-eps fallback + the literal `kda_kernels.install()` drop-in/no-recursion test) and the
full 2400-case CI grid (correctness-or-fallback). `correctness_r8.log` / `cigrid_r8.log`.

## Performance (final) — torch.compile-safe device win via IN-TREE placement

Integrated the #19 way: a **real in-tree placement** of the candidate `.cuh` in SGLang's `csrc`,
keeping SGLang's OWN `register_custom_op` wrapper (**torch.compile-safe**). Full write-up:
`docs/sglang_jit_export.md`.

- **In-tree (torch.compile-safe — both sides through SGLang's identical `register_custom_op`,
  so the ratio is the pure DEVICE delta):** geomean **~1.07–1.12x** (`benchmark.csv`
  `GEOMEAN_intree` 1.1182x, idle B200). Large shapes **1.10–1.33x** (joyai/qwen/qwen-edit/zimage);
  small shapes **~1.0x parity** (the warp kernel is byte-identical to the baseline — no device
  change). Correctness: **10/10 production shapes oracle_ok** through SGLang's own public op.
- Device-fair (symmetric direct JIT modules, interleaved, noise-canceling; the conservative
  device-delta): geomean **1.0679x**, large 1.10–1.26x, small ~1.0x; warp sanity **0.9999x**.
  NCU: B8424 device 109.6→88.1 µs, `long_scoreboard` 11.9→9.29.
- **Mechanism:** `src/qknorm_rope_candidate.cuh`'s `QKNormRopeKernel<...>::run` (what SGLang calls)
  `if constexpr`-delegates the exact production template (128/128/!neox/bf16) with
  `num_tokens>=512` to `QKNormRopeStagedKernel`; everything else uses the warp path. So dropping
  this `.cuh` into SGLang's `csrc` transparently delivers the win with `register_custom_op` intact.
- **NOT taken — the `kda_kernels` overlay** (`kda_kernels.install()`): its eager `GEOMEAN_install`
  was 0.93x→1.22x depending on the wrapper, but it works by replacing the public symbol with a
  PLAIN dispatcher (dropping `register_custom_op`) → **not torch.compile-safe**. Production requires
  torch.compile, so the overlay is **not promoted** (`KDA_OPTIMIZED=False`). The `*__install` rows
  remain in `benchmark.csv` for contrast only.

## Source lineage
`src/qknorm_rope_candidate.cuh` ported from sglang `csrc/diffusion/qknorm_rope.cuh`
@`6965fe0ee`; `QKNormRopeStagedKernel` (CTA-per-token cos/sin staging) added in-workspace.
Tolerance = SGLang split-path oracle, ATOL=8e-2/RTOL=1e-2. Tooling commits:
`e2b54594a`, `69ae5b366`, `56997201e`, `a304b8eac`.

## Promotion status — IN-TREE placement (torch.compile-safe), overlay NOT promoted
- **Shipped integration: in-tree `.cuh` placement** in SGLang's `csrc` (the #19 / AC-8-literal
  way), validated on B200: 10/10 production correctness through SGLang's own op + a
  torch.compile-safe device win (`GEOMEAN_intree` ~1.07–1.12x; large 1.10–1.33x, small parity).
  SGLang's `register_custom_op` wrapper is preserved. Apply via the documented drop-in (replace
  `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` with this task's `.cuh`).
  See `docs/sglang_jit_export.md` + `profile/in_sglang/validate_in_tree.py`.
- **`kda_kernels` overlay: NOT promoted** (`KDA_OPTIMIZED_fused_inplace_qknorm_rope = False`). The
  overlay replaces the public symbol with a plain dispatcher (drops `register_custom_op`) → not
  torch.compile-safe, which production requires. Its eager numbers are kept only for contrast.

(Frozen baseline numbers + exact command + selected GPU id/model are recorded above
in "Frozen Baseline (Round 3 refreeze)".)
