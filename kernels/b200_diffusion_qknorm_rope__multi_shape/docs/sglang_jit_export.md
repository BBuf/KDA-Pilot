# SGLang export — in-tree placement (torch.compile-safe), the #19 way

## Continuation round r9 (2026-06-04) — ARBITER PASS on the jit_kernel/tvm-ffi stack

This round re-ran the full arbiter with review-hardened protocol and fresh same-commit
evidence. **PROMOTION_GATE PASS — in-SGLang device geomean 1.0970x** (`benchmark.csv`
`*__intree_r9` rows + `GEOMEAN_intree_r9`; raw JSONs/logs in `profile/in_sglang/r9/`).

- SGLang files to patch (unchanged): ONLY `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`
  ← this task's `src/qknorm_rope_candidate.cuh` (sha256 candidate `874b1bfa`, baseline `86db2105`).
  Public entry `fused_inplace_qknorm_rope` and its `@register_custom_op(mutates_args=["q","k"])`
  stay byte-unchanged; `load_jit` template args / CUDA wrapper name (`("qknorm_rope",
  "QKNormRopeKernel<head_dim,rope_dim,is_neox,pdl,dtype>::run")`) unchanged.
- Protocol (per pre-arbiter review): isolated SGLang worktree at `0b65588c1`
  (`$RDIR/sglang_intree_cand`); per-side `TVM_FFI_CACHE_DIR` isolation (no module-name
  collision possible); alternating sides, run1 discarded (warm), run2 recorded, run1 used as
  the regression cross-check; material-regression gate (>3%, run1-confirmed) ENFORCED by
  `validate_in_tree.py compare` (exit code); idle B200 GPU 1 (UUID `GPU-709d3f1a`), 0%/0MiB
  before and after.
- Results (run2): large rows 1.1410–1.2714x (joyai 1.2087, qwen 1.2480, qwen-edit 1.1410,
  zimage 1.2575/1.2714); small rows 0.9733–0.9908 — all within the 3% threshold (and small
  medians 22.2–22.8 µs on both sides, stable). Correctness 10/10 through the real op in all
  four measure runs.
- torch.compile preservation: `compile_smoke.py` fullgraph PASS on both sides over a small
  captured row, a large captured row, and a broad-staged synthetic row (B1024/H16) —
  compiled results match eager within task tolerances.
- Broad staged surface (the in-tree gate covers ALL bf16/128/128 non-NeoX ≥512-token calls):
  SGLang's own `python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py` **full grid,
  1248 passed** inside the candidate worktree (`profile/in_sglang/r9/sglang_own_test_cand.log`).
- Host/device decomposition (`profile/in_sglang/r9/decompose_r9.log`): the public custom-op
  layer costs ~7–8 µs/call on both sides (identical layers ⇒ cancels in the ratio); the
  in-tree path adds NO Python on top of SGLang's own op. Note the single-input-set protocol
  yields faster absolute µs than the two-set devfair lane (L2 residency of the in-place q/k);
  same-protocol ratios are the admissible evidence.

The sections below are the prior round's record (mechanism unchanged; numbers superseded by
the r9 rows above).

