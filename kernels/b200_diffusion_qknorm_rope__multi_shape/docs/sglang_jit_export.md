# SGLang export + drop-in validation — b200_diffusion_qknorm_rope__multi_shape

AC-8 deliverable. The candidate is exported into the `kda_kernels` overlay and validated on the
**literal `kda_kernels.install()` drop-in path**. Result: correctness across the full production
+ CI-grid set, and a **net production speedup (geomean ~1.22x)** on the literal install path —
**PROMOTED** (`KDA_OPTIMIZED_fused_inplace_qknorm_rope = True`).

## Export mechanism (repo overlay)

The project promotes via `scripts/export_kda_kernels/export.py`, which copies the task's `src/`
into `kda_kernels/diffusion/qknorm_rope/_impls/b200/` and rewrites the family package so the
public symbol routes through a generated capability-aware dispatcher; `kda_kernels.install()`
monkey-patches `sglang.jit_kernel.diffusion.qknorm_rope.fused_inplace_qknorm_rope` at runtime,
preserving the exact public callable name.

### Touched files (promoted)
- `kda_kernels/diffusion/qknorm_rope/__init__.py` — imports the generated dispatcher;
  `KDA_OPTIMIZED_fused_inplace_qknorm_rope = True`.
- `kda_kernels/diffusion/qknorm_rope/_dispatcher.py` — generated; binds the SGLang baseline at
  import (pre-swap), routes by CUDA capability `(10,0)->b200`, memoizes the resolved target,
  exposes `_preload_kda_impls`.
- `kda_kernels/diffusion/qknorm_rope/_impls/b200/{register.py, wrapper.py,
  qknorm_rope_candidate.cuh, KDA_EXPORTS.json, KDA_STATUS.md}` — the copied task sources.

### Export-ready `src/`
- `src/register.py` — thin, import-light forwarder + `EXPORTS = {"fused_inplace_qknorm_rope":
  optimized_wrapper}`; loads the sibling `wrapper.py` under a **slug-specific** module name via
  `importlib` (never a generic `wrapper` that another task could shadow); `Path(__file__)`
  guarded so `read_exports()` execs it cleanly without `__file__`.
- `src/wrapper.py` — the **lean, custom-op-free** dispatch (see below). Built via SGLang
  `load_jit`/`make_cpp_args`/`cache_once` (relpath to `KERNEL_PATH/csrc` + content-hash cache
  marker; flags match the diffusion baseline, no `--use_fast_math`).

### Reproduce
```bash
python3 scripts/export_kda_kernels/export.py b200_diffusion_qknorm_rope__multi_shape   # promote
python3 scripts/export_kda_kernels/export.py --revert b200_diffusion_qknorm_rope__multi_shape  # undo
```

## Drop-in correctness (PASS)

On B200 (`ion-b200`, `sglang_bbuf`, GPU 4 idle), after the real export, with
`KDA_RUN_CORRECTNESS=1 KDA_RUN_INTEGRATED=1 PYTHONPATH=<repo-root>`:
- `correctness_lean.log`: **10 passed** (`-k "not ci_grid"`) — production rows + negatives +
  `_fast_supported` template gate + staged/warp routing + non-contiguous→fallback + the literal
  `kda_kernels.install()` drop-in test (large→staged, small→warp, oracle-matched; the rare
  fallback resolves to the captured ORIGINAL baseline — verified — so it cannot recurse; baseline
  restored on uninstall).
- `cigrid_lean.log`: full **2400-case CI grid passed** — now routed through the warp
  faithful-port kernel across the WHOLE template space (head_dim 64/128/256, neox, int32/int64),
  a stronger validation than the earlier baseline-fallback grid.

## Install-path performance (NET WIN → PROMOTED)

`benchmark.py --integrated` runs the literal path: capture the original baseline, call
`kda_kernels.install(force=True, strict=True)`, assert the swap, time the original baseline
(custom-op) vs the **installed public symbol** interleaved. Two idle-B200 runs:

| bucket | route | install geomean (run1 / run2) |
|--------|-------|-------------------------------|
| 5 large | staged | 1.19–1.28x |
| 5 small | warp | 1.20–1.23x |
| **all 10** | | **1.2199x / 1.2164x** |

### Why it wins
1. **No `register_custom_op` on the common path.** After install, the public symbol is a plain
   dispatcher; routing straight to the tvm-ffi kernel removes the baseline's per-call torch
   custom-op layer (~10µs) for every shape — this alone wins ~1.2x on the dispatch-bound small
   shapes (whose warp device kernel is byte-identical to the baseline).
2. **cos/sin staging** on the large shapes adds a device win (NCU B8424 109.6→88.1 µs,
   `long_scoreboard` 11.9→9.29) that compounds with (1).

The device-fair diagnostic (1.0679x, device-only) is smaller because it removes the custom-op
layer from both sides; the literal install path additionally captures the host custom-op saving,
which is the production-relevant delta.

## Decision: PROMOTED

`KDA_OPTIMIZED_fused_inplace_qknorm_rope = True`; the overlay ships the b200 impl. Installing it
makes the 10 production shapes ~1.22x faster on B200.

### Caveat (scope)
The win includes removing torch `register_custom_op` on the common path — valid for this task's
**eager, single-op, no-CUDA-graph** scope and the kda_kernels overlay contract (it patches the
public Python symbol; callers use it eagerly). If a deployment wraps this op in `torch.compile` /
CUDA graphs, or invokes it via `torch.ops`, the custom-op registration semantics may matter and
the latency profile could differ; re-validate there before relying on the host-side portion of
the win. The device-side staging win (large shapes) holds regardless.

### History
An earlier heavy wrapper (25-check fail-closed gate + fallback that re-entered the custom-op
baseline for small shapes) was a net regression (0.93x) and was correctly held as a no-go; the
lean design here (route directly to the project kernels, no custom-op on the common path)
reverses it. See `solutions.jsonl` (`lean_overlay_win` supersedes `export_r8`), `docs/dispatch.md`.

## Evidence
- Logs (`REMOTE_KDA_DIR` = `/home/sglang-omni/bbuf/kda_runs/b200_diffusion_qknorm_rope__multi_shape/20260601-224831-25812`):
  `correctness_lean.log`, `cigrid_lean.log`, `install_bench_lean.log`, `install_bench_lean_b.log`.
- `benchmark.csv`: `GEOMEAN_production` 0.9957x (frozen R3 baseline-vs-baseline reference) +
  `*__install` rows + `GEOMEAN_install` 1.2199x.
- `solutions.jsonl`: `lean_overlay_win` (promoted) ; `docs/dispatch.md` decision table.
