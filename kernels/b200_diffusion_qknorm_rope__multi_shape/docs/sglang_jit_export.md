# SGLang export + drop-in validation — b200_diffusion_qknorm_rope__multi_shape

This is the AC-8 deliverable: the candidate was made exportable through the repo's
`kda_kernels` overlay, the **literal `kda_kernels.install()` drop-in** was validated for
correctness, and the production install-path performance was measured. The performance
result is a **net regression**, so the candidate is **NOT promoted** (evidence-backed
no-go). This document records the mechanism, the validation, and the decision.

## Export mechanism (repo overlay, not an in-tree SGLang edit)

This project promotes kernels through `scripts/export_kda_kernels/export.py`, which copies
the task's `src/` into `kda_kernels/diffusion/<family>/_impls/<arch>/` and rewrites the
family package to route the public symbol through a generated, capability-aware dispatcher.
`kda_kernels.install()` then monkey-patches the SGLang public symbol at runtime. This is the
integrated install path the plan's AC-4/AC-8 refer to (the `kda_kernels` references in the
plan's "Relevant References"); it preserves the exact public callable name
`sglang.jit_kernel.diffusion.qknorm_rope.fused_inplace_qknorm_rope`.

### Touched files (when exported)
- `kda_kernels/diffusion/qknorm_rope/__init__.py` — rewritten to import the generated
  dispatcher and flip `KDA_OPTIMIZED_fused_inplace_qknorm_rope = True`.
- `kda_kernels/diffusion/qknorm_rope/_dispatcher.py` — generated; binds the SGLang baseline
  at import (pre-swap), routes by CUDA capability `(10,0)->b200`, memoizes the resolved
  target per `(fn, device)`, and exposes `_preload_kda_impls` (imported by `install()`
  before monkey-patching so fallbacks are non-recursive).
- `kda_kernels/diffusion/qknorm_rope/_impls/b200/{register.py, wrapper.py,
  qknorm_rope_candidate.cuh, KDA_EXPORTS.json, KDA_STATUS.md}` — the copied task sources.

### Export-readiness of `src/` (mirrors the promoted h200 PR #19 tvm-ffi layout)
- `src/register.py` is a thin, import-light forwarder. `Path(__file__)` is guarded by
  `try/except NameError` so `export.py:read_exports()` (which `exec`s the file in a bare
  namespace) returns `EXPORTS = {"fused_inplace_qknorm_rope": ...}` without crashing.
- `src/wrapper.py` holds all heavy machinery: the `.cuh` path, the `load_jit` build (relpath
  to `KERNEL_PATH/csrc` + content-hash JIT cache marker; flags match the diffusion baseline,
  no `--use_fast_math`), the exact-shape fail-closed gate, and `fused_inplace_qknorm_rope =
  optimized_wrapper` (the symbol the generated dispatcher imports).
- Recursion safety: the wrapper captures the SGLang baseline at **import** time (the
  `_preload_kda_impls` hook imports it before the swap), plus a thread-local re-entrancy
  guard, an identity/`__module__` recursion check, and a PyTorch `semantic_reference_inplace`
  safety net. Small/unsupported shapes call the captured ORIGINAL fast baseline, never the
  swapped KDA symbol.

### Reproduce the export
```bash
python3 scripts/export_kda_kernels/export.py b200_diffusion_qknorm_rope__multi_shape
# verify: kda_kernels/diffusion/qknorm_rope/__init__.py sets KDA_OPTIMIZED_...=True
python3 scripts/export_kda_kernels/export.py --revert b200_diffusion_qknorm_rope__multi_shape  # undo
```

## Drop-in correctness (PASS)

On B200 (`ion-b200`, `sglang_bbuf`, GPU 4 idle), after the real export, with
`KDA_RUN_CORRECTNESS=1 KDA_RUN_INTEGRATED=1 PYTHONPATH=<repo-root>`:

- `test_install_path_dropin_and_no_recursion` (the literal `kda_kernels.install(force=True,
  strict=True)` path): the qknorm_rope entry reports **`swapped`**; the installed public
  symbol routes a **large captured row → staged CUDA** (dispatch `cuda`, oracle match) and
  the **small + int32 rows → the captured original baseline** (dispatch `fallback`, oracle
  match, **no recursion**); the baseline is restored on `uninstall()`.
- `correctness_r8.log`: **10 passed** (`-k "not ci_grid"`) — production rows + negatives +
  exact-shape routing + fail-closed gate + fallback + wrong-eps + the install drop-in test.
