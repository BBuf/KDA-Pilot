# PR Discussion Digest

- Source PR: [sgl-project/sglang#4831](https://github.com/sgl-project/sglang/pull/4831)
- Source page: `sources/prs/sglang/PR-4831.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4831`
- Generated at: `2026-05-20T15:30:15.216052+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-27T23:45:31Z`
- Merged: `2025-03-29T01:30:15Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: Fridge003, hebiao064, qingquansong
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-28T00:14:42Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/4831#pullrequestreview-2723983452)
- `2025-03-28T00:17:43Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/4831#pullrequestreview-2723985931)
- `2025-03-28T01:09:05Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/4831#pullrequestreview-2724031133)
- `2025-03-28T01:14:09Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/4831#pullrequestreview-2724035527)
- `2025-03-28T18:55:04Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4831#pullrequestreview-2726428336)
- `2025-03-29T00:48:12Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/4831#pullrequestreview-2727129538)
- `2025-03-29T01:02:50Z` `APPROVED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4831#pullrequestreview-2727141120)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashattention_backend.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-03-28T01:09:05Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashattention_backend.py`:189; signals: attention, cache; excerpt: "Yes, kv lora is c kv with 512 dim, and k rope is the rope part of k with 64 dim. They are concated ..." (https://github.com/sgl-project/sglang/pull/4831#discussion_r2017777510)
- `2025-03-28T00:14:42Z` `inline` by `qingquansong` `python/sglang/srt/layers/attention/flashattention_backend.py`:189; signals: attention; excerpt: "Out of curiosity, since latent dim are shared so it only creates the k buffer and won't create the v buffer in this case? ..." (https://github.com/sgl-project/sglang/pull/4831#discussion_r2017745215)
- `2025-03-28T01:14:09Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashattention_backend.py`:202; signals: attention; excerpt: "Not exactly. Here q all is concatenation of q nope and q rope. q rope has shape (num tokens, num heads, 64) is just ..." (https://github.com/sgl-project/sglang/pull/4831#discussion_r2017780347)
- `2025-03-28T18:55:04Z` `inline` by `hebiao064` `python/sglang/srt/layers/attention/flashattention_backend.py`:126; signals: attention; excerpt: "maybe keep this logic? I thought about the same code refactor like you did, but I think it's better to assert and fail early ..." (https://github.com/sgl-project/sglang/pull/4831#discussion_r2019178540)
- `2025-03-28T00:17:43Z` `inline` by `qingquansong` `python/sglang/srt/layers/attention/flashattention_backend.py`:202; signals: attention; excerpt: "is this q all the c t^q + q rope (basically the low dim c q nope + q rope)" (https://github.com/sgl-project/sglang/pull/4831#discussion_r2017746918)
- `2025-03-29T00:48:12Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/flashattention_backend.py`:126; signals: attention; excerpt: "resolved" (https://github.com/sgl-project/sglang/pull/4831#discussion_r2019631547)
