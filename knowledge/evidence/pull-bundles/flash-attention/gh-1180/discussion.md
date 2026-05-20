# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#1180](https://github.com/Dao-AILab/flash-attention/pull/1180)
- Source page: `sources/prs/flash-attention/PR-1180.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-1180`
- Generated at: `2026-05-20T15:16:29.267340+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2024-08-27T18:52:59Z`
- Merged: `2024-08-28T07:20:47Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 3 (commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: cameronshinn, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2024-08-27T23:20:41Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1180#pullrequestreview-2264632605)
- `2024-08-28T00:04:57Z` `COMMENTED` by `cameronshinn` (https://github.com/Dao-AILab/flash-attention/pull/1180#pullrequestreview-2264664802)
- `2024-08-28T04:27:20Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/1180#pullrequestreview-2265107703)

## Inline Comment Hotspots

- `hopper/flash_bwd_preprocess_kernel.h`: 2 inline comment(s)
- `hopper/flash_bwd_postprocess_kernel.h`: 1 inline comment(s)

## High-Signal Discussion

- `2024-08-27T23:20:41Z` `inline` by `tridao` `hopper/flash_bwd_preprocess_kernel.h`:28; signals: bf16, fp8, hopper, kernel, sm90; excerpt: "This kernel doesn't need SM90. It needs SM75 (if fp16), SM80 (if bf16), and SM89 (if fp8). Is there an easy way to rewrite ..." (https://github.com/Dao-AILab/flash-attention/pull/1180#discussion_r1733633528)
- `2024-08-28T04:27:20Z` `inline` by `tridao` `hopper/flash_bwd_postprocess_kernel.h`:31; signals: hopper, kernel, sm90, tma; excerpt: "This one does need SM90 since it's using TMA" (https://github.com/Dao-AILab/flash-attention/pull/1180#discussion_r1733963353)
- `2024-08-28T00:04:56Z` `inline` by `cameronshinn` `hopper/flash_bwd_preprocess_kernel.h`:28; signals: hopper, kernel; excerpt: "How does this look? It seems to work for me. I added it to the other kernel as well, assuming that has the same ..." (https://github.com/Dao-AILab/flash-attention/pull/1180#discussion_r1733656078)
