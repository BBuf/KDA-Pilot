# SGLang Recent Diffusion B200 Profile Audit - 2026-06-24

This audit records B200 profiling evidence for recent SGLang diffusion model
support and the KDA task boundaries that looked actionable after collecting
real production shapes.

## Source And Machine

- SGLang worktree: `/tmp/sglang_profile_b200`
- SGLang commit: `84a7a8401842b47b9e372df8136b7b7dc0b7e166`
- Host/container: `ion-b200` / `sglang_bbuf`
- GPU: NVIDIA B200
- Native backend gate: all retained benchmark/profile rows came from native
  SGLang diffusion paths.

## Profiled Models

| Model preset | Model | Shape | Denoise / E2E | Peak reserved | Evidence path |
| --- | --- | --- | --- | --- | --- |
| `cosmos3-nano-t2v` | `nvidia/Cosmos3-Nano` | 832x480, 9 frames, 4 steps | 169.55 ms / 216.8 ms | 35,088 MB | `/tmp/sglang_profile_b200/outputs/diffusion_profiles/cosmos3-nano-t2v_nocompile_all/bfc39a58-f657-4c3c-86a4-728c58484da6-full_stages-global-rank0.trace.json.gz` |
| `ideogram4-fp8` | `ideogram-ai/ideogram-4-fp8` | 1024x1024, 20 steps | 5592.9 ms / 5713.1 ms | 33,186 MB | `/tmp/sglang_profile_b200/outputs/diffusion_profiles/ideogram4-fp8_nocompile_all/bf5ca92b-9bc5-41a8-bf2a-8f2db371b9d4-full_stages-global-rank0.trace.json.gz` |
| `sana-1.5-1.6b` | `Efficient-Large-Model/SANA1.5_1.6B_1024px_diffusers` | 1024x1024 | 456.9 ms / 547.0 ms | 9856 MB | `/tmp/sglang_profile_b200/outputs/diffusion_profiles/sana-1.5-1.6b_nocompile_all/3d8259f6-4b7c-4647-b0f4-3847332c116f-full_stages-global-rank0.trace.json.gz` |
| `flux2-klein-base` | `black-forest-labs/FLUX.2-klein-base-4B` | 1024x1024, 50 steps | 3709.1 ms / 3856.4 ms | 13,442 MB | `/tmp/sglang_profile_b200/outputs/diffusion_profiles/flux2-klein-base_nocompile_all/df2cd86f-354e-4576-a41a-6d428f974685-full_stages-global-rank0.trace.json.gz` |
| `joyai-edit` | `jdopensource/JoyAI-Image-Edit-Diffusers` | 1024x1024, 40 steps, CFG parallel | 7.27 s / 8.23 s | 41,976 MB | `/tmp/sglang_profile_b200/outputs/diffusion_profiles/joyai-edit_nocompile_all/f2159a93-363e-4c7c-8bd4-4a93017b3985-full_stages-global-rank0.trace.json.gz` |
| `ltx23-hq-two-stage` | `Lightricks/LTX-2.3` | 1920x1088, 121 frames | 42.34 s / 55.29 s | 67,902 MB | `/tmp/sglang_profile_b200/outputs/diffusion_profiles/ltx23-hq-two-stage_nocompile_all/70769941-6405-49c2-8663-a632325a001b-full_stages-global-rank0.trace.json.gz` |

## Access Notes

- `krea/Krea-2` was not accessible through direct Hugging Face or the HF mirror
  in this environment.
- LingBot model metadata was reachable through Hugging Face and ModelScope, but
  the native path needs image/action inputs and had no benchmark helper preset.
- SANA-WM metadata was reachable through ModelScope, but the full repo is very
  large and had no benchmark helper preset in the profiled tree.
- `flux2-klein-base` was reachable and runnable with a manual native
  `sglang generate` command, although the helper was conservative because the
  FLUX family is listed as gated.

## Actionable KDA Task Boundaries

### Attention concat/copy layout

