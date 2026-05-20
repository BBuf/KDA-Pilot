# PR Discussion Digest

- Source PR: [vllm-project/vllm#23031](https://github.com/vllm-project/vllm/pull/23031)
- Source page: `sources/prs/vllm/PR-23031.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23031`
- Generated at: `2026-05-20T15:37:16.400556+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-16T17:31:02Z`
- Merged: `2025-08-17T00:41:23Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: mgoin, simon-mo, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-16T17:33:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses an FP8 accuracy issue for MoE models like Qwen3. The root cause ... (https://github.com/vllm-project/vllm/pull/23031#pullrequestreview-3125954484)
- `2025-08-16T18:51:29Z` `COMMENTED` by `yewentao256` - Could you also add some lm-eval results to show the problem has already fixed? (https://github.com/vllm-project/vllm/pull/23031#pullrequestreview-3125986427)
- `2025-08-17T00:37:21Z` `APPROVED` by `simon-mo` - verified locally as well. merging. (https://github.com/vllm-project/vllm/pull/23031#pullrequestreview-3126128835)
- `2025-08-17T00:38:49Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23031#pullrequestreview-3126129056)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-08-16T18:51:29Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Could you also add some lm-eval results to show the problem has already fixed?" (https://github.com/vllm-project/vllm/pull/23031#pullrequestreview-3125986427)
- `2025-08-17T00:41:06Z` `issue` by `simon-mo`; signals: fp8; excerpt: "qwen3-30b-fp8 Before After" (https://github.com/vllm-project/vllm/pull/23031#issuecomment-3194005929)
