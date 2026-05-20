# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2025](https://github.com/Dao-AILab/flash-attention/pull/2025)
- Source page: `sources/prs/flash-attention/PR-2025.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2025`
- Generated at: `2026-05-20T15:16:39.276305+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-22T01:54:52Z`
- Merged: `2025-11-25T20:38:30Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: drisspg, fengxie, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-22T23:33:15Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2025#pullrequestreview-3497043571)
- `2025-11-22T23:52:43Z` `COMMENTED` by `fengxie` (https://github.com/Dao-AILab/flash-attention/pull/2025#pullrequestreview-3497075102)
- `2025-11-23T00:23:23Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2025#pullrequestreview-3497144018)
- `2025-11-25T18:08:14Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2025#pullrequestreview-3506267036)
- `2025-11-25T18:09:44Z` `COMMENTED` by `drisspg` (https://github.com/Dao-AILab/flash-attention/pull/2025#pullrequestreview-3506271186)
- `2025-11-25T20:37:41Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2025#pullrequestreview-3506729677)

## Inline Comment Hotspots

- `flash_attn/cute/paged_kv.py`: 3 inline comment(s)
- `flash_attn/cute/flash_bwd_sm100.py`: 1 inline comment(s)
- `flash_attn/cute/tile_scheduler.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-22T23:33:15Z` `inline` by `drisspg` `flash_attn/cute/paged_kv.py`:179; signals: cute, perf; excerpt: "from @fengxie is better but may be a perf hit" (https://github.com/Dao-AILab/flash-attention/pull/2025#discussion_r2553455165)
- `2025-11-22T23:52:43Z` `inline` by `fengxie` `flash_attn/cute/paged_kv.py`:179; signals: cute, perf; excerpt: "Thanks fore reporting. This one probably better for perf." (https://github.com/Dao-AILab/flash-attention/pull/2025#discussion_r2553484139)
- `2025-11-25T18:08:14Z` `inline` by `drisspg` `flash_attn/cute/flash_bwd_sm100.py`:564; signals: cute, sm100; excerpt: "this is all ruff formatting" (https://github.com/Dao-AILab/flash-attention/pull/2025#discussion_r2560955324)
- `2025-11-25T18:09:44Z` `inline` by `drisspg` `flash_attn/cute/tile_scheduler.py`:290; signals: cute, tile; excerpt: "no public divisor attr on the divmods" (https://github.com/Dao-AILab/flash-attention/pull/2025#discussion_r2560958712)
- `2025-11-23T00:23:23Z` `inline` by `drisspg` `flash_attn/cute/paged_kv.py`:179; signals: cute; excerpt: "updated" (https://github.com/Dao-AILab/flash-attention/pull/2025#discussion_r2553544976)
