# PR Discussion Digest

- Source PR: [vllm-project/vllm#23280](https://github.com/vllm-project/vllm/pull/23280)
- Source page: `sources/prs/vllm/PR-23280.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23280`
- Generated at: `2026-05-20T15:37:29.185412+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-20T19:05:53Z`
- Merged: `2025-09-11T22:43:14Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=2, commented=4)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: LucasWilkinson, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-20T19:07:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly enables the SM90 CUTLASS Block FP8 kernel for weight shapes that are ... (https://github.com/vllm-project/vllm/pull/23280#pullrequestreview-3137890861)
- `2025-09-11T15:23:20Z` `COMMENTED` by `yewentao256` - Thanks for the work! (https://github.com/vllm-project/vllm/pull/23280#pullrequestreview-3212302389)
- `2025-09-11T16:47:32Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23280#pullrequestreview-3212754870)
- `2025-09-11T16:48:12Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23280#pullrequestreview-3212759985)
- `2025-09-11T19:25:47Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! (https://github.com/vllm-project/vllm/pull/23280#pullrequestreview-3213330110)
- `2025-09-11T21:21:47Z` `APPROVED` by `LucasWilkinson` - Amazing; thank you for doing this! (https://github.com/vllm-project/vllm/pull/23280#pullrequestreview-3213677329)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`: 5 inline comment(s)

## High-Signal Discussion

- `2025-09-11T16:47:32Z` `inline` by `mgoin` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`:42; signals: block, cutlass, fp8, kernel, sm90; excerpt: "We have this comment in other kernels, it is just something that would be "free" to support if someone wanted to spend the time. ..." (https://github.com/vllm-project/vllm/pull/23280#discussion_r2341741779)
- `2025-09-11T16:48:12Z` `inline` by `mgoin` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`:48; signals: block, cutlass, fp8, sm100, sm90; excerpt: "Just matching the order in scaled mm blockwise sm100 fp8 dispatch.cuh" (https://github.com/vllm-project/vllm/pull/23280#discussion_r2341744957)
- `2025-09-11T15:19:24Z` `inline` by `yewentao256` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`:42; signals: block, cutlass, fp8, sm90; excerpt: "What is the aim of supporting bias, could you share more context?" (https://github.com/vllm-project/vllm/pull/23280#discussion_r2341398154)
- `2025-09-11T15:20:29Z` `inline` by `yewentao256` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`:48; signals: block, cutlass, fp8, sm90; excerpt: "Why a update here" (https://github.com/vllm-project/vllm/pull/23280#discussion_r2341402716)
- `2025-09-11T19:25:14Z` `inline` by `yewentao256` `csrc/quantization/cutlass_w8a8/c3x/scaled_mm_blockwise_sm90_fp8_dispatch.cuh`:42; signals: block, cutlass, fp8, sm90; excerpt: "Make sense" (https://github.com/vllm-project/vllm/pull/23280#discussion_r2342126735)
- `2025-09-11T15:23:20Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Thanks for the work!" (https://github.com/vllm-project/vllm/pull/23280#pullrequestreview-3212302389)
