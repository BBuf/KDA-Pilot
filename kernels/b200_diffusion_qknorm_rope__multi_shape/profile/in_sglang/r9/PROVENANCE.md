# r9 in-SGLang arbiter — provenance and command transcript

One chained remote invocation (2026-06-04, via the `ion-b200` skill SSH pattern into docker
`sglang_bbuf`), `RDIR=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_qknorm_rope__multi_shape/20260604-185755-r9`,
task copy `T=$RDIR/task`, candidate worktree `W=$RDIR/sglang_intree_cand`,
baseline checkout `MAIN=/home/sglang-omni/bbuf/repos/sglang`. `CUDA_VISIBLE_DEVICES=1`.

## Provenance (printed by the run, before any measurement)

- GPU: physical 1, `0 %, 0 MiB`, UUID `GPU-709d3f1a-3fca-36e4-22a6-e4e7e1d8c33e`; after the
  full sequence: `0 %, 0 MiB`.
- Source sha256 (first 20 hex): baseline `$MAIN/.../qknorm_rope.cuh` = `86db210550d97141b932`;
  candidate `$W/.../qknorm_rope.cuh` = `874b1bfa3bd32a37a2b5`. The shipped
  `src/qknorm_rope_candidate.cuh` was restored to byte-identity with the arbiter-validated
  content (`874b1bfa…`) after the rejected `staged2` probe (which existed only at git
  `355f3bf2a`) was removed.
- SGLang commit, both sides: `0b65588c1` (`git -C $MAIN rev-parse` and `git -C $W rev-parse`).
- Task commit at arbiter time: `f46075e69`.

## Cache isolation (pre-arbiter review requirement)

Every baseline-side process ran with `TVM_FFI_CACHE_DIR=$RDIR/tvmffi_base`; every
candidate-side process with `TVM_FFI_CACHE_DIR=$RDIR/tvmffi_cand` — disjoint build caches,
so a module-name collision between the two checkouts is impossible by construction.
(Additionally, tvm-ffi keys builds on a sha256 over the generated wrapper source, which
embeds the absolute `#include` path of each checkout's `.cuh`.)

## Run order and commands (exact, per side)

    # 1) BASE run1 (warm/discard)
    PYTHONPATH=$MAIN/python TVM_FFI_CACHE_DIR=$RDIR/tvmffi_base \
      python profile/in_sglang/validate_in_tree.py measure $RDIR/logs/intree_base_run1.json
    # 2) CAND run1 (warm/discard)
    PYTHONPATH=$W/python    TVM_FFI_CACHE_DIR=$RDIR/tvmffi_cand \
      python profile/in_sglang/validate_in_tree.py measure $RDIR/logs/intree_cand_run1.json
    # 3) BASE run2 (recorded)   — same command, output intree_base_run2.json
    # 4) CAND run2 (recorded)   — same command, output intree_cand_run2.json
    # 5) Enforced compare: run2 pair, run1 pair as the regression cross-check (3% threshold)
    python profile/in_sglang/validate_in_tree.py compare \
      $RDIR/logs/intree_base_run2.json $RDIR/logs/intree_cand_run2.json \
      $RDIR/logs/intree_base_run1.json $RDIR/logs/intree_cand_run1.json
    # 6) compile_smoke.py per side (same PYTHONPATH/TVM_FFI_CACHE_DIR pairs)
    # 7) SGLang's own full grid in the candidate worktree:
    #    cd $W && PYTHONPATH=$W/python TVM_FFI_CACHE_DIR=$RDIR/tvmffi_cand \
    #      python -m pytest python/sglang/jit_kernel/tests/diffusion/test_qknorm_rope.py -q
    # 8) decompose.py three-path attribution on the baseline checkout

All four measure runs printed `[measure] sglang at <side's __init__.py>` (also stored under
the `_provenance` key of each JSON) — base runs resolved to `$MAIN`, cand runs to `$W`.

## Verdict

`[compare] in-SGLang (register_custom_op preserved) device geomean = 1.0970x over 10 shapes;
material-regression threshold = 3.0%` → `PROMOTION_GATE PASS`. Compile smoke PASS ×2 sides
×3 shapes; SGLang full grid `1248 passed` in the worktree; decompose: custom-op layer
7.90 µs (B19) / 7.09 µs (B8424) on the baseline side.

Raw artifacts in this directory: `intree_{base,cand}_run{1,2}.json` (full per-shape stats:
median/mean/std/min/p10/p90), `intree_compare.log`, `compile_smoke_{base,cand}.log`,
`sglang_own_test_cand.log`, `decompose_r9.log`. Remote copies + full console logs:
`$RDIR/logs/` (incl. `intree_*_run*.log`).
