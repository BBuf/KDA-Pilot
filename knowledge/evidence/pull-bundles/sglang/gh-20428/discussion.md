# PR Discussion Digest

- Source PR: [sgl-project/sglang#20428](https://github.com/sgl-project/sglang/pull/20428)
- Source page: `sources/prs/sglang/PR-20428.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-20428`
- Generated at: `2026-05-20T15:29:04.409115+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-12T08:12:59Z`
- Merged: `2026-03-12T14:25:02Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: ispobock, yizhang2077, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2026-03-12T08:18:33Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds a benchmark script to compare the performance and correctness of Triton and ... (https://github.com/sgl-project/sglang/pull/20428#pullrequestreview-3934722166)
- `2026-03-12T08:22:47Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/20428#pullrequestreview-3934740793)
- `2026-03-12T08:23:58Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/20428#pullrequestreview-3934745909)
- `2026-03-12T08:45:07Z` `APPROVED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/20428#pullrequestreview-3934845498)

## Inline Comment Hotspots

- `benchmark/bench_linear_attention/bench_gdn_prefill.py`: 4 inline comment(s)

## High-Signal Discussion

- `2026-03-12T09:21:21Z` `issue` by `yuan-luo`; signals: aligned, benchmark, flashinfer, kernel, triton; excerpt: "The triton kernel use use qk l2norm in kernel=true, while flashinfer kernel use use qk l2norm in kernel=false. There's a small gap here which ..." (https://github.com/sgl-project/sglang/pull/20428#issuecomment-4045190230)
- `2026-03-12T08:23:58Z` `inline` by `yuan-luo` `benchmark/bench_linear_attention/bench_gdn_prefill.py`:81; signals: attention, benchmark, flashinfer, hang; excerpt: "No, compliant with flashinfer implementation. Keep unchanged." (https://github.com/sgl-project/sglang/pull/20428#discussion_r2923011300)
- `2026-03-12T08:22:47Z` `inline` by `yuan-luo` `benchmark/bench_linear_attention/bench_gdn_prefill.py`:398; signals: attention, benchmark; excerpt: "Addressed. Result is the same." (https://github.com/sgl-project/sglang/pull/20428#discussion_r2923006097)
