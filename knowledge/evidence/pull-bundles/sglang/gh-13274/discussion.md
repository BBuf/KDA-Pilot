# PR Discussion Digest

- Source PR: [sgl-project/sglang#13274](https://github.com/sgl-project/sglang/pull/13274)
- Source page: `sources/prs/sglang/PR-13274.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13274`
- Generated at: `2026-05-20T15:27:46.212325+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-14T08:26:28Z`
- Merged: `2025-11-14T20:51:11Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=1, changes_requested=1, commented=4)
- Inline review comments: 4
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: Fridge003, hnyls2002, kaixih
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-14T08:30:55Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request correctly addresses the reported accuracy issue when SGLANG ENABLE FLASHINFER GEMM is enabled. ... (https://github.com/sgl-project/sglang/pull/13274#pullrequestreview-3463626409)
- `2025-11-14T08:36:20Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13274#pullrequestreview-3463652169)
- `2025-11-14T18:09:48Z` `COMMENTED` by `kaixih` (https://github.com/sgl-project/sglang/pull/13274#pullrequestreview-3466140906)
- `2025-11-14T18:51:47Z` `CHANGES_REQUESTED` by `hnyls2002` (https://github.com/sgl-project/sglang/pull/13274#pullrequestreview-3466339761)
- `2025-11-14T19:39:28Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13274#pullrequestreview-3466538106)
- `2025-11-14T20:21:58Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13274#pullrequestreview-3466684163)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/fp8_utils.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-14T08:36:16Z` `inline` by `Fridge003` `python/sglang/srt/models/deepseek_v2.py`:99; signals: flashinfer, fp4, fp8, gemm, kernel; excerpt: "Can we rename this environ to ENABLE FLASHINFER FP8 GEMM so it's not confused with fp4 gemm. When I added this environ like 6 ..." (https://github.com/sgl-project/sglang/pull/13274#discussion_r2526472020)
- `2025-11-14T18:51:27Z` `inline` by `hnyls2002` `python/sglang/srt/layers/quantization/fp8_utils.py`:131; signals: fp8; excerpt: "Do not use get bool env var. Use from sglang.srt.environ." (https://github.com/sgl-project/sglang/pull/13274#discussion_r2528576985)
- `2025-11-14T08:26:50Z` `issue` by `kaixih`; signals: race; excerpt: "@gracehonv @Fridge003" (https://github.com/sgl-project/sglang/pull/13274#issuecomment-3531558968)
- `2025-11-14T18:09:48Z` `inline` by `kaixih` `python/sglang/srt/models/deepseek_v2.py`:99; signals: general review; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/13274#discussion_r2528459821)
