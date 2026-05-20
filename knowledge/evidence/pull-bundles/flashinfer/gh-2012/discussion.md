# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2012](https://github.com/flashinfer-ai/flashinfer/pull/2012)
- Source page: `sources/prs/flashinfer/PR-2012.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2012`
- Generated at: `2026-05-20T15:23:45.508113+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-30T18:19:32Z`
- Merged: `2025-10-30T21:23:36Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bkryu, coderabbitai, nvmbreughe, yongwww, yzh119
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-30T18:40:19Z` `APPROVED` by `nvmbreughe` - LGTM. Thanks, Brian! (https://github.com/flashinfer-ai/flashinfer/pull/2012#pullrequestreview-3401123326)
- `2025-10-30T18:40:27Z` `COMMENTED` by `yongwww` (https://github.com/flashinfer-ai/flashinfer/pull/2012#pullrequestreview-3401123869)
- `2025-10-30T18:40:56Z` `COMMENTED` by `nvmbreughe` (https://github.com/flashinfer-ai/flashinfer/pull/2012#pullrequestreview-3401125616)
- `2025-10-30T21:23:30Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2012#pullrequestreview-3401718682)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-30T18:19:42Z` `issue` by `coderabbitai`; signals: benchmark, cutlass, dtype, flashinfer, fp4, gemm, hang, sm120; excerpt: "Walkthrough Version 12.1 support is added across FP4 backends in benchmarks and the GEMM library. Benchmark utility mappings are extended to recognize "12.1" alongside ..." (https://github.com/flashinfer-ai/flashinfer/pull/2012#issuecomment-3469420532)
- `2025-10-30T18:40:27Z` `inline` by `yongwww` `flashinfer/gemm.py`:1833; signals: flashinfer, gemm; excerpt: "110 is also supported if I remember correctly, cc: @ttyio" (https://github.com/flashinfer-ai/flashinfer/pull/2012#discussion_r2479157164)
- `2025-10-30T18:40:56Z` `inline` by `nvmbreughe` `flashinfer/gemm.py`:1833; signals: flashinfer, gemm; excerpt: "It was explicitly disabled on trtllm in the original checks. The other backends support it" (https://github.com/flashinfer-ai/flashinfer/pull/2012#discussion_r2479158577)
