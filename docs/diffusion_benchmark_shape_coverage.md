# Diffusion Benchmark Shape Coverage

This note maps the standalone diffusion kernel tasks to the SGLang diffusion
benchmark/profile presets in:

`/Users/bbuf/工作目录/Common/sglang/python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/benchmark-and-profile.md`

The current helper script defines 20 presets:

`flux`, `flux2`, `qwen`, `qwen-edit`, `zimage`, `wan-t2v`, `wan-ti2v`,
`ltx2`, `ltx23-ti2v-two-stage`, `wan-i2v`, `ltx23-one-stage`,
`ltx23-two-stage`, `ltx23-two-stage-cfg-parallel`, `hunyuanvideo`,
`mova-720p`, `helios`, `joyai-edit`, `firered-edit-1.0`,
`firered-edit-1.1`, `hunyuan3d-shape`.

The rows below are the union of retained pre-reset shape captures and the
fresh B200/H200 captures run on 2026-06-03. Tensor shapes are
architecture-independent for these kernels, but each B200/H200 task must still
benchmark on its own target GPU. A workload is not complete until
`bench/workloads.json` either contains every relevant row below or records a
live no-call proof for current presets that do not exercise the target entry
point.

## Fresh Capture Audit: 2026-06-03

Valid native SGLang captures:

- `zimage` on B200 (`ion-b200`): native run completed, denoise `0.49s`, 17
  kernel-call rows. It captured RMSNorm, QKNorm+RoPE, and Z-Image
  norm/tanh/mul/add shapes.
- `ltx23-one-stage` on H200 (`ion8-h200`): native run completed, denoise
  `87.11s`, 90 `ltx2_rotary.apply_ltx2_split_rotary_emb` rows.
- `firered-edit-1.1` on H200 (`ion8-h200`): native run completed, denoise
  `24.17s`, 64 target-kernel rows for QKNorm+RoPE, cutedsl norm/scale/shift,
  and Triton scale-shift.
- `helios` on H200 (`ion8-h200`): native run completed, denoise `80.04s`, 20
  target-kernel rows for LayerNorm and
  `scale_residual_norm_scale_shift.fused_norm_scale_shift`.

Invalid or blocked runs, not usable as shape coverage:

- `flux` and `flux2`: both failed with Hugging Face `403` gated-repo access on
  `black-forest-labs/FLUX.*`; the log also hit the native-backend gate
  (`model fell back to the diffusers backend`), so no shape row is valid.
- `ltx23-two-stage-cfg-parallel`: H200 run reached native loading but failed
  before denoise with H200 OOM while loading the LTX-2.3 two-stage transformer.
  B200 was retried for larger memory, but the exact `Lightricks/LTX-2.3`
  snapshot was not cached there and the download was still incomplete after
  more than ten minutes, so the retry was stopped with only install rows.
- `hunyuan3d-shape`: H200 native run reached
  `Hunyuan3DShapeDenoisingStage` but failed at step 0 with
  `_predict_noise_with_cfg() got an unexpected keyword argument 'cfg_policy'`.
  B200 was retried on a different SGLang commit but did not reach any target
  kernel row after several minutes and was stopped. Treat this preset as
  runtime-blocked, not as a no-call proof.

## Known Gaps To Audit

- `firered-edit-1.1`, `ltx23-one-stage`, `helios`, and `zimage` were
  successfully recaptured on 2026-06-03 and the relevant rows are folded into
  the sections below.
- `helios` is a live no-call proof for QKNorm+RoPE and Triton scale-shift in
  the current helper: the native run completed and emitted only
  `norm.norm_infer` plus `scale_residual_norm_scale_shift` target rows.
- `firered-edit-1.1` is a live no-call proof for `norm.norm_infer`,
  `rmsnorm_onepass`, and `norm_tanh_mul_add*`: the native run completed and
  emitted only QKNorm+RoPE, cutedsl norm/scale/shift, and Triton scale-shift
  target rows.
