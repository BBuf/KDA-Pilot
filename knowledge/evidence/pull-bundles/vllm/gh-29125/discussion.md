# PR Discussion Digest

- Source PR: [vllm-project/vllm#29125](https://github.com/vllm-project/vllm/pull/29125)
- Source page: `sources/prs/vllm/PR-29125.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-29125`
- Generated at: `2026-05-20T15:38:38.872423+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-20T22:40:27Z`
- Merged: `2025-12-09T00:31:57Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 8 (approved=2, changes_requested=1, commented=5)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=3
- Human participants with discussion text: Jakub227, chatgpt-codex-connector, mergify, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-20T22:42:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables TRITON MLA for batch invariance by disabling prefix caching, which is a ... (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3490303079)
- `2025-11-20T22:45:40Z` `COMMENTED` by `chatgpt-codex-connector` - 💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub ... (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3490319494)
- `2025-11-20T22:46:43Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3490324578)
- `2025-11-20T22:56:10Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3490378227)
- `2025-11-21T16:17:19Z` `CHANGES_REQUESTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3493470111)
- `2025-11-21T20:37:07Z` `APPROVED` by `Jakub227` (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3494285816)
- `2025-12-02T15:33:57Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3530776012)
- `2025-12-09T00:31:18Z` `APPROVED` by `mgoin` - LGTM (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3554710485)

## Inline Comment Hotspots

- `vllm/v1/core/sched/scheduler.py`: 6 inline comment(s)
- `tests/v1/determinism/test_batch_invariance.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-20T22:45:40Z` `inline` by `chatgpt-codex-connector` `vllm/v1/core/sched/scheduler.py`:185; signals: hang, mla, triton; excerpt: ", enable caching stays true and the scheduler still turns on prefix caching even though TRITON MLA is not supported with prefix caching (the ..." (https://github.com/vllm-project/vllm/pull/29125#discussion_r2547937326)
- `2025-11-21T16:15:40Z` `inline` by `mgoin` `vllm/v1/core/sched/scheduler.py`:184; signals: attention, cache; excerpt: "We should not be checking the environment variable as this isn't set when we choose the backend automatically. I think this only works for ..." (https://github.com/vllm-project/vllm/pull/29125#discussion_r2550285669)
- `2025-12-02T15:33:57Z` `inline` by `yewentao256` `vllm/v1/core/sched/scheduler.py`:184; signals: mla; excerpt: "I have fixed this and could you take another look? @mgoin I don't think we need to wait until 26315 as this is needed ..." (https://github.com/vllm-project/vllm/pull/29125#discussion_r2581713286)
- `2025-11-20T22:45:40Z` `review` `COMMENTED` by `chatgpt-codex-connector`; signals: general review; excerpt: "💡 Codex Review Here are some automated review suggestions for this pull request. ℹ️ About Codex in GitHub Codex has been enabled to automatically ..." (https://github.com/vllm-project/vllm/pull/29125#pullrequestreview-3490319494)
- `2025-12-03T23:24:17Z` `issue` by `yewentao256`; signals: mla; excerpt: "@mgoin CC, we hope to land this first so that user could have an option for MLA models" (https://github.com/vllm-project/vllm/pull/29125#issuecomment-3609251112)
- `2025-11-20T22:46:43Z` `inline` by `yewentao256` `vllm/v1/core/sched/scheduler.py`:185; signals: general review; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/29125#discussion_r2547939990)
- `2025-11-20T22:56:10Z` `inline` by `yewentao256` `vllm/v1/core/sched/scheduler.py`:185; signals: general review; excerpt: "Rocm is not supported with batch invariant" (https://github.com/vllm-project/vllm/pull/29125#discussion_r2547964862)
- `2025-12-09T00:30:07Z` `inline` by `mgoin` `tests/v1/determinism/test_batch_invariance.py`:188; signals: general review; excerpt: "Remove the comment" (https://github.com/vllm-project/vllm/pull/29125#discussion_r2600623877)
- `2025-11-21T16:23:07Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @yewentao256." (https://github.com/vllm-project/vllm/pull/29125#issuecomment-3563759594)
- `2025-11-26T16:56:13Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @yewentao256." (https://github.com/vllm-project/vllm/pull/29125#issuecomment-3582269879)
