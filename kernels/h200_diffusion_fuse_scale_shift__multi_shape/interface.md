# Interface: h200_diffusion_fuse_scale_shift__multi_shape

- Kernel slug: `h200_diffusion_fuse_scale_shift__multi_shape`
- Op type: `fuse_scale_shift`
- Target GPU: NVIDIA H200
- Wrapped SGLang entry points:
- `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_scale_shift_kernel`
- `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_layernorm_scale_shift_gate_select01_kernel`
- `sglang.jit_kernel.diffusion.triton.scale_shift:fuse_residual_layernorm_scale_shift_gate_select01_kernel`

## Export

Provide:

```text
src/register.py
```

with:

```python
KERNEL_SLUG = "h200_diffusion_fuse_scale_shift__multi_shape"
OP_TYPE = "fuse_scale_shift"

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

## Recovered Public Signatures (baseline contract; sglang `0689ba84b`, file commit `47979fb25`)

```python
def fuse_scale_shift_kernel(
    x: torch.Tensor,            # (B, L, C), CUDA, contiguous (asserted)
    scale: torch.Tensor,        # 0D/1D(1-elem) scalar | (B,C)/(1,C) | (B,L,C) + broadcastable 3D | (B,F,1,C)
    shift: torch.Tensor,        # same layout rules as scale (4D path: shift must be per-token (B,L,C))
    scale_constant: float = 1.0,  # compile-time specialized; production captures pass 0
    block_l: int = 128,
    block_c: int = 128,
) -> torch.Tensor               # new tensor (empty_like(x)); y = x * (scale_constant + scale) + shift

def fuse_layernorm_scale_shift_gate_select01_kernel(
    x: torch.Tensor,            # (B, L, C), CUDA, contiguous (asserted)
    weight: torch.Tensor | None,  # 1D [C] or None
    bias: torch.Tensor | None,    # 1D [C] or None
    scale0: torch.Tensor, shift0: torch.Tensor, gate0: torch.Tensor,  # each 2D (B, C)
    scale1: torch.Tensor, shift1: torch.Tensor, gate1: torch.Tensor,  # each 2D (B, C)
    index: torch.Tensor,        # 2D (B, L), int32/int64/bool with values in {0, 1}
    eps: float,
) -> tuple[torch.Tensor, torch.Tensor]  # (output, gate_out), both empty_like(x)
# output = LayerNorm_fp32(x, eps, weight, bias) * (1 + scale_sel) + shift_sel ; gate_out = gate_sel

def fuse_residual_layernorm_scale_shift_gate_select01_kernel(
    x: torch.Tensor,            # (B, L, C), CUDA, contiguous (asserted)
    residual: torch.Tensor,     # (B, L, C), contiguous, same shape as x (asserted)
    residual_gate: torch.Tensor,  # (B, L, C), contiguous, same shape as x (asserted)
    weight: torch.Tensor | None, bias: torch.Tensor | None,
    scale0, shift0, gate0, scale1, shift1, gate1,  # each 2D (B, C)
    index: torch.Tensor,        # 2D (B, L)
    eps: float,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]  # (output, residual_out, gate_out)
# residual_out = residual + residual_gate * x (fp32 compute; LN consumes the unrounded fp32 values)
```

Output-allocation policy: every output is a fresh `torch.empty_like(x)`; no
in-place variants. Compute precision: LayerNorm reductions and the modulation
epilogue run in fp32 (scale/shift loads upcast; gate passes through in native
dtype); the elementwise kernel computes in the promoted dtype of `(x, scale)`.
Full recovered behavior notes: `docs/baseline_source.md`.

## Evidence Requirements

Before promotion, update this file with:

- final wrapper signature(s);
- per-shape dispatch table (which underlying candidate kernel handles
which shape bucket);
- fallback cases;
- PyTorch-FP32 or `_reference()` tolerance methodology used in tests;
- benchmark command and latency formula;
- source lineage for copied or ported helper code.

## Final Evidence (cuda-flat-v5, promoted via in-tree drop-in)

- Final wrapper signatures: the three recovered baseline signatures above,
  preserved exactly; `src/register.py` exposes them plus `optimized_wrapper`
  (signature-binding resolution) and a bare-exec-safe `EXPORTS` dict. The
  shipping wrapper is `intree/scale_shift_kda.py` (in-tree:
  `python/sglang/jit_kernel/diffusion/scale_shift_kda.py`).
- Per-shape dispatch table: `docs/dispatch.md` — 15/15 production rows native
  (elementwise:ss for all fuse_scale_shift rows incl. mixed-dtype and the
  non-contiguous fp32 scale; ln_select01 / ln_select01_residual for the two
  Family B rows); full eligibility predicates listed there.
- Fallback cases: out-of-contract device/dtype/rank/stride/alignment
  signatures, both-scalar scale/shift (baseline zero-copy semantics kept),
  C not divisible by the 16B vector width, B*L > 65535 (elementwise) or
  C > 8192 bf16-equivalent (LN family) — all reach the baseline (locally the
  vendored copy; in-tree the original Triton bodies), verified by the
  negative-parity suite and the in-tree fallback checks.
- Tolerance methodology: fixed oracle tolerances (atol=rtol=5e-2 fp16/bf16,
  1e-5 fp32) candidate-vs-baseline PLUS the dynamic cross-check
  max|cand-ref32| <= 2.0*max|base-ref32| + floor (bench/reference.py), with
  NaN/Inf guards; comparator self-test rejects corruption and NaN.
- Benchmark command and latency formula:
  `python bench/benchmark.py --gpu-id <id> --tag <candidate>` — same-process
  interleaved A/B, per-call sync-wall and CUDA-event medians over
  auto-scaled iterations (~60 ms/side), stats median/mean/std/min/p10/p90;
  speedup = baseline_median_us / candidate_median_us; geomean via
  `--geomean` over the latest valid row per shape. Shipping-path validation:
  `profile/in_sglang/validate_in_tree.py --gpu-id <id>` (ABBA blocks through
  the unchanged public SGLang callables).
- Source lineage: `docs/baseline_source.md` (vendored Triton baseline,
  bit-identical 21/21 vs live SGLang at copy time); design idea sources in
  `solutions.jsonl` (KernelWiki pr-sglang-14717, technique-vectorized-loads;
  qknorm_rope.cuh / group_norm_silu_kda.cuh exemplars).
- Results (cuda-flat-v5, centered-variance build): local geomeans sync
  1.2878x / device 1.2238x / amort 1.2911x (docs/results.md); FINAL
  shipping-path geomeans sync **1.2643x** / stream-span **1.3433x** (the two
  registered select01 rows measured through their CustomOp production
  callsite; run r3), oracle 288/288, all rows positive (min 1.1258x)
  (docs/sglang_jit_export.md). PERF_FALLBACK empty.
