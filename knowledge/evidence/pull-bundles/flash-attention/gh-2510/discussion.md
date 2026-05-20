# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2510](https://github.com/Dao-AILab/flash-attention/pull/2510)
- Source page: `sources/prs/flash-attention/PR-2510.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2510`
- Generated at: `2026-05-20T15:17:11.160905+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-28T00:47:04Z`
- Merged: `2026-04-30T19:06:16Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: drisspg, v0i0
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-28T00:53:43Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2510#pullrequestreview-4185042300)
- `2026-04-28T00:59:19Z` `COMMENTED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2510#pullrequestreview-4185064218)
- `2026-04-30T18:40:54Z` `COMMENTED` by `v0i0` (https://github.com/Dao-AILab/flash-attention/pull/2510#pullrequestreview-4207707563)
- `2026-04-30T19:04:02Z` `APPROVED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2510#pullrequestreview-4207840418)

## Inline Comment Hotspots

- `flash_attn/cute/flash_bwd_sm90.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-28T00:59:19Z` `inline` by `v0i0` `flash_attn/cute/flash_bwd_sm90.py`:406; signals: benchmark, cute, sm100, sm90; excerpt: "good question, not sure (i just ported over the sm100 code). we should benchmark and see." (https://github.com/Dao-AILab/flash-attention/pull/2510#discussion_r3150967852)
- `2026-04-28T00:53:43Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm90.py`:406; signals: cute, sm100, sm90; excerpt: "I havent looked at sm100 code, but 2 semaphores as opposed to mdkv is for overlap?" (https://github.com/Dao-AILab/flash-attention/pull/2510#discussion_r3150950943)
- `2026-04-30T18:40:54Z` `inline` by `v0i0` `flash_attn/cute/flash_bwd_sm90.py`:406; signals: benchmark, cute, sm90; excerpt: "benchmarked, two semaphores is faster, presumable smaller critical section" (https://github.com/Dao-AILab/flash-attention/pull/2510#discussion_r3170122839)
