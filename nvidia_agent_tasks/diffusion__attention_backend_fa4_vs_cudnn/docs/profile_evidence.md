# Profile evidence: diffusion attention backend on sm_103

## Measured on this box, tonight (B300 SXM6, sm_103, torch 2.13.0+cu130)

`bench/fa4_vs_cudnn.json` (contiguous q/k/v) and `bench/fa4_noncontig.json` (q/k/v as
slices of one fused QKV buffer, which is what the DiT actually hands the backend).
Ratios below are **FA4 / cuDNN**, so <1 means the FA4 CuTe kernel is faster.

| shape | seq | heads | cuDNN SDPA (ms) | FA4 CuTe (ms) | FA4/cuDNN contiguous | FA4/cuDNN fused-QKV |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `wan22_ti2v_5b_self_832x480x81f` | 8190 | 24 | 0.5234 | 0.5113 | 0.977 | 0.9687 |
| `wan22_ti2v_5b_cross` | 8190 | 24 | 0.0477 | 0.0469 | 0.9834 | - |
| `h3_video_tower_per_rank` | 37736 | 14 | 8.6444 | 6.7827 | 0.9438 | 0.9512 |
| `h3_audio_tower` | 26 | 16 | 0.0184 | 0.0224 | 1.2415 | - |
| `h3_small_component` | 24 | 14 | 0.0182 | 0.0223 | 1.2484 | - |
| `wan22_ti2v_5b_self_720p` | 15600 | 24 | 2.1535 | 2.4566 | 1.1407 | 0.9574 |
| `wan22_a14b_480p_class` | 32760 | 40 | 16.4598 | 17.89 | 1.1654 | 0.9518 |
| `long_video_75k` | 75000 | 24 | 48.1071 | 45.5947 | 0.9506 | - |
| `lingbot_506k_class` | 126464 | 16 | 89.8371 | 86.0336 | 0.9577 | - |

### What this says

* **With the layout the model really uses (fused-QKV slices), FA4 wins every large shape**
  by 4-5%: Wan2.2-TI2V-5B self 0.969, its 720p variant 0.957, the H3 video tower 0.951,
  an A14B-class 32k x 40-head shape 0.952.
* **cuDNN only wins at very short sequences**: 24-26 tokens, where FA4 is 1.24x slower.
  That regime is not a curiosity - it is H3's audio tower, and FA4 served it 200 times in
  one request in our capture.
* **Layout flips the mid-size verdict.** At 15.6k and 32.7k tokens cuDNN is 1.14-1.17x
  faster on contiguous tensors and 0.95x slower on fused-QKV slices. Whatever predicate
  picks a backend has to see the layout, not just the shape.

### Correction to our own earlier claim

Our August campaign measured cuDNN 9.19 SDPA beating the vendored FA4 CuTe kernel by
**1.24-1.98x** on 11 real diffusion shapes, and that is why SGLang currently defaults
sm_100+ diffusion attention to cuDNN. **That result does not reproduce on B300 with the
current stack** - the numbers above are from tonight, same measurement style, and FA4 is
ahead on the long shapes. The earlier run was B200, cuDNN 9.19, and an older flash-attn
wheel. Two honest conclusions follow:

1. our sm_100+ cuDNN default needs re-examining on sm_103 (that is our job, not NVIDIA's), and
2. the task we are handing over is no longer *make FA4 catch up on long shapes*. It is the
   two items below.

### The remaining asks

1. **The short-sequence regime**: FA4 is 1.24x slower than cuDNN at 24-26 tokens x 14-16
   heads x head_dim 128. Small absolute numbers (22 vs 18 us) but hundreds of calls per
   request, and it is the branch a sparse backend also falls back to (see
   `minimax_h3__sparse_backend_fallback`).
2. **Re-verify the B200 gap** with the current wheel: if 1.24-1.98x still holds there,
   FA4's Blackwell tuning is generation-specific and we should say so in the dispatch
   predicate rather than hard-coding a backend per architecture.

### Method notes

* Both arms are timed the same way: 5 warmup calls, then 5 trials x 20-30 iterations,
  median of trials, and cuDNN is sampled twice (before and after the FA4 arm) so a clock
  drift on this air-cooled part cannot be mistaken for a win. The reported ratio uses the
  faster of the two cuDNN samples, i.e. it is biased *against* FA4.
* cuDNN is forced through `sdpa_kernel(SDPBackend.CUDNN_ATTENTION)`; note that importing
  the SGLang diffusion stack globally disables cuDNN SDPA and pins FA ver 4 on sm_100, so
  an A/B needs that override lifted (the bench script does it).
* Shapes come from the captured rows (`bench/workloads_wan.json`, `bench/workloads_h3.json`)
  plus brackets for the A14B and LingBot points, which we could not capture this round.
