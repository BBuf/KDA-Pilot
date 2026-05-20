# PR Discussion Digest

- Source PR: [sgl-project/sglang#16622](https://github.com/sgl-project/sglang/pull/16622)
- Source page: `sources/prs/sglang/PR-16622.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-16622`
- Generated at: `2026-05-20T15:28:21.907739+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-07T05:56:03Z`
- Merged: `2026-01-08T14:24:12Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, ispobock, luoyuyan
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-07T09:53:20Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16622#pullrequestreview-3634109187)
- `2026-01-07T14:52:20Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16622#pullrequestreview-3635269672)
- `2026-01-07T16:30:49Z` `COMMENTED` by `luoyuyan` (https://github.com/sgl-project/sglang/pull/16622#pullrequestreview-3635717516)
- `2026-01-08T02:07:18Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/16622#pullrequestreview-3637420215)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-01-07T14:52:18Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8.py`:568; signals: deepgemm, fp8, gemm, hang, moe; excerpt: "Maybe change the function name to is deepgemm moe runner backend enabled, to avoid the confusion with fp8 gemm usage" (https://github.com/sgl-project/sglang/pull/16622#discussion_r2668777148)
- `2026-01-07T09:53:15Z` `inline` by `Fridge003` `python/sglang/srt/layers/quantization/fp8.py`:819; signals: fp8, hang, moe; excerpt: "Maybe we should put the logic from line 819 to line 823 in a standalone function, and call the same function in create moe ..." (https://github.com/sgl-project/sglang/pull/16622#discussion_r2667762336)
- `2026-01-07T16:30:49Z` `inline` by `luoyuyan` `python/sglang/srt/layers/quantization/fp8.py`:568; signals: fp8; excerpt: "Done :)" (https://github.com/sgl-project/sglang/pull/16622#discussion_r2669155950)
