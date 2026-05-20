# PR Discussion Digest

- Source PR: [sgl-project/sglang#13094](https://github.com/sgl-project/sglang/pull/13094)
- Source page: `sources/prs/sglang/PR-13094.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13094`
- Generated at: `2026-05-20T15:27:44.383805+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-11T20:39:05Z`
- Merged: `2025-11-18T04:46:24Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: FlamingoPg, Oasis-Git, b8zhong, ispobock
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-11T20:42:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for ModelOpt FP8 with Piecewise CUDA Graphs. The main changes include ... (https://github.com/sgl-project/sglang/pull/13094#pullrequestreview-3450009040)
- `2025-11-11T20:55:35Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/13094#pullrequestreview-3450075001)
- `2025-11-13T03:16:39Z` `COMMENTED` by `ispobock` - @b8zhong Could you add CI test for this change? (https://github.com/sgl-project/sglang/pull/13094#pullrequestreview-3457007196)
- `2025-11-14T09:42:33Z` `APPROVED` by `FlamingoPg` (https://github.com/sgl-project/sglang/pull/13094#pullrequestreview-3463988646)
- `2025-11-16T03:07:53Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/13094#pullrequestreview-3469206536)
- `2025-11-17T04:22:32Z` `COMMENTED` by `b8zhong` (https://github.com/sgl-project/sglang/pull/13094#pullrequestreview-3470933756)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_utils.py`: 3 inline comment(s)
- `test/srt/test_piecewise_cuda_graph.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-13T03:16:39Z` `review` `COMMENTED` by `ispobock`; signals: hang; excerpt: "@b8zhong Could you add CI test for this change?" (https://github.com/sgl-project/sglang/pull/13094#pullrequestreview-3457007196)
- `2025-11-17T04:22:31Z` `inline` by `b8zhong` `test/srt/test_piecewise_cuda_graph.py`:212; signals: cuda; excerpt: "Kk, I bumped it up from 450s - 600s (but it feels long, perhaps I can split it up into test piecewise A and ..." (https://github.com/sgl-project/sglang/pull/13094#discussion_r2532651379)
- `2025-11-11T20:55:35Z` `inline` by `b8zhong` `python/sglang/srt/layers/quantization/fp8_utils.py`:658; signals: fp8; excerpt: "Ah, good point." (https://github.com/sgl-project/sglang/pull/13094#discussion_r2515781666)
- `2025-11-16T03:07:53Z` `inline` by `ispobock` `test/srt/test_piecewise_cuda_graph.py`:212; signals: cuda; excerpt: "Do we need to adjust the estimated time in the run suite.py?" (https://github.com/sgl-project/sglang/pull/13094#discussion_r2531051371)
- `2025-11-14T20:10:05Z` `issue` by `b8zhong`; signals: register; excerpt: "Errr, it looks like was merged before this, I will move it bc otherwise it's hard to find where they are acc registered" (https://github.com/sgl-project/sglang/pull/13094#issuecomment-3534394026)
