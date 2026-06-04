# Baseline Source Lineage

## Upstream

- Repo: local SGLang checkout `/Users/bbuf/工作目录/Common/sglang` (sgl-project/sglang fork, KDA development state)
- Pinned commit: `0689ba84b88c991684b0f99ee9b50c3ce485b483`
  (`[KDA] wire direct triton_group_norm_silu public entry to the candidate dispatcher`)
- Working tree state for the copied paths at vendoring time: clean (no local modifications under
  `python/sglang/jit_kernel/diffusion/cutedsl/`)
- Vendoring date: 2026-06-04

## Copied Files

| Upstream path (under `python/sglang/jit_kernel/diffusion/cutedsl/`) | Vendored path | Edits |
|---|---|---|
| `norm_tanh_mul_add_norm_scale.py` | `baseline/norm_tanh_mul_add_norm_scale.py` | 4 lines (see below) |
| `common/norm_fusion.py` | `baseline/common/norm_fusion.py` | 1 line (see below) |
| `common/reduce.py` | `baseline/common/reduce.py` | none (verbatim) |
| `utils.py` | `baseline/utils.py` | none (verbatim) |
| — (new) | `baseline/__init__.py` | new file: re-exports the two entry points |
| — (new) | `baseline/common/__init__.py` | new file: empty package marker |

## Exact Local Edits

All edits are import-path rewrites or custom-op namespace renames. No computational,
validation, dispatch, or allocation logic was changed.

`baseline/norm_tanh_mul_add_norm_scale.py`:

1. `from sglang.jit_kernel.diffusion.cutedsl.common.norm_fusion import (` → `from .common.norm_fusion import (`
2. `from sglang.jit_kernel.diffusion.cutedsl.utils import TORCH_TO_CUTE_DTYPE, WARP_SIZE` → `from .utils import TORCH_TO_CUTE_DTYPE, WARP_SIZE`
3. `@torch.library.custom_op("sglang::fused_norm_tanh_mul_add", mutates_args=())` → `@torch.library.custom_op("kda_baseline::fused_norm_tanh_mul_add", mutates_args=())`
4. `@torch.library.custom_op("sglang::fused_norm_tanh_mul_add_norm_scale", mutates_args=())` → `@torch.library.custom_op("kda_baseline::fused_norm_tanh_mul_add_norm_scale", mutates_args=())`

`baseline/common/norm_fusion.py`:

5. `from sglang.jit_kernel.diffusion.cutedsl.common.reduce import (` → `from .reduce import (`

Rationale for edits 3-4: the vendored module must be importable in the same process as the
real `sglang` package (parity check), and `torch.library.custom_op` forbids registering the
same `sglang::` op name twice. The rename keeps the IDENTICAL custom-op + fake-registration
wrapper machinery (symmetric host layer), only the namespace string differs.

## Vendored File Hashes (sha256)

```
1d438a5461f5cf409247dbcea38e949adc8574ce0aaee245bf94dabbba80b657  baseline/__init__.py
3202060d00f8cc08ea46cd20bad6e6cfd08258dbb23e14c1bf3e87dc87345bb7  baseline/norm_tanh_mul_add_norm_scale.py
11439328fbc48f81547d181b049e0e662f1f308b58292b750bb2784ee39643fe  baseline/utils.py
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  baseline/common/__init__.py
383e4d58cb8e93f6677270bab19dcbe1308cd2e7112d2dde8a5b17a30e5ac26e  baseline/common/norm_fusion.py
90b8a0ea9a857849799ae8c17e3306271b68156082fcc4c257b28a1d051e7e2e  baseline/common/reduce.py
```

## Third-Party Runtime Dependencies (unvendored)

`torch`, `cutlass` / `cutlass.cute` (nvidia-cutlass-dsl), `cuda.bindings.driver`
(cuda-python), `einops`. All are provided by the `sglang_bbuf` container environment.
The unmodified `sglang` package may be imported read-only in the same process
(parity check / build utilities); patching, monkey-patching, or installing into any
SGLang checkout at correctness/benchmark runtime is forbidden.

## Parity Check

`tests/test_baseline_parity.py` compares the vendored entry points against the
`sglang` package entry points at the pinned commit on the 4 captured production
signatures (fixed seeds) and asserts bitwise equality (`torch.equal`), plus
matching ValueError behavior on out-of-domain D. Run inside the `sglang_bbuf`
container on an idle H200 (see `docs/captured_shapes_h200.md` for the signatures).

## Recovered Public Contract Notes (from the pinned source)

- `fused_norm_tanh_mul_add(x, weight, bias, scale, shift, norm_type, eps=1e-5) -> Tensor`:
  `y = norm(x) * tanh(scale) + shift`.
- `fused_norm_tanh_mul_add_norm_scale(x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps=1e-5) -> (y, y2)`:
  additionally `y2 = norm2(y) * (1 + scale2)` (no tanh on `scale2`).
- IMPORTANT: `validate_3d` runs BEFORE `broadcast_tensor_for_bsfd`, so `scale`/`shift`/`scale2`
  for THIS kernel pair must be 3-D `[1|B, 1|S, D]` with unit stride on D. 1-D/2-D/4-D layouts
  from the sister-family grid (`1`, `D`, `1D`, `BD`, `BF1D`) raise ValueError at the public
  boundary of these two ops. The 9-layout grid in the task prompt describes the shared BSFD
  helper, not this pair's public contract.
- `weight`/`bias`/`weight2`/`bias2`: `None` or `[D]`, unit stride.
- Domain: `D % 256 == 0` and `D <= 8192`, dtype in {fp16, bf16, fp32}, else ValueError.
- Outputs allocated inside via `torch.empty_like(x)`; launch on `torch.cuda.current_stream()`.
- Compile-time specialization key: `(norm_type, per-tensor (dtype, ndim, D))`; runtime values
  otherwise. Grid `[B*S, 1, 1]`, block `[D//256*32, 1, 1]` (D=3840 → 480 threads / 15 warps).
