# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2390](https://github.com/Dao-AILab/flash-attention/pull/2390)
- Source page: `sources/prs/flash-attention/PR-2390.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2390`
- Generated at: `2026-05-20T15:16:56.085909+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-25T02:57:21Z`
- Merged: `2026-03-25T17:45:13Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: jayhshah, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-25T06:30:41Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2390#pullrequestreview-4004322955)
- `2026-03-25T06:40:50Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2390#pullrequestreview-4004357813)
- `2026-03-25T10:06:56Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2390#pullrequestreview-4005476572)
- `2026-03-25T10:07:01Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2390#pullrequestreview-4005477116)
- `2026-03-25T17:35:52Z` `COMMENTED` by `jayhshah` (https://github.com/Dao-AILab/flash-attention/pull/2390#pullrequestreview-4008532415)

## Inline Comment Hotspots

- `flash_attn/cute/tile_scheduler.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-25T06:40:50Z` `inline` by `jayhshah` `flash_attn/cute/tile_scheduler.py`:660; signals: block, correctness, cute, hang, tile; excerpt: "This change is meant to get the right head swizzle heuristic for 2cta bwd, by accounting for the num m blocks being defined with ..." (https://github.com/Dao-AILab/flash-attention/pull/2390#discussion_r2986134790)
- `2026-03-25T10:06:55Z` `inline` by `tridao` `flash_attn/cute/tile_scheduler.py`:660; signals: correctness, cute, tile; excerpt: "For the tile shape mn[0] do we pass the CTA's tile shape or the cluster tile shape? I think we had this discussion and ..." (https://github.com/Dao-AILab/flash-attention/pull/2390#discussion_r2987135795)
- `2026-03-25T17:35:52Z` `inline` by `jayhshah` `flash_attn/cute/tile_scheduler.py`:660; signals: cute, tile; excerpt: "Currently for the tile scheduler args we pass cta tiler[:2] as tile shape min and cluster shape mn as a separate parameter; this makes ..." (https://github.com/Dao-AILab/flash-attention/pull/2390#discussion_r2989885398)
- `2026-03-25T06:30:41Z` `inline` by `tridao` `flash_attn/cute/tile_scheduler.py`:660; signals: cute, tile; excerpt: "does this affect any of the 2cta bwd code?" (https://github.com/Dao-AILab/flash-attention/pull/2390#discussion_r2986101111)
