# PR Discussion Digest

- Source PR: [vllm-project/vllm#16745](https://github.com/vllm-project/vllm/pull/16745)
- Source page: `sources/prs/vllm/PR-16745.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16745`
- Generated at: `2026-05-20T15:34:59.644157+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-16T22:10:49Z`
- Merged: `2025-05-02T14:03:32Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: ElizaWszola, bnellnm, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-29T22:35:22Z` `APPROVED` by `bnellnm` - LGTM. Is there a test for this? (https://github.com/vllm-project/vllm/pull/16745#pullrequestreview-2805220405)
- `2025-04-30T05:42:36Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/16745#pullrequestreview-2805808188)
- `2025-04-30T20:13:28Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/16745#pullrequestreview-2808336584)
- `2025-05-02T14:03:24Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/16745#pullrequestreview-2812098261)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-30T20:13:28Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:605; signals: fp8, moe; excerpt: "Good catch, this is just copied from FP8. I don't think it matters as scales should always be present" (https://github.com/vllm-project/vllm/pull/16745#discussion_r2069377538)
- `2025-04-30T05:42:36Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/quantization/compressed_tensors/compressed_tensors_moe.py`:605; signals: moe; excerpt: "Why is this ones? Are the scales not always present?" (https://github.com/vllm-project/vllm/pull/16745#discussion_r2067889171)
