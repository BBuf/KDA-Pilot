# PR Discussion Digest

- Source PR: [sgl-project/sglang#7268](https://github.com/sgl-project/sglang/pull/7268)
- Source page: `sources/prs/sglang/PR-7268.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7268`
- Generated at: `2026-05-20T15:31:09.068887+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-17T08:46:46Z`
- Merged: `2025-06-24T09:05:47Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=0
- Human participants with discussion text: HaiShaw, alexsun07, whitememory, zyeric
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 9

## Review Decisions

- `2025-06-17T08:47:10Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @alexsun07, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7268#pullrequestreview-2934735177)
- `2025-06-17T08:50:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request successfully integrates AITer's fused MoE kernels into the DeepEP path for AMD GPUs, ... (https://github.com/sgl-project/sglang/pull/7268#pullrequestreview-2934746508)
- `2025-06-19T08:20:01Z` `COMMENTED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/7268#pullrequestreview-2942054344)
- `2025-06-24T08:59:51Z` `APPROVED` by `HaiShaw` - LGTM (https://github.com/sgl-project/sglang/pull/7268#pullrequestreview-2952840162)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 4 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/token_dispatcher.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-06-19T08:18:16Z` `inline` by `HaiShaw` `python/sglang/srt/layers/moe/ep_moe/layer.py`:1147; signals: moe; excerpt: "add a comment to +1 above and :-1 here" (https://github.com/sgl-project/sglang/pull/7268#discussion_r2156429086)
- `2025-06-19T08:19:48Z` `inline` by `HaiShaw` `python/sglang/srt/layers/moe/ep_moe/layer.py`:1180; signals: moe; excerpt: "add a comment on the scope of forward aiter here w.r.t. original path." (https://github.com/sgl-project/sglang/pull/7268#discussion_r2156431787)
- `2025-06-21T11:10:54Z` `issue` by `alexsun07`; signals: moe; excerpt: "@alexsun07 please provide full server launch commands for a reprod. Sure! To enable aiter fused moe for EP, please set env SGLANG USE AITER=1. ..." (https://github.com/sgl-project/sglang/pull/7268#issuecomment-2993525554)
