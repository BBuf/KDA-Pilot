# PR Discussion Digest

- Source PR: [vllm-project/vllm#27284](https://github.com/vllm-project/vllm/pull/27284)
- Source page: `sources/prs/vllm/PR-27284.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-27284`
- Generated at: `2026-05-20T15:38:15.312451+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-21T19:15:43Z`
- Merged: `2025-11-04T15:49:26Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LyrisZhong, djmmoss, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-21T19:19:13Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a swap A/B optimization for FP8 GEMM on SM100 architectures to improve ... (https://github.com/vllm-project/vllm/pull/27284#pullrequestreview-3362360034)
- `2025-10-31T03:53:50Z` `APPROVED` by `mgoin` - LGTM, great speedups reported. We should make sure to run the lm-eval blackwell test and that should be ... (https://github.com/vllm-project/vllm/pull/27284#pullrequestreview-3402501541)

## Inline Comment Hotspots

- `csrc/quantization/w8a8/cutlass/c3x/scaled_mm_sm100_fp8_dispatch.cuh`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-31T03:52:23Z` `inline` by `mgoin` `csrc/quantization/w8a8/cutlass/c3x/scaled_mm_sm100_fp8_dispatch.cuh`:214; signals: cutlass, fp8, sm100, sm90; excerpt: "This matches the usage in sm90 fp8 swapab" (https://github.com/vllm-project/vllm/pull/27284#discussion_r2480097688)
- `2025-10-31T03:53:50Z` `review` `APPROVED` by `mgoin`; signals: accuracy, blackwell, gemm, speedup; excerpt: "LGTM, great speedups reported. We should make sure to run the lm-eval blackwell test and that should be sufficient for accuracy. Is there a ..." (https://github.com/vllm-project/vllm/pull/27284#pullrequestreview-3402501541)
