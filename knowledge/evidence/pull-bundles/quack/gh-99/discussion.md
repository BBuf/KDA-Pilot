# PR Discussion Digest

- Source PR: [Dao-AILab/quack#99](https://github.com/Dao-AILab/quack/pull/99)
- Source page: `sources/prs/quack/PR-99.md`
- Evidence bundle: `evidence/pull-bundles/quack/gh-99`
- Generated at: `2026-05-20T15:17:27.485543+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-07T18:00:21Z`
- Merged: `2026-04-14T07:25:39Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: santoshmo, thakkarV, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-07T18:43:57Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/99#pullrequestreview-4070487096)
- `2026-04-07T19:39:14Z` `COMMENTED` by `santoshmo` (https://github.com/Dao-AILab/quack/pull/99#pullrequestreview-4070814139)
- `2026-04-07T21:16:13Z` `COMMENTED` by `thakkarV` (https://github.com/Dao-AILab/quack/pull/99#pullrequestreview-4071345423)
- `2026-04-14T07:15:28Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/99#pullrequestreview-4104017250)

## Inline Comment Hotspots

- `quack/gemm_sm100.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-07T19:39:14Z` `inline` by `santoshmo` `quack/gemm_sm100.py`:249; signals: gemm, hang, sm100, tile; excerpt: "changed the hardcoded 4 to mma inst tile k: Literal[4] Unknown = self.mma tiler[2] // self.mma inst shape mnk[2] if self.mma tiler[2] 1 else ..." (https://github.com/Dao-AILab/quack/pull/99#discussion_r3047447708)
- `2026-04-07T18:43:52Z` `inline` by `thakkarV` `quack/gemm_sm100.py`:249; signals: gemm, sm100, tile; excerpt: "why is this hard coded to 4? this should be inferred by applying the tiled MMA to the tile shape mnk and then taking ..." (https://github.com/Dao-AILab/quack/pull/99#discussion_r3047160863)
- `2026-04-07T21:16:13Z` `inline` by `thakkarV` `quack/gemm_sm100.py`:305; signals: gemm, sm100, tile; excerpt: "this assumes MMA tiler and instruction shape are flat, which is not always a sound assumption: also why do you have a conditional path ..." (https://github.com/Dao-AILab/quack/pull/99#discussion_r3047910952)
- `2026-04-07T18:45:19Z` `issue` by `thakkarV`; signals: tile; excerpt: "@tridao have you considered exposing tile shape K as a parameter as well rather than just tile shape mn? that would avoid having to ..." (https://github.com/Dao-AILab/quack/pull/99#issuecomment-4201417545)
- `2026-04-13T03:03:11Z` `issue` by `tridao`; signals: tile; excerpt: "Yeah i think exposing tile shape mnk would be the cleanest API. If only 2 values are passed, then we set K = 4 ..." (https://github.com/Dao-AILab/quack/pull/99#issuecomment-4233476214)
- `2026-04-13T20:34:11Z` `issue` by `santoshmo`; signals: tile; excerpt: "Yeah i think exposing tile shape mnk would be the cleanest API. If only 2 values are passed, then we set K = 4 ..." (https://github.com/Dao-AILab/quack/pull/99#issuecomment-4239445220)