Real evidence:

- JoyAI profile: `aten::contiguous` on `[1,8048,32,128]` took 748.6 ms over
  3200 calls and the matching `aten::copy_` took 705.1 ms. `aten::cat` for
  `[[1,8048,32,128], [1,1004,32,128]]` took 71.6 ms over 4800 calls. The GPU
  trace also showed `CatArrayBatchedCopy` at 521.5 ms.
- FLUX.2 Klein Base profile: `aten::copy_` on `[1,4608,24,128]` took 154.9 ms
  over 4000 calls. `aten::cat` for `[[1,512,24,128], [1,4096,24,128]]` took
  51.2 ms over 1500 calls.
- Source boundary: `python/sglang/multimodal_gen/runtime/layers/attention/layer.py`
  has repeated `contiguous()` plus `torch.cat` paths in
  `USPAttention._forward_with_replicated_prefix` and
  `_forward_with_replicated_kv_prefix_split`.

KDA task: `b200_diffusion_attention_concat_copy__multi_model`.

### Residual gate add and broadcast add

Real evidence:

- LTX-2.3 HQ profile: aggregate CUDA kernels were dominated by elementwise
  add/mul around the DiT blocks (`aten::add` and `aten::mul` shapes include
  `[1,8160,4096]`, `[1,32640,4096]`, and `[1,126,2048]`). CPU op shape totals
  include 27,927 adds on `[1,8160,4096]`, 25,143 muls on `[1,8160,4096]`,
  33,123 adds on `[1,126,2048]`, and 26,877 muls on `[1,126,2048]`.
- LTX also has a very hot broadcast add shape:
  `[1,1,3,2048] + [1,126,3,2048]`, 13,392 calls and 3139.4 ms CPU op time.
- Ideogram4 FP8 profile: `aten::mul` on `[1,1,4608] * [1,4096,4608]` took
  150.7 ms over 1360 calls, with surrounding `x + gate * norm(...)` source in
  `runtime/models/dits/ideogram.py`.
- FLUX.2 Klein Base profile: repeated gate/modulation shapes include
  `[1,1,3072] * [1,4608,3072]`, `[1,1,3072] * [1,4096,3072]`, and
  `[1,1,3072] * [1,512,3072]`.

KDA task: `b200_diffusion_residual_gate_add__multi_shape`.

### Causal Conv3D cat/pad

Real evidence:

- Cosmos3 Nano T2V all-stage profile showed `_fused_cat_pad_5d_kernel` at
  11.94 ms across the VAE/decode path.
- Shape capture path:
  `/tmp/sglang_profile_b200/outputs/shape_captures/cosmos3-nano-t2v_no_compile_v2.jsonl`
- Representative bf16 workloads include:
  - `x=[1,1024,1,30,52]`, `cache=[1,1024,1,30,52]`, padding `[1,1,1,1,2,0]`
  - `x=[1,1024,2,60,104]`, `cache=[1,1024,1,60,104]`, padding `[1,1,1,1,2,0]`
  - `x=[1,512,4,120,208]`, `cache=[1,512,1,120,208]`, padding `[1,1,1,1,2,0]`
  - `x=[1,256,4,240,416]`, `cache=[1,256,1,240,416]`, padding `[1,1,1,1,2,0]`

KDA task: `b200_diffusion_causal_conv3d_cat_pad__multi_shape`.

## No-Go Or Existing-Task Notes

- QKNorm+RoPE is already covered by existing KDA diffusion tasks. New profiles
  confirm calls in FLUX.2, JoyAI, and Cosmos3, but standalone time was not the
  largest remaining opportunity.
- LTX2 split RoPE is already covered by the existing rotary task; the LTX-2.3
  HQ trace showed `_ltx2_split_rotary_kernel` as a real cost but smaller than
  the surrounding elementwise block work.
- SANA 1.5 1.6B was fast on B200 and did not expose a new standalone CUDA task
  with a large enough expected gain.
