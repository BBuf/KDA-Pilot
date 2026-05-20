# PR Discussion Digest

- Source PR: [vllm-project/vllm#15914](https://github.com/vllm-project/vllm/pull/15914)
- Source page: `sources/prs/vllm/PR-15914.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-15914`
- Generated at: `2026-05-20T15:34:43.765929+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-02T01:29:33Z`
- Merged: `2025-04-03T17:19:38Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 8 (approved=3, changes_requested=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: WoosukKwon, bnellnm, houseroad, mgoin, tlrmchlsmth
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-04-02T01:36:30Z` `APPROVED` by `tlrmchlsmth` - LGTM (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2734353403)
- `2025-04-02T01:41:08Z` `COMMENTED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2734357388)
- `2025-04-02T01:45:56Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2734362111)
- `2025-04-02T04:00:49Z` `CHANGES_REQUESTED` by `WoosukKwon` - Let's merge this after the next release cc @robertgshaw2-redhat (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2734598685)
- `2025-04-02T04:01:44Z` `COMMENTED` by `houseroad` (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2734599406)
- `2025-04-02T12:55:02Z` `COMMENTED` by `bnellnm` (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2736179949)
- `2025-04-03T16:04:15Z` `APPROVED` by `WoosukKwon` (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2740437715)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/fused_moe.py`: 2 inline comment(s)
- `tests/kernels/test_cutlass_moe.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-02T04:01:44Z` `inline` by `houseroad` `tests/kernels/test_cutlass_moe.py`:134; signals: cutlass, kernel, moe; excerpt: "uncomment?" (https://github.com/vllm-project/vllm/pull/15914#discussion_r2024031482)
- `2025-04-02T12:55:02Z` `inline` by `bnellnm` `tests/kernels/test_cutlass_moe.py`:134; signals: cutlass, kernel, moe; excerpt: "These prints were just spamming the test output with tensors." (https://github.com/vllm-project/vllm/pull/15914#discussion_r2024772384)
- `2025-04-02T01:41:08Z` `inline` by `tlrmchlsmth` `vllm/model_executor/layers/fused_moe/fused_moe.py`:451; signals: hang, moe; excerpt: "Why is topk weights optional now? I thought it would be to make it easier to skip application of the weight application and reduction ..." (https://github.com/vllm-project/vllm/pull/15914#discussion_r2023884847)
- `2025-04-02T01:45:56Z` `inline` by `bnellnm` `vllm/model_executor/layers/fused_moe/fused_moe.py`:451; signals: moe; excerpt: "If we leave mul routed weight false then we don't need the weights (and we won't have them once things are modularized). I'll see ..." (https://github.com/vllm-project/vllm/pull/15914#discussion_r2023887765)
- `2025-04-02T04:00:49Z` `review` `CHANGES_REQUESTED` by `WoosukKwon`; signals: general review; excerpt: "Let's merge this after the next release cc @robertgshaw2-redhat" (https://github.com/vllm-project/vllm/pull/15914#pullrequestreview-2734598685)