- `flux` and `flux2` remain blocked by gated Hugging Face access. Do not mark
  their shapes complete until rerun with an authorized token and a native
  SGLang backend log.
- `ltx23-two-stage-cfg-parallel` remains blocked. The H200 run failed with OOM;
  a B200 retry needs a completed `Lightricks/LTX-2.3` cache before it can be a
  valid shape capture.
- `hunyuan3d-shape` remains blocked by current SGLang runtime behavior. Do not
  treat the failed runs as no-call evidence.

## `diffusion_qknorm_rope__multi_shape`

Entry point: `qknorm_rope.fused_inplace_qknorm_rope`.

Required retained live shape rows:

- `qwen`: `q/k=[19,24,128]`, `[47,24,128]`, `[4096,24,128]` bf16;
  `cos_sin_cache=[S,128]` fp32; `positions=[S]` int64; `eps=1e-6`.
- `qwen-edit`: `q/k=[189,24,128]`, `[195,24,128]`, `[8424,24,128]` bf16;
  `cos_sin_cache=[S,128]` fp32; `positions=[S]` int64; `eps=1e-6`.
- `zimage`: `q/k=[32,30,128]`, `[4096,30,128]`, `[4128,30,128]` bf16;
  `cos_sin_cache=[S,128]` fp32; `positions=[S]` int64; `eps=1e-5`.
- `joyai-edit`: `q/k=[7904,32,128]` bf16; `cos_sin_cache=[7904,128]`
  fp32; `positions=[7904]` int64; `eps=1e-6`.
- `firered-edit-1.1`: `q/k=[189,24,128]`, `[195,24,128]`,
  `[8424,24,128]` bf16; `cos_sin_cache=[S,128]` fp32; `positions=[S]`
  int64; `eps=1e-6`.

Current-preset audit status: `helios` was live no-call; `firered-edit-1.1`
was captured; `flux` and `flux2` are blocked by gated access; `hunyuan3d-shape`
is runtime-blocked. `firered-edit-1.0` remains covered only by retained rows
unless recaptured.

## `diffusion_norm_infer__multi_shape`

Entry points:

- `norm.norm_infer`
- `rmsnorm_onepass.triton_one_pass_rms_norm`

Required retained live shape rows:

- `helios` LayerNorm: `x=[8640,5120]` fp32, `weight=[5120]` fp32,
  `bias=[5120]` fp32, `eps=1e-6`, `is_rms_norm=False`.
- `zimage` RMSNorm: `x=[4096,128]` and `[16384,128]` bf16,
  `weight=[128]` bf16, `eps=1e-6`.
- `hunyuanvideo` RMSNorm: `x=[1320,128]`, `[648720,128]`,
  `[650040,128]` bf16, `weight=[128]` bf16, `eps=1e-6`.

Current-preset audit status: `firered-edit-1.1` was live no-call for both
entry points; `flux2` is blocked by gated access; `hunyuan3d-shape` is
runtime-blocked.

## `diffusion_cutedsl_norm_tanh_mul_add__multi_shape`

Entry points:

- `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add`
- `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale`

Required retained live shape rows:

- `zimage`: `hidden=[1,4096,3840]` and `[1,4128,3840]` bf16,
  norm weight `[3840]` bf16, modulation `[1,1,3840]` bf16, residual/output
  `[1,S,3840]` bf16, `norm_type=rms`, `eps=1e-5`.

Current-preset audit status: `firered-edit-1.1`, `helios`, and
`ltx23-one-stage` were live no-call for these two entry points;
`hunyuan3d-shape` is runtime-blocked.

## `diffusion_cutedsl_norm_scale_shift__multi_shape`

Entry points:

- `scale_residual_norm_scale_shift.fused_norm_scale_shift`
- `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift`

Required retained live shape rows:

- `qwen`: `hidden=[1,S,3072]` bf16 for `S=19,47,4096`; scale/shift are
  `[1,3072]` or `[1,1,3072]` bf16.
