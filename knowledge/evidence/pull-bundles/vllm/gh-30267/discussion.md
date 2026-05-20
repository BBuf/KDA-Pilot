# PR Discussion Digest

- Source PR: [vllm-project/vllm#30267](https://github.com/vllm-project/vllm/pull/30267)
- Source page: `sources/prs/vllm/PR-30267.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-30267`
- Generated at: `2026-05-20T15:38:57.359145+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-08T16:06:20Z`
- Merged: `2025-12-09T01:05:27Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=4
- Human participants with discussion text: yewentao256, zhewenl
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-12-08T16:08:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix an issue with DeepGEMM by using a configured flag self.use ... (https://github.com/vllm-project/vllm/pull/30267#pullrequestreview-3552849335)
- `2025-12-08T16:08:54Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/30267#pullrequestreview-3552849994)
- `2025-12-08T16:41:50Z` `COMMENTED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/30267#pullrequestreview-3553009945)
- `2025-12-08T16:58:08Z` `COMMENTED` by `zhewenl` (https://github.com/vllm-project/vllm/pull/30267#pullrequestreview-3553077338)
- `2025-12-08T20:21:34Z` `COMMENTED` by `yewentao256` - LGTM, thanks for the work! One small update before landed (https://github.com/vllm-project/vllm/pull/30267#pullrequestreview-3553904648)
- `2025-12-08T20:48:44Z` `APPROVED` by `yewentao256` (https://github.com/vllm-project/vllm/pull/30267#pullrequestreview-3554007527)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-12-08T16:41:46Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:272; signals: fp8, hopper; excerpt: "I am curious of this, E8M0 should be default on Hopper as well, do you set this off or something else broken?" (https://github.com/vllm-project/vllm/pull/30267#discussion_r2599333950)
- `2025-12-08T16:57:58Z` `inline` by `zhewenl` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:272; signals: fp8, hang; excerpt: "Yes, let me update the change" (https://github.com/vllm-project/vllm/pull/30267#discussion_r2599389725)
- `2025-12-08T16:08:50Z` `inline` by `yewentao256` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:275; signals: fp8; excerpt: "For the packed version, it is required to be e8m0" (https://github.com/vllm-project/vllm/pull/30267#discussion_r2599218946)
- `2025-12-08T20:21:34Z` `review` `COMMENTED` by `yewentao256`; signals: general review; excerpt: "LGTM, thanks for the work! One small update before landed" (https://github.com/vllm-project/vllm/pull/30267#pullrequestreview-3553904648)
