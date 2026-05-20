# PR Discussion Digest

- Source PR: [sgl-project/sglang#8258](https://github.com/sgl-project/sglang/pull/8258)
- Source page: `sources/prs/sglang/PR-8258.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8258`
- Generated at: `2026-05-20T15:31:23.668733+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-22T13:25:48Z`
- Merged: `2025-07-27T09:28:50Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 8
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=5
- Human participants with discussion text: BBuf, ch-wan, merrymercy, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-22T13:26:28Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3043004787)
- `2025-07-22T13:28:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for triton kernels v3.4.0 for fused moe. I've identified a few ... (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3043013343)
- `2025-07-23T13:19:04Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3047419105)
- `2025-07-23T13:33:55Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3047488625)
- `2025-07-25T02:17:27Z` `APPROVED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3053886226)
- `2025-07-25T13:51:21Z` `COMMENTED` by `merrymercy` (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3055487390)
- `2025-07-25T15:21:41Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3055895481)
- `2025-07-25T18:58:08Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/8258#pullrequestreview-3056502418)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 3 inline comment(s)
- `python/sglang/srt/layers/quantization/unquant.py`: 2 inline comment(s)
- `python/sglang/srt/models/deepseek.py`: 1 inline comment(s)
- `python/sglang/srt/models/qwen2_moe.py`: 1 inline comment(s)
- `python/sglang/srt/models/qwen3_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-07-25T15:21:40Z` `inline` by `yuan-luo` `python/sglang/srt/layers/moe/ep_moe/layer.py`:327; signals: flashinfer, gemm, hang, moe, triton; excerpt: "@merrymercy , thanks for the comments. The current approach is the agreement @ch-wan and I discussed and reached. The background is that (@ch-wan proposed) ..." (https://github.com/sgl-project/sglang/pull/8258#discussion_r2231408793)
- `2025-07-24T05:52:59Z` `issue` by `yuan-luo`; signals: compile, cuda, hang, memory; excerpt: "We can see cuda graph capture error in current CI results. [07/24] The reason is after modifying TopKOutput to the following, dynamic memory allocation ..." (https://github.com/sgl-project/sglang/pull/8258#issuecomment-3112076671)
- `2025-07-25T18:58:08Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/ep_moe/layer.py`:327; signals: kernel, moe, triton; excerpt: "Yes, this is a part of my on-going refactor. We temporarily use this format because oai needs triton kernel support." (https://github.com/sgl-project/sglang/pull/8258#discussion_r2231817822)
- `2025-07-25T13:51:21Z` `inline` by `merrymercy` `python/sglang/srt/layers/moe/ep_moe/layer.py`:327; signals: hang, moe; excerpt: "this seems to fragile. 1. How do you make sure you change all places? 2. Is it better to use the name to index ..." (https://github.com/sgl-project/sglang/pull/8258#discussion_r2231141812)
- `2025-07-23T13:33:55Z` `inline` by `yuan-luo` `python/sglang/srt/layers/quantization/unquant.py`:236; signals: general review; excerpt: "Revised." (https://github.com/sgl-project/sglang/pull/8258#discussion_r2225636750)