AC-8 deliverable, redone the way the promoted h200 qknorm_rope (PR #19, AC-13) did it: a **real
in-tree placement** of the candidate `.cuh` inside SGLang's `csrc`, keeping SGLang's **own**
`register_custom_op` wrapper. This is **torch.compile-safe** (the public op stays a registered
custom op), and it delivers the genuine device win.

> Why not the `kda_kernels` overlay: `kda_kernels.install()` replaces the public symbol with a
> plain Python dispatcher (no `register_custom_op`), which is **not torch.compile-safe** and whose
> apparent eager win came mostly from dropping the custom-op host layer (a false economy under
> torch.compile). Production here requires torch.compile, so the overlay path is **not promoted**
> (`KDA_OPTIMIZED_fused_inplace_qknorm_rope = False`); see `solutions.jsonl` (`export_r8`,
> `in_tree_torch_compile_safe`).

## Mechanism (real in-tree placement)
- The candidate kernel lives in `src/qknorm_rope_candidate.cuh`. Its `QKNormRopeKernel<head_dim,
  rope_dim,is_neox,pdl,dtype>::run` (the class SGLang's wrapper calls) **internally delegates** the
  exact production template (`head_dim=128, rope_dim=128, is_neox=False, bf16`) with
  `num_tokens >= kStagedMinTokens (512)` to `QKNormRopeStagedKernel` (CTA-per-token cos/sin
  staging — the device win); every other template/shape uses the unchanged warp path. The delegation
  is `if constexpr`-gated to the production template, so the CI grid's other configs are untouched.
- Therefore a **plain swap of this `.cuh`** into SGLang's
  `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` makes SGLang's own
  `fused_inplace_qknorm_rope` → `_jit_qknorm_rope_module` → `load_jit(..., cuda_wrappers=[("qknorm_rope",
  "QKNormRopeKernel<...>::run")])` build the candidate transparently, with SGLang's
  `register_custom_op` wrapper (and torch.compile compatibility) intact. No `EXPORTS`, no monkeypatch,
  no `torch.utils.cpp_extension`; flags = SGLang diffusion default (no `--use_fast_math`).

### Reproduce (B200; the #19 AC-13 flow)
```bash
git -C /home/sglang-omni/bbuf/repos/sglang worktree add --detach /tmp/sglang_kda_b200_intree HEAD
cp <KDIR>/src/qknorm_rope_candidate.cuh \
   /tmp/sglang_kda_b200_intree/python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh
cd <KDIR>
CUDA_VISIBLE_DEVICES=4 PYTHONPATH=/tmp/sglang_kda_b200_intree/python \
  python profile/in_sglang/validate_in_tree.py measure cand.json     # candidate (my .cuh in-tree)
CUDA_VISIBLE_DEVICES=4 PYTHONPATH=/home/sglang-omni/bbuf/repos/sglang/python \
  python profile/in_sglang/validate_in_tree.py measure base.json     # baseline (unchanged)
python profile/in_sglang/validate_in_tree.py compare base.json cand.json
```

## In-SGLang results (idle B200, GPU 4; isolated worktree at SGLang HEAD `0b65588c1`)
- **Correctness: 10/10 production shapes `oracle_ok`** through SGLang's OWN public op (vs the split
  oracle `fused_inplace_qknorm` + FlashInfer RoPE, ATOL=8e-2/RTOL=1e-2); no NaN/Inf.
- **Device delta (torch.compile-safe — both sides go through SGLang's identical
  `register_custom_op`):** geomean **~1.07–1.12x** — large shapes **1.10–1.33x** (joyai-edit B7904,
  qwen B4096, qwen-edit B8424, zimage B4096/B4128), small shapes **~1.0x parity** (the small/warp
  kernel is byte-identical to the baseline, so no device change — its win is 0 by construction).
- Robust cross-check: the **device-fair** interleaved A/B (same process, symmetric, noise-canceling)
  is **1.0679x** (large 1.10–1.26x, small ~1.0x; warp faithful-port sanity 0.9999x) — the
  conservative device-delta. The in-tree run confirms it through SGLang's real op.
- **Measurement caveat (honest):** the in-tree candidate vs baseline must run in SEPARATE processes
  (distinct SGLang checkouts), so it cannot interleave to cancel shared-box clock drift. A first run
  mis-measured the small shapes at ~0.60x (impossible for a byte-identical kernel — pure cross-process
  noise); a back-to-back warm re-run gave the correct small ~1.0x parity (geomean 1.1182x). The
  device-fair (interleaved) number is the trustworthy device-delta; the in-tree run validates
  correctness + that the large win shows through SGLang's real custom-op.

## Decision
**Ship the in-tree placement** (torch.compile-safe device win, ~1.07x geomean driven by the large
bucket; small parity). **Do NOT promote the `kda_kernels` overlay** (it is torch.compile-unsafe).
This mirrors the promoted h200 qknorm_rope (#19). Evidence: `benchmark.csv` (`GEOMEAN_intree`
1.1182x; `GEOMEAN_install` 0.9301x overlay-eager for contrast; `GEOMEAN_production` 0.9957x baseline
reference), `solutions.jsonl` (`in_tree_torch_compile_safe`), `profile/in_sglang/validate_in_tree.py`,
and `intree_{cand,base}.json` in REMOTE_KDA_DIR.
