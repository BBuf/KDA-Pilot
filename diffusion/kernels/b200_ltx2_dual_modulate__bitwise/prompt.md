# b200_ltx2_dual_modulate__bitwise

Target GPU: NVIDIA B200.

This task replaces the closed SGLang PR:

- `sgl-project/sglang#29392` (`[Diffusion] Fuse LTX2 dual modulation`)

The PR showed useful speed potential but did not satisfy full-model diffusion
consistency. Do not copy the failed Triton implementation as the candidate.
Use it only as source context for the callsite and shapes.

Target SGLang diffusion source patterns to copy as local baseline:

- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_rmsnorm_dual_modulate`
- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_try_fused_rmsnorm_ca_dual_modulate`
- the PyTorch fallback code in `LTX2VideoTransformerBlock.forward` around the
  audio-to-video and video-to-audio cross-attention modulation path.

Goal: produce a standalone optimized kernel pair for LTX2 dual modulation that
is **bit-wise equal** to the PyTorch eager baseline for every supported row, so
the result can later replace the SGLang path without changing diffusion CI
golden outputs.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

## Required Baseline Semantics

Implement the local PyTorch eager baseline first. The candidate must match this
baseline with `torch.equal` / byte-level equality. Tolerances are forbidden.

### Explicit dual modulation

Inputs:

- `x`: `[B, S, D]`, `torch.bfloat16`, contiguous.
- `scale0`, `shift0`, `scale1`, `shift1`: each `[B, D]`, `[B, 1, D]`, or
  `[B, S, D]`, `torch.bfloat16`, last-dim contiguous.
- `eps`: `1e-6` unless a workload explicitly overrides it.

Baseline:

```python
normed = torch.nn.functional.rms_norm(x, normalized_shape=(D,), eps=eps)
y0 = normed * (1 + scale0.expand_as(x)) + shift0.expand_as(x)
y1 = normed * (1 + scale1.expand_as(x)) + shift1.expand_as(x)
```

### Cross-attention dual modulation from timestep embedding

Inputs:

- `x`: `[B, S, D]`, `torch.bfloat16`, contiguous.
- `temb_scale_shift`: `[B, 1, 4 * D]` for the captured LTX2/LTX2.3
  production path, or `[B, S, 4 * D]` if a future callsite proves it live;
  `torch.bfloat16`, contiguous.
- `scale_shift_table`: `[4, D]`, `torch.bfloat16` or `torch.float32`,
  last-dim contiguous.
- `eps`: `1e-6` unless a workload explicitly overrides it.

Baseline:

```python
temb_seq = temb_scale_shift.shape[1]
assert temb_seq in (1, S)
scale0, shift0, scale1, shift1 = (
    scale_shift_table.to(dtype=x.dtype).view(1, 1, 4, D)
    + temb_scale_shift.reshape(B, temb_seq, 4, D)
).unbind(dim=2)
normed = torch.nn.functional.rms_norm(x, normalized_shape=(D,), eps=eps)
y0 = normed * (1 + scale0) + shift0
y1 = normed * (1 + scale1) + shift1
```

The optimized candidate must preserve PyTorch's visible rounding points. Do not
reassociate multiply/add operations if doing so changes bfloat16 output bits.
If one monolithic fusion cannot be bit-wise exact, split the candidate into
multiple kernels that match the PyTorch operation boundaries.

## Required Workload Rows

Use real model shapes, not synthetic shape guesses. Include these rows in
`bench/workloads.json` and correctness tests. They were captured from
`Lightricks/LTX-2.3` with `LTX2TwoStagePipeline`, `width=768`, `height=512`,
`num_frames=121`, `num_gpus=2`, `cfg_parallel_size=2`,
`num_inference_steps=1` on `ion-b200` on 2026-06-28.
The task already contains an initial `bench/workloads.json` seeded with these
rows; keep that file and this section consistent.

Explicit dual modulation rows:

- first stage video AV cross-attention: `x=[2,1536,4096]`, params
  `[2,1,4096]`, bf16, `eps=1e-6`.
- first stage audio AV cross-attention: `x=[2,126,2048]`, params
  `[2,1,2048]`, bf16, `eps=1e-6`.
- second stage video AV cross-attention: `x=[1,6144,4096]`, params
  `[1,1,4096]`, bf16, `eps=1e-6`.
- second stage audio AV cross-attention: `x=[1,126,2048]`, params
  `[1,1,2048]`, bf16, `eps=1e-6`.

Cross-attention-from-timestep rows:

- first stage video AV cross-attention: `x=[2,1536,4096]`,
  `temb_scale_shift=[2,1,16384]`, `scale_shift_table=[4,4096]`, table dtype
  `bf16`, `eps=1e-6`.
- first stage audio AV cross-attention: `x=[2,126,2048]`,
  `temb_scale_shift=[2,1,8192]`, `scale_shift_table=[4,2048]`, table dtype
  `bf16`, `eps=1e-6`.
- second stage video AV cross-attention: `x=[1,6144,4096]`,
  `temb_scale_shift=[1,1,16384]`, `scale_shift_table=[4,4096]`, table dtype
  `bf16`, `eps=1e-6`.
- second stage audio AV cross-attention: `x=[1,126,2048]`,
  `temb_scale_shift=[1,1,8192]`, `scale_shift_table=[4,2048]`, table dtype
  `bf16`, `eps=1e-6`.

Reject or fall back for unsupported rows instead of producing approximate
answers:

- non-CUDA inputs
- non-bfloat16 `x`
- non-contiguous last dimension
- hidden size not divisible by 256 or greater than 8192
- parameter hidden size mismatch

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
