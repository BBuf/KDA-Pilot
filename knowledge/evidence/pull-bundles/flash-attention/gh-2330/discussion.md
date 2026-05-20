# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2330](https://github.com/Dao-AILab/flash-attention/pull/2330)
- Source page: `sources/prs/flash-attention/PR-2330.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2330`
- Generated at: `2026-05-20T15:16:51.288676+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-11T19:14:24Z`
- Merged: `2026-03-12T21:07:33Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 9 (approved=1, commented=8)
- Inline review comments: 8
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=0, outdated=4
- Human participants with discussion text: blake-snc, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-12T12:15:16Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3936110922)
- `2026-03-12T12:15:54Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3936114352)
- `2026-03-12T16:54:18Z` `COMMENTED` by `blake-snc` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3938222277)
- `2026-03-12T16:54:20Z` `COMMENTED` by `blake-snc` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3938222460)
- `2026-03-12T18:11:07Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3938712339)
- `2026-03-12T18:11:40Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3938716117)
- `2026-03-12T18:59:26Z` `COMMENTED` by `blake-snc` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3939005846)
- `2026-03-12T18:59:28Z` `COMMENTED` by `blake-snc` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3939005959)
- `2026-03-12T21:07:11Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2330#pullrequestreview-3939765005)

## Inline Comment Hotspots

- `flash_attn/cute/interface.py`: 8 inline comment(s)

## High-Signal Discussion

- `2026-03-12T18:59:26Z` `inline` by `blake-snc` `flash_attn/cute/interface.py`:1175; signals: compile, cute, hang, sm120, sm90; excerpt: "Fixed — changed to [8, 9, 12]. SM80 uses the same compile key format as SM90/SM120." (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2926724337)
- `2026-03-12T16:54:18Z` `inline` by `blake-snc` `flash_attn/cute/interface.py`:1236; signals: attention, cute, sm120; excerpt: "Done — now uses flash bwd obj cls to pick between FlashAttentionBackwardSm120 and FlashAttentionBackwardSm80, then calls the constructor once." (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2926027851)
- `2026-03-12T12:15:54Z` `inline` by `tridao` `flash_attn/cute/interface.py`:1387; signals: cute, hang; excerpt: "This is confusing, we should just change postprocess to do the same for arch 80 and arch 120" (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2924226756)
- `2026-03-12T16:54:20Z` `inline` by `blake-snc` `flash_attn/cute/interface.py`:1387; signals: cute; excerpt: "Done — postprocess now handles arch 120 natively (same path as arch 80 via arch // 10 family checks). No more post arch = ..." (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2926027991)
- `2026-03-12T18:59:27Z` `inline` by `blake-snc` `flash_attn/cute/interface.py`:1266; signals: cute; excerpt: "Done — flash bwd obj cls + constructor now inside if arch // 10 in [8, 12]:, keeping the if/elif/else chain clean." (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2926724429)
- `2026-03-12T12:15:16Z` `inline` by `tridao` `flash_attn/cute/interface.py`:1236; signals: cute; excerpt: "can you just set flash bwd obj cls and use the same arguments, instead of repeating?" (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2924223599)
- `2026-03-12T18:11:07Z` `inline` by `tridao` `flash_attn/cute/interface.py`:1175; signals: cute; excerpt: "this should be [8, 9, 12]" (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2926468612)
- `2026-03-12T18:11:40Z` `inline` by `tridao` `flash_attn/cute/interface.py`:1266; signals: cute; excerpt: "let's move it under an if arch // 10 in [8, 12]:" (https://github.com/Dao-AILab/flash-attention/pull/2330#discussion_r2926471927)
