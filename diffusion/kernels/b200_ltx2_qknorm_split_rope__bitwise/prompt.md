# b200_ltx2_qknorm_split_rope__bitwise

Target GPU: NVIDIA B200.

This task replaces the closed SGLang PR:

- `sgl-project/sglang#29399` (`[Diffusion] Fuse LTX2 qknorm split-RoPE`)

The PR showed useful speed potential but used tolerance-based checks and did
not yet prove full-model-safe bit-wise equivalence. Do not copy the failed
Triton implementation as the candidate. Use it only as source context for the
callsite and shapes.

Target SGLang diffusion source patterns to copy as local baseline:

- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_qknorm_split_rope`
- `sglang.multimodal_gen.runtime.models.dits.ltx_2:apply_split_rotary_emb`
- the PyTorch fallback code in the LTX2 attention path:
  `q_norm(q)`, `k_norm(k)`, then split RoPE on Q and K.

Goal: produce an optimized Q/K RMSNorm plus split-RoPE pair kernel for LTX2
that is **bit-wise equal** to the real SGLang LTX2.3 production baseline, so the
eventual SGLang replacement does not change diffusion CI golden outputs.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

## Required Baseline Semantics

This task must target the production SGLang LTX2.3 path, not a forced-eager
standalone approximation. The correctness oracle is the attention subgraph as it
runs inside the denoising loop:

- `server_args.disable_autocast=false`
- `dit_precision=bf16`
- `torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=True)`
  is active around the transformer call.
- `apply_split_rotary_emb` must include the current bf16 Triton fast path
  dispatch from `sglang.jit_kernel.diffusion.triton.ltx2_rotary` for live rows.

The previous task version removed that fast path and optimized against the eager
fallback. That is not sufficient: real LTX2.3 CI and benchmarks enter the
production split-RoPE fast path when q/k norm outputs are bf16 CUDA contiguous
tensors and cos/sin are bf16 4-D split-RoPE tables.

Inputs:

- `q`: `[B, Q, H]`, `torch.bfloat16`, contiguous.
- `k`: `[B, K, H]`, `torch.bfloat16`, contiguous.
- `q_norm`, `k_norm`: PyTorch `torch.nn.RMSNorm(H, eps=eps)` with bf16
  weights.
- `q_cos`, `q_sin`: `[B, num_heads, Q, head_dim / 2]`, bf16, last-dim
  contiguous.
- `k_cos`, `k_sin`: `[B, num_heads, K, head_dim / 2]`, bf16, last-dim
  contiguous.
- `H = num_heads * head_dim`.

Baseline:

```python
q_normed = q_norm(q)
k_normed = k_norm(k)
q_out = apply_split_rotary_emb(q_normed, (q_cos, q_sin))
k_out = apply_split_rotary_emb(k_normed, (k_cos, k_sin))
```

The task-local baseline must use a copied implementation of production
`apply_split_rotary_emb`, including the same fast-path dispatch and Triton kernel
semantics as SGLang. The candidate must match `q_out` and `k_out` with
`torch.equal` / byte-level equality. Tolerances are forbidden.

The optimized candidate must preserve production-visible rounding points for
RMSNorm and the split-RoPE fast path. Do not use an algebraic rearrangement or
FMA contraction if it changes bfloat16 output bits. If one monolithic kernel
cannot be bit-wise exact, split the candidate into staged kernels or dispatch
different implementations by shape while matching production operation
boundaries.

Hot-path exception fallback is not success. Unsupported rows must be rejected by
cheap Python/C++ preflight guards before launching the raw kernel; repeated
dtype/shape exceptions inside the benchmark or SGLang integration count as a
regression even if the fallback output is correct.

## Required Workload Rows

Use real model shapes, not synthetic shape guesses. Include these rows in
`bench/workloads.json` and correctness tests. The task already contains an
initial `bench/workloads.json` seeded with the rows below; keep that file and
this section consistent.

Source A: SGLang CI / comparison-config shape. These rows were captured from
`Lightricks/LTX-2.3` with `LTX2TwoStagePipeline`, `width=768`, `height=512`,
`num_frames=121`, `num_gpus=2`, `cfg_parallel_size=2`,
`num_inference_steps=1` on `ion-b200` on 2026-06-28. This corresponds to the
`scripts/ci/utils/diffusion/comparison_configs.json`
`ltx2.3_twostage_ti2v_2gpus` command family.

All rows use bf16 contiguous `q/k`, bf16 non-contiguous split-RoPE cos/sin
tables with last-dim stride 1, `num_heads=32`, and `eps=1e-6`.

- first stage video self-attention (`ltx2.attn1`):
  `q=[2,1536,4096]`, `k=[2,1536,4096]`, `head_dim=128`,
  `q/k cos/sin=[2,32,1536,64]`.
- first stage audio self-attention (`ltx2.audio_attn1`):
  `q=[2,126,2048]`, `k=[2,126,2048]`, `head_dim=64`,
  `q/k cos/sin=[2,32,126,32]`.
- first stage audio-to-video cross-attention:
  `q=[2,1536,2048]`, `k=[2,126,2048]`, `head_dim=64`,
  `q cos/sin=[2,32,1536,32]`, `k cos/sin=[2,32,126,32]`.
- first stage video-to-audio cross-attention:
  `q=[2,126,2048]`, `k=[2,1536,2048]`, `head_dim=64`,
  `q cos/sin=[2,32,126,32]`, `k cos/sin=[2,32,1536,32]`.
- second stage video self-attention (`ltx2.attn1`):
  `q=[1,6144,4096]`, `k=[1,6144,4096]`, `head_dim=128`,
  `q/k cos/sin=[1,32,6144,64]`.
- second stage audio self-attention (`ltx2.audio_attn1`):
  `q=[1,126,2048]`, `k=[1,126,2048]`, `head_dim=64`,
  `q/k cos/sin=[1,32,126,32]`.
- second stage audio-to-video cross-attention:
  `q=[1,6144,2048]`, `k=[1,126,2048]`, `head_dim=64`,
  `q cos/sin=[1,32,6144,32]`, `k cos/sin=[1,32,126,32]`.
- second stage video-to-audio cross-attention:
  `q=[1,126,2048]`, `k=[1,6144,2048]`, `head_dim=64`,
  `q cos/sin=[1,32,126,32]`, `k cos/sin=[1,32,6144,32]`.

Source B: the closed SGLang PR benchmark command family used by
`sgl-project/sglang#29392`, `#29396`, and `#29399`:

