# PR Discussion Digest

- Source PR: [vllm-project/vllm#34673](https://github.com/vllm-project/vllm/pull/34673)
- Source page: `sources/prs/vllm/PR-34673.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34673`
- Generated at: `2026-05-20T15:39:53.060229+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-17T06:30:52Z`
- Merged: `2026-02-18T21:03:25Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 8 (approved=4, changes_requested=1, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: haosdent, mgoin, robertgshaw2-redhat, tlrmchlsmth, wwl2755
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-02-17T06:32:10Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly fixes an issue where an incorrect routing method was selected for MoE ... (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3811968842)
- `2026-02-17T14:17:58Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3814213522)
- `2026-02-17T14:48:17Z` `APPROVED` by `tlrmchlsmth` (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3814399621)
- `2026-02-17T16:52:40Z` `COMMENTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3815104942)
- `2026-02-17T16:52:44Z` `CHANGES_REQUESTED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3815105220)
- `2026-02-18T03:16:22Z` `COMMENTED` by `wwl2755` (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3817481765)
- `2026-02-18T18:14:29Z` `APPROVED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3821479992)
- `2026-02-18T18:43:41Z` `APPROVED` by `robertgshaw2-redhat` (https://github.com/vllm-project/vllm/pull/34673#pullrequestreview-3821604781)

## Inline Comment Hotspots

- `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-17T16:52:40Z` `inline` by `robertgshaw2-redhat` `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`:149; signals: moe; excerpt: "why do we need to pass num expert group to these cstors? if it has num expert group, then it is GroupedTopk type. So ..." (https://github.com/vllm-project/vllm/pull/34673#discussion_r2818030369)
- `2026-02-18T03:16:22Z` `inline` by `wwl2755` `vllm/model_executor/layers/fused_moe/router/fused_topk_bias_router.py`:149; signals: moe; excerpt: "Thanks for pointing out!" (https://github.com/vllm-project/vllm/pull/34673#discussion_r2820136915)
- `2026-02-17T17:01:57Z` `issue` by `robertgshaw2-redhat`; signals: failing; excerpt: "note: failing tests are due to infra" (https://github.com/vllm-project/vllm/pull/34673#issuecomment-3915910997)
- `2026-02-17T16:53:43Z` `issue` by `robertgshaw2-redhat`; signals: general review; excerpt: "We should not pass the num expert group attribute to the constructors. If the num expert group is not None, then its a GroupedTopK ..." (https://github.com/vllm-project/vllm/pull/34673#issuecomment-3915871188)
