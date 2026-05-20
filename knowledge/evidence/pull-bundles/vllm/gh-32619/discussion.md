# PR Discussion Digest

- Source PR: [vllm-project/vllm#32619](https://github.com/vllm-project/vllm/pull/32619)
- Source page: `sources/prs/vllm/PR-32619.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-32619`
- Generated at: `2026-05-20T15:39:30.725824+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-19T21:28:54Z`
- Merged: `2026-01-22T20:47:04Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: heheda12345, mgoin, xyang16
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-01-19T21:30:55Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces an optimization for DeepGemm on Hopper by creating TMA-aligned input scale tensors ... (https://github.com/vllm-project/vllm/pull/32619#pullrequestreview-3679660836)
- `2026-01-19T22:47:57Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/32619#pullrequestreview-3679805803)
- `2026-01-19T22:49:00Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/32619#pullrequestreview-3679807027)
- `2026-01-22T00:32:18Z` `APPROVED` by `mgoin` - Nice find! Looks reasonable to me. It's a little bit messy having this arg on the general QuantFP8 ... (https://github.com/vllm-project/vllm/pull/32619#pullrequestreview-3690066926)
- `2026-01-22T03:25:02Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/32619#pullrequestreview-3690444801)
- `2026-01-22T05:21:37Z` `COMMENTED` by `xyang16` (https://github.com/vllm-project/vllm/pull/32619#pullrequestreview-3690636960)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/utils/fp8_utils.py`: 6 inline comment(s)

## High-Signal Discussion

- `2026-01-22T03:25:02Z` `inline` by `xyang16` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:928; signals: fp8, hang; excerpt: "Fixed. The original code only works for 2D input scale tensor. If the tensor is 3D, shape will be (hidden size // group size, ..." (https://github.com/vllm-project/vllm/pull/32619#discussion_r2715163372)
- `2026-01-22T05:21:36Z` `inline` by `xyang16` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:925; signals: fp8, hang; excerpt: "This change is to address gemini's code review. This was just copied from the old code. But since I touched this line, gemini commented ..." (https://github.com/vllm-project/vllm/pull/32619#discussion_r2715345344)
- `2026-01-19T22:47:56Z` `inline` by `xyang16` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:920; signals: fp8; excerpt: "Yes I think it only supports 2D and 3D tensors." (https://github.com/vllm-project/vllm/pull/32619#discussion_r2706254645)
- `2026-01-19T22:49:00Z` `inline` by `xyang16` `vllm/model_executor/layers/quantization/utils/fp8_utils.py`:928; signals: fp8; excerpt: "This was copied from the old code." (https://github.com/vllm-project/vllm/pull/32619#discussion_r2706256047)
- `2026-01-22T00:32:18Z` `review` `APPROVED` by `mgoin`; signals: fp8; excerpt: "Nice find! Looks reasonable to me. It's a little bit messy having this arg on the general QuantFP8 op but not sure of a ..." (https://github.com/vllm-project/vllm/pull/32619#pullrequestreview-3690066926)
