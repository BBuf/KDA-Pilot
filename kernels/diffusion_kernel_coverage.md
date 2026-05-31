# Diffusion Kernel × Model Coverage Matrix

Maps each SGLang `python/sglang/jit_kernel/diffusion/` kernel entry point to the
benchmark preset models known to exercise it. This is the cross-task coverage
view used together with the per-task `prompt.md` shape tables.

The matrix is composed of two columns of evidence:

- **Empirical** — observed live during a `kernel_shape_capture.py` sweep over
  the SGLang diffusion benchmark presets on `ion-b200` (B200) and
  `ion8-h200` / `ion9-h200` (H200). The raw JSONL captures land under
  `kernels/<task>/docs/captured_shapes_<arch>.jsonl`.
- **Analytical** — derived from the upstream model architecture configs and
  SGLang code paths but not yet observed live.

Note: tensor shapes are arch-independent for these kernels, so empirical
captures from H200 are valid evidence for the matching B200 task too. The
sweep was therefore run mostly on the two H200 boxes; the B200 box additionally
contributed live captures for `qwen-edit`, `zimage`, `wan-ti2v`, and partial
`ltx2`.

## Preset Sweep Coverage (12 SGLang diffusion benchmark presets)

| Preset | Model | Hosts | Captures |
|---|---|---|---|
| `flux` | FLUX.1-dev | ion8-h200 (phase 2) | ✅ qknorm_rope @ 24 heads, 3 regimes (512 / 4096 / 4608 tokens) |
| `flux2` | FLUX.2-dev | ion8-h200 (phase 2) | ✅ qknorm_rope @ 48 heads, same 3-regime layout |
| `qwen` | Qwen-Image-2512 | ion8-h200 | ✅ qknorm_rope, fuse_scale_shift, CuTe-DSL fused_norm_scale_shift (+residual) |
| `qwen-edit` | Qwen-Image-Edit-2511 | ion-b200, ion8-h200 (retry) | ✅ all above + `fuse_layernorm_scale_shift_gate_select01` (+residual) |
| `zimage` | Z-Image-Turbo | ion-b200, ion8-h200 | ✅ qknorm_rope, triton_one_pass_rms_norm, CuTe-DSL fused_norm_tanh_mul_add (+norm_scale) |
| `wan-ti2v` | Wan2.2-TI2V-5B | ion9-h200 (retry), ion-b200 | ✅ CuTe-DSL fused_norm_scale_shift (D=3072, S=18144, fp32 scale/shift) |
| `wan-i2v` | Wan2.2-I2V-A14B | ion9-h200, ion8-h200 (phase 2) | ⚠️ install events only; CFG-parallel run exited before kernels fired |
| `wan-t2v` | Wan2.2-T2V-A14B | ion9-h200, ion8-h200 (phase 2) | ✅ CuTe-DSL fused_norm_scale_shift (D=5120, S=37800, fp32 scale/shift) |
| `ltx2` | LTX-2 | ion9-h200 | ✅ `ltx2_rotary.apply_ltx2_split_rotary_emb` @ 32 heads with split half_dim |
| `hunyuanvideo` | HunyuanVideo | ion9-h200 (phase 2) | ✅ standard `apply_rotary_embedding`, GroupNorm+SiLU VAE (image and 5D video), CuTe-DSL fused_norm_scale_shift, scale_shift, triton_one_pass_rms_norm |
| `mova-720p` | MOVA-720p | ion8-h200 (phase 2) | ⚠️ install events only; 4-GPU launch slow + timed out before DiT kernels |
| `helios` | Helios-Base | ion9-h200 + ion8-h200 (phase 2) | ✅ qknorm_rope, scale_shift, scale_residual_norm_scale_shift, **`norm.norm_infer`** (new — the 2-pass LayerNorm baseline) |

## Kernel Capture Status (14 entry points)

| Kernel entry point | Empirical models | Status |
|---|---|---|
| `qknorm_rope.fused_inplace_qknorm_rope` | qwen, qwen-edit, zimage, flux, flux2, helios | ✅ |
| `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add` | zimage | ✅ |
| `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale` | zimage | ✅ |
| `scale_residual_norm_scale_shift.fused_norm_scale_shift` | qwen, qwen-edit, wan-ti2v, wan-t2v, hunyuanvideo, helios | ✅ |
| `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | qwen, qwen-edit, wan-ti2v, wan-t2v, hunyuanvideo, helios | ✅ |
| `scale_shift.fuse_scale_shift_kernel` | qwen, qwen-edit, hunyuanvideo, helios | ✅ |
| `scale_shift.fuse_layernorm_scale_shift_gate_select01_kernel` | qwen-edit | ✅ |
| `scale_shift.fuse_residual_layernorm_scale_shift_gate_select01_kernel` | qwen-edit | ✅ |
| `rmsnorm_onepass.triton_one_pass_rms_norm` | zimage, flux2, hunyuanvideo | ✅ |
| `norm.norm_infer` | helios | ✅ (new in phase 2) |
| `ltx2_rotary.apply_ltx2_split_rotary_emb` | ltx2 | ✅ |
| `rotary.apply_rotary_embedding` | hunyuanvideo | ✅ (new in phase 2) |
| `group_norm_silu.apply_group_norm_silu` | hunyuanvideo | ✅ (new in phase 2) |
| `group_norm_silu.triton_group_norm_silu` | hunyuanvideo | ✅ (new in phase 2) |

**14 of 14 tracked kernel entry points have empirical capture coverage** after
the phase-2 sweep (helios picked up `norm.norm_infer` as the very last
addition).

## Re-capture procedure

To extend coverage or refresh shapes after a model preset / SGLang code-path
change, repeat the sweep from
`scripts/diffusion_shape_capture/sweep_models.sh` and re-run
`finalize.sh` to regenerate the per-task ledgers:

```bash
ssh <host> 'docker exec sglang_bbuf bash -lc "
  HOST_LABEL=<host> ARCH_LABEL=<arch> GPU_LIST_1GPU=<ids> GPU_LIST_4GPU=<ids> \
  HF_TOKEN=<token> /root/diffusion_shape_capture/sweep_models.sh \
  flux,flux2,qwen,qwen-edit,zimage,wan-ti2v,ltx2,wan-i2v,wan-t2v,hunyuanvideo,mova-720p,helios \
  /tmp/shapes_<host>.jsonl
"'
bash scripts/diffusion_shape_capture/finalize.sh
```

The shape-capture script is `scripts/diffusion_shape_capture/kernel_shape_capture.py`;
the bench script and the diffusion-skill env helper are copied into the
container at `/root/bench_diffusion_denoise.py` and
`/root/diffusion_skill_env.py`. Required artifacts inside the container:

- `/home/sglang-omni/bbuf/repos/sglang/inputs/diffusion_benchmark/figs/cat.png`
  (used by `qwen-edit`, `wan-ti2v`, `wan-i2v`).
- `/home/sglang-omni/bbuf/repos/sglang/inputs/diffusion_benchmark/figs/mova_single_person.jpg`
  (used by `mova-720p`; download from the OpenMOSS MOVA repo).

The `wan-i2v` and `mova-720p` presets need ≥ 4 idle GPUs and substantial HF
download budget (each ~30-70GB). When disk pressure is high, prefer running
just the `qwen`, `qwen-edit`, `zimage`, `flux`, `flux2`, `hunyuanvideo`,
`helios` subset — between them they exercise all 13 captured kernel families.
