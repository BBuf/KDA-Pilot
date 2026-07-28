# H100 SOL Attention Quality Gate

This experiment track evaluates the SOL Attention backend before any SGLang
integration PR.

## Source

- repository: `https://github.com/NVlabs/Sana`
- branch: `sol-engine`
- commit: `6f064c542a8d8676d332b123d71c9d6166d870a0`
- source directory: `techniques/sparse_backends/sol_attn`
- license: Apache-2.0; preserve upstream notices in adapted files

## Hardware And Tensor Contract

- H100 / SM90 and B200 / SM100;
- forward-only BF16 attention;
- BTHD Q/K/V with head dimension 128;
- 64-token routing blocks;
- H100 split-KV factors 1, 2, and 4;
- exact text KV sink blocks;
- exact Hunyuan text query rows;
- configured diagonal/exact threshold.

Unsupported head dimensions, dtypes, backward, and architectures must fail
closed before kernel launch.

## Evidence Required Before SGLang PR

1. Compare the upstream dense reference and SOL output at the attention layer.
2. Run fixed-seed SGLang denoise trajectories and report per-step tensor error.
3. Run fixed-prompt image/video output comparisons with SSIM, LPIPS, PSNR,
   mean/max pixel difference, and the model's existing GT gate.
4. Report denoise and end-to-end latency on H100, including routing overhead.
5. Keep the backend opt-in. A model-specific default requires separate evidence.

The latest SOL Engine branch notes that fresh end-to-end benchmarks are still
pending. Do not attribute historical stack-level speedups to this exact commit.

## H100 Layer Validation, 2026-07-29

Environment:

- NVIDIA H100 80GB HBM3, SM90;
- PyTorch `2.11.0+cu130`, Triton `3.6.0`;
- SOL Attention commit
  `6f064c542a8d8676d332b123d71c9d6166d870a0`.

For BF16 Q/K/V shaped `[1, 2048, 4, 128]`, with Q/K scaled by `0.25`,
`tau=1.0`, and a float32 dense SDPA reference:

- diagonal and exact threshold modes both produced finite outputs;
- cosine similarity was `0.998544` to `0.998635`;
- mean absolute error was `0.000951` to `0.000983`;
- maximum absolute error was at most `0.006601`;
- both zero sink tokens and a 77-token exact KV sink were exercised.

For `[1, 16384, 1, 128]`, exact threshold mode, `tau=1.0`, and a 77-token
sink, `kv_splits=1`, `2`, and `4` all produced finite output. Relative to
split 1, split 2/4 had cosine similarity at least `0.9999948` and maximum
absolute difference `0.0001220703125`.

This is layer-level SM90 evidence only. It does not satisfy the denoise
trajectory, output GT, or end-to-end latency gates above, so no SGLang
integration PR is authorized by this result.