- `qwen-edit`: `hidden=[1,S,3072]` bf16 for `S=189,195`; scale/shift are
  `[1,3072]` bf16.
- `firered-edit-1.0`: `hidden=[1,8424,3072]` bf16; scale/shift are
  `[1,1,3072]` bf16.
- `joyai-edit`: `hidden=[1,S,4096]` bf16 for `S=997,1004,7904`;
  scale/shift are `[1,4096]` bf16.
- `hunyuanvideo`: `hidden=[1,S,3072]` bf16 for `S=55,27030,27085`;
  scale/shift are `[1,3072]` bf16.
- `wan-ti2v`: `hidden=[1,18144,3072]` bf16; scale/shift include both bf16
  `[1,18144,3072]` and fp32 `[1,18144,3072]` variants.
- `wan-t2v`: `hidden=[1,37800,5120]` and `[1,75600,5120]` bf16;
  scale/shift include fp32 `[1,1,5120]` and bf16 `[1,1,5120]` variants.
- `wan-i2v`: `hidden=[1,37044,5120]` and `[1,74088,5120]` bf16;
  scale/shift include fp32 `[1,1,5120]` and bf16 `[1,1,5120]` variants.
- `mova-720p`: `hidden=[1,101,1536]`, `[1,44100,5120]`,
  `[1,176400,5120]` bf16.
- `helios` `fused_norm_scale_shift`: `hidden=[1,8640,5120]` bf16 with
  bf16 full-shape scale/shift, and `hidden=[1,11040,5120]` bf16 with fp32
  full-shape scale/shift; residual args are `None`; `norm_type=layer`,
  `eps=1e-6`.
- `firered-edit-1.1`:
  - `fused_norm_scale_shift`: `hidden=[1,S,3072]` bf16 for
    `S=189,195,8424`; residual args are `None`; scale/shift are
    `[1,3072]` bf16 for `S=189,195` and `[1,1,3072]` bf16 for `S=8424`;
    `norm_type=layer`, `eps=1e-6`.
  - `fused_scale_residual_norm_scale_shift`: `hidden=[1,S,3072]`,
    `residual=[1,S,3072]`, and output/residual-output tensors are bf16 for
    `S=189,195,8424`; pre-scale is `[1,1,3072]` bf16; scale/shift are
    `[1,3072]` bf16 for `S=189,195` and `[1,1,3072]` bf16 for `S=8424`;
    `norm_type=layer`, `eps=1e-6`.

For the residual entry point, include the matching residual tensors shown by
the copied SGLang baseline ABI for each row.

Current-preset audit status: `firered-edit-1.1` was captured for both entry
points; `helios` was captured for `fused_norm_scale_shift` only;
`hunyuan3d-shape` is runtime-blocked. Any new preset added after this document
must still be freshly audited.

## `diffusion_fuse_scale_shift__multi_shape`

Entry points:

- `scale_shift.fuse_scale_shift_kernel`
- `scale_shift.fuse_layernorm_scale_shift_gate_select01_kernel`
- `scale_shift.fuse_residual_layernorm_scale_shift_gate_select01_kernel`

Required retained live shape rows:

- `qwen`: `x=[1,S,3072]` bf16 for `S=19,47,4096`; scale/shift is
  `[1,1,3072]` bf16; `scale_constant=0`.
- `qwen-edit`: `x=[1,S,3072]` bf16 for `S=189,195,8424`;
  `fuse_scale_shift_kernel` includes both `[1,1,3072]` and full-shape
  `[1,8424,3072]` scale/shift cases.
- `qwen-edit` gated variants: `x=[1,8424,3072]` bf16, `index=[1,8424]`
  int32, `scale{0,1}/shift{0,1}/gate{0,1}=[1,3072]` bf16; residual variant
  also has `residual=[1,8424,3072]` and
  `residual_gate=[1,8424,3072]` bf16.
- `firered-edit-1.0`: `x=[1,8424,3072]` bf16, scale/shift
  `[1,1,3072]` bf16.
