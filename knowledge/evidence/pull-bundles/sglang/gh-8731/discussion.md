# PR Discussion Digest

- Source PR: [sgl-project/sglang#8731](https://github.com/sgl-project/sglang/pull/8731)
- Source page: `sources/prs/sglang/PR-8731.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-8731`
- Generated at: `2026-05-20T15:31:25.933907+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-03T14:36:56Z`
- Merged: `2025-08-11T20:50:54Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 11 (approved=2, changes_requested=1, commented=8)
- Inline review comments: 11
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=6, outdated=5
- Human participants with discussion text: BBuf, ispobock, yyihuang, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-03T14:37:17Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @BBuf, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3082204469)
- `2025-08-03T14:39:21Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a caching mechanism to optimize the check for fusing allreduce with residual ... (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3082205275)
- `2025-08-03T15:28:38Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3082217967)
- `2025-08-04T00:22:05Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3082428805)
- `2025-08-04T00:22:46Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3082429158)
- `2025-08-04T00:23:25Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3082429496)
- `2025-08-11T08:27:43Z` `COMMENTED` by `yyihuang` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3104651927)
- `2025-08-11T08:32:03Z` `APPROVED` by `yyihuang` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3104663845)
- `2025-08-11T08:33:40Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3104668826)
- `2025-08-11T10:15:27Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3105114827)
- `2025-08-11T20:12:58Z` `CHANGES_REQUESTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/8731#pullrequestreview-3107643490)

## Inline Comment Hotspots

- `python/sglang/srt/models/deepseek_v2.py`: 9 inline comment(s)
- `python/sglang/srt/layers/flashinfer_comm_fusion.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-03T15:28:27Z` `inline` by `ispobock` `python/sglang/srt/models/deepseek_v2.py`:1929; signals: cache; excerpt: "Can we just pre-compute all the valid cases in a table and lookup it in the run time? Instead of updating the cache table ..." (https://github.com/sgl-project/sglang/pull/8731#discussion_r2250020438)
- `2025-08-11T08:27:43Z` `inline` by `yyihuang` `python/sglang/srt/layers/flashinfer_comm_fusion.py`:95; signals: flashinfer; excerpt: "We could profile some other max token num settings (like 1024, 4096) later. But it's good the use 2048 here for now." (https://github.com/sgl-project/sglang/pull/8731#discussion_r2266008348)
- `2025-08-04T00:22:46Z` `inline` by `BBuf` `python/sglang/srt/models/deepseek_v2.py`:224; signals: hang; excerpt: "Yes, I change it to should allreduce fusion now." (https://github.com/sgl-project/sglang/pull/8731#discussion_r2250201962)
- `2025-08-04T00:23:25Z` `inline` by `BBuf` `python/sglang/srt/models/deepseek_v2.py`:1893; signals: hang; excerpt: "I habe changed it to a static table now." (https://github.com/sgl-project/sglang/pull/8731#discussion_r2250202228)
- `2025-08-11T08:33:40Z` `inline` by `BBuf` `python/sglang/srt/layers/flashinfer_comm_fusion.py`:95; signals: flashinfer; excerpt: "Make sense, we can restruct it after v0.5.0 released." (https://github.com/sgl-project/sglang/pull/8731#discussion_r2266019455)
- `2025-08-03T15:24:02Z` `inline` by `ispobock` `python/sglang/srt/models/deepseek_v2.py`:224; signals: general review; excerpt: "nit: the name seems too long" (https://github.com/sgl-project/sglang/pull/8731#discussion_r2250018960)
- `2025-08-03T15:25:39Z` `inline` by `ispobock` `python/sglang/srt/models/deepseek_v2.py`:1893; signals: general review; excerpt: "For large model, is 100 enough?" (https://github.com/sgl-project/sglang/pull/8731#discussion_r2250019486)
- `2025-08-04T00:22:05Z` `inline` by `BBuf` `python/sglang/srt/models/deepseek_v2.py`:1929; signals: general review; excerpt: "Good idea, I have modified it." (https://github.com/sgl-project/sglang/pull/8731#discussion_r2250201671)
- `2025-08-11T20:12:54Z` `inline` by `zhyncs` `python/sglang/srt/models/deepseek_v2.py`:1988; signals: general review; excerpt: "this is duplicate" (https://github.com/sgl-project/sglang/pull/8731#discussion_r2267919657)
