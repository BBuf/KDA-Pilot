# SGLang jit_kernel / tvm-ffi export + in-SGLang replacement test (AC-13)

Final packaging/sanity step, after the RLCR loop converged. ion8-h200 GPU7 (external idle
util=0% mem=70MiB), container `sglang_omni_bbuf_kda`, sglang `c47f0e7cd`.

> Round-1 note: the round-0 attempt used a runtime monkeypatch (no SGLang files placed), which Codex
> correctly rejected as not the required in-tree placement. This is the corrected, real test.

## Export mechanics (real in-tree placement, isolated checkout)
- **Isolated SGLang checkout**: `git -C /home/sglang-omni/bbuf/repos/sglang worktree add --detach
  /tmp/sglang_kda_export c47f0e7cd` — the shared `repos/sglang` working tree is left untouched.
- **Candidate `.cuh` placed in the SGLang tree**: copied to
  `/tmp/sglang_kda_export/python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` (replacing the
  baseline). It defines the same `QKNormRopeKernel<head_dim,rope_dim,is_neox,pdl,dtype>::run` class.
- **Normal resolution (no monkeypatch)**: with `PYTHONPATH=/tmp/sglang_kda_export/python`, SGLang's own
  public `fused_inplace_qknorm_rope` → `_jit_qknorm_rope_module` →
  `load_jit("qknorm_rope", *make_cpp_args(head_dim,rope_dim,is_neox,is_arch_support_pdl(),dtype),
  cuda_files=["diffusion/qknorm_rope.cuh"], cuda_wrappers=[("qknorm_rope","QKNormRopeKernel<...>::run")])`
  builds the candidate kernel. Flags = SGLang diffusion default (no `--use_fast_math`).
- No `torch.utils.cpp_extension`, no `EXPORTS`. Candidate vs baseline run in separate processes with
  distinct sglang paths (`/tmp/sglang_kda_export` vs `/home/.../repos/sglang`) → distinct JIT builds
  (no cache collision; confirmed by the ~1.05–1.08× delta).

## In-SGLang results (`docs/evidence/export_cand.json`, `export_base.json`)
- **Correctness inside SGLang**: all 9 captured shapes `oracle_ok=True`, no NaN, vs the split oracle
  (`fused_inplace_qknorm` + FlashInfer RoPE) from the same checkout.
- **Smoke benchmark** (worktree public fn vs baseline repos/sglang public fn, wrapper-level, idle GPU7):
  per-shape 1.016–1.084× (large 1.075–1.084×), **geomean 1.0452×** (parity-or-speedup on every shape).
- **Fallback preserved**: the KDA `optimized_wrapper` on a CPU input → dispatch `"fallback"`, no raise
  (`CPU_FALLBACK PASS`). (SGLang's public fn itself has no CPU fallback — same as the original baseline;
  the safe fallback is the KDA wrapper layer that wraps it for promotion.)
- **Verdict**: `VERDICT PASS`.

## Reproduce
```
git -C /home/sglang-omni/bbuf/repos/sglang worktree add --detach /tmp/sglang_kda_export c47f0e7cd
cp <RKD>/src/csrc/qknorm_rope_kernel.cuh /tmp/sglang_kda_export/python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh
CUDA_VISIBLE_DEVICES=7 bash <RKD>/run_export_real.sh <RKD>     # candidate + baseline + fallback + geomean
```

---

# Continuation round re-run (2026-06-04, candidate `cossin-vec` `6669bd218e336c9d`)

Re-promotion arbiter for the continuation candidate (float4 cos/sin loads + base-alignment launcher
guard layered on d3-final). ion8-h200 GPU 7 (externally idle util=0% mem=42MiB before AND after),
container `sglang_bbuf` (torch 2.11.0+cu130 / nvcc 13.0 — the prior round's container no longer
exists; toolchain delta documented in `docs/draft.md`), both legs at SGLang pin `c47f0e7cd`.

## Mechanics (same contract, stricter isolation)
- Candidate tree: detached worktree `<RKD>/sglang_arbiter` @ `c47f0e7cd`; candidate `.cuh`
  placed as `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` and **hash-verified in-tree
  (`6669bd218e336c9d`) before the run**. SGLang's OWN public `fused_inplace_qknorm_rope`
  (`@register_custom_op` intact) builds it through normal `load_jit`/`make_cpp_args`/`cache_once`.
- Baseline tree: the separate, unmodified `<RKD>/sglang_pin` worktree at the SAME commit (original
  baseline `.cuh`), run in a separate process — distinct JIT builds, no cache collision.
  `repos/sglang` untouched. No monkeypatch anywhere.

## Results (`docs/evidence/export_cand_cossin-vec.json`, `export_base_cossin-vec.json`,
`arbiter_run_cossin-vec.log`)
- **Correctness inside SGLang**: all 9 captured shapes `oracle_ok=True`, no NaN.
- **Smoke benchmark** (public fn vs public fn): per-shape 1.005–1.222× — parity-or-speedup on
  every shape; large shapes 1.188–1.222×; **geomean 1.0945×** (prior promoted candidate measured
  1.0452× on this same arbiter).
- **Misaligned-cache negative (new, Codex-required)**: a contiguous `[4096, 128]` float32 cache
  with `data_ptr() % 16 == 4` through the IN-TREE public op → the launcher's base-alignment guard
  routes it to the scalar one-head path; output matches the split oracle (PASS). Permanent
  regression coverage added as
  `tests/test_correctness.py::test_misaligned_cos_sin_cache_still_oracle_correct`.
- **Fallback preserved**: KDA `optimized_wrapper` on a CPU input → dispatch `"fallback"`, no raise.
- **Verdict**: `VERDICT PASS`.

## Reproduce (continuation)
```
sh <RKD>/stage_arbiter.sh        # worktree + .cuh placement + hash check
sh <RKD>/run_arbiter.sh          # pytest -k misaligned, candidate/baseline legs, in-tree misaligned, fallback, geomean
```

## kda_kernels re-export (round 1, closing the review gap)

`scripts/export_kda_kernels/export.py h200_diffusion_qknorm_rope__multi_shape` refreshed
`kda_kernels/diffusion/qknorm_rope/_impls/h200/` from the stale incumbent to the continuation
candidate — copied `.cuh` sha verified `6669bd218e336c9d`; family `__init__.py`/`_dispatcher.py`
regenerated; `KDA_EXPORTS.json`/`KDA_STATUS.md` stamped with commit `72fdfaa3b` and
**`KDA_SPEEDUP = 1.0677x`** — deliberately the LITERAL install()-path geomean (not the 1.0945×
in-tree arbiter number), per the project rule that the overlay package reports its own shipping
number. Smoke through the INSTALLED path (`profile/integration/validate_overlay.py`, idle GPU 7,
pin `c47f0e7cd`): `kda_kernels.install()` swaps the public symbol → generated dispatcher →
`_impls/h200`; all 9 captured shapes route `path=cuda`, oracle-close, no NaN, in-place; fp16 CUDA →
dispatcher fallback, no raise; **install() geomean 1.0677× all-9 / 1.1536× large** (prior promoted
candidate measured 1.0118–1.0181× / 1.055–1.063× on this same validator); tiny 0.987–1.029
(launch-bound parity + dispatcher overhead — same honest production behavior as the prior round).
Evidence: `docs/evidence/overlay_smoke_cossin-vec.log`, `benchmark.csv` rows tagged
`export-cossin-vec` / `export-cossin-vec-overlay`.
