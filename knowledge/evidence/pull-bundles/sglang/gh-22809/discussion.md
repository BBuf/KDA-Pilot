# PR Discussion Digest

- Source PR: [sgl-project/sglang#22809](https://github.com/sgl-project/sglang/pull/22809)
- Source page: `sources/prs/sglang/PR-22809.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22809`
- Generated at: `2026-05-20T15:29:30.806599+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-14T13:45:41Z`
- Merged: `2026-04-22T21:11:11Z`

## Discussion Counts

- Issue comments: 19
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: chatgpt-codex-connector, sshleifer, yushengsu-thu
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T13:55:21Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: 1099f03814 ℹ️ About ... (https://github.com/sgl-project/sglang/pull/22809#pullrequestreview-4106466446)
- `2026-04-22T01:51:18Z` `APPROVED` by `yushengsu-thu` (https://github.com/sgl-project/sglang/pull/22809#pullrequestreview-4151645335)
- `2026-04-22T17:54:26Z` `APPROVED` by `yushengsu-thu` (https://github.com/sgl-project/sglang/pull/22809#pullrequestreview-4156841898)

## Inline Comment Hotspots

- `python/sglang/srt/lora/lora_moe_runners.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-14T13:55:21Z` `inline` by `chatgpt-codex-connector` `python/sglang/srt/lora/lora_moe_runners.py`:450; signals: alignment, kernel, moe, speedup; excerpt: "- compute lora alignment()), which launches LoRA-specific kernels during graph capture/replay. In adapter-free batches this means the nolora graph still contains LoRA routing work, ..." (https://github.com/sgl-project/sglang/pull/22809#discussion_r3079969461)
- `2026-04-14T13:55:21Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. Reviewed commit: 1099f03814 ℹ️ About Codex in GitHub [Your team has ..." (https://github.com/sgl-project/sglang/pull/22809#pullrequestreview-4106466446)
