# PR Discussion Digest

- Source PR: [vllm-project/vllm#14454](https://github.com/vllm-project/vllm/pull/14454)
- Source page: `sources/prs/vllm/PR-14454.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-14454`
- Generated at: `2026-05-20T15:34:26.081101+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-07T18:26:44Z`
- Merged: `2025-03-24T23:45:31Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: ProExpertProg, charlifu, divakar-amd, gshtras, mergify, mgoin, robertgshaw2-redhat
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-20T15:52:06Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14454#pullrequestreview-2703279753)
- `2025-03-20T21:39:29Z` `COMMENTED` by `charlifu` (https://github.com/vllm-project/vllm/pull/14454#pullrequestreview-2704184774)
- `2025-03-24T20:59:17Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/14454#pullrequestreview-2711667028)
- `2025-03-24T21:05:52Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/14454#pullrequestreview-2711679591)

## Inline Comment Hotspots

- `vllm/envs.py`: 2 inline comment(s)
- `vllm/model_executor/layers/fused_moe/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-11T15:32:04Z` `issue` by `charlifu`; signals: fp8, kernel, moe; excerpt: "Hi, this feature should work for any model which extends the FusedMoe class. However, if you are only importing the fused moe kernel to ..." (https://github.com/vllm-project/vllm/pull/14454#issuecomment-2714780204)
- `2025-03-11T15:14:26Z` `issue` by `divakar-amd`; signals: kernel, moe; excerpt: "Hi, this feature should work for any model which extends the FusedMoe class. However, if you are only importing the fused moe kernel to ..." (https://github.com/vllm-project/vllm/pull/14454#issuecomment-2714714445)
- `2025-03-11T15:16:28Z` `issue` by `charlifu`; signals: fp8, moe; excerpt: "QQ - would we ever not want to do this if we are on ROCm for MoE? We could do the same condition check ..." (https://github.com/vllm-project/vllm/pull/14454#issuecomment-2714723096)
- `2025-03-20T15:51:26Z` `inline` by `ProExpertProg` `vllm/model_executor/layers/fused_moe/layer.py`:100; signals: moe; excerpt: "Maybe call maybe pad weight?" (https://github.com/vllm-project/vllm/pull/14454#discussion_r2005956666)
- `2025-03-08T00:04:35Z` `issue` by `gshtras`; signals: moe; excerpt: "QQ - would we ever not want to do this if we are on ROCm for MoE? It has been mostly tested for Mixtral, ..." (https://github.com/vllm-project/vllm/pull/14454#issuecomment-2707753768)
- `2025-03-10T22:32:47Z` `issue` by `mgoin`; signals: moe; excerpt: "does not apply to any MoE model I think this feature should be improved so it generally satisfies the FusedMoE interface. This seems like ..." (https://github.com/vllm-project/vllm/pull/14454#issuecomment-2711994902)
- `2025-03-07T22:49:18Z` `issue` by `robertgshaw2-redhat`; signals: moe; excerpt: "QQ - would we ever not want to do this if we are on ROCm for MoE?" (https://github.com/vllm-project/vllm/pull/14454#issuecomment-2707655652)
- `2025-03-20T15:51:50Z` `inline` by `ProExpertProg` `vllm/envs.py`:529; signals: general review; excerpt: "Why is this not enabled by default?" (https://github.com/vllm-project/vllm/pull/14454#discussion_r2005957574)
- `2025-03-20T21:39:29Z` `inline` by `charlifu` `vllm/envs.py`:529; signals: general review; excerpt: "It used to be enabled by default." (https://github.com/vllm-project/vllm/pull/14454#discussion_r2006493146)
- `2025-03-20T21:40:55Z` `issue` by `mergify`; signals: general review; excerpt: "This pull request has merge conflicts that must be resolved before it can be merged. Please rebase the PR, @gshtras." (https://github.com/vllm-project/vllm/pull/14454#issuecomment-2741733656)
