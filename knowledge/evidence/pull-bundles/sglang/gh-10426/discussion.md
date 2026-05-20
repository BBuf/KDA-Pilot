# PR Discussion Digest

- Source PR: [sgl-project/sglang#10426](https://github.com/sgl-project/sglang/pull/10426)
- Source page: `sources/prs/sglang/PR-10426.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-10426`
- Generated at: `2026-05-20T15:27:18.326940+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-14T14:51:11Z`
- Merged: `2025-09-15T01:41:10Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 4
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: ch-wan, fzyzcjy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-14T14:51:22Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @fzyzcjy, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/10426#pullrequestreview-3222146750)
- `2025-09-14T14:53:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly fixes a data type mismatch for correction bias in biased grouped topk ... (https://github.com/sgl-project/sglang/pull/10426#pullrequestreview-3222147431)
- `2025-09-14T20:15:29Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/10426#pullrequestreview-3222411820)
- `2025-09-14T23:26:56Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/10426#pullrequestreview-3222548998)
- `2025-09-15T00:13:45Z` `COMMENTED` by `ch-wan` (https://github.com/sgl-project/sglang/pull/10426#pullrequestreview-3222598545)
- `2025-09-15T00:38:26Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/10426#pullrequestreview-3222620119)
- `2025-09-15T01:37:50Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/10426#pullrequestreview-3222687084)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/topk.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-09-14T23:26:56Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/topk.py`:678; signals: fp4, moe, nvfp4; excerpt: "it is more about UB in nvfp4 ckpt, not check in detail yesterday, I will check today." (https://github.com/sgl-project/sglang/pull/10426#discussion_r2347641912)
- `2025-09-15T01:40:52Z` `issue` by `zhyncs`; signals: cutlass, fp4, moe; excerpt: "fix dsv3 fp4 cutlass moe etp" (https://github.com/sgl-project/sglang/pull/10426#issuecomment-3290198254)
- `2025-09-14T20:15:29Z` `inline` by `zhyncs` `python/sglang/srt/layers/moe/topk.py`:678; signals: accuracy, moe; excerpt: "In which use case will we have accuracy issues?" (https://github.com/sgl-project/sglang/pull/10426#discussion_r2347553049)
- `2025-09-15T00:13:45Z` `inline` by `ch-wan` `python/sglang/srt/layers/moe/topk.py`:678; signals: moe; excerpt: "Is it related to 9834?" (https://github.com/sgl-project/sglang/pull/10426#discussion_r2347669385)
- `2025-09-15T00:38:26Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/moe/topk.py`:678; signals: moe; excerpt: "yes I think so, I am going to investigate it today" (https://github.com/sgl-project/sglang/pull/10426#discussion_r2347684392)
