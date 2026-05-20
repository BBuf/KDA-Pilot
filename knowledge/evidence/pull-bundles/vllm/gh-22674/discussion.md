# PR Discussion Digest

- Source PR: [vllm-project/vllm#22674](https://github.com/vllm-project/vllm/pull/22674)
- Source page: `sources/prs/vllm/PR-22674.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22674`
- Generated at: `2026-05-20T15:37:09.278318+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-11T20:43:46Z`
- Merged: `2025-08-27T05:00:21Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: mgoin, yewentao256
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-11T20:48:51Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request expands the Mixture of Experts (MoE) matching logic to support NFP4 and FP8 ... (https://github.com/vllm-project/vllm/pull/22674#pullrequestreview-3107738522)
- `2025-08-21T20:58:30Z` `COMMENTED` by `yewentao256` - Thanks for the work! Could you also add results from lm-eval to make sure we don't hurt the ... (https://github.com/vllm-project/vllm/pull/22674#pullrequestreview-3142257398)
- `2025-08-26T20:06:36Z` `APPROVED` by `mgoin` - Nice work, less code than I expected (https://github.com/vllm-project/vllm/pull/22674#pullrequestreview-3157147622)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-21T20:58:30Z` `review` `COMMENTED` by `yewentao256`; signals: accuracy; excerpt: "Thanks for the work! Could you also add results from lm-eval to make sure we don't hurt the accuracy?" (https://github.com/vllm-project/vllm/pull/22674#pullrequestreview-3142257398)
