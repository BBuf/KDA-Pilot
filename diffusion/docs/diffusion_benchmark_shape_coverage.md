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

## Fresh Capture Audit: 2026-06-28 LTX2 Bitwise Tasks

Valid native SGLang capture:

- `Lightricks/LTX-2.3` on B200 (`ion-b200`), container
  `sglang_bbuf_pr29315`, worktree
  `/home/sglang-omni/bbuf/tmp/ltx2_shape_capture_main`, commit
  `828411e6f1` (`origin/main`). Command shape:
  `CUDA_VISIBLE_DEVICES=5,6 HF_HUB_OFFLINE=1 LTX2_SHAPE_CAPTURE_PATH=...`
  `sglang generate --model-path Lightricks/LTX-2.3 --prompt "A cat and a dog baking a cake together in a kitchen."`
  `--width 768 --height 512 --num-frames 121 --seed 42 --num-gpus 2`
  `--cfg-parallel-size 2 --pipeline-class-name LTX2TwoStagePipeline`
  `--ltx2-two-stage-device-mode original --num-inference-steps 1`
  `--warmup false --enable-torch-compile false --no-save-output`.
  The run completed and emitted 42 target rows:
  18 `rms_adaln`, 12 `qknorm_split_rope_pair`, 6 `dual_modulate`, and
  6 `ca_dual_modulate_from_temb`.

Blocked run:

- `Lightricks/LTX-2` on the same B200 setup failed before denoise because the
  local Hugging Face cache snapshot
  `47da56e2ad66ce4125a9922b4a8826bf407f9d0a` was incomplete: the transformer
  index was present but all 8 transformer safetensors shards were missing.
  Do not treat that failed run as shape coverage.

## `b200_ltx2_rms_adaln__bitwise`

Entry points:

- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_rms_adaln`
- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_rms_adaln`

Required live shape rows from the 2026-06-28 LTX2.3 capture:

- first stage video self-attention / prompt-Q / MLP:
  `x=[2,1536,4096]`, `scale/shift=[2,1536,4096]`, bf16 contiguous,
  `eps=1e-6`.
- first stage audio self-attention / prompt-Q / MLP:
  `x=[2,126,2048]`, `scale/shift=[2,126,2048]`, bf16 contiguous,
  `eps=1e-6`.
- second stage video self-attention / prompt-Q / MLP:
  `x=[1,6144,4096]`, `scale/shift=[1,6144,4096]`, bf16 contiguous,
  `eps=1e-6`.
- second stage audio self-attention / prompt-Q / MLP:
  `x=[1,126,2048]`, `scale/shift=[1,126,2048]`, bf16 contiguous,
  `eps=1e-6`.

## `b200_ltx2_dual_modulate__bitwise`

Entry points:

- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_rmsnorm_dual_modulate`
- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_rmsnorm_ca_dual_modulate`

Required live explicit dual-modulation rows from the 2026-06-28 LTX2.3
capture:

- first stage video AV cross-attention: `x=[2,1536,4096]`,
  `scale0/shift0/scale1/shift1=[2,1,4096]`, bf16, `eps=1e-6`.
- first stage audio AV cross-attention: `x=[2,126,2048]`,
  `scale0/shift0/scale1/shift1=[2,1,2048]`, bf16, `eps=1e-6`.
- second stage video AV cross-attention: `x=[1,6144,4096]`,
  `scale0/shift0/scale1/shift1=[1,1,4096]`, bf16, `eps=1e-6`.
- second stage audio AV cross-attention: `x=[1,126,2048]`,
  `scale0/shift0/scale1/shift1=[1,1,2048]`, bf16, `eps=1e-6`.

Required live cross-attention-from-timestep rows:

- first stage video AV cross-attention: `x=[2,1536,4096]`,
  `temb_scale_shift=[2,1,16384]`, `scale_shift_table=[4,4096]` bf16,
  `eps=1e-6`.
- first stage audio AV cross-attention: `x=[2,126,2048]`,
  `temb_scale_shift=[2,1,8192]`, `scale_shift_table=[4,2048]` bf16,
  `eps=1e-6`.
