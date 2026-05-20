# PR Discussion Digest

- Source PR: [sgl-project/sglang#12361](https://github.com/sgl-project/sglang/pull/12361)
- Source page: `sources/prs/sglang/PR-12361.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12361`
- Generated at: `2026-05-20T15:27:38.228686+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-30T01:07:09Z`
- Merged: `2025-11-08T23:10:25Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Fridge003, fzyzcjy, wenscarl
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-10-30T01:08:46Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a fix for the trtllm-mla backend, specifically for cases where chunked prefix ... (https://github.com/sgl-project/sglang/pull/12361#pullrequestreview-3397073993)
- `2025-10-30T01:26:51Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/12361#pullrequestreview-3397106569)
- `2025-10-30T01:36:40Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12361#pullrequestreview-3397119270)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/trtllm_mla_backend.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-10-30T16:07:05Z` `issue` by `wenscarl`; signals: attention, cache, kernel, kv cache, mla, perf; excerpt: "Could you link to the issue here? The failure should be caused by trtllm ragged attention deepseek is used for the prefill with weight ..." (https://github.com/sgl-project/sglang/pull/12361#issuecomment-3468786887)
- `2025-10-30T17:46:04Z` `issue` by `Fridge003`; signals: cache, kv cache, mla; excerpt: "trtllm batch decode with kv cache mla Will do it in the next PR" (https://github.com/sgl-project/sglang/pull/12361#issuecomment-3469287221)
- `2025-10-30T01:26:51Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:548; signals: attention, mla; excerpt: "nit: shall we put it into forward prefill metadata etc to be more organized" (https://github.com/sgl-project/sglang/pull/12361#discussion_r2476147307)
- `2025-10-30T01:36:40Z` `inline` by `Fridge003` `python/sglang/srt/layers/attention/trtllm_mla_backend.py`:548; signals: attention, mla; excerpt: "Done" (https://github.com/sgl-project/sglang/pull/12361#discussion_r2476157567)
- `2025-10-30T01:07:26Z` `issue` by `Fridge003`; signals: nan; excerpt: "cc @ishandhanani @fzyzcjy" (https://github.com/sgl-project/sglang/pull/12361#issuecomment-3465743328)
