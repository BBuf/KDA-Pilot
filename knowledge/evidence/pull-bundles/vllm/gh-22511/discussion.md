# PR Discussion Digest

- Source PR: [vllm-project/vllm#22511](https://github.com/vllm-project/vllm/pull/22511)
- Source page: `sources/prs/vllm/PR-22511.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22511`
- Generated at: `2026-05-20T15:37:06.503958+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-08T08:48:59Z`
- Merged: `2025-08-12T12:51:00Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: mgoin, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-08T08:50:20Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces necessary fixes to enable Llama4 models with FlashInfer FP4 MoE. The changes ... (https://github.com/vllm-project/vllm/pull/22511#pullrequestreview-3099981432)
- `2025-08-10T18:33:58Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/22511#pullrequestreview-3103712000)
- `2025-08-11T02:33:58Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/22511#pullrequestreview-3103877266)
- `2025-08-11T02:56:39Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/22511#pullrequestreview-3103894784)
- `2025-08-11T02:58:04Z` `COMMENTED` by `nvpohanh` (https://github.com/vllm-project/vllm/pull/22511#pullrequestreview-3103895643)
- `2025-08-11T16:28:42Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/22511#pullrequestreview-3106729372)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`: 3 inline comment(s)
- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-11T02:33:58Z` `inline` by `nvpohanh` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:173; signals: accuracy, cutlass, flashinfer, moe; excerpt: "Great point! I will fix this. For some reason this didn't degrade Llama4 Scout accuracy, which is a little weird." (https://github.com/vllm-project/vllm/pull/22511#discussion_r2265568454)
- `2025-08-11T02:58:04Z` `inline` by `nvpohanh` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:173; signals: accuracy, cutlass, flashinfer, moe; excerpt: "I have added it in the "prepare" part and confirmed that it improved the accuracy" (https://github.com/vllm-project/vllm/pull/22511#discussion_r2265585812)
- `2025-08-10T18:33:16Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:173; signals: cutlass, flashinfer, moe; excerpt: "It looks like apply router weight on input isn't being used at all in this function, how does the moe know to apply this?" (https://github.com/vllm-project/vllm/pull/22511#discussion_r2265393173)
- `2025-08-10T18:33:28Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py`:63; signals: cutlass, flashinfer, moe; excerpt: "ditto" (https://github.com/vllm-project/vllm/pull/22511#discussion_r2265393219)
- `2025-08-11T02:56:39Z` `inline` by `nvpohanh` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py`:63; signals: cutlass, flashinfer, moe; excerpt: "I have added the logic for apply router weight on input Before: After:" (https://github.com/vllm-project/vllm/pull/22511#discussion_r2265585096)
