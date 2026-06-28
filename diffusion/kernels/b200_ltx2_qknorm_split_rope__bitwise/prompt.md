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
that is **bit-wise equal** to the PyTorch eager baseline, so the eventual
SGLang replacement does not change diffusion CI golden outputs.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

## Required Baseline Semantics

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

The task-local baseline must use a copied implementation of
`apply_split_rotary_emb` with the same layout and operation order as SGLang.
The candidate must match `q_out` and `k_out` with `torch.equal` / byte-level
equality. Tolerances are forbidden.

The optimized candidate must preserve PyTorch's visible rounding points for
RMSNorm and the split-RoPE multiply/add/sub sequence. Do not use an algebraic
rearrangement or FMA contraction if it changes bfloat16 output bits. If one
monolithic kernel cannot be bit-wise exact, split the candidate into staged
kernels that still reduce overhead while matching PyTorch operation boundaries.

## Required Workload Rows

Use real model shapes, not synthetic shape guesses. Include these rows in
`bench/workloads.json` and correctness tests. They were captured from
`Lightricks/LTX-2.3` with `LTX2TwoStagePipeline`, `width=768`, `height=512`,
`num_frames=121`, `num_gpus=2`, `cfg_parallel_size=2`,
`num_inference_steps=1` on `ion-b200` on 2026-06-28.
The task already contains an initial `bench/workloads.json` seeded with these
rows; keep that file and this section consistent.

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
2. Implement a task-local PyTorch eager baseline adapter with the exact
   semantics above.
3. Expose the candidate through the exact same ABI in `solution/`.
4. Verify the seeded `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.
5. Make correctness fail on any non-bitwise result. Use `torch.equal`, not
   `torch.testing.assert_close`.

Do not import, patch, or monkey-patch SGLang during correctness or benchmark
runs. All benchmark code must call only files in this task directory.
