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
to the real SGLang LTX2.3 production baseline, so the eventual SGLang
replacement does not change diffusion CI golden outputs.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

## Required Baseline Semantics

This task is no longer allowed to target standalone PyTorch eager in isolation.
The correctness oracle is the expression as executed by SGLang's denoising loop:

- `server_args.disable_autocast=false`
- `dit_precision=bf16`
- `torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=True)`
  is active around the transformer call.

For the live LTX2.3 rows, the visible output of the expression below is fp32.
The candidate ABI must therefore write fp32 outputs bit-for-bit equal to the
production expression. Writing bf16 because `x` is bf16 is a task failure.

Inputs:

- `x`: `[B, S, D]`, `torch.bfloat16`, contiguous.
- `scale`: `[D]`, `[B, D]`, `[B, 1, D]`, or `[B, S, D]`,
  `torch.bfloat16`, last-dim contiguous.
- `shift`: same supported layouts and dtype as `scale`.
- `eps`: `1e-6` unless a workload explicitly overrides it.

Baseline:

```python
with torch.autocast(device_type="cuda", dtype=torch.bfloat16, enabled=True):
    normed = torch.nn.functional.rms_norm(x, normalized_shape=(D,), eps=eps)
    y = normed * (1 + scale) + shift
```

The task-local baseline must execute this production expression in this order
and use the same broadcasting semantics as the original `ltx_2.py` fallback.
The candidate must match the final fp32 `y` with `torch.equal` / byte-level
equality. Tolerances are forbidden.

The optimized candidate must preserve production-visible rounding and promotion
points under autocast. Do not reinterpret an autocast `rms_norm` result as bf16;
that was the root cause of prior NaN/Inf failures. If a single fused kernel
cannot be bit-wise exact, use a staged candidate that still reduces launch or
memory overhead while matching the production operation boundaries.

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
`8160`. Required RMS AdaLN rows from this command family:

- HQ first stage video self-attention / prompt-Q / MLP:
  `x=[1,8160,4096]`, `scale/shift=[1,8160,4096]`, `eps=1e-6`.
- HQ second stage video self-attention / prompt-Q / MLP:
  `x=[1,32640,4096]`, `scale/shift=[1,32640,4096]`, `eps=1e-6`.
- HQ audio rows use the same single-GPU audio shape already listed above:
  `x=[1,126,2048]`, `scale/shift=[1,126,2048]`, `eps=1e-6`.

Source C: SGLang LTX2.3 cookbook/API commands. The documented one-stage and
two-stage default commands use `Lightricks/LTX-2.3`, `768x512`, `121` frames.
Their RMS AdaLN shape coverage is already represented by the unique
`[1,6144,4096]` / `[1,126,2048]` full-resolution rows and the CI two-stage
rows above. Do not add duplicate benchmark rows unless a live model run proves a
new tensor shape or stride.

## Shape-Specialized Dispatch Requirement

The final optimized solution may use different kernels, template parameters,
or launch policies for different `(B, S, D, scale_layout, shift_layout)` rows.
In fact, prefer an explicit shape table or dispatcher when a single generic
kernel loses on either the CI rows or the HQ PR rows. It is acceptable to
dispatch separately for video `S in {1536,6144,8160,32640}` and audio
`S=126`, and for `D in {4096,2048}`, as long as every selected path is
bit-wise equal to the production baseline and unsupported shapes fail closed or
fall back to the exact production implementation.

Do not claim success from an average speedup if one of the production shape
families regresses. Report per-shape timings and explain the dispatcher choice.

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
2. Implement a task-local SGLang production baseline adapter with the exact
   autocast semantics above.
3. Expose the candidate through the exact same ABI in `solution/`.
4. Verify the seeded `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.
5. Make correctness fail on any non-bitwise result, output dtype mismatch, NaN,
   Inf, or hot exception fallback. Use `torch.equal`, not
   `torch.testing.assert_close`.

Do not import, patch, or monkey-patch SGLang during correctness or benchmark
runs. All benchmark code must call only files in this task directory.
