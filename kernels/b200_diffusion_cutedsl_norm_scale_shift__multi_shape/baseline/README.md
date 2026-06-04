# baseline/ — vendored SGLang baseline (runtime-isolated)

- `upstream_jit_kernel/jit_kernel/**`: byte-identical subset (17 files) of
  the `python/sglang/jit_kernel` tree at SGLang commit
  `edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7` — the baseline CuTe-DSL module
  + helpers, the `load_jit` build stack, the core `sgl_kernel` headers, and
  the upstream oracle test. No file is edited; unrelated kernels were
  pruned before the PR (full provenance + prune rationale in
  `../docs/baseline_source.md`).
- `loader.py`: registers the snapshot as `sglang.jit_kernel` in `sys.modules`
  so the snapshot's absolute imports resolve without an installed SGLang.
  Refuses to run if a real SGLang is already imported; `assert_snapshot_only()`
  is the harness guard. Also registers a behavior-equivalent `sglang.utils`
  stub providing `is_in_ci` (the single out-of-snapshot symbol imported by
  `jit_kernel/utils.py`; env-based, False in normal runs).
- `entry.py`: the local entry ABI used by correctness/benchmark harnesses —
  same positional signatures as the SGLang public ops, resolving to the
  snapshot's custom-op wrappers (identical host-side dispatch cost).

Parity evidence (snapshot vs real SGLang op, run as two separate processes on
ion-b200): see `../docs/baseline_source.md` and `../bench/parity_check.py`.

Dependencies expected in the execution environment (all present in the
`sglang_bbuf` container): `torch`, `cuda.bindings` (cuda-python), `cutlass`
(nvidia-cutlass-dsl), `einops`.
