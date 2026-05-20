# PR Discussion Digest

- Source PR: [vllm-project/vllm#28968](https://github.com/vllm-project/vllm/pull/28968)
- Source page: `sources/prs/vllm/PR-28968.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28968`
- Generated at: `2026-05-20T15:38:36.676222+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-18T23:19:03Z`
- Merged: `2025-11-19T21:30:04Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: LucasWilkinson, chatgpt-codex-connector, mgoin, zyongye
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-18T23:20:44Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix an issue with the Rotary Positional Embedding (RoPE) in the ... (https://github.com/vllm-project/vllm/pull/28968#pullrequestreview-3480050087)
- `2025-11-18T23:22:21Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28968#pullrequestreview-3480055302)
- `2025-11-18T23:45:26Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/28968#pullrequestreview-3480104144)
- `2025-11-19T00:48:03Z` `COMMENTED` by `zyongye` (https://github.com/vllm-project/vllm/pull/28968#pullrequestreview-3480254636)
- `2025-11-19T21:29:47Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/28968#pullrequestreview-3484816453)

## Inline Comment Hotspots

- `vllm/model_executor/layers/mla.py`: 3 inline comment(s)
- `vllm/model_executor/models/deepseek_v2.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-18T23:22:21Z` `inline` by `chatgpt-codex-connector` `vllm/model_executor/layers/mla.py`:28; signals: attention, mla; excerpt: ". Constructing those models will now raise TypeError: MLAModules. init () missing 1 required positional argument: 'indexer rotary emb' before attention ever runs, breaking ..." (https://github.com/vllm-project/vllm/pull/28968#discussion_r2539929783)
- `2025-11-19T00:48:03Z` `inline` by `zyongye` `vllm/model_executor/layers/mla.py`:28; signals: hang, mla; excerpt: "You're right. Changed." (https://github.com/vllm-project/vllm/pull/28968#discussion_r2540072152)
- `2025-11-18T23:22:21Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28968#pullrequestreview-3480055302)
- `2025-11-18T23:45:26Z` `inline` by `LucasWilkinson` `vllm/model_executor/layers/mla.py`:28; signals: mla; excerpt: "@zyongye I think this a fair concern; can we add defaults?" (https://github.com/vllm-project/vllm/pull/28968#discussion_r2539970370)
