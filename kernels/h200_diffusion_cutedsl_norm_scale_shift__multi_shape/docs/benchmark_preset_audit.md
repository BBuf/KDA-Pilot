# Benchmark Preset Audit — diffusion_cutedsl_norm_scale_shift (H200)

Audit of all 20 current SGLang diffusion benchmark presets against this task family's two entry
points (`fused_norm_scale_shift`, `fused_scale_residual_norm_scale_shift`). Source of truth:
`../../docs/diffusion_benchmark_shape_coverage.md` (rows = union of retained pre-reset captures and
the fresh B200/H200 captures of 2026-06-03). Every retained live shape row for this family is
present in `bench/workloads.json` (validated by `bench/check_workloads.py`).

## Presets with captured rows for this family (in `bench/workloads.json`)

- `qwen` — captured (retained rows): S=19/47/4096, D=3072, both entry points.
- `qwen-edit` — captured (retained rows): S=189/195, D=3072, both entry points.
- `firered-edit-1.0` — captured (retained rows): S=8424, D=3072, both entry points.
- `firered-edit-1.1` — captured (fresh native H200 run, ion8-h200, 2026-06-03): S=189/195/8424,
  D=3072, both entry points; signatures coincide with the qwen-edit/firered-edit-1.0 unique rows
  (recorded as model attribution on those rows).
- `joyai-edit` — captured (retained rows): S=997/1004/7904, D=4096, `fused_norm_scale_shift`.
- `hunyuanvideo` — captured (retained rows): S=55/27030/27085, D=3072 (residual variant for
  S=55/27030).
- `wan-ti2v` — captured (retained rows): S=18144, D=3072, bf16 + fp32 full-shape `[1,S,D]`
  scale/shift variants, residual variants incl. fp32 weight/bias affine row.
- `wan-t2v` — captured (retained rows): S=37800/75600, D=5120, fp32 + bf16 `[1,1,5120]`
  scale/shift variants, residual variants.
- `wan-i2v` — captured (retained rows): S=37044/74088, D=5120, fp32 + bf16 variants, residual
  variants.
- `mova-720p` — captured (retained rows): S=101 (D=1536), S=44100/176400 (D=5120), residual
  variants for S=101/44100.
- `helios` — captured (fresh native H200 run, ion8-h200, 2026-06-03): S=8640 (bf16 full-shape) and
  S=11040 (fp32 full-shape), D=5120, `fused_norm_scale_shift` only — the run emitted no
  `fused_scale_residual_norm_scale_shift` calls.

## Presets with live no-call proof for this family

- `zimage` — live no-call (fresh native B200 run, ion-b200, 2026-06-03, denoise 0.49s completed):
  emitted only RMSNorm, QKNorm+RoPE, and norm/tanh/mul/add target rows; zero calls to either
  entry point of this family.
- `ltx23-one-stage` — live no-call (fresh native H200 run, ion8-h200, 2026-06-03, denoise 87.11s
  completed): emitted only `ltx2_rotary.apply_ltx2_split_rotary_emb` rows; zero calls to this
  family.

## Presets with no-call evidence from retained full captures

- `ltx2` — no-call (retained full capture emitted only split-RoPE rows for this preset; the LTX2
  pipeline does not route through the CuTe DSL norm/scale/shift entry points).
- `ltx23-ti2v-two-stage` — no-call (retained full capture, split-RoPE rows only, same pipeline
  family as `ltx2`).
- `ltx23-two-stage` — no-call (retained full capture, high-resolution split-RoPE rows only).

## Blocked presets (neither capture nor no-call proof obtainable at audit time)

- `flux` — blocked: Hugging Face `403` gated-repo access on `black-forest-labs/FLUX.*`; the run
  also fell back to the diffusers backend, so no native shape row is valid. Do not mark complete
  until rerun with an authorized token and a native SGLang backend log.
- `flux2` — blocked: same gated-access failure as `flux`.
- `ltx23-two-stage-cfg-parallel` — blocked: H200 native run OOMed while loading the LTX-2.3
  two-stage transformer; B200 retry lacked a complete `Lightricks/LTX-2.3` snapshot cache.
- `hunyuan3d-shape` — blocked: native run fails at denoise step 0 with
  `_predict_noise_with_cfg() got an unexpected keyword argument 'cfg_policy'` (runtime-blocked;
  failed runs are not no-call evidence).

Per the standing decision for this task, blocked presets are recorded as blocked with no recapture
attempt; any new preset added after this audit must be freshly audited before workloads change
(workload changes after tuning require deleting results and remeasuring both sides).

Tally: 11 captured + 2 live no-call + 3 retained no-call + 4 blocked = 20 presets.
