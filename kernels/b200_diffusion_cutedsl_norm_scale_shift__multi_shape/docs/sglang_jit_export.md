# In-SGLang Export & Drop-in Replacement Test (promotion arbiter)

Run twice on 2026-06-04 on ion-b200 / sglang_bbuf / GPU 1 (idle), task-owned
editable checkout `$REMOTE_KDA_DIR/sglang_export` (git clone --shared of
`/sgl-workspace/sglang`, detached at the pinned baseline commit
`edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7`). The shared production checkout
was never modified. Driver script: `export/run_export_test.sh`; logs under
`$REMOTE_KDA_DIR/logs/export_*` and `$REMOTE_KDA_DIR/logs/export_rerun_r2.log`.

The numbers below are from the SECOND run, executed at the CURRENT candidate
source (joint src hash `b91d6e1abc50`, i.e. including the final-audit
comment-only `.cuh` header fix): the current `.cuh` was re-copied in-tree and
the official grid + smoke + fallback probe re-executed. Results are
statistically identical to the first run (the source delta carried no code
change).

## SGLang files touched (exact shipping shape)

| File | Change |
|---|---|
| `python/sglang/jit_kernel/csrc/diffusion/norm_scale_shift.cuh` | ADDED — the candidate device kernel (verbatim copy of `src/csrc/norm_scale_shift.cuh`) |
| `python/sglang/jit_kernel/diffusion/norm_scale_shift_native.py` | ADDED — in-tree dispatch glue (`export/norm_scale_shift_native.py`): operand classification, `load_jit` build, try-native-or-None, `set_native_enabled` toggle |
| `python/sglang/jit_kernel/diffusion/cutedsl/scale_residual_norm_scale_shift.py` | MODIFIED — minimal patch (`export/apply_patch.py`, pinned-hash-guarded): a try-native-first block at the top of each public custom-op BODY; the `@torch.library.custom_op` + `@register_fake` registrations are untouched |

## Preserved entry points

- `sglang::fused_norm_scale_shift` and
  `sglang::fused_scale_residual_norm_scale_shift` remain the registered
  custom ops; `torch.ops.sglang.*` resolution asserted in the smoke run.
- Unsupported signatures fall through to the ORIGINAL CuTe-DSL body inside
  the same op (probe: `norm_type="rms"` output bitwise-identical with the
  native path enabled vs disabled).

## load_jit invocation (in-tree)

- Module: `load_jit("diffusion_norm_scale_shift_native", <src-sha1-12>,
  cuda_files=[csrc/diffusion/norm_scale_shift.cuh], cuda_wrappers=<10 combos>)`
- Template wrappers: the 10 production combos listed in `docs/dispatch.md`
  (`kda_norm_scale_shift::NormScaleShiftKernel<...>::run`,
  `ScaleResidualNormScaleShiftKernel<...>::run/run_nogate`,
  `ScaleResidualNormScaleShiftAffineKernel<...>::run`).
- Flags: SGLang `jit_kernel` defaults only (arch flag + `-std=c++20 -O3
  --expt-relaxed-constexpr`); no `--use_fast_math`; no
  `torch.utils.cpp_extension`.

## Results

1. **Official SGLang oracle**: `python/sglang/jit_kernel/tests/diffusion/
   test_fused_norm_scale_shift.py` on the patched checkout —
   **147 passed** (full upstream grid: 5 shapes x fp16/bf16/fp32 x layer/rms
   x affine D/NAT x 9 index modes + gate modes + validation tests), i.e. the
   drop-in is correct through the real public ops for both native-routed and
   fallback-routed cases.
2. **Symmetric same-op A/B smoke** (identical public op, in-body toggle;
   median of 50 interleaved iterations; `export/smoke_bench.py`; re-run at
   the current source):

   | Case (bucket) | original us | native us | speedup |
   |---|---|---|---|
   | nss 176400x5120 bf16 bcast (huge video) | 1127.5 | 836.1 | 1.348x |
   | nss 11040x5120 per-token fp32 (parity bucket) | 168.7 | 151.2 | 1.116x |
   | nss 47x3072 bf16 (tiny) | 94.6 | 64.7 | 1.463x |
   | srnss 8424x3072 gated bf16 (mid) | 118.1 | 93.0 | 1.270x |
   | srnss 37800x5120 wan affine | 423.6 | 323.4 | 1.310x |
   | srnss 44100x5120 gnone bf16 (huge) | 389.5 | 326.8 | 1.192x |

   Native outputs matched the original CuTe outputs within the SGLang test
   tolerance on every smoke case before timing (correctness echo).
3. **Fallback verification**: rms probe bitwise-identical (native glue
   returns None; original path executes).

## Verdict

Parity-or-speedup confirmed on the exact shipping integration, with the
production custom-op contract (registration, fake impls, output allocation,
stream behavior) preserved. The in-tree numbers corroborate the final
kernel-folder benchmark (`benchmark.csv` **r6-final**: geomean 1.3022x
end-to-end / 1.2878x device over 39 unique signatures, joint source hash
d0f645a016cb). The in-tree smoke was last executed at b91d6e1abc50; the only
delta to d0f645a016cb is the register.py arity-routing fix in the LOCAL
registration shim, which is not part of the in-tree integration surface
(the in-tree glue has its own dispatch module), so the smoke remains valid.
