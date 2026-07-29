# b200_wan_vae_rmsnorm_silu__bitwise

Target GPU: NVIDIA B200.

Research baseline verified against:

- repository: `https://github.com/sgl-project/sglang`
- branch: `main`
- commit: `86ee545388677733df8da4cf8726c13d7b445875`
- verified: `2026-07-29`

Resolve `main` again when the task is launched and record the then-current
commit in `docs/baseline_source.md`. All four configured entry points still
exist at the audit commit.

This task replaces the closed SGLang PR:

- `sgl-project/sglang#30171` (`[diffusion] Fuse Wan VAE RMSNorm SiLU`)

The PR proved that local fused-helper tolerance tests are not enough for Wan
VAE. The fused RMSNorm + SiLU path changed `wan22_modelopt_nvfp4_t2v` video
pixels even after the kernel was adjusted to better match eager rounding. Do
not copy the failed Triton implementation as the candidate. Use it only as
source context for callsites, tensor layouts, and the failed validation
evidence.

Target SGLang diffusion source patterns to copy as local baseline:

- `sglang.multimodal_gen.runtime.models.vaes.wanvae:WanRMS_norm`
- `sglang.multimodal_gen.runtime.models.vaes.wanvae:residual_block_forward`
- `sglang.multimodal_gen.runtime.models.vaes.wanvae:WanEncoder3d.forward`
- `sglang.multimodal_gen.runtime.models.vaes.wanvae:WanDecoder3d.forward`
- every Wan VAE callsite of the form `nonlinearity(norm(x))`, where
  `nonlinearity` is `torch.nn.SiLU`.

Goal: produce optimized Wan VAE RMSNorm + SiLU kernels that are **bit-wise
equal** to the real SGLang Wan2.2 production baseline in the B200 diffusion
server path, so an eventual SGLang replacement does not change diffusion CI
golden videos or same-prompt generated frames.

Before writing an optimized kernel, read and follow:

- `../../docs/standalone_diffusion_benchmark.md`
- `../../docs/diffusion_kernel_rules.md`
- `../../docs/diffusion_correctness_contract.md`

## Failed PR Evidence To Preserve

Use this evidence to set the correctness bar. Do not treat any of these failed
variants as acceptable candidates:

- Failing PR: `sgl-project/sglang#30171`
- CI job:
  `https://github.com/sgl-project/sglang/actions/runs/28768288693/job/85546452103?pr=30171`
- CI merge commit: `b238a27e92ab40fe50ec752bac08b0b8a65b3f37`
- Merge parent / base commit: `b1942fc3ea95086edb55a9ef044f274428a82f47`
- Head commit: `65908633c2c8b85fc61a7bedd192390901252bcc`

The failing CI case was:

- test:
  `sglang/multimodal_gen/test/server/test_server_b200.py::TestDiffusionServerOneGpuB200::test_diffusion_generation[wan22_modelopt_nvfp4_t2v]`
- model: `nvidia/Wan2.2-T2V-A14B-Diffusers-NVFP4`
- model snapshot:
  `ac69f2655787c3af65e1756d001303cd4a4daa46`
- prompt: `A curious raccoon`
- seed: `0`
- size: `640x384`
- frames: `17`
- denoise steps: `12`
- layerwise offload components: `dit`, `text_encoder`, `image_encoder`
- VAE remains resident and uses `channels_last_3d` Conv3d weights.

Remote reproduction on `ion-b200` with the same model snapshot and offload
shape showed:

- PR / fused path output:
  - frame 0: `SSIM=0.9553`, `PSNR=35.6374`, `mean_abs_diff=2.7768`
  - frame mid: `SSIM=0.9188`, `PSNR=32.6963`, `mean_abs_diff=4.0707`
  - frame last: `SSIM=0.9097`, `PSNR=32.0419`, `mean_abs_diff=4.3359`
  - summary: `min_ssim=0.9097`, below the CI threshold `0.92`
- Base / production output:
  - frame 0: `SSIM=1.0000`, `PSNR=inf`, `mean_abs_diff=0.0000`
  - frame mid: `SSIM=1.0000`, `PSNR=inf`, `mean_abs_diff=0.0000`
  - frame last: `SSIM=1.0000`, `PSNR=inf`, `mean_abs_diff=0.0000`

The PR unit test `test/registered/jit/diffusion/test_wan_rmsnorm_silu.py`
passed with dtype tolerances, but the full server video consistency case failed.
Therefore the task success criterion is production-visible bit equality, not
`torch.testing.assert_close`.

## Required Baseline Semantics

This task must target the production SGLang Wan VAE path, not a standalone eager
approximation. The correctness oracle is the exact subgraph as it runs inside
Wan VAE encode/decode during the diffusion server request.

The failed PR replaced these production operation boundaries:

```python
x = norm(x)
x = nonlinearity(x)
```

with a single fused helper at:

- residual block first normalization / activation
- residual block second normalization / activation
- encoder head normalization / activation
- decoder head normalization / activation

The task-local baseline must preserve the same operation order, dtype
promotion, rounding, broadcasting, memory format, and graph boundaries as
SGLang production. The candidate must match every visible output tensor with
`torch.equal` / byte-level equality. Tolerances are forbidden.

