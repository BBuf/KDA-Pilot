# PR Discussion Digest

- Source PR: [vllm-project/vllm#34900](https://github.com/vllm-project/vllm/pull/34900)
- Source page: `sources/prs/vllm/PR-34900.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-34900`
- Generated at: `2026-05-20T15:39:55.015851+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-19T17:07:56Z`
- Merged: `2026-02-22T00:28:01Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 12 (approved=3, commented=9)
- Inline review comments: 13
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=5, outdated=2
- Human participants with discussion text: DarkLight1337, LucasWilkinson, ProExpertProg, mergify, mgoin, robertgshaw2-redhat, tlrmchlsmth, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-02-19T17:09:59Z` `COMMENTED` by `gemini-code-assist` - Code Review The pull request introduces a significant performance optimization for CustomOp by allowing selective dynamic shape marking. ... (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827225942)
- `2026-02-19T17:18:27Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827283153)
- `2026-02-19T18:36:39Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827773151)
- `2026-02-19T18:38:01Z` `APPROVED` by `LucasWilkinson` - Makes sense to me, would be good for @ProExpertProg to look at. Left a couple nits (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827774131)
- `2026-02-19T19:00:11Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827916412)
- `2026-02-19T19:00:24Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827918213)
- `2026-02-19T19:00:32Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827919132)
- `2026-02-19T19:00:36Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3827919675)
- `2026-02-20T05:37:40Z` `APPROVED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3830091961)
- `2026-02-20T10:24:08Z` `COMMENTED` by `vadiklyutiy` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3831249842)
- `2026-02-20T15:11:10Z` `COMMENTED` by `ProExpertProg` (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3832583744)
- `2026-02-21T16:41:04Z` `APPROVED` by `tlrmchlsmth` - Very nice trick (https://github.com/vllm-project/vllm/pull/34900#pullrequestreview-3835690620)

## Inline Comment Hotspots

- `vllm/model_executor/custom_op.py`: 13 inline comment(s)

## High-Signal Discussion

- `2026-02-19T19:15:25Z` `issue` by `vadiklyutiy`; signals: compile, kernel; excerpt: "holy moly I always believed in torch.compile, not in hand-written kernels :-)" (https://github.com/vllm-project/vllm/pull/34900#issuecomment-3929388268)
- `2026-02-20T05:37:11Z` `inline` by `ProExpertProg` `vllm/model_executor/custom_op.py`:304; signals: general review; excerpt: "If we're just setting this as a class property, can we just set it directly in the class declaration?" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2831471681)
- `2026-02-20T10:24:08Z` `inline` by `vadiklyutiy` `vllm/model_executor/custom_op.py`:304; signals: general review; excerpt: "We can, but current implementationt I like more because: 1. It correspond how we do it in compilation for model forward path. 2. Explicit ..." (https://github.com/vllm-project/vllm/pull/34900#discussion_r2832482008)
- `2026-02-19T17:18:27Z` `inline` by `vadiklyutiy` `vllm/model_executor/custom_op.py`:252; signals: general review; excerpt: "This code is not on hot path" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829108084)
- `2026-02-19T18:36:13Z` `inline` by `mgoin` `vllm/model_executor/custom_op.py`:208; signals: general review; excerpt: "I think keeping these comments are valuable, especially for the new section since it is so dense" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829512992)
- `2026-02-19T18:36:22Z` `inline` by `LucasWilkinson` `vllm/model_executor/custom_op.py`:214; signals: general review; excerpt: "nit: why remove?" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829513597)
- `2026-02-19T18:36:25Z` `inline` by `LucasWilkinson` `vllm/model_executor/custom_op.py`:219; signals: general review; excerpt: "nit: why remove?" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829513911)
- `2026-02-19T18:36:29Z` `inline` by `LucasWilkinson` `vllm/model_executor/custom_op.py`:208; signals: general review; excerpt: "nit: why remove?" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829514195)
- `2026-02-19T19:00:10Z` `inline` by `vadiklyutiy` `vllm/model_executor/custom_op.py`:208; signals: general review; excerpt: "removed by mistake. fixed" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829633614)
- `2026-02-19T19:00:24Z` `inline` by `vadiklyutiy` `vllm/model_executor/custom_op.py`:208; signals: general review; excerpt: "removed by mistake. fixed" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829634813)
- `2026-02-19T19:00:32Z` `inline` by `vadiklyutiy` `vllm/model_executor/custom_op.py`:219; signals: general review; excerpt: "removed by mistake. fixed" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829635418)
- `2026-02-19T19:00:36Z` `inline` by `vadiklyutiy` `vllm/model_executor/custom_op.py`:214; signals: general review; excerpt: "removed by mistake. fixed" (https://github.com/vllm-project/vllm/pull/34900#discussion_r2829635715)
