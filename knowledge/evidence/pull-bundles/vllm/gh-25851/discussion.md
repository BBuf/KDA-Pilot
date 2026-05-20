# PR Discussion Digest

- Source PR: [vllm-project/vllm#25851](https://github.com/vllm-project/vllm/pull/25851)
- Source page: `sources/prs/vllm/PR-25851.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25851`
- Generated at: `2026-05-20T15:37:58.159285+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-29T04:01:47Z`
- Merged: `2025-09-29T06:03:51Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: DarkLight1337, Isotr0py, wwl2755, ywang96
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-09-29T04:03:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the ViT attention backend fallback for Blackwell GPUs by moving the logic ... (https://github.com/vllm-project/vllm/pull/25851#pullrequestreview-3277794746)
- `2025-09-29T04:06:16Z` `APPROVED` by `Isotr0py` (https://github.com/vllm-project/vllm/pull/25851#pullrequestreview-3277798992)
- `2025-09-29T05:50:27Z` `COMMENTED` by `wwl2755` (https://github.com/vllm-project/vllm/pull/25851#pullrequestreview-3278014150)

## Inline Comment Hotspots

- `vllm/model_executor/models/qwen3_vl.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-29T05:50:27Z` `inline` by `wwl2755` `vllm/model_executor/models/qwen3_vl.py`:327; signals: blackwell; excerpt: "QQ: Does FA has the similar problem in Blackwell? Because this logic may still select upstream FA is available." (https://github.com/vllm-project/vllm/pull/25851#discussion_r2386773461)
