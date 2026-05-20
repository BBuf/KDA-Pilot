# PR Discussion Digest

- Source PR: [vllm-project/vllm#28740](https://github.com/vllm-project/vllm/pull/28740)
- Source page: `sources/prs/vllm/PR-28740.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28740`
- Generated at: `2026-05-20T15:38:33.731098+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-14T17:17:39Z`
- Merged: `2025-11-14T22:13:46Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: hjjq, mgoin
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-14T17:22:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug where shared experts incorrectly received combined hidden states when both ... (https://github.com/vllm-project/vllm/pull/28740#pullrequestreview-3465958236)
- `2025-11-14T17:35:42Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28740#pullrequestreview-3466012195)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-14T17:34:17Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:1752; signals: moe; excerpt: "It would be best to leave a comment why we don't want to overwrite hidden states for future logic" (https://github.com/vllm-project/vllm/pull/28740#discussion_r2528364738)
