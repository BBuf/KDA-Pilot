# PR Discussion Digest

- Source PR: [sgl-project/sglang#7631](https://github.com/sgl-project/sglang/pull/7631)
- Source page: `sources/prs/sglang/PR-7631.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7631`
- Generated at: `2026-05-20T15:31:18.593284+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-29T09:56:42Z`
- Merged: `2025-08-14T06:13:22Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: M0gician, ch-wan
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-29T09:57:04Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @M0gician, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7631#pullrequestreview-2969183777)
- `2025-06-29T09:58:11Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds new fused MoE kernel configurations for Triton 3.3 on NVIDIA H20 GPUs, ... (https://github.com/sgl-project/sglang/pull/7631#pullrequestreview-2969184043)
- `2025-06-29T12:55:28Z` `COMMENTED` by `M0gician` (https://github.com/sgl-project/sglang/pull/7631#pullrequestreview-2969246410)
- `2025-08-14T06:13:13Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/7631#pullrequestreview-3119154863)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_3_1/E=128,N=384,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-29T12:55:28Z` `inline` by `M0gician` `python/sglang/srt/layers/moe/fused_moe_triton/configs/triton_3_3_1/E=128,N=384,device_name=NVIDIA_H20,dtype=fp8_w8a8,block_shape=[128, 128].json`:146; signals: benchmark, block, dtype, fp8, moe, triton; excerpt: "DeepSeek-V3 Deploy model: Benchmark: Result (without Moe config): Result (with Moe config): Qwen3-235B-A22B-FP8 Deploy model: Benchmark: Result (without Moe config): Result (with Moe config): ..." (https://github.com/sgl-project/sglang/pull/7631#discussion_r2173749390)
