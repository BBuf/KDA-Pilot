# Baseline Source Lineage — `baseline/`

## Upstream

- Project: SGLang — https://github.com/sgl-project/sglang
- Authoritative runtime checkout (the one the container executes): `/sgl-workspace/sglang` inside `sglang_bbuf` on `ion-b200`, commit `edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7` (branch `main`, clean tree, pip editable `sglang 0.0.0.dev1+gedb1b3f8f`).
- Local recovery checkout used to materialize the copy: `/Users/bbuf/工作目录/Common/sglang` @ `0689ba84b8` (branch `kda/group_norm_silu_export`).
- Equivalence proof: sha256 of every copied source file is IDENTICAL between the two checkouts (verified 2026-06-04; full hash table in `docs/env_b200_snapshot.md`).

## Copied files (upstream path → local path, upstream sha256)

| Upstream (python/sglang/jit_kernel/diffusion/cutedsl/) | Local | sha256 (upstream, both checkouts) |
|---|---|---|
| `norm_tanh_mul_add_norm_scale.py` | `baseline/norm_tanh_mul_add_norm_scale.py` | `b4a77d302827f3060a595030ef683c725e13cdb15e3d1e574680b4af09532769` |
| `common/norm_fusion.py` | `baseline/common/norm_fusion.py` | `4cec65996625b63f4e7d09a1d877991bec23176039f54d82f133a5b39fae4fd3` |
| `common/reduce.py` | `baseline/common/reduce.py` | `90b8a0ea9a857849799ae8c17e3306271b68156082fcc4c257b28a1d051e7e2e` |
| `utils.py` | `baseline/utils.py` | `11439328fbc48f81547d181b049e0e662f1f308b58292b750bb2784ee39643fe` |

`baseline/__init__.py` and `baseline/common/__init__.py` are new local files (package markers / re-exports), not upstream copies.

## Local edits (exhaustive)

1. `baseline/norm_tanh_mul_add_norm_scale.py`
   - `from sglang.jit_kernel.diffusion.cutedsl.common.norm_fusion import ...` → `from .common.norm_fusion import ...`
   - `from sglang.jit_kernel.diffusion.cutedsl.utils import ...` → `from .utils import ...`
   - Removed `@torch.library.custom_op("sglang::fused_norm_tanh_mul_add", mutates_args=())` and `@torch.library.custom_op("sglang::fused_norm_tanh_mul_add_norm_scale", mutates_args=())` decorators — the baseline copy exposes RAW callables so local A/B comparisons go through the same low-overhead entry ABI on both sides. The registered-custom-op layer is exercised only in the final in-SGLang drop-in test (the promotion arbiter), where it is preserved on BOTH sides.
   - Removed the two `register_fake` helper functions (`_fused_norm_tanh_mul_add_fake`, `_fused_norm_tanh_mul_add_norm_scale_fake`) — they attach to the removed custom-op objects.
   - Added a provenance header comment.
2. `baseline/common/norm_fusion.py`
   - `from sglang.jit_kernel.diffusion.cutedsl.common.reduce import ...` → `from .reduce import ...`
   - Added a provenance header comment.
3. `baseline/common/reduce.py`, `baseline/utils.py`
   - Verbatim copies; only a provenance header comment added.

No other changes: validators (`validate_3d`, `validate_weight_bias`), the `D % 256 == 0 && D <= 8192` gate, broadcast handling, compile-cache keying, `cute.compile(..., options="--enable-tvm-ffi")`, stream handling, and kernel code are unmodified.

## Recovered public contract notes (from upstream source, relevant to tests)

- `scale`/`shift` (and `scale2`) MUST be 3-D `[1|B, 1|S, D]` with last-dim stride 1 — `validate_3d` rejects 1-D/2-D/4-D inputs at the public boundary, so index modes `1, D, 1D, BD, BF1D` are contract-REJECTION cases for these two ops (the broader mode list belongs to the sister `fused_norm_scale_shift` family which shares the helpers).
- `weight`/`bias` (and `weight2`/`bias2`): `None` or `[D]`, last-dim stride 1.
- Supported dtypes: fp16 / bf16 / fp32. `norm_type`: `"layer"` or `"rms"`. `eps` default `1e-5`.
- Math: `y = round_to_out_dtype(norm(x)) * tanh(scale) + shift` (norm reductions in fp32, normalized result rounded to the I/O dtype before modulation); second variant additionally `y2 = norm2(y_rounded) * (1 + scale2)`, returns `(y, y2)`.
- Runtime deps of the copy: torch, cutlass / cutlass.cute (nvidia-cutlass-dsl), cuda.bindings (cuda-python), einops. No `sglang` import at runtime.
