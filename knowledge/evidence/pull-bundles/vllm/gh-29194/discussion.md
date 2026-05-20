# PR Discussion Digest

- Source PR: [vllm-project/vllm#29194](https://github.com/vllm-project/vllm/pull/29194)
- Source page: `sources/prs/vllm/PR-29194.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29194`
- Generated at: `2026-05-20T15:38:38.876134+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-21T18:38:49Z`
- Merged: `2025-11-23T17:42:52Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 4 (commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LucasWilkinson, WoosukKwon, chatgpt-codex-connector
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-21T19:01:40Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/29194#pullrequestreview-3494017653)
- `2025-11-22T05:50:00Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/29194#pullrequestreview-3495736822)
- `2025-11-23T17:42:08Z` `COMMENTED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/29194#pullrequestreview-3497912976)
- `2025-11-23T17:42:29Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29194#pullrequestreview-3497913075)

## Inline Comment Hotspots

- `vllm/v1/worker/gpu/model_runner.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-11-22T05:50:00Z` `inline` by `LucasWilkinson` `vllm/v1/worker/gpu/model_runner.py`:485; signals: attention, flashinfer, kernel, nan; excerpt: "I think we can refactor (I assume you are referring to: it soon-ish (next couple weeks) since its should be backwards compatible. You may ..." (https://github.com/vllm-project/vllm/pull/29194#discussion_r2552227859)
- `2025-11-23T17:42:29Z` `inline` by `chatgpt-codex-connector` `vllm/v1/worker/gpu/model_runner.py`:485; signals: attention, block, cache; excerpt: "will assume far more cached tokens than actually exist, which can schedule attention over uninitialized KV blocks and yield incorrect results or OOB access ..." (https://github.com/vllm-project/vllm/pull/29194#discussion_r2554225165)
- `2025-11-23T17:42:08Z` `inline` by `WoosukKwon` `vllm/v1/worker/gpu/model_runner.py`:485; signals: flashinfer; excerpt: "Thanks for the explanation. As it turns out, this hack doesn’t work with FlashInfer correctly. For now, I’ve added a gate to raise an ..." (https://github.com/vllm-project/vllm/pull/29194#discussion_r2554224968)
- `2025-11-23T17:42:29Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/29194#pullrequestreview-3497913075)
- `2025-11-21T19:01:40Z` `inline` by `WoosukKwon` `vllm/v1/worker/gpu/model_runner.py`:485; signals: general review; excerpt: "@LucasWilkinson This is my current hack, which is totally undesirable. I plan to use a tighter upper bound for seq lens np, but I'd ..." (https://github.com/vllm-project/vllm/pull/29194#discussion_r2550701383)
