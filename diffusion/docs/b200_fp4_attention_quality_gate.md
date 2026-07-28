# B200 FP4 Attention Quality Gate

This experiment track covers FP4 attention only for checkpoints trained or
calibrated for the corresponding Q/K quantization scheme.

## Source

- FastVideo repository: `https://github.com/hao-ai-lab/FastVideo`
- commit: `1b2b2a0161bc6b3b80158d1fa6380a051c6530c7`
- RTX 5090 / SM120 modified SageAttention3: PR 1455
- B200/GB300 FA4 FP4 Q/K with BF16 P/V: PR 1647
- license: Apache-2.0; preserve upstream notices in adapted files

## Gates

- H100 validation must prove import safety and deterministic architecture
  rejection; H100 cannot validate FP4 tensor-core performance.
- B200 or GB300 validates the SM100 kernel, numerical output, memory use, and
  speed.
- SM120 validation is a separate path and cannot stand in for SM100 evidence.
- Generic BF16 checkpoints must never silently enter FP4 attention.
- Enablement requires checkpoint metadata that explicitly declares the trained
  or calibrated FP4 attention scheme.

## Evidence Required Before SGLang PR

1. Layer-level comparison against the checkpoint's reference implementation.
2. Fixed-seed denoise-trajectory error over all steps.
3. Existing SGLang GT quality check plus SSIM, LPIPS, PSNR, and pixel deltas.
4. Denoise and end-to-end latency, peak memory, and architecture-gate tests.
5. Explicit fallback or rejection for H100, unsupported head dimensions, and
   checkpoints without FP4 attention metadata.

The reported FastVideo LTX2.3 numbers may be cited as upstream evidence, not as
SGLang results. SGLang performance claims require a fresh controlled run.

## H100 Negative-Path Validation, 2026-07-29

FastVideo commit `1b2b2a0161bc6b3b80158d1fa6380a051c6530c7` was built on an
NVIDIA H100 80GB HBM3 with CUDA 13.0 and `TORCH_CUDA_ARCH_LIST=9.0a`.

- `fastvideo-kernel 0.3.2` imported successfully;
- the build summary disabled the SM120-only FP4 extensions;
- neither `fp4attn_cuda` nor `fp4quant_cuda` was present;
- importing `attn_qat_infer.api` failed closed with
  `ModuleNotFoundError: fp4attn_cuda`;
- FastVideo's `tests/test_attn_qat_infer.py` was collected and skipped through
  its explicit missing-extension architecture gate.

This proves import safety for the general kernel package and deterministic
exclusion of the FP4 path on H100. It is not numerical or performance evidence
for SM100/SM120.
