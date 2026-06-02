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
