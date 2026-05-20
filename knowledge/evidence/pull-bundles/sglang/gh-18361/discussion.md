# PR Discussion Digest

- Source PR: [sgl-project/sglang#18361](https://github.com/sgl-project/sglang/pull/18361)
- Source page: `sources/prs/sglang/PR-18361.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18361`
- Generated at: `2026-05-20T15:28:36.984847+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-06T09:36:21Z`
- Merged: `2026-03-03T12:30:48Z`

## Discussion Counts

- Issue comments: 11
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 10
- Review threads observed: 10
- Resolved/outdated thread markers: resolved=0, outdated=10
- Human participants with discussion text: Swipe4057, hlu1, shiyu7, xutizhou, yizhang2077, yuan-luo, yyihuang
- Automation comments/reviews omitted from high-signal summary: 12
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2026-02-06T09:45:15Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for K-last SSM state layout to leverage FlashInfer's high-performance GDN kernels, ... (https://github.com/sgl-project/sglang/pull/18361#pullrequestreview-3761908794)
- `2026-02-28T08:16:14Z` `APPROVED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/18361#pullrequestreview-3870234134)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/hybrid_linear_attn_backend.py`: 4 inline comment(s)
- `benchmark/compare_klast_vlast_precision.py`: 4 inline comment(s)
- `python/sglang/jit_kernel/cutedsl_gdn_verify.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-02-11T01:21:44Z` `issue` by `xutizhou`; signals: flashinfer, kernel; excerpt: "Hi @xutizhou. Can you confirm if there is any duplication in 17918 so we can close it? Yes, 17918 and 18361 use the exact ..." (https://github.com/sgl-project/sglang/pull/18361#issuecomment-3881607042)
- `2026-02-11T02:15:58Z` `issue` by `hlu1`; signals: accuracy; excerpt: "@xutizhou @samuellees If you have gpqa accuracy results, please add it to the PR description" (https://github.com/sgl-project/sglang/pull/18361#issuecomment-3881732225)
