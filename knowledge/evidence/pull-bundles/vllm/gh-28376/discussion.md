# PR Discussion Digest

- Source PR: [vllm-project/vllm#28376](https://github.com/vllm-project/vllm/pull/28376)
- Source page: `sources/prs/vllm/PR-28376.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28376`
- Generated at: `2026-05-20T15:38:27.954200+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-10T03:20:12Z`
- Merged: `2025-11-24T03:26:00Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: SageMoore, apinge, chatgpt-codex-connector, mergify, micah-wil, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-10T03:21:17Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Whisper v1 on ROCm by enabling Aiter Unified Attention and ... (https://github.com/vllm-project/vllm/pull/28376#pullrequestreview-3440662512)
- `2025-11-10T03:23:33Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/28376#pullrequestreview-3440664876)
- `2025-11-10T03:51:31Z` `COMMENTED` by `apinge` (https://github.com/vllm-project/vllm/pull/28376#pullrequestreview-3440703297)
- `2025-11-20T18:29:51Z` `APPROVED` by `SageMoore` (https://github.com/vllm-project/vllm/pull/28376#pullrequestreview-3489300262)
- `2025-11-21T01:05:13Z` `APPROVED` by `tjtanaa` (https://github.com/vllm-project/vllm/pull/28376#pullrequestreview-3490728563)

## Inline Comment Hotspots

- `vllm/v1/attention/backends/rocm_aiter_fa.py`: 2 inline comment(s)
- `vllm/v1/attention/backends/rocm_attn.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-14T01:49:22Z` `issue` by `apinge`; signals: accuracy, attention, flash attention, hang, nan; excerpt: "There are the same review questions related to PR 28346 . We will wait for the other PR issue to sort out the issues. ..." (https://github.com/vllm-project/vllm/pull/28376#issuecomment-3530470920)
- `2025-11-10T03:23:33Z` `inline` by `chatgpt-codex-connector` `vllm/v1/attention/backends/rocm_attn.py`:246; signals: attention, block, cache, kv cache; excerpt: "![P1 Badge]( Handle encoder–decoder calls without key/value tensors The constructor now accepts AttentionType.ENCODER DECODER, but forward still assumes key and value are always present. ..." (https://github.com/vllm-project/vllm/pull/28376#discussion_r2508601408)
- `2025-11-10T03:23:33Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/28376#pullrequestreview-3440664876)
- `2025-11-10T03:51:31Z` `inline` by `apinge` `vllm/v1/attention/backends/rocm_aiter_fa.py`:733; signals: attention; excerpt: "Fixed in latest commit to correctly handle None key/value in cross-attention." (https://github.com/vllm-project/vllm/pull/28376#discussion_r2508633767)
- `2025-11-10T04:06:57Z` `issue` by `tjtanaa`; signals: general review; excerpt: "@apinge I understand that you have stated that we need to use latest AITER commit. Is there any chance that this work with the ..." (https://github.com/vllm-project/vllm/pull/28376#issuecomment-3509309654)
- `2025-11-10T07:57:22Z` `issue` by `apinge`; signals: general review; excerpt: "@apinge I understand that you have stated that we need to use latest AITER commit. Is there any chance that this work with the ..." (https://github.com/vllm-project/vllm/pull/28376#issuecomment-3509979686)
- `2025-11-13T05:20:47Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @apinge." (https://github.com/vllm-project/vllm/pull/28376#issuecomment-3525458812)
- `2025-11-13T05:22:31Z` `issue` by `tjtanaa`; signals: general review; excerpt: "There are the same review questions related to PR . We will wait for the other PR issue to sort out the issues." (https://github.com/vllm-project/vllm/pull/28376#issuecomment-3525464528)
