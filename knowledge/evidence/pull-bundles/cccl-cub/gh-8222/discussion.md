# PR Discussion Digest

- Source PR: [NVIDIA/cccl#8222](https://github.com/NVIDIA/cccl/pull/8222)
- Source page: `sources/prs/cccl-cub/PR-8222.md`
- Evidence bundle: `evidence/pull-bundles/cccl-cub/gh-8222`
- Generated at: `2026-05-20T15:20:34.571144+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-31T07:14:22Z`
- Merged: `2026-03-31T14:19:34Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: bernhardmgruber, miscco
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-31T07:15:19Z` `COMMENTED` by `bernhardmgruber` (https://github.com/NVIDIA/cccl/pull/8222#pullrequestreview-4035219249)
- `2026-03-31T07:20:25Z` `APPROVED` by `miscco` (https://github.com/NVIDIA/cccl/pull/8222#pullrequestreview-4035242300)

## Inline Comment Hotspots

- `thrust/testing/scan.cu`: 1 inline comment(s)
- `cub/cub/device/dispatch/dispatch_scan.cuh`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-31T07:15:19Z` `inline` by `bernhardmgruber` `thrust/testing/scan.cu`:739; signals: failing, hang; excerpt: "This check is currently failing spuriously in the CI, because rhs[lhs[i]] reads out of bounds here sometimes. This change makes the failure deterministic and ..." (https://github.com/NVIDIA/cccl/pull/8222#discussion_r3013984682)
- `2026-03-31T07:19:42Z` `inline` by `miscco` `cub/cub/device/dispatch/dispatch_scan.cuh`:509; signals: general review; excerpt: "I knew C++ error messages are long, but that they classify as novels is something ^^" (https://github.com/NVIDIA/cccl/pull/8222#discussion_r3014004528)
