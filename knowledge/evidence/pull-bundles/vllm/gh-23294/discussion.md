# PR Discussion Digest

- Source PR: [vllm-project/vllm#23294](https://github.com/vllm-project/vllm/pull/23294)
- Source page: `sources/prs/vllm/PR-23294.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-23294`
- Generated at: `2026-05-20T15:37:29.191669+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-20T22:37:36Z`
- Merged: `2025-08-21T17:11:28Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: WoosukKwon, mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-20T22:39:54Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23294#pullrequestreview-3138463474)
- `2025-08-20T22:43:06Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses an accuracy issue with the DeepSeek-R1 model by adding a new code ... (https://github.com/vllm-project/vllm/pull/23294#pullrequestreview-3138469769)
- `2025-08-20T22:51:54Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/23294#pullrequestreview-3138480870)
- `2025-08-21T14:42:36Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/23294#pullrequestreview-3141010890)
- `2025-08-21T17:11:27Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/23294#pullrequestreview-3141612883)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-08-20T22:39:48Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/fp8.py`:1102; signals: fp8; excerpt: "I think no need to say "do not delete"" (https://github.com/vllm-project/vllm/pull/23294#discussion_r2289450063)
- `2025-08-20T22:51:54Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/fp8.py`:1102; signals: fp8; excerpt: "Fixed" (https://github.com/vllm-project/vllm/pull/23294#discussion_r2289463936)
- `2025-08-21T14:42:35Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/fp8.py`:1119; signals: fp8; excerpt: "Nice bot!" (https://github.com/vllm-project/vllm/pull/23294#discussion_r2291291434)
- `2025-08-20T22:46:45Z` `issue` by `WoosukKwon`; signals: accuracy; excerpt: "Can we have any tests to prevent this kind of issues happening again? IIRC we had similar accuracy issues for deepseek several times before." (https://github.com/vllm-project/vllm/pull/23294#issuecomment-3208293971)
- `2025-08-21T14:34:20Z` `issue` by `yewentao256`; signals: accuracy; excerpt: "Can we have any tests to prevent this kind of issues happening again? IIRC we had similar accuracy issues for deepseek several times before. ..." (https://github.com/vllm-project/vllm/pull/23294#issuecomment-3210869005)
- `2025-08-21T16:46:28Z` `issue` by `yewentao256`; signals: general review; excerpt: "@WoosukKwon Do you think we can land this first? And we can have another issue talking about how to prevent this kind of issues ..." (https://github.com/vllm-project/vllm/pull/23294#issuecomment-3211372491)
