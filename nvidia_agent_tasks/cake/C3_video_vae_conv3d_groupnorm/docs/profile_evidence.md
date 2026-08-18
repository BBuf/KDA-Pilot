# Profile evidence: video VAE decode kernels

## Which models actually call these kernels (verified in the SGLang tree, this commit)

| kernel | call site |
| --- | --- |
| `kernels/ops/diffusion/causal_conv3d_cat_pad.py::fused_causal_conv3d_cat_pad_cuda` | `runtime/models/vaes/autoencoder_kl_qwenimage.py:91` |
| `kernels/ops/diffusion/group_norm_silu.py::apply_group_norm_silu` | `runtime/models/vaes/hunyuanvae.py:25` |
| `kernels/ops/diffusion/triton/group_norm_silu_twopass.py::group_norm_silu_4d` / `group_norm_silu_rows` | `runtime/models/vaes/flux2_vae_cuda_opt.py:74,260` |

This is a correction worth stating plainly: we first ran the capture against
**Wan2.2-TI2V-5B** and these kernels fired **zero** times - the Wan VAE has its own
optimized decoder (`wan_vae_cuda_opt`) that does not go through them. The right
capture targets for this task are the **Qwen-Image**, **FLUX.2** and **Hunyuan**
VAE decoders. Their weights were not staged on the capture box in this pass, so
this task ships with the call sites and the prior measurement evidence rather
than a fresh shape table.

## Prior measurement evidence (our campaign logs, not this capture run)

* Our own fused kernels already beat their Triton predecessors: `causal_conv3d_cat_pad`
  **2.06x** (production rows 1.60-2.45x, bitwise-exact B300 gate), `group_norm_silu`
  **2.31x** (small/mid-C rows 1.37-4.98x, NC rows up to 3.65x).
* On LTX-2 the pad kernel is only **1-3%** of the conv cost, while moving the decode
  to `channels_last_3d` is worth about **3x** - that is the real target, and it needs a
  conv3d that is fast in a layout cuDNN does not prefer plus a layout-preserving
  causal pad.
* Decode-stage share of end-to-end ranges from **1.7%** (8-GPU speed configs) to
  **~62%** (2-GPU offload CI config), so this task's value is deployment-shaped; state
  which configuration a win is claimed for.

## How to capture the shape table (one command per model)

```bash
PYTHONPATH=<repo>/nvidia_agent_tasks/tools:<sglang>/python \
NVCAP_DIR=cap/diff_qwenimage NVCAP_CONFIG=tools/targets/diffusion_focus.json \
NVCAP_MAX_TENSOR_MB=24 \
  sglang generate --backend=sglang --model-path=Qwen/Qwen-Image \
    --model-id=Qwen/Qwen-Image --prompt "..." --width=1328 --height=1328 \
    --enable-torch-compile=false --save-output
python tools/merge_manifests.py cap/diff_qwenimage
```

`--enable-torch-compile=false` matters: with compile on, the Python-level entry
points are traced once and the capture sees only the first step.
