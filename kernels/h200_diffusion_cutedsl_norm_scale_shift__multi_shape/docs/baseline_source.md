# Baseline Source Provenance

## Upstream Lineage

- Repository URL: `https://github.com/sgl-project/sglang.git`
- Branch: `main`
- Resolved commit SHA: `133254086bf1f5b887c8c99d311719102d58a7eb`
- Resolution method: `git ls-remote https://github.com/sgl-project/sglang.git refs/heads/main`
- Resolution time (UTC): `2026-06-04T15:00:08Z`
- Extraction method: `git show <SHA>:<path>` from a fetched clone (byte-identical to upstream blobs
  by construction; per-file sha256 manifest below).

## Target Entry Points

- `sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_norm_scale_shift`
- `sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift:fused_scale_residual_norm_scale_shift`

Both are `torch.library.custom_op`s (`sglang::fused_norm_scale_shift`,
`sglang::fused_scale_residual_norm_scale_shift`) with `register_fake`. Both allocate their outputs
internally (`torch.empty_like(x)`); neither accepts destination tensors. They JIT-compile a CuTe DSL
kernel via `cute.compile(..., options="--enable-tvm-ffi")` keyed on
(norm_type, per-tensor (dtype, ndim, D)), launch one CTA per row (`grid=[B*S]`,
`block=[D/8]` threads, 128-bit vectorized copies), and run on the current torch CUDA stream.

## Copied Files (snapshot root: `baseline/upstream_jit_kernel/jit_kernel/`)

All copied verbatim from `python/sglang/jit_kernel/<path>` at commit `1332540`:

| Path | sha256 |
|------|--------|
| `__init__.py` (empty upstream) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `utils.py` (load_jit / tvm-ffi build stack) | `081a0eea7c31a57fd0b7ae0bedd688b5bd1f0ef4f3b64e9bafbef62c6a2fe8a3` |
| `diffusion/cutedsl/scale_residual_norm_scale_shift.py` | `d6818e5da8d3c5ace3950313e996a22b4c051edc29ab7026eb8cb9d79e414df9` |
| `diffusion/cutedsl/utils.py` | `11439328fbc48f81547d181b049e0e662f1f308b58292b750bb2784ee39643fe` |
| `diffusion/cutedsl/common/norm_fusion.py` | `4cec65996625b63f4e7d09a1d877991bec23176039f54d82f133a5b39fae4fd3` |
| `diffusion/cutedsl/common/reduce.py` | `90b8a0ea9a857849799ae8c17e3306271b68156082fcc4c257b28a1d051e7e2e` |
| `tests/diffusion/test_fused_norm_scale_shift.py` (canonical grid reference) | `fe01710f49490cbda8a10fe94fdb793bd78dd9ba974e4efd706f13c0d69f71bf` |
| `include/sgl_kernel/tensor.h` | `b417f6ac51acd6f21a56b00338a4007781b237c4145dd37e87cd8dbb76060479` |
| `include/sgl_kernel/math.cuh` | `7679e20835c478de20826d9d5266bbf41c22099275ed01f44909a856eca25da1` |
| `include/sgl_kernel/runtime.cuh` | `4cf9f6edffb30a5fabc334bab5be67a746d0bc0778550b06a491c36c12ecae20` |
| `include/sgl_kernel/utils.cuh` | `6dcb47c69906cb32e1d014db21b459ff27e11408ad81449f6fdc5b86eac14582` |
| `include/sgl_kernel/vec.cuh` | `eba7c4cc8ca2e778fcaf37edb309682b46be3f99a3a4933abf848fad9ad1c880` |
| `include/sgl_kernel/warp.cuh` | `3254a491733811043f923423ea7eefec2d2697311bb520a0553ef3cdb177db57` |
| `include/sgl_kernel/utils.h` | `d0e4bf235e004b2cc61924b377f57e876ae6988bfadc61c6f0422306f4f17aac` |
| `include/sgl_kernel/type.cuh` | `f70277be81e61c2737875067a0d91f7ca2c7e2f806be1353319273c55a93e6a5` |
| `include/sgl_kernel/source_location.h` | `cd43da52aa20deafdffb0973bed1b101f634c728362aeef06959f0f5700f4973` |

Selection rationale: the two entry points live in `scale_residual_norm_scale_shift.py`, which imports
`common/norm_fusion.py` (statistics + BSFD broadcast/slicing), `common/reduce.py` (warp/CTA
reductions), and `diffusion/cutedsl/utils.py` (dtype map). `jit_kernel/utils.py` provides the
`load_jit` tvm-ffi build stack used to build the candidate through the same snapshot loader
(equivalent-builder rule). The eight `include/sgl_kernel` headers are the transitive include closure
needed by a native CUDA candidate built through that loader (`tensor.h`, `math.cuh`, `runtime.cuh`,
`utils.cuh`, `vec.cuh`, `warp.cuh` plus their internal includes `utils.h`, `type.cuh`, and
`source_location.h` — the latter pulled in by `utils.h` via a quoted relative include). The
canonical test file is vendored as the correctness-grid reference.

## Local Additions / Edits

- `csrc/.gitkeep` (local addition, empty): `jit_kernel/utils.py::_resolve_kernel_path()` requires both
  `include/` and `csrc/` directories to exist next to `utils.py` at import time. Upstream has a
  populated `csrc/`; none of its files are needed by this task family, so an empty marker directory
  is used instead of vendoring unrelated kernel sources.
- No copied file is modified. Zero diffs vs upstream blobs (sha256 manifest above).
- The import alias that lets the snapshot's absolute `sglang.jit_kernel.*` imports resolve without an
  installed SGLang (synthetic `sglang` package + minimal `sglang.utils.is_in_ci` shim required by
  `jit_kernel/utils.py`) lives OUTSIDE the snapshot in the task's local adapter
  (`baseline/binding.py`), so the vendored tree stays byte-identical to upstream.

## Runtime Dependencies (provided by the H200 container environment, not vendored)

- `torch`, `cuda-python` (`cuda.bindings.driver`), `nvidia-cutlass-dsl` (`cutlass`, `cutlass.cute`),
  `einops`, `tvm_ffi`.

## Parity Plan

- Structural parity: guaranteed by extraction method + sha256 manifest (this file).
- Behavioral parity (vendored snapshot vs real `sglang` at the same commit, same GPU): executed in the
  remote H200 phase as a two-process check over representative production signatures
  (`torch.equal` expected — identical code, identical device); results recorded in `docs/run_log.md`.
