# PR Discussion Digest

- Source PR: [vllm-project/vllm#25503](https://github.com/vllm-project/vllm/pull/25503)
- Source page: `sources/prs/vllm/PR-25503.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-25503`
- Generated at: `2026-05-20T15:37:56.209027+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-23T18:32:15Z`
- Merged: `2025-09-24T22:50:04Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: djmmoss, mergify, mgoin, vadiklyutiy, youkaichao
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 3

## Review Decisions

- `2025-09-23T18:34:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables BF16 support for the FlashInfer Fused Cutlass MoE kernel, targeting Hopper and ... (https://github.com/vllm-project/vllm/pull/25503#pullrequestreview-3259183372)
- `2025-09-23T19:47:00Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/25503#pullrequestreview-3259286290)
- `2025-09-23T19:58:16Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/25503#pullrequestreview-3259410204)
- `2025-09-23T21:16:24Z` `COMMENTED` by `djmmoss` (https://github.com/vllm-project/vllm/pull/25503#pullrequestreview-3259620441)
- `2025-09-24T22:49:59Z` `APPROVED` by `mgoin` - LGTM, thanks. Would be good to expand this kernel's usage in the future if possible (https://github.com/vllm-project/vllm/pull/25503#pullrequestreview-3264957479)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-23T19:58:16Z` `inline` by `djmmoss` `vllm/model_executor/layers/fused_moe/layer.py`:305; signals: blackwell, moe, perf, performance, sm100, sm90, triton; excerpt: "I will add the check for SM90 and SM100. Tuned Triton still give the best performance in the TP only case (apart from high ..." (https://github.com/vllm-project/vllm/pull/25503#discussion_r2373318275)
- `2025-09-23T19:11:33Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:141; signals: cutlass, flashinfer, moe; excerpt: "It looks like activation is ignored in FlashInferExperts::apply. Could we assert it or pass it through to the function?" (https://github.com/vllm-project/vllm/pull/25503#discussion_r2373226054)
- `2025-09-23T19:46:57Z` `inline` by `mgoin` `vllm/model_executor/layers/fused_moe/layer.py`:305; signals: moe, sm100, sm90; excerpt: "We should also check device capability is sm90 or sm100 - only those are supported right? Also have you tried TP?" (https://github.com/vllm-project/vllm/pull/25503#discussion_r2373296506)
- `2025-09-24T16:14:07Z` `issue` by `mgoin`; signals: blackwell, hopper, perf, performance; excerpt: "Are your performance numbers for Hopper for Blackwell?" (https://github.com/vllm-project/vllm/pull/25503#issuecomment-3329723823)
- `2025-09-23T21:16:24Z` `inline` by `djmmoss` `vllm/model_executor/layers/fused_moe/flashinfer_cutlass_moe.py`:141; signals: cutlass, flashinfer, moe; excerpt: "asserted" (https://github.com/vllm-project/vllm/pull/25503#discussion_r2373475306)
- `2025-09-24T16:58:36Z` `issue` by `djmmoss`; signals: blackwell, hopper; excerpt: "These numbers are for Hopper, for Blackwell the % diff is the same or better." (https://github.com/vllm-project/vllm/pull/25503#issuecomment-3329871605)
- `2025-09-24T22:49:59Z` `review` `APPROVED` by `mgoin`; signals: kernel; excerpt: "LGTM, thanks. Would be good to expand this kernel's usage in the future if possible" (https://github.com/vllm-project/vllm/pull/25503#pullrequestreview-3264957479)
- `2025-09-24T19:44:58Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @djmmoss." (https://github.com/vllm-project/vllm/pull/25503#issuecomment-3330415010)
