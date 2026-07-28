# b200_ernie_adaln_residual_gate__bitwise

Target GPU: NVIDIA B200.

Research baseline verified against:

- repository: `https://github.com/sgl-project/sglang`
- branch: `main`
- commit: `86ee545388677733df8da4cf8726c13d7b445875`
- verified: `2026-07-29`

Resolve `main` again when the task is launched and record the then-current
commit in `docs/baseline_source.md`. The commit above is the task-definition
audit point, not permission to use a stale baseline.

This task replaces the closed / abandoned SGLang PR direction:

- `sgl-project/sglang#30170` (`ERNIE-Image fused AdaLN / residual-gate fast path`)

The PR showed that local fused helper tests are not enough for ERNIE. Diffusion
trajectory sensitivity amplified tiny arithmetic and graph-boundary changes into
large image differences. Do not copy the failed implementation as the candidate.
Use it only as source context for callsites, tensor layouts, and the failed
validation evidence.

Target SGLang diffusion source patterns to copy as local baseline:

- `sglang.multimodal_gen.runtime.models.dits.ernie_image:ErnieImageSharedAdaLNBlock.forward`
- `sglang.multimodal_gen.runtime.layers.layernorm:RMSNorm.forward_cuda`
- `sglang.multimodal_gen.runtime.layers.layernorm:RMSNorm.forward_native`

The three historical helper names `_ernie_norm_scale_shift`,
`_ernie_scale_residual_norm_scale_shift`, and `_ernie_residual_gate_add` no
longer exist on current SGLang `main`. Do not recreate them as the baseline.
The authoritative production boundaries are the eager expressions in
`ErnieImageSharedAdaLNBlock.forward` and the current CUDA RMSNorm dispatch.

Goal: produce optimized ERNIE AdaLN / residual-gate fused kernels that are
**bit-wise equal** to the real SGLang ERNIE-Image Turbo production baseline in
the `torch.compile` path, so an eventual SGLang replacement does not change
diffusion CI golden outputs or same-prompt generated images.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

## Failed PR Evidence To Preserve

Use this evidence to set the correctness bar. Do not treat any of these failed
variants as acceptable candidates:

- Baseline: SGLang main / production ERNIE eager expressions, same prompt and
  seed.
- Current #30170 path with only `_ernie_residual_gate_add` still fused after
  reverting the two AdaLN RMSNorm fused helpers:
  - `SSIM=0.736905`
  - `PSNR=17.265267`
  - `mean_abs=18.938561`
  - `max_abs=255`
  - `identical=False`
- One-rounding final add experiment
  (`out = round(residual + update * gate)` in the custom CUDA kernel):
  - `SSIM=0.802430`
  - `PSNR=18.769675`
  - `mean_abs=15.324255`
  - `max_abs=255`
  - `identical=False`
  - also breaks the shared `residual_gate_add` bitwise unit-test contract.
- Full eager / no fused AdaLN helpers:
  - `SSIM=1.000000`
  - `mean_abs=0`
  - `max_abs=0`
  - `identical=True`
- Compile-fallback experiment, where the ERNIE helper returns the original
  expression while `torch.compiler.is_compiling()` is true:
  - `SSIM=1.000000`
  - `mean_abs=0`
  - `max_abs=0`
  - `identical=True`

Diagnostic command family used for the evidence above:

```bash
sglang generate \
  --model-path baidu/ERNIE-Image-Turbo \
  --backend sglang \
  --config /tmp/ernie_quality_config.json \
  --save-output \
  --output-file-path /tmp/ernie_quality_outputs/<label>/ernie.png \
  --perf-dump-path /tmp/ernie_quality_outputs/<label>/perf.json \
  --warmup \
  --enable-torch-compile
```

with config:

```json
{
  "backend": "sglang",
  "model_path": "baidu/ERNIE-Image-Turbo",
  "prompt": "A futuristic cyberpunk city at night, neon lights reflecting on wet streets",
  "seed": 42,
  "width": 1024,
  "height": 1024,
  "use_pe": false
}
```

The evidence run used the native SGLang diffusion backend:

- log contains `Using pipeline from model_index.json: ErnieImagePipeline`
- log does not contain `Falling back to diffusers backend`
- log does not contain `Using diffusers backend`
- log does not contain `Loaded diffusers pipeline`

## Required Baseline Semantics

This task must target the production SGLang ERNIE-Image Turbo path, not a
standalone eager approximation. The correctness oracle is the block subgraph as
it runs inside the denoising loop with `--enable-torch-compile`.

The production ERNIE command currently runs with:

- `model_path=baidu/ERNIE-Image-Turbo`
- native `ErnieImagePipeline`
- `dit_precision=bf16`
- `server_args.disable_autocast=true`
- `torch.compile` enabled for the transformer
- no prompt enhancement for the required fixed-prompt validation row
  (`use_pe=false`, `PromptEnhancementStage` finishes in `0.0000s`)

Baseline block semantics:

