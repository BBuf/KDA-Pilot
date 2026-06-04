# In-Tree SGLang Export & Drop-In Validation (promotion arbiter)

Date: 2026-06-04. Host `ion-h200-8`, container `sglang_bbuf`, GPU 3 (NVIDIA
H200; idle verified before AND after: `valid=True`), torch 2.11.0+cu130.

## Where the candidate lives in-tree

Task-owned worktree of the SGLang checkout (no shared-checkout mutation):
`git -C /home/sglang-omni/bbuf/repos/sglang worktree add --detach
$REMOTE_KDA_DIR/sglang_intree HEAD` → detached at `84e1108312b5`
("Optimize ngram decode id computation (#24757)"); the pre-patch
`triton/scale_shift.py` md5 equals the pinned baseline source
(`b4c069aca94ccb7b2bbea2d2571634a1`) — `intree/apply_patch.py` refuses to run
otherwise.

SGLang files touched (full in-tree diff: 18 inserted lines + 2 new files):

1. `python/sglang/jit_kernel/csrc/diffusion/scale_shift_kda.cuh` — NEW; exact
   copy of `solution/scale_shift_kda.cuh` (final candidate cuda-flat-v5,
   centered-variance build).
2. `python/sglang/jit_kernel/diffusion/scale_shift_kda.py` — NEW wrapper
   (source: `intree/scale_shift_kda.py`): `load_jit` with the RELATIVE
   `cuda_files=["diffusion/scale_shift_kda.cuh"]`, `make_cpp_args`,
   `cache_once` module caching, DEFAULT jit_kernel flags only (no
   `--use_fast_math`), PDL off (`SGLANG_SCALE_SHIFT_KDA_PDL=1` available).
   `try_native_*` gates return `None` for out-of-contract signatures.
3. `python/sglang/jit_kernel/diffusion/triton/scale_shift.py` — 18 lines
   inserted (one import + a 5/6-line try-native block at the top of each
   public function); the original Triton bodies are UNCHANGED and remain the
   in-function fallback.

`load_jit` template args / wrapper names:
- `FuseScaleShiftKernel<DTypeX, DTypeScale, DTypeShift, kScaleSplat,
  kShiftSplat, kFrameMode, kUsePDL>::run` exported as `fuse_scale_shift`
  (module marker `scale_shift_kda`).
- `FuseLNSelect01Kernel<DTypeX, kHasWeight, kHasBias, kHasResidual,
  kUsePDL>::run` exported as `fuse_ln_select01` (marker `ln_select01_kda`).

## Preserved production contract

- Public callable names, signatures, return arities, output-allocation policy
  and module path are untouched: `fuse_scale_shift_kernel`,
  `fuse_layernorm_scale_shift_gate_select01_kernel`,
  `fuse_residual_layernorm_scale_shift_gate_select01_kernel` remain the same
  function objects in the same module.
- The CustomOp / torch.compile registration layer above the select01 kernels
  (`python/sglang/multimodal_gen/runtime/layers/fused_scale_shift_gate.py`)
  is NOT modified — it keeps calling the same public functions.
- No overlay / monkey-patching anywhere; toggle `SGLANG_SCALE_SHIFT_KDA=0`
  restores pure-Triton behavior inside the same functions.
- Both-scalar scale/shift calls intentionally decline native so the original
  wrapper's zero-check copy short-circuit semantics are preserved exactly.

## Validation results (commands run from the kernel workspace)

1. **Oracle** — SGLang's own test, native ON, unchanged public ops:
   `PYTHONPATH=$WT/python CUDA_VISIBLE_DEVICES=3 python -m pytest -q
   $WT/python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py`
   → **288 passed** (53.6s).
2. **Routing proof** — harness-side counting wrappers (removed before any
   timing): 15/15 production rows served natively (13 elementwise + 1
   select01 + 1 residual).
3. **Parity** — native vs original Triton through the SAME public functions,
   all 15 rows within the oracle tolerances, outputs finite.
4. **Fallback** — with native ON: fp64 reaches the original Triton body with
   IDENTICAL results; non-contiguous x and CPU tensors raise the same
   AssertionError in both modes.
5. **Smoke benchmark (shipping path)** — ABBA interleaved blocks through the
   identical public callables, only the module-level native toggle differs;
   instrumentation (per-call events + sync) identical on both sides:
   `PYTHONPATH=$WT/python CUDA_VISIBLE_DEVICES=3 python
   profile/in_sglang/validate_in_tree.py --gpu-id 3 --json
   $REMOTE_KDA_DIR/in_tree_validation_r1.json`