`WanRMS_norm` channel-first semantics must be copied exactly. In particular,
the local baseline must preserve the production behavior equivalent to:

```python
y = torch.nn.functional.normalize(x, dim=1) * norm.scale * norm.gamma
if norm.bias is not None:
    y = y + norm.bias
out = torch.nn.functional.silu(y)
```

Do not use algebraic rearrangement, FMA contraction, one-rounding epilogues, or
dtype shortcuts unless byte-level tests prove they are identical in the copied
production context. If a single fused kernel cannot be bit-wise exact, use
staged kernels that still reduce launch or memory overhead while matching the
production operation boundaries.

Hot-path exception fallback is not success. Unsupported rows must be rejected by
cheap Python/C++ preflight guards before launching the raw kernel; repeated
dtype/shape exceptions inside the benchmark or SGLang integration count as a
regression even if fallback output is correct.

## Required Workload Rows

Use real model shapes, not synthetic shape guesses. Include these rows in
`bench/workloads.json` and correctness tests, then update this section if a live
B200 capture proves additional rows.

Source A: Wan2.2 ModelOpt NVFP4 text-to-video CI row.

- model: `nvidia/Wan2.2-T2V-A14B-Diffusers-NVFP4`
- native SGLang backend, `WanPipeline`
- prompt: `A curious raccoon`
- seed: `0`
- output: `640x384`, `17` frames
- denoise steps: `12`
- target test: `wan22_modelopt_nvfp4_t2v`
- VAE dtype: `torch.bfloat16`
- optimized-path memory format: `torch.channels_last_3d`
- full-video validation must compare against the CI golden frames from
  `sgl-project/ci-data` revision
  `46b9b53a429606cb6739c861f275c1277c314a10`.

Required sub-rows for every captured VAE stage:

- residual block first normalization + SiLU:
  `out = SiLU(WanRMS_norm(x))`
- residual block second normalization + SiLU:
  `out = SiLU(WanRMS_norm(x))`
- encoder head normalization + SiLU:
  `out = SiLU(WanRMS_norm(x))`
- decoder head normalization + SiLU:
  `out = SiLU(WanRMS_norm(x))`

Capture and record the exact `(B, C, T, H, W)`, strides, dtype, bias presence,
and `norm.scale` for each retained row before implementing the candidate. Keep
only live production rows in the benchmark workload list. Non-production
negative rows belong in support-gate tests, not benchmark averages.

Source B: full-video validation row:

- model: `nvidia/Wan2.2-T2V-A14B-Diffusers-NVFP4`
- prompt: `A curious raccoon`
- seed: `0`
- size: `640x384`
- frames: `17`
- `num_inference_steps=12`
- B200, single GPU
- server-style launch with automatic memory policy that keeps VAE resident and
  layerwise-offloads `dit`, `text_encoder`, and `image_encoder`.

The full-video validation must compare candidate output against a freshly
generated production baseline from the same source commit and command. Report
per-frame SSIM, PSNR, mean absolute pixel difference, max absolute pixel
difference, and byte-level `identical` status for frame 0, middle frame, and
last frame. Success requires `identical=True` or zero pixel diff for all three
frames unless the task owner explicitly updates this prompt with a stricter
production-approved oracle.

## Shape-Specialized Dispatch Requirement

The final optimized solution may use different kernels, template parameters, or
launch policies for different VAE stages and channel counts. Prefer an explicit
dispatcher if one generic kernel cannot satisfy both bitwise correctness and
speed.

Support gates must be explicit and fail closed:

- CUDA only
- `torch.bfloat16` only for the initial optimized path unless a live production
  row proves another dtype
- 5-D tensor layout `[B, C, T, H, W]`
- `torch.channels_last_3d` contiguous input and output for optimized path
- channel dimension no greater than the chosen kernel's proven maximum
- `norm.gamma` and optional `norm.bias` are CUDA bf16 tensors on the same device
- no in-place aliasing between destination and source tensors unless the
  baseline proves the same aliasing is production-visible
- no candidate path inside `torch.compile` unless the compiled full-video
  output is bit-wise equal to the production baseline

Do not claim success from average speedup if any sub-row or full-video
validation fails bitwise. Report per-row timings and explain any dispatcher
choice.

## Required First Milestone

1. Copy the relevant upstream SGLang snippets into `baseline/` and record the
   exact source commit in `docs/baseline_source.md`.
2. Implement a task-local SGLang production baseline adapter that preserves the
   exact Wan VAE semantics above. Do not benchmark against a simplified eager
   expression alone.
3. Expose candidate kernels through the exact same ABI in `solution/`.
4. Create `bench/workloads.json`, copy the standard template to
   `bench/benchmark.py`, implement `bench/adapter.py`, and create
   `bench/correctness.py`.
5. Make correctness fail on any non-bitwise result, output dtype mismatch, NaN,
   Inf, hot exception fallback, missing workload capture, or missing full-video
   validation evidence. Use `torch.equal`, not `torch.testing.assert_close`.

Do not import, patch, or monkey-patch SGLang during standalone correctness or
benchmark runs. All standalone benchmark code must call only files in this task
directory. Full-video validation may run SGLang, but it must compare a clean
production baseline against the candidate branch under the same command.
