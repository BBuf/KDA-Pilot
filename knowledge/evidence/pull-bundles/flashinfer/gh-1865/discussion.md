# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1865](https://github.com/flashinfer-ai/flashinfer/pull/1865)
- Source page: `sources/prs/flashinfer/PR-1865.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1865`
- Generated at: `2026-05-20T15:23:31.585744+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-04T22:35:00Z`
- Merged: `2025-10-05T20:47:12Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: Edenzzzz, yzh119
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-04T22:36:35Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug that occurs when the query tensor q is non-contiguous, which ... (https://github.com/flashinfer-ai/flashinfer/pull/1865#pullrequestreview-3302099921)
- `2025-10-05T00:55:57Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1865#pullrequestreview-3302127100)
- `2025-10-05T01:02:11Z` `COMMENTED` by `Edenzzzz` (https://github.com/flashinfer-ai/flashinfer/pull/1865#pullrequestreview-3302128075)
- `2025-10-05T01:12:40Z` `COMMENTED` by `yzh119` - LGTM, please add related unittest as well (https://github.com/flashinfer-ai/flashinfer/pull/1865#pullrequestreview-3302129994)
- `2025-10-05T20:47:07Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1865#pullrequestreview-3302536351)

## Inline Comment Hotspots

- `flashinfer/attention.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-05T00:55:54Z` `inline` by `yzh119` `flashinfer/attention.py`:158; signals: attention, flashinfer; excerpt: "empty like will not inherit input tensor strides: Can you double checking this behavior?" (https://github.com/flashinfer-ai/flashinfer/pull/1865#discussion_r2404224565)
- `2025-10-05T01:02:11Z` `inline` by `Edenzzzz` `flashinfer/attention.py`:158; signals: attention, flashinfer; excerpt: "You are right, reverting" (https://github.com/flashinfer-ai/flashinfer/pull/1865#discussion_r2404225697)
- `2025-10-05T01:12:40Z` `review` `COMMENTED` by `yzh119`; signals: general review; excerpt: "LGTM, please add related unittest as well" (https://github.com/flashinfer-ai/flashinfer/pull/1865#pullrequestreview-3302129994)