```bash
sglang generate \
  --backend=sglang \
  --model-path=Lightricks/LTX-2.3 \
  --pipeline-class-name=LTX2TwoStageHQPipeline \
  --ltx2-two-stage-device-mode original \
  --width=1920 --height=1088 --num-frames=121 \
  --num-inference-steps=15 \
  --save-output --warmup
```

The HQ command is single-GPU, has `enable_cfg_parallel=false`, and does not use
torch compile. Its Stage 2 video latent shape was logged on `ion-b200` as
`[1,32640,128]` before transformer projection. `LTX2TwoStageHQPipeline` halves
resolution before Stage 1, so the corresponding Stage 1 video token count is
`8160`. Required Q/K norm + split-RoPE rows from this command family:

- HQ first stage video self-attention:
  `q=[1,8160,4096]`, `k=[1,8160,4096]`, `head_dim=128`,
  `q/k cos/sin=[1,32,8160,64]`.
- HQ first stage audio-to-video cross-attention:
  `q=[1,8160,2048]`, `k=[1,126,2048]`, `head_dim=64`,
  `q cos/sin=[1,32,8160,32]`, `k cos/sin=[1,32,126,32]`.
- HQ first stage video-to-audio cross-attention:
  `q=[1,126,2048]`, `k=[1,8160,2048]`, `head_dim=64`,
  `q cos/sin=[1,32,126,32]`, `k cos/sin=[1,32,8160,32]`.
- HQ second stage video self-attention:
  `q=[1,32640,4096]`, `k=[1,32640,4096]`, `head_dim=128`,
  `q/k cos/sin=[1,32,32640,64]`.
- HQ second stage audio-to-video cross-attention:
  `q=[1,32640,2048]`, `k=[1,126,2048]`, `head_dim=64`,
  `q cos/sin=[1,32,32640,32]`, `k cos/sin=[1,32,126,32]`.
- HQ second stage video-to-audio cross-attention:
  `q=[1,126,2048]`, `k=[1,32640,2048]`, `head_dim=64`,
  `q cos/sin=[1,32,126,32]`, `k cos/sin=[1,32,32640,32]`.
- HQ audio self-attention uses the same single-GPU audio shape already listed:
  `q/k=[1,126,2048]`, `head_dim=64`, `q/k cos/sin=[1,32,126,32]`.

Source C: SGLang LTX2.3 cookbook/API commands. The documented one-stage and
two-stage default commands use `Lightricks/LTX-2.3`, `768x512`, `121` frames.
Their Q/K norm + split-RoPE shape coverage is already represented by the unique
`[1,6144,*]` / `[1,126,*]` rows and the CI two-stage rows above. Do not add
duplicate benchmark rows unless a live model run proves a new tensor shape or
stride.

## Shape-Specialized Dispatch Requirement

The final optimized solution may use different kernels, template parameters,
or launch policies for different `(B, Q, K, hidden, head_dim)` rows. Prefer an
explicit dispatcher if one generic kernel cannot win simultaneously on CI
`video_seq in {1536,6144}` and HQ `video_seq in {8160,32640}`. It is acceptable
to dispatch separately for video self-attention, audio self-attention,
audio-to-video, and video-to-audio, and to specialize for `head_dim=128` versus
`head_dim=64`, as long as every selected path is bit-wise equal to the
production baseline and unsupported shapes fail closed or fall back to the exact
production implementation.

Do not claim success from an average speedup if one of the production shape
families regresses. Report per-shape timings and explain the dispatcher choice.

Reject or fall back for unsupported rows instead of producing approximate
answers:

- tensor-parallel world size other than 1
- non-`torch.nn.RMSNorm`
- `q_norm.eps != eps` or `k_norm.eps != eps`
- fp32 norm weights
- interleaved/non-split RoPE tensors
- non-contiguous Q/K or cos/sin last dimension
- dtype other than `torch.bfloat16`

## Required First Milestone

1. Copy the relevant upstream SGLang snippets into `baseline/` and record the
   exact source commit in `docs/baseline_source.md`.
2. Implement a task-local SGLang production baseline adapter with the exact
   autocast / split-RoPE fast-path semantics above.
3. Expose the candidate through the exact same ABI in `solution/`.
4. Verify the seeded `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.
5. Make correctness fail on any non-bitwise result, output dtype mismatch, NaN,
   Inf, or hot exception fallback. Use `torch.equal`, not
   `torch.testing.assert_close`.

Do not import, patch, or monkey-patch SGLang during correctness or benchmark
runs. All benchmark code must call only files in this task directory.
