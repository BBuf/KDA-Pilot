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
