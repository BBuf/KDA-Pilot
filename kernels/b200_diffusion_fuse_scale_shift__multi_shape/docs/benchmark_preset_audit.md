# Benchmark Preset Audit — b200_diffusion_fuse_scale_shift__multi_shape

Audit target: the 20 presets defined by the current SGLang diffusion
benchmark/profile helper (per `../../docs/diffusion_benchmark_shape_coverage.md`,
which mirrors `sglang-diffusion-benchmark-profile/benchmark-and-profile.md`):
`flux`, `flux2`, `qwen`, `qwen-edit`, `zimage`, `wan-t2v`, `wan-ti2v`, `ltx2`,
`ltx23-ti2v-two-stage`, `wan-i2v`, `ltx23-one-stage`, `ltx23-two-stage`,
`ltx23-two-stage-cfg-parallel`, `hunyuanvideo`, `mova-720p`, `helios`,
`joyai-edit`, `firered-edit-1.0`, `firered-edit-1.1`, `hunyuan3d-shape`.

Audit date: 2026-06-04. Evidence base: the coverage doc's retained rows for
the `diffusion_fuse_scale_shift__multi_shape` family plus its
"Fresh Capture Audit: 2026-06-03" and "Known Gaps To Audit" sections.

## Presets covered by retained live shape rows (in `bench/workloads.json`)

| Preset | Rows in workloads.json |
|--------|------------------------|
| `qwen` | `qwen_s{19,47,4096}_c3072_bcast11` (scale_constant=0 captured) |
| `qwen-edit` | `qwen_edit_s{189,195,8424}_c3072_bcast11`, `qwen_edit_s8424_c3072_full3d`, `qwen_edit_gated_s8424_c3072`, `qwen_edit_resgated_s8424_c3072` |
| `firered-edit-1.0` | `firered10_s8424_c3072_bcast11` |
| `firered-edit-1.1` | `firered11_s{189,195,8424}_c3072_bcast11` (fresh capture 2026-06-03 on ion8-h200, 64 target-kernel rows incl. Triton scale-shift; scale_constant=0 captured) |
| `hunyuanvideo` | `hunyuanvideo_s{55,27030,27085}_c3072_bcast2d` |
| `wan-ti2v` | `wan_ti2v_s18144_c3072_full_nc_fp32` (non-contiguous fp32 scale/shift) |
| `wan-t2v` | `wan_t2v_s37800_c5120_bcast11_fp32` |
| `wan-i2v` | `wan_i2v_s37044_c5120_bcast11_fp32` |

Field notes recorded in `bench/workloads.json`:

- `scale_constant` is captured only for `qwen` and `firered-edit-1.1` (both 0).
  All other EP1 rows use the upstream default `1.0` and are marked
  `scale_constant_source: "default"`; if a future live capture reports a
  different value for those presets, the row must be re-frozen and both sides
  remeasured.
- The coverage rows for the gated `qwen-edit` entries list no `weight`/`bias`
  tensors, so production rows use `weight=None, bias=None`
  (`weight_bias_source: "coverage-rows-omit-affine"`); with-affine forms are
  covered by regression riders and the canonical grid in `bench/correctness.py`.
- Production `eps` is not stated by the coverage rows; rows use the contract
  grid value `1e-6` (`eps_source: "contract-default"`).
- The `wan-ti2v` non-contiguous fp32 layout is constructed deterministically as
  `layout: "chunk2"`: parent fp32 tensor `[1, S, 2*C]` sliced `[:, :, :C]`,
  giving strides `(2*S*C, 2*C, 1)` — last dimension contiguous with a doubled
  row stride, the chunked-modulation pattern.

## Presets not represented by retained rows — disposition

| Preset | Disposition for this family |
|--------|------------------------------|
| `helios` | **Live no-call proof** (2026-06-03, ion8-h200): native run completed (denoise 80.04s) and emitted only `norm.norm_infer` and `scale_residual_norm_scale_shift.fused_norm_scale_shift` target rows — the coverage doc names `helios` explicitly as a live no-call proof for Triton scale-shift. |
| `zimage` | **Live no-call evidence** (2026-06-03, ion-b200): native run completed (denoise 0.49s, 17 kernel-call rows) and captured only RMSNorm, QKNorm+RoPE, and Z-Image norm/tanh/mul/add shapes — no Triton scale-shift rows. |
| `ltx23-one-stage` | **Live no-call evidence** (2026-06-03, ion8-h200): native run completed (denoise 87.11s) and emitted only `ltx2_rotary.apply_ltx2_split_rotary_emb` rows — no Triton scale-shift rows. |
| `ltx2` | Retained-only no-call: pre-reset retained captures place this preset in the rotary-embedding family only; no scale-shift rows exist and no fresh 2026-06-03 run was made. Recapture would be needed only if a future helper change routes LTX-2 modulation through these entry points. |
| `ltx23-ti2v-two-stage` | Retained-only no-call: same status as `ltx2` (rotary-family rows only). |
| `ltx23-two-stage` | Retained-only no-call: same status as `ltx2` (rotary-family rows only). |
| `ltx23-two-stage-cfg-parallel` | **Blocked** (carried from coverage doc): H200 OOM while loading the LTX-2.3 two-stage transformer; B200 retry lacked a complete model cache. Not a valid capture and not no-call evidence. |
| `flux` / `flux2` | **Blocked** (carried from coverage doc): Hugging Face 403 gated-repo access plus diffusers-backend fallback; no valid shape rows. Do not mark complete until rerun with an authorized token and a native SGLang backend log. |
| `mova-720p` | Retained-only no-call: skill-only preset; retained captures place it in other kernel families; no scale-shift rows and no fresh run. |
| `joyai-edit` | Retained-only (carried from coverage doc): "remains retained-only unless recaptured"; its retained rows belong to other families (e.g. QKNorm+RoPE) and no scale-shift rows exist. |
| `hunyuan3d-shape` | **Runtime-blocked** (carried from coverage doc): `_predict_noise_with_cfg() got an unexpected keyword argument 'cfg_policy'` at step 0 on H200; B200 retry reached no target kernel row. Explicitly *not* to be treated as no-call evidence. |

## Conclusion

Every retained live shape row for this family and arch is present in
`bench/workloads.json` (19 production rows), and every current preset missing
from the retained rows has a live no-call note, a retained-only no-call note,
or an explicit blocked status carried from the canonical 2026-06-03 audit.
The task satisfies the readiness gate for optimization. Workloads are frozen
as of this audit; any change after tuning starts requires deleting results and
remeasuring both baseline and candidate.