```python
residual = x
x = adaLN_sa_ln(x) * (1 + scale_msa) + shift_msa
attention_output = self_attention(x, rotary_pos_emb)

residual = residual + gate_msa * attention_output
x = adaLN_mlp_ln(residual) * (1 + scale_mlp) + shift_mlp
x = residual + gate_mlp * mlp(x)
```

The task-local baseline must preserve the same operation order, dtype promotion,
rounding, broadcasting, and `torch.compile` graph boundaries as SGLang
production. The candidate must match every visible output tensor with
`torch.equal` / byte-level equality. Tolerances are forbidden.

Local op-level equality is not sufficient. A custom op that is locally close or
even algebraically equivalent can still change the compiled graph boundary and
fail full-image consistency. The final milestone must include same-prompt image
comparison against a production baseline, with `identical=True` or
`SSIM=1.000000` and zero pixel diff.

If a single monolithic fused kernel cannot be bit-wise exact, use staged kernels
that still reduce launch or memory overhead while matching the production
operation boundaries. Do not use FMA contraction, reassociation, one-rounding
epilogues, or dtype shortcuts unless byte-level tests prove they are identical
in the compiled production context.

Hot-path exception fallback is not success. Unsupported rows must be rejected by
cheap Python/C++ preflight guards before launching the raw kernel; repeated
dtype/shape exceptions inside the benchmark or SGLang integration count as a
regression even if fallback output is correct.

## Required Workload Rows

Use real model shapes, not synthetic shape guesses. Include these rows in
`bench/workloads.json` and correctness tests, then update this section if a live
B200 capture proves additional rows.

Source A: ERNIE-Image Turbo, 1024x1024 text-to-image, seed 42, native SGLang
pipeline, `--enable-torch-compile`.

Captured / expected production rows for `ErnieImageSharedAdaLNBlock`:

- token tensor: `x=[1,4096,4096]`, `torch.bfloat16`, contiguous
- modulation tensors:
  - `shift_msa=[1,1,4096]`, `scale_msa=[1,1,4096]`,
    `gate_msa=[1,1,4096]`, bf16
  - `shift_mlp=[1,1,4096]`, `scale_mlp=[1,1,4096]`,
    `gate_mlp=[1,1,4096]`, bf16
- RMSNorm weights:
  - `adaLN_sa_ln.weight=[4096]`, bf16
  - `adaLN_mlp_ln.weight=[4096]`, bf16
- RMSNorm epsilon: use the value from the copied SGLang `RMSNorm` module; do
  not hard-code a different epsilon in the candidate.

Required sub-rows:

- self-attention AdaLN:
  `out = RMSNorm(x) * (1 + scale_msa) + shift_msa`
- attention residual plus MLP AdaLN:
  `residual_out = residual + gate_msa * attention_output`
  then `out = RMSNorm(residual_out) * (1 + scale_mlp) + shift_mlp`
- MLP residual gate:
  `out = residual + gate_mlp * mlp_output`

Source B: full-image validation row:

- model: `baidu/ERNIE-Image-Turbo`
- prompt:
  `A futuristic cyberpunk city at night, neon lights reflecting on wet streets`
- seed: `42`
- width/height: `1024x1024`
- `use_pe=false`
- `--backend sglang`
- `--enable-torch-compile`
- `--warmup`

The full-image validation must compare candidate output against a freshly
generated production baseline image from the same source commit and command.
Report SSIM, PSNR, mean absolute pixel difference, max absolute pixel
difference, and `identical`.

## Shape-Specialized Dispatch Requirement

The final optimized solution may use different kernels, template parameters, or
launch policies for different sub-rows. Prefer an explicit dispatcher if one
generic kernel cannot satisfy both bitwise correctness and speed.

Support gates must be explicit and fail closed:

- CUDA only
- `torch.bfloat16` only for the optimized path unless a live production row
  proves another dtype
- contiguous last dimension
- hidden size exactly `4096` for the initial ERNIE production row
- modulation tensors in `[1, 1, D]` broadcast layout for the initial optimized
  path
- no in-place aliasing between destination and source tensors unless the
  baseline proves the same aliasing is production-visible
- no candidate path inside `torch.compile` unless the compiled full-image output
  is bit-wise equal to the production baseline

Do not claim success from average speedup if any sub-row or the full-image
validation fails bitwise. Report per-row timings and explain any dispatcher
choice.

## Required First Milestone

1. Copy the relevant upstream SGLang snippets into `baseline/` and record the
   exact source commit in `docs/baseline_source.md`.
2. Implement a task-local SGLang production baseline adapter that preserves the
   exact `torch.compile` semantics above. Do not benchmark against a simplified
   eager expression alone.
3. Expose candidate kernels through the exact same ABI in `solution/`.
4. Create `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.
5. Make correctness fail on any non-bitwise result, output dtype mismatch, NaN,
   Inf, hot exception fallback, or missing full-image validation evidence. Use
   `torch.equal`, not `torch.testing.assert_close`.

Do not import, patch, or monkey-patch SGLang during standalone correctness or
benchmark runs. All standalone benchmark code must call only files in this task
directory. Full-image validation may run SGLang, but it must compare a clean
production baseline against the candidate branch under the same command.
