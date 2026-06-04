# Interface: h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape

- Kernel slug: `h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`
- Op type: `cutedsl_norm_tanh_mul_add`
- Target GPU: NVIDIA H200
- Wrapped SGLang entry points:
- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add`
- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale`

## Export

Provide:

```text
src/register.py
```

with:

```python
KERNEL_SLUG = "h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
OP_TYPE = "cutedsl_norm_tanh_mul_add"

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

## Final Evidence (promotion record, 2026-06-04)

### Final wrapper signatures (recovered public contract, preserved exactly)

`optimized_wrapper(*args, **kwargs)` dispatches by arity via `dispatch_decision()`
(`src/wrapper.py`; single source of truth, exposed through `src/register.py`):

- single (6 or 7 positional args; `eps` defaults to 1e-5):
  `fused_norm_tanh_mul_add(x, weight: Optional[Tensor], bias: Optional[Tensor], scale, shift, norm_type: str, eps: float = 1e-5) -> Tensor`
- dual (9 or 10 positional args):
  `fused_norm_tanh_mul_add_norm_scale(x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps=1e-5) -> Tuple[Tensor, Tensor]`
- keyword-style calls and unrecognized arities route to the vendored baseline,
  which binds its own defaults or raises its own contract error (unmasked).
- The local fast path is wrapped in `torch.library.custom_op("kda_candidate::...")`
  (+ fake registration) for host-layer parity with the baseline's custom ops.

### Dispatch table

One fast-path family — the 4 captured production signatures and any row count with
the same per-row layout (no per-bucket split; `docs/dispatch.md` not needed):

| gate | fast path (native CUDA, `norm_tanh_mul_add_kernel<...>`) | fallback (vendored pinned baseline) |
|---|---|---|
| dtype | bf16 (all of x/weight/scale/shift/weight2/scale2) | fp16, fp32, mixed |
| norm_type | "rms" | "layer" |
| D | 3840 | any other (incl. valid 256-multiples) |
| weight / bias | weight=[D] present, bias=None (weight2/bias2 same) | weight absent or bias present |
| scale / scale2 | [1,1,D], unit stride | any other accepted 3-D layout |
| shift | full [B,S,D], contiguous | [1,1,D], [B,1,D], [1,S,D] broadcasts |
| alignment | all tensors 16-byte aligned | misaligned contiguous views (baseline then raises its own ValueError) |
| rows | B*S ≤ 2^31-1 | larger (grid limit) |
| device / call style | CUDA, positional | CPU, kwargs |

### Tolerance methodology (tests/test_correctness.py)

Compositional verification: stage-1 `y` vs a pure fp32 oracle
(`torch.rms_norm`/`layer_norm` + `* tanh(scale) + shift`) with the kernel's
storage-dtype boundary mirrored (norm output quantized to the element dtype) and a
backward-error model — per element `|a-e| <= atol + rtol*max(|e|, |n*tanh(scale)|+|shift|)`
(the term scale covers cancellation rounding); dual `y2` vs `norm2(actual_y)*(1+scale2)`.
Coefficients are the task's hard contract: atol=rtol=1e-5 fp32, 5e-2 fp16/bf16.
Candidate additionally bounded by baseline noise: max-err ≤ 2× baseline max-err + 1e-6
(stage-1 vs the pure oracle; stage-2 vs each side's own stage-2 reference).
NaN/Inf validators on every output; sensitivity tests prove the checker rejects
`(1+scale)`-for-`tanh(scale)` and `tanh(scale2)`-for-`(1+scale2)` mutations and a
y2-only perturbation of 10× the dynamic bound.

### Benchmark command and latency formula

```bash
python benchmark.py --lock --host ion8-h200                      # freeze baseline (idle GPU)
python benchmark.py --host ion8-h200 --candidate-version <sha>   # candidate A/B
```

Per shape: wall latency = median over 100 iters of `perf_counter` around the public
call + `cuda.synchronize` (25-iter JIT/module warmup excluded); device time =
median CUDA-event elapsed; host overhead = wall − device. Headline = geometric mean
of per-shape speedups over all 4 captured shapes; the PRIMARY local number is the
alternating same-process interleaved A/B (`mode=interleaved_ab` rows), with
sequential-vs-locked (`candidate_vs_locked`) and `baseline_seq_rerun` drift rows as
support. Roofline denominator = fused-logical bytes (actual NCU bytes reported
alongside in `profile/ncu_anchor_r2/REPORT.md` FINAL ADDENDUM).

### Source lineage

- `baseline/` = pinned SGLang `0689ba84b88c991684b0f99ee9b50c3ce485b483` (see
  `docs/baseline_source.md`; 5 documented line edits, sha256 manifest).
- Candidate `.cuh` host launcher pattern mirrors
  `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` (TensorMatcher /
  SymbolicSize / LaunchKernel) per KernelWiki `pr-sglang-19059`; reduction
  structure ports `baseline/common/reduce.py` (CuTe warp+CTA reduction, fp32
  accumulation) from `pr-sglang-14717`; kernel origin context `pr-sglang-18762`.
  Build via unmodified `sglang.jit_kernel.utils.load_jit` (read-only import,
  DEC-4), default flags, no `--use_fast_math`.
- Benchmark/A-B harness patterns adapted from sibling
  `kernels/h200_diffusion_norm_infer__multi_shape` (`--lock`, baseline-locked
  JSON, interleaved A/B).

### Result

Geomean over the 4 captured shapes (3 sessions): interleaved 1.3253–1.3621x,
sequential 1.4463–1.4695x, device-only 1.38–1.66x vs the locked baseline.
Full details: `docs/results.md`; bound analysis: `profile/ncu_anchor_r2/REPORT.md`.
