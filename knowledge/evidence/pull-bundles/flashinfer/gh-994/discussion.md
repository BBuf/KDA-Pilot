# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#994](https://github.com/flashinfer-ai/flashinfer/pull/994)
- Source page: `sources/prs/flashinfer/PR-994.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-994`
- Generated at: `2026-05-20T15:26:51.521364+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-01T22:09:32Z`
- Merged: `2025-04-18T03:01:26Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: yzh119
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-02T03:57:07Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/994#pullrequestreview-2734594001)
- `2025-04-16T06:01:20Z` `COMMENTED` by `yzh119` - Please do not move anything in src directory to include (see changes which would break the compilation of ... (https://github.com/flashinfer-ai/flashinfer/pull/994#pullrequestreview-2770998585)
- `2025-04-18T03:01:21Z` `APPROVED` by `yzh119` - Let's merge this one first, in the future we might design standarize APIs as flashinfer.distributed. The main purpose ... (https://github.com/flashinfer-ai/flashinfer/pull/994#pullrequestreview-2777404046)

## Inline Comment Hotspots

- `include/flashinfer/customAllReduceKernels.h`: 3 inline comment(s)
- `csrc/customAllReduceKernels.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-04-16T06:01:20Z` `review` `COMMENTED` by `yzh119`; signals: benchmark, hang; excerpt: "Please do not move anything in src directory to include (see changes which would break the compilation of C++ benchmarks/unittests. I checked the codebase ..." (https://github.com/flashinfer-ai/flashinfer/pull/994#pullrequestreview-2770998585)
- `2025-04-18T03:01:21Z` `review` `APPROVED` by `yzh119`; signals: block, flashinfer, nan; excerpt: "Let's merge this one first, in the future we might design standarize APIs as flashinfer.distributed. The main purpose of this PR is to unblock ..." (https://github.com/flashinfer-ai/flashinfer/pull/994#pullrequestreview-2777404046)
- `2025-04-02T03:56:11Z` `inline` by `yzh119` `include/flashinfer/customAllReduceKernels.h`:19; signals: flashinfer, kernel; excerpt: "Can you find a minimal runtime dependency in these headers?" (https://github.com/flashinfer-ai/flashinfer/pull/994#discussion_r2024028124)
- `2025-04-02T03:56:16Z` `inline` by `yzh119` `include/flashinfer/customAllReduceKernels.h`:23; signals: flashinfer, kernel; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/994#discussion_r2024028165)
- `2025-04-02T03:56:21Z` `inline` by `yzh119` `include/flashinfer/customAllReduceKernels.h`:24; signals: flashinfer, kernel; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/994#discussion_r2024028204)
- `2025-04-02T03:56:42Z` `inline` by `yzh119` `csrc/customAllReduceKernels.cu`:18; signals: kernel; excerpt: "ditto" (https://github.com/flashinfer-ai/flashinfer/pull/994#discussion_r2024028437)
