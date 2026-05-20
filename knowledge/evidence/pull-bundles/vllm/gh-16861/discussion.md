# PR Discussion Digest

- Source PR: [vllm-project/vllm#16861](https://github.com/vllm-project/vllm/pull/16861)
- Source page: `sources/prs/vllm/PR-16861.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16861`
- Generated at: `2026-05-20T15:35:04.443343+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-18T17:25:29Z`
- Merged: `2025-04-22T03:44:33Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=3, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: bnellnm, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-18T17:40:37Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/16861#pullrequestreview-2779094399)
- `2025-04-18T17:54:44Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/16861#pullrequestreview-2779117094)
- `2025-04-18T17:55:30Z` `APPROVED` by `bnellnm` - lgtm! (https://github.com/vllm-project/vllm/pull/16861#pullrequestreview-2779118528)
- `2025-04-21T14:36:25Z` `APPROVED` by `tlrmchlsmth` - Looks good to me, thanks! (https://github.com/vllm-project/vllm/pull/16861#pullrequestreview-2781410952)
- `2025-04-21T20:29:51Z` `APPROVED` by `mgoin` - LGTM and needs a force merge (https://github.com/vllm-project/vllm/pull/16861#pullrequestreview-2782185720)

## Inline Comment Hotspots

- `tests/kernels/test_cutlass_moe.py`: 1 inline comment(s)
- `vllm/model_executor/layers/fused_moe/cutlass_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-04-18T17:40:37Z` `inline` by `bnellnm` `tests/kernels/test_cutlass_moe.py`:334; signals: cutlass, kernel, moe; excerpt: "ep size: int" (https://github.com/vllm-project/vllm/pull/16861#discussion_r2050919763)
- `2025-04-18T17:54:44Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/cutlass_moe.py`:137; signals: cutlass, moe; excerpt: "nit: Can you add a comment for posterity about why (a map + c2) need to be initialized to zeros instead of empty?" (https://github.com/vllm-project/vllm/pull/16861#discussion_r2050934234)
