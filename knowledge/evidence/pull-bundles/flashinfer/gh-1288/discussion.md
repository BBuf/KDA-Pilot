# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1288](https://github.com/flashinfer-ai/flashinfer/pull/1288)
- Source page: `sources/prs/flashinfer/PR-1288.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1288`
- Generated at: `2026-05-20T15:22:10.135273+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-18T16:45:50Z`
- Merged: `2025-07-21T22:35:17Z`

## Discussion Counts

- Issue comments: 9
- Review submissions: 11 (approved=1, commented=10)
- Inline review comments: 15
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=10, outdated=7
- Human participants with discussion text: Anerudhan, elfiegg, ttyio, yzh119
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-18T16:46:20Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @ttyio, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3034182306)
- `2025-07-18T16:47:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for FP4 matrix multiplication using the cuDNN backend. I've identified a ... (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3034185520)
- `2025-07-18T16:53:18Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3034201704)
- `2025-07-18T16:55:21Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3034207179)
- `2025-07-18T16:56:16Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3034209650)
- `2025-07-18T16:59:50Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3034209127)
- `2025-07-18T17:05:07Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3034239292)
- `2025-07-19T00:22:00Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3035012350)
- `2025-07-19T06:08:45Z` `COMMENTED` by `elfiegg` - Minor issue regarding CUDA graph mode. (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3035171430)
- `2025-07-21T06:57:45Z` `COMMENTED` by `yzh119` - Thanks @ttyio for creating this PR and thanks @elfiegg @Anerudhan for your input. I tried this PR on ... (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3036801427)
- `2025-07-21T17:32:58Z` `APPROVED` by `yzh119` - Overall LGTM, and thank all of you for the effort. cc @Anerudhan for another look on @ttyio 's ... (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3039073934)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 13 inline comment(s)
- `tests/test_mm_fp4.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-07-21T16:02:15Z` `issue` by `Anerudhan`; signals: cuda, flashinfer, fp4, gemm, perf; excerpt: "Thanks @ttyio for creating this PR and thanks @elfiegg @Anerudhan for your input. I tried this PR on different environments and it seems dependency ..." (https://github.com/flashinfer-ai/flashinfer/pull/1288#issuecomment-3097356245)
- `2025-07-18T16:56:16Z` `inline` by `ttyio` `flashinfer/gemm.py`:1149; signals: block, flashinfer, fp4, gemm; excerpt: "this FP4 BLOCK SIZE only lived in this mm fp4 function, no need to add to module-level and exposed." (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2216494236)
- `2025-07-21T06:57:45Z` `review` `COMMENTED` by `yzh119`; signals: flashinfer, fp4, gemm; excerpt: "Thanks @ttyio for creating this PR and thanks @elfiegg @Anerudhan for your input. I tried this PR on different environments and it seems dependency ..." (https://github.com/flashinfer-ai/flashinfer/pull/1288#pullrequestreview-3036801427)
- `2025-07-18T16:59:12Z` `inline` by `yzh119` `flashinfer/gemm.py`:1119; signals: block, flashinfer, gemm; excerpt: "The block size is not mentioned in the docstring and might confuse people. We can still add a block size argument (and when it's ..." (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2216506383)
- `2025-07-18T16:53:18Z` `inline` by `ttyio` `flashinfer/gemm.py`:1151; signals: flashinfer, gemm, hang; excerpt: "leave this unchange to make the sample code more short?" (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2216489093)
- `2025-07-19T06:08:20Z` `inline` by `elfiegg` `flashinfer/gemm.py`:782; signals: cuda, flashinfer, gemm; excerpt: "May we please add something like to ensure CUDA graph can be captured on the right device?" (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2217165171)
- `2025-07-20T07:08:49Z` `issue` by `elfiegg`; signals: benchmark, cache, cute; excerpt: "Two suggestions from the local test from my end: 1. Ensure cached graph is built on the same stream as input, and 2. Ensure ..." (https://github.com/flashinfer-ai/flashinfer/pull/1288#issuecomment-3093753123)
- `2025-07-18T16:55:21Z` `inline` by `ttyio` `flashinfer/gemm.py`:1064; signals: flashinfer, gemm; excerpt: "the minor dim always has stride 1, and other dims has stride multiply by 2, so code in the PR is correct?" (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2216492565)
- `2025-07-18T16:56:03Z` `inline` by `yzh119` `flashinfer/gemm.py`:1102; signals: flashinfer, gemm; excerpt: "Please also handle the logic of early torch versions (e.g. torch 2.7.1 stable do not support torch.float4 e2m1fn x2)." (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2216493841)
- `2025-07-20T06:57:01Z` `issue` by `yzh119`; signals: cuda, cudagraph, kernel; excerpt: "@elfiegg can you put your script for capturing the kernel in cudagraph mode?" (https://github.com/flashinfer-ai/flashinfer/pull/1288#issuecomment-3093691165)
- `2025-07-18T16:56:51Z` `inline` by `yzh119` `flashinfer/gemm.py`:1070; signals: flashinfer, gemm; excerpt: "sounds more clear to me." (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2216495292)
- `2025-07-18T16:57:27Z` `inline` by `yzh119` `flashinfer/gemm.py`:1149; signals: flashinfer, gemm; excerpt: "Please also document it clearly in the documentation." (https://github.com/flashinfer-ai/flashinfer/pull/1288#discussion_r2216497837)
