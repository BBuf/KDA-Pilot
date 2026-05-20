# PR Discussion Digest

- Source PR: [sgl-project/sglang#5371](https://github.com/sgl-project/sglang/pull/5371)
- Source page: `sources/prs/sglang/PR-5371.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5371`
- Generated at: `2026-05-20T15:30:23.007548+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-14T09:23:50Z`
- Merged: `2025-04-14T23:24:26Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: BBuf, lambert0312, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-14T09:41:22Z` `COMMENTED` by `lambert0312` (https://github.com/sgl-project/sglang/pull/5371#pullrequestreview-2763757451)
- `2025-04-14T09:44:06Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/5371#pullrequestreview-2763764553)
- `2025-04-14T23:03:34Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/5371#pullrequestreview-2765967862)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/topk.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-14T09:44:06Z` `inline` by `BBuf` `python/sglang/srt/layers/moe/topk.py`:225; signals: cuda, kernel, moe; excerpt: "There are still some unresolved issues with 5125, so we won't rely on it for now. Later, I will implement the n share experts ..." (https://github.com/sgl-project/sglang/pull/5371#discussion_r2041797335)
- `2025-04-14T09:41:22Z` `inline` by `lambert0312` `python/sglang/srt/layers/moe/topk.py`:225; signals: moe; excerpt: "After is merged, there is no need to judge by default. Just pass the n share experts fusion parameter to moe fused gate." (https://github.com/sgl-project/sglang/pull/5371#discussion_r2041792956)
- `2025-04-14T09:42:36Z` `issue` by `BBuf`; signals: general review; excerpt: "This PR relies on 5125 Not dependent; the main branch does not enable shared experts fusion by default, so this PR can be merged ..." (https://github.com/sgl-project/sglang/pull/5371#issuecomment-2801111974)
- `2025-04-14T09:43:29Z` `issue` by `lambert0312`; signals: general review; excerpt: "Not dependent; the main branch does not enable shared experts fusion by default, so this PR can be merged directly. Ok" (https://github.com/sgl-project/sglang/pull/5371#issuecomment-2801114270)