| row | sync_wall base→cand (x) | device_ev base→cand (x) |
|---|---|---|
| prod00 firered 8424x3072 | 81.2→68.5 (1.187) | 66.8→54.2 (1.233) |
| prod01 hunyuan 27030 | 168.1→149.3 (1.126) | 153.4→134.9 (1.137) |
| prod02 hunyuan 55 | 52.3→39.1 (1.336) | 39.1→26.2 (1.493) |
| prod03 hunyuan 27085 | 167.8→149.1 (1.125) | 153.4→134.7 (1.139) |
| prod04 qwen 4096 | 61.5→48.1 (1.278) | 48.3→34.9 (1.384) |
| prod05 qwen 19 | 47.6→35.6 (1.337) | 34.5→22.7 (1.522) |
| prod06 qwen 47 | 47.6→35.6 (1.337) | 34.6→22.7 (1.525) |
| prod07 select01 8424 | 91.9→80.0 (**1.149**) | 77.7→65.8 (1.181) |
| prod08 residual 8424 | 135.5→117.7 (**1.151**) | 121.1→103.7 (1.168) |
| prod09 per-token 8424 | 91.6→78.7 (1.164) | 77.6→64.8 (1.197) |
| prod10 qwen-edit 195 | 48.4→36.0 (1.345) | 35.4→23.1 (1.529) |
| prod11 qwen-edit 189 | 48.2→35.8 (1.346) | 35.1→22.9 (1.535) |
| prod12 wan-i2v 37044x5120 | 413.2→292.4 (1.413) | 398.1→277.8 (1.433) |
| prod13 wan-t2v 37800x5120 | 420.6→297.7 (1.413) | 405.6→283.2 (1.432) |
| prod14 wan-ti2v NC | 180.2→159.3 (1.131) | 165.8→145.1 (1.143) |

Direct-public-function geomean (all 15 rows): sync_wall 1.2513x, device_ev
1.3269x (run r1, `bench/reports/remote_r0/in_tree_validation_r1.json`).

## Registered-CustomOp-layer coverage (the production callsite for select01)

The two select01 production rows are called in production through the
registered layer in `multimodal_gen/runtime/layers/fused_scale_shift_gate.py`
(`CustomOp.register("fuse_layernorm_scale_shift_gate_select01")` /
`...residual...`), which adds nn.Module dispatch + its own contiguity
handling above the public functions. Validation run r2 resolves those classes
from `CustomOp.op_registry`, instantiates them, and runs parity + ABBA timing
through `op(*args, **kwargs)` with the same native toggle:

- CustomOp-layer parity: **2/2 rows** within oracle tolerances, outputs finite.
- CustomOp-layer timing (the layer adds ~4 us symmetrically to both sides;
  ratios match the direct path):

| row | path | sync_wall base→cand (x) | device_ev base→cand (x) |
|---|---|---|---|
| prod07 select01 | customop | 95.8→84.1 (**1.139**) | 81.7→70.3 (1.162) |
| prod08 residual | customop | 140.1→121.4 (**1.154**) | 125.8→107.6 (1.169) |

(values from run r3, the centered-variance build; the direct-path table above
is the r1 run kept for lineage — per-row r3 direct values live in the raw
`in_tree_validation_r3.json`.)

**FINAL promotion geomeans (all 15 rows; the two registered rows counted via
the CustomOp layer, the other 13 via the direct public functions; run r3 with
the centered-variance build cuda-flat-v5): sync_wall 1.2643x, device_ev
1.3433x; all rows positive, min 1.1258x sync; CustomOp rows 1.139x/1.154x
sync, 1.162x/1.169x stream** (valid=True, idle before/after; raw:
`bench/reports/remote_r0/in_tree_validation_r3.json`, remote original at
`$REMOTE_KDA_DIR/in_tree_validation_r3.json`). Run r3 re-validated everything
after the code-review fix that restored the baseline-faithful CENTERED
LayerNorm variance (oracle re-passed 288/288; direct parity 15/15; CustomOp
parity 2/2; fallback checks 3/3). Historical runs: r1 (direct-only)
1.2513x/1.3269x; r2 (CustomOp-inclusive, single-pass-variance build)
1.2496x/1.3233x.

Command: `PYTHONPATH=$WT/python CUDA_VISIBLE_DEVICES=3 python
profile/in_sglang/validate_in_tree.py --gpu-id 3 --json
$REMOTE_KDA_DIR/in_tree_validation_r3.json` (after re-applying
`intree/apply_patch.py` to the refreshed worktree).

Coverage note: the in-tree ORACLE (288/288) exercises the direct public
functions (that is what SGLang's own test calls); the CustomOp layer is
covered by the r2 parity + timing above. `fuse_scale_shift_kernel` has no
custom-op wrapper in production (called directly from the layernorm /
elementwise layers), so the direct path IS its production callsite.

Notes: (a) the in-tree `device_ev` brackets the whole public call on the
stream, so for host-bound rows it includes wrapper submit gaps on BOTH sides
— the bare-kernel device comparison remains the r0 local evidence
(docs/results.md); (b) absolute latencies sit ~15 us above the r0 local
harness on both sides because the per-call event records + the fuller sglang
import context are inside the timed region — identical for both sides, so
ratios are unaffected.

## Perf-fallback re-adjudication (DEC-1)

Every production row wins BOTH shipping-path metrics through its REAL
production callsite (all rows positive, min 1.1258x sync, incl. the
CustomOp-layer rows at 1.139x/1.154x), versus 0.933x/0.979x on the
bare-kernel device view for the two Family B rows (centered-variance build).
`PERF_FALLBACK` therefore remains EMPTY; no row is routed back to Triton for
performance.

## Promotion verdict

**PROMOTE.** Correctness: 288/288 in-tree oracle + 15/15 direct parity + 2/2
CustomOp-layer parity + fallback checks, on top of the local 2424/2424.
Performance through the exact shipping path (identical wrapper/dispatch/
registration on both sides — incl. the registered CustomOp layer for the two
select01 rows — only the device path differs): **final geomean 1.2643x
end-to-end / 1.3433x stream-span, all 15 rows positive (run r3,
centered-variance build).**
