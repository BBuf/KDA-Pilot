# PR Discussion Digest

- Source PR: [vllm-project/vllm#21121](https://github.com/vllm-project/vllm/pull/21121)
- Source page: `sources/prs/vllm/PR-21121.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-21121`
- Generated at: `2026-05-20T15:36:27.874399+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-17T14:58:22Z`
- Merged: `2025-07-18T10:55:52Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: ElizaWszola, mgoin
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-17T15:00:29Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request reduces memory allocation in non-batched CUTLASS MoE by optimizing the calculation of N ... (https://github.com/vllm-project/vllm/pull/21121#pullrequestreview-3029921714)
- `2025-07-17T16:02:02Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/21121#pullrequestreview-3030144825)
- `2025-07-17T16:09:10Z` `COMMENTED` by `ElizaWszola` (https://github.com/vllm-project/vllm/pull/21121#pullrequestreview-3030173636)
- `2025-07-17T17:26:16Z` `APPROVED` by `mgoin` - LGTM, thanks Eliza! (https://github.com/vllm-project/vllm/pull/21121#pullrequestreview-3030406281)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-07-17T16:09:10Z` `inline` by `ElizaWszola` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:286; signals: cutlass, moe, triton; excerpt: "Looks like the variables are just flipped. In Triton (workspace13 is the same tensor as workspace1): In CUTLASS: The CUTLASS names seem to make ..." (https://github.com/vllm-project/vllm/pull/21121#discussion_r2213760228)
- `2025-07-17T16:02:02Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:286; signals: cutlass, moe, triton; excerpt: "Is there a reason why this is the inverse of TritonExperts?" (https://github.com/vllm-project/vllm/pull/21121#discussion_r2213743238)
