# PR Discussion Digest

- Source PR: [vllm-project/vllm#21497](https://github.com/vllm-project/vllm/pull/21497)
- Source page: `sources/prs/vllm/PR-21497.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21497`
- Generated at: `2026-05-20T15:36:45.081933+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-24T04:55:19Z`
- Merged: `2025-07-24T22:56:08Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: WoosukKwon, njhill
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-07-24T04:56:12Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a more balanced expert sharding strategy when the number of experts is ... (https://github.com/vllm-project/vllm/pull/21497#pullrequestreview-3049978524)
- `2025-07-24T08:44:57Z` `APPROVED` by `njhill` - Nice :) (https://github.com/vllm-project/vllm/pull/21497#pullrequestreview-3050693981)
- `2025-07-24T20:14:38Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/21497#pullrequestreview-3053140621)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/layer.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-07-24T20:14:38Z` `inline` by `WoosukKwon` `vllm/model_executor/layers/fused_moe/layer.py`:590; signals: moe; excerpt: "Actually I'm not sure if the suggested code is simpler. 😅 We need to compute local num experts anyways because it's one of the ..." (https://github.com/vllm-project/vllm/pull/21497#discussion_r2229485361)
- `2025-07-24T08:44:16Z` `inline` by `njhill` `vllm/model_executor/layers/fused_moe/layer.py`:590; signals: moe; excerpt: "Suggestion for more concise version:" (https://github.com/vllm-project/vllm/pull/21497#discussion_r2227863707)
