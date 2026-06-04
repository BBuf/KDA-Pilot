# In-SGLang Export & Drop-In Replacement Record (task13 arbiter)

**Status: EXPORT ARBITER PASS** (2026-06-04, ion8-h200 GPU0 idle; final run with
device-fallback probes: `logs/export_arbiter_run2.log`; initial run:
`logs/export_arbiter.log` — superseded after the round-3 review caught missing
`.is_cuda` gates in the exported predicate, fixed and re-validated in run2).

## What was exported

Applied to an ISOLATED git worktree of the container's sglang repo at HEAD
`84e1108312` (kernel files byte-identical to the pin `0689ba84b`; the shared
checkout `/home/sglang-omni/bbuf/repos/sglang` was never modified in place):

| file | change |
|---|---|
| `python/sglang/jit_kernel/csrc/diffusion/norm_tanh_mul_add.cuh` | NEW — the promoted anchor kernel (lean, anchor-only; bf16-production-only documented in the header) |
| `python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py` | native fast path inserted INSIDE the existing public custom ops |

Full shipping diff: `docs/sglang_export.patch` (390 lines). Patch generator:
`src/export/apply_export.py` (deterministic, anchored string insertion);
validator: `src/export/export_validate.py`.

## Preserved production contract

- `@torch.library.custom_op("sglang::fused_norm_tanh_mul_add", mutates_args=())`
  and the dual op + both `register_fake` registrations: **byte-unchanged** (the
  fast path lives inside the op bodies after the existing validation + D guard).
- Public callable names, signatures, defaults (`eps=1e-5`), validation errors,
  output allocation (`torch.empty_like`), current-stream launch: unchanged.
- Fallback: every non-fast-path signature continues through the original
  CuTe-DSL path. **Probed in the arbiter** (`export_validate.py`, run2): fp32
  (bitwise vs pinned baseline), all-CPU single, all-CPU dual, and mixed-device
  (CUDA x + CPU scale) — error-class parity with the pinned baseline in every
  case (both raise the same ValueError; the native module is never entered).
  The remaining fallback classes (D≠3840, bias-present, non-`[1,1,D]` scale,
  non-full shift, misaligned views, kwargs) are enforced by the same predicate
  logic and are covered exhaustively by the TASK-LOCAL suite
  (`tests/test_correctness.py::test_dispatch_branch_contract`,
  `test_misaligned_view_falls_back`, `test_fallback_equals_baseline`) against
  the identical gate implementation in `src/wrapper.py`.
- Fast-path gates mirror the task wrapper: **CUDA device on every tensor**
  (`x/weight/scale/shift(/weight2/scale2).is_cuda`) + bf16 + rms + weight-only +
  D==3840 (production-only per DEC-1; the kernel itself supports any
  D%256==0 ≤ 8192 as defense-in-depth) + `scale(/scale2)=[1,1,D]` + full
  contiguous shift + 16-byte alignment + `B*S ≤ 2^31-1`.

## load_jit wiring (inside the patched module)

```python
@cache_once   # module-level: load_jit must not re-enter per call
def _native_norm_tanh_module():
    return load_jit(
        "norm_tanh_mul_add",
        cuda_files=["diffusion/norm_tanh_mul_add.cuh"],
        cuda_wrappers=[
            ("single", "NormTanhMulAddSingleKernel<bf16_t>::run"),
            ("dual", "NormTanhMulAddDualKernel<bf16_t>::run"),
        ],
    )
```

Default jit_kernel flags (`-std=c++20 -O3 --expt-relaxed-constexpr` + arch
define); **no `--use_fast_math`**.

## Arbiter results (PYTHONPATH=worktree/python; both sides through identical custom-op machinery)

Correctness (fp32 oracle with storage-dtype mirroring + term-scale model; dynamic
bound vs the pinned baseline's own error):

| check | S=4096 | S=4128 |
|---|---|---|
| single oracle | OK (err 3.12e-2 ≤ 2× base 4.22e-2) | OK (3.12e-2 ≤ 2× 4.54e-2) |
| dual oracle (y, y2) | OK | OK |
| fp32 fallback → CuTe path | bitwise ≡ pinned baseline | bitwise ≡ pinned baseline |

Device-fallback probes (run2): `cpu-all single`, `mixed-device single`,
`cpu-all dual` — all parity OK (same ValueError class as the pinned baseline,
native module never entered).

Smoke benchmark (alternating interleaved wall medians, 100 iters, warmed;
run1 / run2 — session variance, both decisively parity-or-speedup):

| entry | S=4096 | S=4128 |
|---|---|---|
| single: sglang-native vs pinned baseline | **1.200x** / 1.170x | **1.196x** / 1.173x |
| dual | **1.215x** / 1.183x | **1.203x** / 1.175x |

Parity-or-speedup confirmed on every entry/shape (the in-SGLang number is lower
than the task-wrapper geomean because the patched op runs the baseline's full
validation chain before the native gate — that cost ships with the integration
and is honestly included).

## Reproduction

```bash
WT=<workspace>/sglang_export
git -C /home/sglang-omni/bbuf/repos/sglang worktree add --detach $WT HEAD
cp src/export/norm_tanh_mul_add.cuh $WT/python/sglang/jit_kernel/csrc/diffusion/
python src/export/apply_export.py $WT
CUDA_VISIBLE_DEVICES=<idle> PYTHONPATH=$WT/python python src/export/export_validate.py <kernel_task_dir>
```

torch.compile note: the custom-op + fake registrations are byte-unchanged, so the
compile/CUDA-graph contract is preserved by construction; the native path adds no
graph-unsafe operations (one `torch.empty_like` + one tvm-ffi launch on the
current stream — same shape as the CuTe path).
