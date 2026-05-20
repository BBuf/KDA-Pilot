# PR Discussion Digest

- Source PR: [sgl-project/sglang#4596](https://github.com/sgl-project/sglang/pull/4596)
- Source page: `sources/prs/sglang/PR-4596.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4596`
- Generated at: `2026-05-20T15:30:11.277977+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-19T21:02:17Z`
- Merged: `2025-03-22T07:47:53Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Edwardf0t1, hebiao064, qingquansong, yundai424
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-19T21:39:28Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4596#pullrequestreview-2700311219)
- `2025-03-19T21:40:43Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4596#pullrequestreview-2700316877)
- `2025-03-19T21:47:03Z` `COMMENTED` by `yundai424` (https://github.com/sgl-project/sglang/pull/4596#pullrequestreview-2700340842)
- `2025-03-19T22:14:42Z` `COMMENTED` by `qingquansong` (https://github.com/sgl-project/sglang/pull/4596#pullrequestreview-2700400787)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/utils.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-03-21T04:32:44Z` `issue` by `Edwardf0t1`; signals: cuda, fp8, kernel; excerpt: "LGTM, thanks for the fix. qq: modelopt's scalar scale for per tensor fp8 worked fine previously. Is this because there's some recent updates to ..." (https://github.com/sgl-project/sglang/pull/4596#issuecomment-2742235260)
- `2025-03-19T22:14:41Z` `inline` by `qingquansong` `python/sglang/srt/layers/quantization/utils.py`:79; signals: vector; excerpt: "would this affect the loading of the llm compressor model with per tensor quantization 👀 Synced offline, model opt is scalar scale for per ..." (https://github.com/sgl-project/sglang/pull/4596#discussion_r2004390959)
- `2025-03-19T21:40:43Z` `inline` by `hebiao064` `python/sglang/srt/layers/quantization/utils.py`:79; signals: general review; excerpt: "there is a util that you might be able to reuse: but feel free to ignore it if it doesn't meet your need" (https://github.com/sgl-project/sglang/pull/4596#discussion_r2004349375)
- `2025-03-21T07:18:39Z` `issue` by `yundai424`; signals: hang; excerpt: "@Edwardf0t1 guess it could be due to this change --" (https://github.com/sgl-project/sglang/pull/4596#issuecomment-2742548116)
- `2025-03-19T21:39:28Z` `inline` by `hebiao064` `python/sglang/srt/layers/quantization/utils.py`:77; signals: general review; excerpt: "maybe add a test here?" (https://github.com/sgl-project/sglang/pull/4596#discussion_r2004347444)
- `2025-03-19T21:47:03Z` `inline` by `yundai424` `python/sglang/srt/layers/quantization/utils.py`:79; signals: general review; excerpt: "im exactly modifying this method lol" (https://github.com/sgl-project/sglang/pull/4596#discussion_r2004358694)