- second stage video AV cross-attention: `x=[1,6144,4096]`,
  `temb_scale_shift=[1,1,16384]`, `scale_shift_table=[4,4096]` bf16,
  `eps=1e-6`.
- second stage audio AV cross-attention: `x=[1,126,2048]`,
  `temb_scale_shift=[1,1,8192]`, `scale_shift_table=[4,2048]` bf16,
  `eps=1e-6`.

## `b200_ltx2_qknorm_split_rope__bitwise`

Entry points:

- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_qknorm_split_rope`
- `sglang.multimodal_gen.runtime.models.dits.ltx_2:apply_split_rotary_emb`

Required live shape rows from the 2026-06-28 LTX2.3 capture. All rows use
bf16 contiguous `q/k`, bf16 non-contiguous split-RoPE cos/sin tensors with
last-dim stride 1, `num_heads=32`, and `eps=1e-6`.

- first stage video self-attention: `q/k=[2,1536,4096]`, `head_dim=128`,
  `cos/sin=[2,32,1536,64]`.
- first stage audio self-attention: `q/k=[2,126,2048]`, `head_dim=64`,
  `cos/sin=[2,32,126,32]`.
- first stage audio-to-video cross-attention: `q=[2,1536,2048]`,
  `k=[2,126,2048]`, `head_dim=64`, `q cos/sin=[2,32,1536,32]`,
  `k cos/sin=[2,32,126,32]`.
- first stage video-to-audio cross-attention: `q=[2,126,2048]`,
  `k=[2,1536,2048]`, `head_dim=64`, `q cos/sin=[2,32,126,32]`,
  `k cos/sin=[2,32,1536,32]`.
- second stage video self-attention: `q/k=[1,6144,4096]`, `head_dim=128`,
  `cos/sin=[1,32,6144,64]`.
- second stage audio self-attention: `q/k=[1,126,2048]`, `head_dim=64`,
  `cos/sin=[1,32,126,32]`.
- second stage audio-to-video cross-attention: `q=[1,6144,2048]`,
  `k=[1,126,2048]`, `head_dim=64`, `q cos/sin=[1,32,6144,32]`,
  `k cos/sin=[1,32,126,32]`.
- second stage video-to-audio cross-attention: `q=[1,126,2048]`,
  `k=[1,6144,2048]`, `head_dim=64`, `q cos/sin=[1,32,126,32]`,
  `k cos/sin=[1,32,6144,32]`.

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
- `ltx23-two-stage-cfg-parallel` was blocked in the 2026-06-03 audit, but the
  2026-06-28 B200 LTX2.3 capture above completed for the three bitwise LTX2
  task entry points. Any other target entry point in that preset still needs
  its own live capture.
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

## `diffusion_causal_conv3d_cat_pad__multi_shape`

Entry point:

- `causal_conv3d_pad.fused_causal_conv3d_cat_pad`

Fresh B200 capture audit: 2026-06-24, `cosmos3-nano-t2v`,
`nvidia/Cosmos3-Nano`, 832x480, 9 frames, 4 denoise steps. The all-stage trace
showed `_fused_cat_pad_5d_kernel` at 11.94 ms. Raw capture:

`/tmp/sglang_profile_b200/outputs/shape_captures/cosmos3-nano-t2v_no_compile_v2.jsonl`

Required live shape rows:

- bf16 contiguous `x=[1,1024,1,30,52]`,
  `cache=[1,1024,1,30,52]`, padding `[1,1,1,1,2,0]`.
- bf16 contiguous `x=[1,1024,1,30,52]`,
  `cache=[1,1024,2,30,52]`, padding `[1,1,1,1,2,0]`.
- bf16 contiguous `x=[1,1024,2,60,104]`,
  `cache=[1,1024,1,60,104]`, padding `[1,1,1,1,2,0]`.
- bf16 contiguous `x=[1,1024,2,60,104]`,
  `cache=[1,1024,2,60,104]`, padding `[1,1,1,1,2,0]`.
- bf16 contiguous `x=[1,512,4,120,208]`,
  `cache=[1,512,1,120,208]`, padding `[1,1,1,1,2,0]`.
- bf16 contiguous `x=[1,512,4,120,208]`,
  `cache=[1,512,2,120,208]`, padding `[1,1,1,1,2,0]`.
- bf16 contiguous `x=[1,256,4,240,416]`,
  `cache=[1,256,1,240,416]`, padding `[1,1,1,1,2,0]`.
- bf16 contiguous `x=[1,256,4,240,416]`,
  `cache=[1,256,2,240,416]`, padding `[1,1,1,1,2,0]`.

Include the low-count cache-null, no-pad, and captured non-contiguous rows as
regression rows in `bench/workloads.json`.

## `diffusion_attention_concat_copy__multi_model`

Entry source patterns:

- `USPAttention._forward_with_replicated_prefix`
- `USPAttention._forward_with_replicated_kv_prefix_split`
- local `contiguous()` plus `torch.cat(..., dim=1)` attention layout patterns
  in `runtime/layers/attention/layer.py`.

Fresh B200 capture audit: 2026-06-24, retained from torch profiler shapes for
JoyAI Image Edit and FLUX.2 Klein Base.

Required live shape rows:

- `concat_sequence`: bf16 `a=[1,512,24,128]`, `b=[1,4096,24,128]`,
  output `[1,4608,24,128]`.
- `concat_sequence`: bf16 `a=[1,8048,32,128]`, `b=[1,1004,32,128]`,
  output `[1,9052,32,128]`.
- `copy_contiguous`: bf16 `[1,4608,24,128]`.
- `copy_contiguous`: bf16 `[1,8048,32,128]`.
- `copy_contiguous`: bf16 `[1,1004,32,128]`.
- `slice_heads_then_concat_sequence`: bf16 prefix/shard rows matching FLUX.2
  prefix length 512, shard length 4096, heads 24, head dim 128.
- `slice_heads_then_concat_sequence`: bf16 prefix/shard rows matching JoyAI
  lengths 1004 and 8048, heads 32, head dim 128.

Current evidence: JoyAI trace showed `CatArrayBatchedCopy` at 521.5 ms and
large contiguous/copy rows; FLUX.2 Klein Base showed repeated copy/cat rows in
the replicated-prefix attention path.

## `diffusion_residual_gate_add__multi_shape`

Entry source patterns:

- `LTX2TransformerBlock.forward`
- `Ideogram4TransformerBlock.forward`
- FLUX.2 modulation and residual gate expressions in `flux_2.py`.

Fresh B200 capture audit: 2026-06-24, retained from torch profiler shapes for
LTX-2.3 HQ, Ideogram4 FP8, and FLUX.2 Klein Base.

Required live shape rows:

- `residual_gate_add`: bf16 `residual=[1,8160,4096]`,
  `update=[1,8160,4096]`, `gate=[1,8160,4096]`.
- `residual_gate_add`: bf16 `residual=[1,32640,4096]`,
  `update=[1,32640,4096]`, `gate=[1,1,4096]`.
- `residual_gate_add`: bf16 `residual=[1,126,2048]`,
  `update=[1,126,2048]`, `gate=[1,126,2048]`.
- `residual_gate_add`: bf16 `residual=[1,4096,4608]`,
  `update=[1,4096,4608]`, `gate=[1,1,4608]`.
- `residual_gate_add`: bf16 `residual=[1,4608,3072]`,
  `update=[1,4608,3072]`, `gate=[1,1,3072]`.
- `residual_gate_add`: bf16 `residual=[1,4096,3072]`,
  `update=[1,4096,3072]`, `gate=[1,1,3072]`.
- `residual_gate_add`: bf16 `residual=[1,512,3072]`,
  `update=[1,512,3072]`, `gate=[1,1,3072]`.
- `broadcast_add_4d`: bf16 `a=[1,1,3,2048]`, `b=[1,126,3,2048]`,
  output `[1,126,3,2048]`.

Current evidence: LTX-2.3 HQ trace showed elementwise add at 7260.2 ms and mul
at 4022.4 ms across all CUDA kernels. These rows are memory-bandwidth tasks;
GEMM, attention, QKNorm+RoPE, and existing norm/scale/shift kernels are out of
scope for this family.
