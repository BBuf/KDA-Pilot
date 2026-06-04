# Interface: b200_diffusion_rotary_embedding__multi_shape

- Kernel slug: `b200_diffusion_rotary_embedding__multi_shape`
- Op type: `rotary_embedding`
- Target GPU: NVIDIA B200
- Wrapped SGLang entry points:
- `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`
- `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb`

## Export

Provide:

```text
src/register.py
```

with:

```python
KERNEL_SLUG = "b200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"

def optimized_wrapper(*args, **kwargs):
...

def register() -> dict:
return {
"name": KERNEL_SLUG,
"op_type": OP_TYPE,
"callable": optimized_wrapper,
"version": "dev",
"source": __file__,
}
```

`optimized_wrapper` must preserve the recovered SGLang callsite contract
for every wrapped entry point. It must fall back to the baseline
implementation for any shape, dtype, layout, device, normalization type,
or feature flag that is not part of the configured shape table.

The exact public signature for each wrapped entry point should be filled
after baseline recovery. Typical wrappers for this family accept the same
positional and keyword arguments as the SGLang baseline (see `prompt.md`),
plus optional `*, dispatcher_hint=` keyword for dispatcher overrides.

## Evidence Requirements

Before promotion, update this file with:

- final wrapper signature(s);
- per-shape dispatch table (which underlying candidate kernel handles
which shape bucket);
- fallback cases;
- PyTorch-FP32 or `_reference()` tolerance methodology used in tests;
- benchmark command and latency formula;
- source lineage for copied or ported helper code.

## Final Result (cuda-v4; hardened Rounds 1–2)

**Final wrapper signatures** (out-of-place, exact recovered SGLang contract), exposed via `src/register.py` `EXPORTS` and `optimized_wrapper`:
- `apply_rotary_embedding(x, cos, sin, interleaved=False) -> Tensor` — standard adjacent-pair RoPE.
- `apply_ltx2_split_rotary_emb(x, cos, sin) -> Tensor` — LTX-2 split-half RoPE.

**Per-shape dispatch table** (CUDA fast path; all else falls back to the SGLang Triton baseline):
- `apply_rotary_embedding` CUDA path: `x` bf16 3D `(T,H,D)` or 4D `(B=1,S,H,D)` with `(H,D)` inner contiguous, `cos`/`sin` fp32 `(tokens, D/2)` contiguous-last, `interleaved=False`, on CUDA. Captured: `x=[1,27030,24,128]`, `cos=sin=[27030,64]`.
- `apply_ltx2_split_rotary_emb` CUDA path: `x` bf16 `(B,S,H*2*half)` inner-contiguous, `cos`/`sin` bf16 `(B,H,S,half)` with inner (`half`) contiguous (structured non-contiguous outer is fine, indexed by stride), `H*2*half == inner`. Captured: `B∈{1,2}`, `H=32`, `half∈{32,64}`, `S∈{126,1536,6144,24576}`.
- **Fallback** (recursion-safe): any non-captured dtype/device/dim/flag/layout → the original baseline object captured at import (does not recurse after a public-symbol swap). Verified by `test_fallback_non_captured`.

**Tolerance methodology**: oracle = SGLang diffusion Triton baseline; cross-checked vs a PyTorch FP32 reference. Dynamic BF16-aware bound — candidate's error vs FP32 must not exceed ~2× the baseline's own bf16 quantization noise (floor 2^-7). Achieved: **bit-exact** (`pair_diff = 0`) on all 11 unique signatures.

**Benchmark command** (idle B200, container `sglang_bbuf`): `CUDA_VISIBLE_DEVICES=<idle> python benchmark.py --warmup 50 --iters 300 --candidate cuda-v4`. Parent/worker harness: the parent validates `nvidia-smi` idleness before AND after the CUDA worker (a separate process) exits, and refuses to record unless both pass; latency = CUDA-event single-call median (µs). Final metric = geometric mean of per-shape `baseline_median/candidate_median` over the 11 unique signatures = **≈1.45×** (3 idle-gated parent/worker runs with verified `idle_before` AND `idle_after` = `{util 0, mem 0, n_compute_procs 0}`: 1.4417 / 1.4505 / 1.4633×; consistent with earlier ~1.45× and Round-0 1.3834×). The candidate is `>= baseline` on every shape; the spread reflects Triton-baseline run-to-run variance on launch-bound shapes (candidate times are stable).