- `cigrid_r8.log`: the full **2400-case CI grid passed** (correctness-or-fallback).

So the export + drop-in is **functionally correct**: it preserves the public callable,
computes correctly on the accelerated route, falls back correctly (and non-recursively) on
the unsupported tail, and is cleanly uninstallable.

## Install-path performance (NET REGRESSION → no-go)

`benchmark.py --integrated` runs the literal install path: it captures the original baseline
public op, calls `kda_kernels.install(force=True, strict=True)`, asserts the swap, and times
the original baseline (custom-op) vs the **installed public symbol** interleaved on identical
inputs. Two idle-B200 runs:

| shape | bucket | route | install speedup (run1 / run2) |
|-------|--------|-------|-------------------------------|
| joyai-edit B7904/H32 | large | staged | **1.209x / 1.205x** |
| qwen B4096/H24 | large | staged | 0.972x / 0.954x |
| qwen-edit B8424/H24 | large | staged | 0.998x / 0.991x |
| zimage B4096/H30 | large | staged | 0.929x / 0.913x |
| zimage B4128/H30 | large | staged | 0.925x / 0.921x |
| qwen B19/H24 | small | baseline | 0.868x / 0.850x |
| qwen B47/H24 | small | baseline | 0.859x / 0.849x |
| qwen-edit B195/H24 | small | baseline | 0.868x / 0.855x |
| qwen-edit B189/H24 | small | baseline | 0.857x / 0.857x |
| zimage B32/H30 | small | baseline | 0.866x / 0.845x |
| **GEOMEAN** | | | **0.9301x / 0.9185x** |

### Why — named active bound
The staged DEVICE kernel is a real win: the same-session **device-fair** A/B (both kernels
through their direct JIT modules, symmetric, no custom op) gives geomean **1.0679x** (large
**1.10–1.26x**), with a warp faithful-port **0.9999x** sanity confirming the comparison is
fair; NCU corroborates (B8424 device 109.6→88.1 µs, `long_scoreboard` 11.9→9.29).

The gap between device-fair (1.07x) and the literal install (0.93x) is the **`kda_kernels`
overlay per-call Python dispatch tax** (generated dispatcher + wrapper frame + gate, ~7 µs
more than the baseline's C-level `register_custom_op`). On this small-per-call,
**host-dispatch-bound** workload (small shapes: ~9.7 µs device vs ~65 µs end-to-end), that
tax dominates: only joyai-edit B7904/H32 has a device saving (~18 µs) large enough to
overcome it; the other four large shapes (save 4.5–11 µs) land parity-to-loss, and the five
dispatch-bound small shapes (no device saving) eat the full tax. The equal-weight geomean
over the 10 production rows is therefore **< 1.0 on the production install path**.

This is exactly the failure mode the plan and `.humanize/bitlesson.md` anticipated — *"any
Python dispatcher … can erase kernel-level wins."* The proxy benchmark used through Round 7
(timing `optimized_wrapper` directly, geomean 1.0793x) understated this because it skipped
the real overlay frame; the literal install path is the production truth.

## Decision: evidence-backed no-go (NOT promoted)

Per the plan's allowance for a well-supported no-go (frozen baseline + real candidate
attempts + NCU evidence + a named active bound), the candidate is **not promoted**: the
export was **reverted** so the shipped `kda_kernels` overlay stays the un-promoted stub
(`KDA_OPTIMIZED_fused_inplace_qknorm_rope = False`) and installing it does not regress
production. The export-ready `src/` and all evidence remain; `export.py` reproduces the
overlay for any future re-evaluation.

The staged cos/sin device optimization would only become a net production win if the
overlay had a near-zero-overhead (C-level) dispatch path, or if these calls were issued
under CUDA graphs — both outside this single-op, no-CUDA-graph task boundary.

## Evidence
- Logs (`REMOTE_KDA_DIR` = `/home/sglang-omni/bbuf/kda_runs/b200_diffusion_qknorm_rope__multi_shape/20260601-224831-25812`):
  `correctness_r8.log`, `cigrid_r8.log`, `install_bench_r8.log`, `install_bench_r8b.log`,
  `devicefair_staged_r8.log`, `devicefair_warp_r8.log`.
- `benchmark.csv`: `GEOMEAN_production` 0.9957x (baseline-vs-baseline R3) + `*__install` rows
  + `GEOMEAN_install` 0.9301x (R8).
- `solutions.jsonl`: `id=export_r8` (this no-go), `id=dispatcher_r7` (the corrected proxy).
- `docs/dispatch.md`: device-fair vs install decision table + bound analysis.