- `firered-edit-1.1`: `x=[1,S,3072]` bf16 for `S=189,195,8424`;
  scale is `[1,1,3072]` bf16, output is `[1,S,3072]` bf16,
  `scale_constant=0`.
- `hunyuanvideo`: `x=[1,S,3072]` bf16 for `S=55,27030,27085`;
  scale/shift `[1,3072]` bf16.
- `wan-ti2v`: `x=[1,18144,3072]` bf16, scale/shift
  `[1,18144,3072]` fp32 non-contiguous.
- `wan-t2v`: `x=[1,37800,5120]` bf16, scale/shift `[1,1,5120]` fp32.
- `wan-i2v`: `x=[1,37044,5120]` bf16, scale/shift `[1,1,5120]` fp32.

Current-preset audit status: `helios` was live no-call; `firered-edit-1.1`
was captured; `joyai-edit` remains retained-only unless recaptured;
`hunyuan3d-shape` is runtime-blocked.

## `diffusion_rotary_embedding__multi_shape`

Entry points:

- `rotary.apply_rotary_embedding`
- `ltx2_rotary.apply_ltx2_split_rotary_emb`

Required retained live shape rows:

- `hunyuanvideo` standard RoPE: `x=[1,27030,24,128]` bf16,
  `cos=[27030,64]` fp32, `sin=[27030,64]` fp32, `interleaved=False`.
- `ltx2`: split RoPE rows:
  `[1,126,2048]` with cos/sin `[1,32,126,32]` bf16 non-contiguous,
  `[1,1536,2048]` with `[1,32,1536,32]`,
  `[1,1536,4096]` with `[1,32,1536,64]`,
  `[1,6144,2048]` with `[1,32,6144,32]`,
  `[1,6144,4096]` with `[1,32,6144,64]`.
- `ltx23-ti2v-two-stage`: same single-batch split rows as `ltx2` for
  `S=126,1536,6144` and hidden sizes `2048/4096`.
- `ltx23-one-stage`: split RoPE rows captured live on 2026-06-03:
  `[1,126,2048]` with cos/sin `[1,32,126,32]` bf16 non-contiguous,
  `[1,6144,2048]` with `[1,32,6144,32]`, and
  `[1,6144,4096]` with `[1,32,6144,64]`.
- `ltx23-two-stage`: high-resolution split rows:
  `[2,126,2048]`, `[2,6144,2048]`, `[2,6144,4096]`,
  `[1,24576,2048]`, `[1,24576,4096]`, with matching non-contiguous
  `[B,32,S,32/64]` cos/sin tensors.

Current-preset audit status: `ltx23-one-stage` was captured;
`ltx23-two-stage-cfg-parallel` remains blocked by H200 OOM and missing B200
cache; `hunyuan3d-shape` is runtime-blocked.

## `diffusion_group_norm_silu__multi_shape`

Entry points:

- `group_norm_silu.apply_group_norm_silu`
- `group_norm_silu.triton_group_norm_silu`

Required retained live shape rows:

- `hunyuanvideo` VAE shapes only.
- Dtype is fp16. `num_groups=32`, `eps=1e-6` for the Triton entry point.
- Include both contiguous and non-contiguous cases when observed by the target
  arch. The retained union covers channels `512`, `256`, and `128`, temporal
  depths `2`, `3`, `5`, `9`, and `17`, and spatial pairs including
  `12x10`, `12x32`, `24x20`, `24x64`, `32x10`, `32x32`, `48x40`,
  `48x128`, `64x20`, `64x64`, `96x80`, `96x256`, `128x40`,
  `128x128`, `256x80`, and `256x256`.

Because this family has many rows, generate `bench/workloads.json` from a live
HunyuanVideo capture or from the retained raw JSONL in the pre-reset git
history, not from a hand-written reduced list.

Current-preset audit status: `zimage`, `firered-edit-1.1`, `helios`, and
`ltx23-one-stage` were live no-call for these entry points;
`hunyuan3d-shape` is runtime-blocked.
