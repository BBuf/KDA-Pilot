# b200_ltx2_rms_adaln__bitwise

Target GPU: NVIDIA B200.

This task replaces the closed SGLang PR:

- `sgl-project/sglang#29396` (`[Diffusion] Fuse LTX2 RMS AdaLN modulation`)

The PR reused a fused norm-scale-shift path but full-model LTX2.3 HQ
consistency still failed. Do not treat tolerance-based unit tests as success.

Target SGLang diffusion source patterns to copy as local baseline:

- `sglang.multimodal_gen.runtime.models.dits.ltx_2:_ltx2_rms_adaln`
- every PyTorch fallback callsite of the form:
  `rms_norm_layer(x, eps) * (1 + scale) + shift`
- `sglang.multimodal_gen.runtime.layers.layernorm:RMSNormNoWeight`

Goal: produce an optimized RMS AdaLN kernel for LTX2 that is **bit-wise equal**
to the PyTorch eager baseline, so the eventual SGLang replacement does not
change diffusion CI golden outputs.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

## Required Baseline Semantics

Inputs:

- `x`: `[B, S, D]`, `torch.bfloat16`, contiguous.
- `scale`: `[D]`, `[B, D]`, `[B, 1, D]`, or `[B, S, D]`,
  `torch.bfloat16`, last-dim contiguous.
- `shift`: same supported layouts and dtype as `scale`.
- `eps`: `1e-6` unless a workload explicitly overrides it.

Baseline:

```python
normed = torch.nn.functional.rms_norm(x, normalized_shape=(D,), eps=eps)
y = normed * (1 + scale) + shift
```

The task-local baseline must execute the PyTorch eager operations in this order
and use the same broadcasting semantics as the original `ltx_2.py` fallback.
The candidate must match the final `y` with `torch.equal` / byte-level equality.
Tolerances are forbidden.

The optimized candidate must preserve PyTorch's visible rounding points. Do not
use a generic fused RMSNorm-scale-shift kernel if it changes bfloat16 output
bits. If a single fused kernel cannot be bit-wise exact, use a staged candidate
that still reduces launch or memory overhead while matching PyTorch operation
boundaries.

## Required Workload Rows

Use real model shapes, not synthetic shape guesses. Include these rows in
`bench/workloads.json` and correctness tests. They were captured from
`Lightricks/LTX-2.3` with `LTX2TwoStagePipeline`, `width=768`, `height=512`,
`num_frames=121`, `num_gpus=2`, `cfg_parallel_size=2`,
`num_inference_steps=1` on `ion-b200` on 2026-06-28.
The task already contains an initial `bench/workloads.json` seeded with these
rows; keep that file and this section consistent.

The captured RMS AdaLN production rows all use full-shape bf16 modulation
tensors with the same shape as `x`:

- first stage video self-attention / prompt-Q / MLP:
  `x=[2,1536,4096]`, `scale/shift=[2,1536,4096]`, `eps=1e-6`.
- first stage audio self-attention / prompt-Q / MLP:
  `x=[2,126,2048]`, `scale/shift=[2,126,2048]`, `eps=1e-6`.
- second stage video self-attention / prompt-Q / MLP:
  `x=[1,6144,4096]`, `scale/shift=[1,6144,4096]`, `eps=1e-6`.
- second stage audio self-attention / prompt-Q / MLP:
  `x=[1,126,2048]`, `scale/shift=[1,126,2048]`, `eps=1e-6`.

If a support-gate unit test uses a non-production negative row, keep it out of
the benchmark workload list and require fallback or bit-wise exact behavior.
Do not report non-production rows as shape coverage.

Support gates must be explicit and fail closed:

- CUDA only
- `torch.bfloat16` only for optimized path
- last-dim contiguous inputs
- hidden size divisible by 256 and no greater than 8192 for any
  shape-specialized fused path
- scale/shift broadcast layout exactly covered by the local adapter

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