**Active bounds (NCU + roofline)**: see `profile/ncu-v2/REPORT.md` — LTX-2-large-half64 DRAM-bandwidth bound (85% SOL, parity = ceiling); standard compute/BW-balanced (59/62% SOL, 1.80×); LTX-2-large-half32 BW-leaning (75% SOL, 1.21–1.23×); small launch/latency-bound (1.66–1.71×).

**Source lineage**: launcher pattern mirrors `sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` (`TensorView`/`host::TensorMatcher`/`SymbolicSize`/`host::LaunchKernel`, `PDLWaitPrimary`); build via `sglang.jit_kernel.utils.load_jit`+`make_cpp_args`. No third-party kernel code copied. Pinned baseline SGLang `0b65588c1` (`0.5.12.dev472`).

**Export validated (in-tree, AC-9)**: `.cuh` physically placed at `python/sglang/jit_kernel/csrc/diffusion/rotary_embedding.cuh` in a task-owned worktree; `cache_once` + relative-path `load_jit` loader; in-SGLang oracle bit-exact 11/11, smoke parity-or-speedup, fp16 fallback, originals restored, worktree removed (no shared-checkout mutation). See `docs/sglang_jit_export.md`.

**Dispatch gates (AC-4)**: only the exact captured signatures take CUDA; non-captured dtype/shape/layout (incl. contiguous LTX-2 cos/sin) fall back. Tight gating is also a safety requirement — the 128-bit vectorized loads assume the 16-byte alignment that only the captured shapes/strides guarantee.

## Continuation Result (cuda-v6; k09 run, 2026-06-04)

Signatures, dispatch table, fallback behavior, and tolerance methodology are UNCHANGED from the
cuda-v4 section above. Continuation deltas only:

- **Standard kernel improved** (`src/csrc/rotary_embedding.cuh`, src hash `317e2fab7ade`): the
  per-token cos/sin vectors are hoisted into registers (each thread's pair segment is invariant
  across its grid-stride passes; the launcher enforces `blockDim % kVecPerHead == 0`) and the
  block size is chosen as the largest full-pass divisor that also divides the 2048-thread SM
  budget (128 threads for the captured 24-head/128-dim shape; measured sweep in `docs/draft.md`).
  Captured standard shape: 61.86 → **57.7 µs** = **1.0709–1.0718× vs cuda-v4** (3 idle-gated
  paired runs, 3-of-3 beyond the 3% noise band). Still **bit-exact**: `pair_diff = 0.000e+00` on
  all 11 signatures (raw log: `docs/logs/correctness_cuda_v6_20260604.log`).
- **LTX-2 kernel functionally unchanged** (comment-only source delta vs the v4 snapshot
  `f4c8b844044f`; diff: `docs/logs/v4_to_v6_rotary_cuh.diff`). Paired deltas within ≤0.6% on the
  large shapes (24576-row shapes exact parity at displayed precision); worst small-shape paired
  delta +1.198%, within its ~8% cross-run band.
- **Paired benchmark mode**: `CUDA_VISIBLE_DEVICES=<idle> python benchmark.py --warmup 50
  --iters 300 --candidate cuda-v6 --compare-src <v4-src-snapshot> --compare-label cuda-v4` —
  times baseline, v4-snapshot, and candidate in the SAME worker process through the identical
  wrapper ABI; rows `cuda-v6_vs_cuda-v4` in `benchmark.csv`. Pair geomeans 1.0038/1.0061/1.0066×.
- **Environment note (mandatory with any geomean claim)**: the 2026-06-04 container baseline is
  SGLang `edb1b3f8f`, whose LTX-2 Triton kernel lacks PR #24732 and is 2–8× slower at scale than
  the 2026-06-01 pinned baseline — geomean vs the CURRENT baseline is **3.1682–3.1965×** but is
  environment-inflated; the like-for-like estimate vs the 2026-06-01 environment is **~1.46×**
  (= 1.4505 × paired 1.0038–1.0066; see `docs/draft.md` BASELINE SHIFT + corrections).
- **Active bounds refreshed** (`profile/ncu-v3/REPORT.md`): standard now memory-paced (DRAM 69.8%,
  compute 47.1%, ~75% effective of peak; MLP probe cuda-v7 zero movement → at bound; bf16-packed
  math no-go by evidence); LTX-2 large-half32 76.1% DRAM SOL clean-access no-go; small shapes
  launch-floor no-go (grid-halving experiment regressed 12%); large-half64 no-go stands (ncu-v2).
