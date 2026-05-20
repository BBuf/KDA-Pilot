# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2186](https://github.com/Dao-AILab/flash-attention/pull/2186)
- Source page: `sources/prs/flash-attention/PR-2186.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2186`
- Generated at: `2026-05-20T15:16:44.025715+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-16T03:45:19Z`
- Merged: `2026-03-20T10:40:24Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-17T17:01:53Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2186#pullrequestreview-3962360025)
- `2026-03-17T17:27:04Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2186#pullrequestreview-3962514531)
- `2026-03-18T09:44:09Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2186#pullrequestreview-3966429713)

## Inline Comment Hotspots

- `flash_attn/cute/flash_fwd_sm100.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-17T17:27:04Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm100.py`:491; signals: cute, sm100, warp; excerpt: "I think you can use more than 1 warp to load Q since we have some empty warps? That might make it a bit ..." (https://github.com/Dao-AILab/flash-attention/pull/2186#discussion_r2948407710)
- `2026-03-17T17:01:54Z` `inline` by `tridao` `flash_attn/cute/flash_fwd_sm100.py`:490; signals: cute, sm100, tile; excerpt: "you can use quack.copy utils.tiled copy 2d?" (https://github.com/Dao-AILab/flash-attention/pull/2186#discussion_r2948256515)
- `2026-03-17T19:08:36Z` `issue` by `tridao`; signals: general review; excerpt: "Do we have tests that hit this code path? I guess we set nheads=6 and for mqa it should hit this code path?" (https://github.com/Dao-AILab/flash-attention/pull/2186#issuecomment-4077371495)
