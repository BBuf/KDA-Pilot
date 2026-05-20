# PR Discussion Digest

- Source PR: [vllm-project/vllm#22758](https://github.com/vllm-project/vllm/pull/22758)
- Source page: `sources/prs/vllm/PR-22758.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22758`
- Generated at: `2026-05-20T15:37:11.939226+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-12T19:33:38Z`
- Merged: `2025-09-16T21:27:11Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: gshtras, maleksan85, mergify, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-12T19:34:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a fix for torch.compile errors related to q scale assertions in the ... (https://github.com/vllm-project/vllm/pull/22758#pullrequestreview-3112483967)
- `2025-08-12T20:32:28Z` `APPROVED` by `gshtras` - Thanks for the fix To clarify: this issue would present itself when using full cuda graph:true and using ... (https://github.com/vllm-project/vllm/pull/22758#pullrequestreview-3112723582)
- `2025-08-12T21:24:16Z` `COMMENTED` by `maleksan85` (https://github.com/vllm-project/vllm/pull/22758#pullrequestreview-3112905065)
- `2025-09-10T20:47:34Z` `APPROVED` by `yewentao256` - LGTM, thanks for the work! Please try merge from main to fix the ci issue (https://github.com/vllm-project/vllm/pull/22758#pullrequestreview-3207770553)
- `2025-09-13T14:14:42Z` `COMMENTED` by `yewentao256` - Please merge from main to solve the pre-commit issue (https://github.com/vllm-project/vllm/pull/22758#pullrequestreview-3220864196)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/kv_cache.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-12T20:32:28Z` `review` `APPROVED` by `gshtras`; signals: attention, cuda; excerpt: "Thanks for the fix To clarify: this issue would present itself when using full cuda graph:true and using the unified attention backend. Would happen ..." (https://github.com/vllm-project/vllm/pull/22758#pullrequestreview-3112723582)
- `2025-09-13T14:14:42Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "Please merge from main to solve the pre-commit issue" (https://github.com/vllm-project/vllm/pull/22758#pullrequestreview-3220864196)
- `2025-08-12T21:24:16Z` `inline` by `maleksan85` `vllm/model_executor/layers/quantization/kv_cache.py`:127; signals: cache; excerpt: "thanks!" (https://github.com/vllm-project/vllm/pull/22758#discussion_r2271295893)
- `2025-08-20T20:14:23Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @maleksan85." (https://github.com/vllm-project/vllm/pull/22758#issuecomment-3207958263)
- `2025-09-09T16:55:53Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @maleksan85." (https://github.com/vllm-project/vllm/pull/22758#issuecomment-3271536822)
- `2025-09-13T14:15:18Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @maleksan85." (https://github.com/vllm-project/vllm/pull/22758#issuecomment-3288437276)
