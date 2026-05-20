# PR Discussion Digest

- Source PR: [vllm-project/vllm#16674](https://github.com/vllm-project/vllm/pull/16674)
- Source page: `sources/prs/vllm/PR-16674.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16674`
- Generated at: `2026-05-20T15:34:56.459454+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-15T17:22:06Z`
- Merged: `2025-04-17T18:44:34Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: hongxiayang, houseroad, sijiac, tjtanaa
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-16T01:55:28Z` `APPROVED` by `hongxiayang` - LGTM. We need to enable the graph mode in order to achieve the full performance benefit comparing with ... (https://github.com/vllm-project/vllm/pull/16674#pullrequestreview-2770421852)
- `2025-04-16T18:24:08Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16674#pullrequestreview-2773448231)
- `2025-04-16T18:25:18Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/16674#pullrequestreview-2773450797)
- `2025-04-16T18:34:29Z` `COMMENTED` by `sijiac` (https://github.com/vllm-project/vllm/pull/16674#pullrequestreview-2773471022)
- `2025-04-17T17:55:55Z` `APPROVED` by `houseroad` - Looks good. (https://github.com/vllm-project/vllm/pull/16674#pullrequestreview-2776541445)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`: 3 inline comment(s)

## High-Signal Discussion

- `2025-04-16T18:34:29Z` `inline` by `sijiac` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:53; signals: dtype, moe; excerpt: "yes, the passed-in topk weights must in fp32 dtype, otherwise, it will have numeric issues" (https://github.com/vllm-project/vllm/pull/16674#discussion_r2047500090)
- `2025-04-16T01:55:28Z` `review` `APPROVED` by `hongxiayang`; signals: perf, performance; excerpt: "LGTM. We need to enable the graph mode in order to achieve the full performance benefit comparing with V1 graph mode without aiter." (https://github.com/vllm-project/vllm/pull/16674#pullrequestreview-2770421852)
- `2025-04-16T18:24:08Z` `inline` by `houseroad` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:46; signals: moe; excerpt: "can we assert topk weights.dim() == 2?" (https://github.com/vllm-project/vllm/pull/16674#discussion_r2047486004)
- `2025-04-16T18:25:18Z` `inline` by `houseroad` `vllm/model_executor/layers/fused_moe/rocm_aiter_fused_moe.py`:53; signals: moe; excerpt: "Does AITER require fp32 weight?" (https://github.com/vllm-project/vllm/pull/16674#discussion_r2047487728)
- `2025-04-16T03:26:26Z` `issue` by `tjtanaa`; signals: kernel; excerpt: "As a supplementary information this PR: The GSM8K lmeval score of AITER kernel of meta-llama/Llama-4-Scout-17B-16E-Instruct: The GSM8K lmeval score of AITER kernel of meta-llama/Llama-4-Maverick-17B-128E-Instruct:" (https://github.com/vllm-project/vllm/pull/16674#issuecomment-2808131015)
