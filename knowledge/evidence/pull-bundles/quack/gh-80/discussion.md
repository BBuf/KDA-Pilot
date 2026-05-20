# PR Discussion Digest

- Source PR: [Dao-AILab/quack#80](https://github.com/Dao-AILab/quack/pull/80)
- Source page: `sources/prs/quack/PR-80.md`
- Evidence bundle: `evidence/pull-bundles/quack/gh-80`
- Generated at: `2026-05-20T15:17:24.921797+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-11T02:42:53Z`
- Merged: `2026-03-25T22:30:31Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: GarlGuo, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-23T17:00:48Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/80#pullrequestreview-3993203771)
- `2026-03-23T17:46:37Z` `COMMENTED` by `GarlGuo` (https://github.com/Dao-AILab/quack/pull/80#pullrequestreview-3993527203)
- `2026-03-23T18:18:27Z` `COMMENTED` by `tridao` (https://github.com/Dao-AILab/quack/pull/80#pullrequestreview-3993704004)
- `2026-03-25T22:30:20Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/80#pullrequestreview-4010290904)

## Inline Comment Hotspots

- `quack/gemm_config.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-23T17:46:37Z` `inline` by `GarlGuo` `quack/gemm_config.py`:59; signals: gemm, sm100, sm90; excerpt: "@tridao do you mean sm90 by default not use dynamic persistent and sm100 by default use dynamic persistent (CLC)?" (https://github.com/Dao-AILab/quack/pull/80#discussion_r2976601649)
- `2026-03-23T17:00:49Z` `inline` by `tridao` `quack/gemm_config.py`:59; signals: gemm, sm90; excerpt: "I think sm90 default should have dynamic persistent=False and sm90 default should have dynamic persistent=True. Anyway to accomplish that?" (https://github.com/Dao-AILab/quack/pull/80#discussion_r2976338425)
- `2026-03-23T18:18:27Z` `inline` by `tridao` `quack/gemm_config.py`:59; signals: gemm; excerpt: "yes" (https://github.com/Dao-AILab/quack/pull/80#discussion_r2976766283)
- `2026-03-11T06:30:59Z` `issue` by `tridao`; signals: perf; excerpt: "How big is the perf diff? And I think we should reuse the name dynamic-persistent for this instead of CLC" (https://github.com/Dao-AILab/quack/pull/80#issuecomment-4036841054)
- `2026-03-11T17:37:30Z` `issue` by `GarlGuo`; signals: moe; excerpt: "For one of the MoE configs, the diff is about 10% for up-proj & down-proj forward pass, and up-proj activation gradient. In general, CLC ..." (https://github.com/Dao-AILab/quack/pull/80#issuecomment-4040933286)
- `2026-03-11T18:15:09Z` `issue` by `GarlGuo`; signals: blackwell; excerpt: "@tridao If we reuse the name of dynamic persistence when passing the argument, how can we differentiate the case where we use actual dynamic ..." (https://github.com/Dao-AILab/quack/pull/80#issuecomment-4041172149)
- `2026-03-11T18:24:00Z` `issue` by `tridao`; signals: blackwell; excerpt: "On blackwell there's no reason to do the old dynamic persistnet with gmem semaphore, CLC is strictly better than that. So on blackwell dynamic ..." (https://github.com/Dao-AILab/quack/pull/80#issuecomment-4041225328)
