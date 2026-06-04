# Benchmark Preset Audit — `group_norm_silu` family on H200

Task entry points: `triton_group_norm_silu`, `apply_group_norm_silu`
(`python/sglang/jit_kernel/diffusion/{triton/,}group_norm_silu.py`).

Audit baseline: upstream SGLang `main` @ `133254086bf1f5b887c8c99d311719102d58a7eb`
(resolved 2026-06-04T15:16:13Z; see `docs/baseline_source.md`).

## Method

1. **Mechanical call-site enumeration** at the resolved commit:

   ```bash
   git grep -l "group_norm_silu" 1332540 -- python/sglang/multimodal_gen/runtime/models/
   ```

   Exactly **two** production modules reference the entry points:
   - `runtime/models/vaes/hunyuanvae.py` (HunyuanVideo VAE decode path), and
   - `runtime/models/upsampler/latent_upsampler.py` (LTX-2 spatial latent
     upsampler; calls added by upstream #26045 `f651b48764`, merged 2026-06-02).

   No other VAE or model module (`wanvae.py`, `autoencoder_kl_qwenimage.py`,
   `autoencoder_kl_flux2.py`, `ltx_2_vae.py`, `hunyuan3d_vae.py`,
   `autoencoder_dc.py`, `autoencoder.py`, `zimage`/`helios`/`mova`/`joy`
   model stacks) references them. A preset can therefore reach this kernel
   family only by loading one of those two modules.

2. **Live evidence** from the 2026-06-03 native capture sweep recorded in
   `../../docs/diffusion_benchmark_shape_coverage.md` (run with #26045 already
   in tree, merged 2026-06-02).

3. **Fresh live captures** (this round, per user decision DEC-5): the three
   runnable two-stage LTX presets get reduced-step live captures on ion8-h200
   before the workload freeze. Upsampler GroupNorm shapes depend on
   width/height/frames, not step count, so reduced `--num-inference-steps`
   captures are shape-faithful; presets run at their canonical resolutions.

## Evidence classes

- `retained-rows` — pre-reset live capture rows retained in git history; they
  anchor `bench/workloads.json`.
- `live-no-call` — a completed native run on 2026-06-03 emitted no rows for
  these entry points.
- `blocked` — the preset cannot currently produce a valid native run
  (documented blocker; not treated as no-call proof).
- `static-no-call` — source-inspection proof at the resolved commit: the
  preset's pipeline loads neither `hunyuanvae.py` nor `latent_upsampler.py`.
- `live-capture-pending` — source-REACHABLE (loads `latent_upsampler.py` via
  `LTX2TwoStagePipeline`); fresh live capture scheduled this round (DEC-5).

## Per-preset audit (20 presets)

| Preset | Evidence class | Evidence |
|---|---|---|
| hunyuanvideo | retained-rows | 96 retained rows (48 unique fp16 signatures × 2 entries) from the pre-reset ion8-h200 capture; source: `runtime/models/vaes/hunyuanvae.py` via `configs/pipeline_configs/hunyuan.py`. Anchors `bench/workloads.json`. |
| zimage | live-no-call | 2026-06-03 native B200 run completed (denoise 0.49s, 17 kernel rows) — zero `group_norm_silu` rows. Static cross-check: Z-Image stack (`configs/pipeline_configs/zimage.py`) loads neither calling module. |
| helios | live-no-call | 2026-06-03 native H200 run completed (denoise 80.04s, 20 target rows: `norm_infer` + `fused_norm_scale_shift` only). Static cross-check: `configs/pipeline_configs/helios.py` loads neither calling module. |
| firered-edit-1.1 | live-no-call | 2026-06-03 native H200 run completed (denoise 24.17s, 64 rows: QKNorm+RoPE, cutedsl norm/scale/shift, Triton scale-shift only). Static cross-check: pipeline loads neither calling module. |
| ltx23-one-stage | live-no-call | 2026-06-03 native H200 run completed (denoise 87.11s, 90 split-rotary rows) — zero `group_norm_silu` rows. Consistent with source: one-stage runs build no `LTX2UpsampleStage`, and `ltx_2_vae.py` (decode) does not call the entry points. |
| flux | blocked | Hugging Face 403 gated-repo on `black-forest-labs/FLUX.*` + native-backend gate fell back to diffusers (2026-06-03). Static note: `configs/pipeline_configs/flux.py` loads neither calling module, but no completed native run exists, so this stays `blocked`, not no-call. |
| flux2 | blocked | Same gated-403 blocker as `flux` (2026-06-03). Static note as above (`autoencoder_kl_flux2.py` has no entry-point reference). |
| hunyuan3d-shape | blocked | 2026-06-03 H200 native run failed at step 0 (`_predict_noise_with_cfg() ... 'cfg_policy'`); B200 retry reached no target rows. Static note: Hunyuan3D uses `hunyuan3d_vae.py` (no entry-point reference) — but runtime-blocked stays the verdict per the shape-coverage doc. |
| ltx23-two-stage-cfg-parallel | blocked | 2026-06-03 H200 run OOMed loading the LTX-2.3 two-stage transformer; B200 retry lacked the model cache. Source-REACHABLE (LTX2TwoStagePipeline → upsampler), so this blocker must be re-audited when the preset becomes runnable. |
| ltx2 | live-capture-pending | Source-REACHABLE: preset runs `LTX2TwoStagePipeline` (`Lightricks/LTX-2`, 768x512, 121 frames, 2 GPUs, cfg-parallel) → `LTX2UpsampleStage` → `latent_upsampler.py:118/249/259` `apply_group_norm_silu`. Fresh reduced-step capture scheduled (DEC-5); model snapshot may need download on ion8-h200. |
| ltx23-ti2v-two-stage | live-capture-pending | Source-REACHABLE: `LTX2TwoStagePipeline` (`Lightricks/LTX-2.3`, 768x512, 121 frames, 2 GPUs, cfg-parallel-size 2) → upsampler. Fresh reduced-step capture scheduled (DEC-5); LTX-2.3 cached on ion8-h200 (one-stage ran 2026-06-03). |
| ltx23-two-stage | live-capture-pending | Source-REACHABLE: `LTX2TwoStagePipeline` (`Lightricks/LTX-2.3`, 1536x1024, 121 frames, 2 GPUs) → upsampler. Fresh reduced-step capture scheduled (DEC-5); memory headroom to be checked (the cfg-parallel variant OOMed; this variant lacks the cfg duplication). |
| qwen | static-no-call | `configs/pipeline_configs/qwen_image.py` → `autoencoder_kl_qwenimage.py`; neither it nor any module in the Qwen-Image pipeline references the entry points (mechanical enumeration above). |
| qwen-edit | static-no-call | Same Qwen-Image pipeline family/VAE as `qwen`; no calling module loaded. |
| wan-t2v | static-no-call | `configs/pipeline_configs/wan.py` → `wanvae.py`; no entry-point reference in the Wan stack. |
| wan-ti2v | static-no-call | Same Wan pipeline family/VAE; no calling module loaded. |
| wan-i2v | static-no-call | Same Wan pipeline family/VAE; no calling module loaded. |
| mova-720p | static-no-call | `configs/pipeline_configs/mova.py`; MOVA stack references neither calling module. |
| joyai-edit | static-no-call | `configs/pipeline_configs/joy_image.py`; Joy stack references neither calling module. |
| firered-edit-1.0 | static-no-call | Same pipeline family as `firered-edit-1.1` (live no-call above); no calling module loaded. |

## Round outcome (to complete before workload freeze)

- [ ] `ltx2` capture on ion8-h200 → rows or live no-call recorded here.
- [ ] `ltx23-ti2v-two-stage` capture on ion8-h200 → rows or live no-call recorded here.
- [ ] `ltx23-two-stage` capture on ion8-h200 → rows or live no-call recorded here.
- Captured LTX upsampler shapes (if any) join `bench/workloads.json` as
  `production=false` diagnostic rows with candidate correctness coverage; the
  production headline remains the 48 retained HunyuanVideo signatures (DEC-2,
  DEC-5).
