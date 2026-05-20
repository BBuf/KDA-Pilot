# PR Discussion Digest

- Source PR: [vllm-project/vllm#28166](https://github.com/vllm-project/vllm/pull/28166)
- Source page: `sources/prs/vllm/PR-28166.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28166`
- Generated at: `2026-05-20T15:38:25.506397+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-05T22:21:28Z`
- Merged: `2025-11-06T05:52:17Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: mxz297, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-05T22:22:48Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses two errors encountered when using FlashInfer's All-to-All with CUTLASS MoE. The first ... (https://github.com/vllm-project/vllm/pull/28166#pullrequestreview-3424738776)
- `2025-11-05T22:25:16Z` `COMMENTED` by `mxz297` (https://github.com/vllm-project/vllm/pull/28166#pullrequestreview-3424749740)
- `2025-11-05T23:43:04Z` `APPROVED` by `pavanimajety` - LGTM, thank you for the fix! (https://github.com/vllm-project/vllm/pull/28166#pullrequestreview-3424980850)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-05T23:03:44Z` `issue` by `mxz297`; signals: b200, cutlass, fp4, moe, nvfp4; excerpt: "After PR, FI-cutlass NVFP4 moe + FI-a2av works with DEP16 non-disagg on GB200 and got gsm8k score 0.96" (https://github.com/vllm-project/vllm/pull/28166#issuecomment-3493981535)
- `2025-11-05T22:25:16Z` `inline` by `mxz297` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_prepare_finalize.py`:251; signals: cutlass, flashinfer, moe; excerpt: "No, the goal here is not type cast but reinterpret the bit values" (https://github.com/vllm-project/vllm/pull/28166#discussion_r2496393411)
