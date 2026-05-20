# PR Discussion Digest

- Source PR: [vllm-project/vllm#25895](https://github.com/vllm-project/vllm/pull/25895)
- Source page: `sources/prs/vllm/PR-25895.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25895`
- Generated at: `2026-05-20T15:37:58.159962+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-29T17:16:46Z`
- Merged: `2025-09-30T14:51:31Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 6
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=1, outdated=2
- Human participants with discussion text: alexm-redhat, mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 2

## Review Decisions

- `2025-09-29T17:19:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces important fixes for FP8 MoE, particularly for TRT-LLM latency kernels. The changes ... (https://github.com/vllm-project/vllm/pull/25895#pullrequestreview-3280907990)
- `2025-09-29T17:52:49Z` `APPROVED` by `alexm-redhat` - LGTM (https://github.com/vllm-project/vllm/pull/25895#pullrequestreview-3281040224)
- `2025-09-29T18:06:21Z` `COMMENTED` by `pavanimajety` (https://github.com/vllm-project/vllm/pull/25895#pullrequestreview-3281091147)
- `2025-09-30T14:51:05Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25895#pullrequestreview-3285392628)

## Inline Comment Hotspots

- `vllm/model_executor/layers/quantization/fp8.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-09-30T14:49:21Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/fp8.py`:468; signals: fp8, gemm; excerpt: "Note for future self: we should clean up these logs now that VLLM USE DEEP GEMM=1 by default" (https://github.com/vllm-project/vllm/pull/25895#discussion_r2391881817)
- `2025-09-29T17:52:42Z` `inline` by `alexm-redhat` `vllm/model_executor/layers/quantization/fp8.py`:942; signals: fp8; excerpt: "One line fix, so simple, we really need CI tests working properly" (https://github.com/vllm-project/vllm/pull/25895#discussion_r2388768624)
- `2025-09-29T18:06:20Z` `inline` by `pavanimajety` `vllm/model_executor/layers/quantization/fp8.py`:942; signals: fp8; excerpt: "Yeah, this and the return in the line below." (https://github.com/vllm-project/vllm/pull/25895#discussion_r2388803979)
- `2025-09-30T14:50:46Z` `inline` by `mgoin` `vllm/model_executor/layers/quantization/fp8.py`:965; signals: fp8; excerpt: "Is this a bug too? It seems like we need to return here rather than write to result" (https://github.com/vllm-project/vllm/pull/25895#discussion_r2391889330)
