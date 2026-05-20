# PR Discussion Digest

- Source PR: [sgl-project/sglang#4515](https://github.com/sgl-project/sglang/pull/4515)
- Source page: `sources/prs/sglang/PR-4515.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4515`
- Generated at: `2026-05-20T15:30:11.270906+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-17T13:35:52Z`
- Merged: `2025-03-19T07:02:43Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: BBuf, strgrb
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-18T07:32:11Z` `APPROVED` by `BBuf` - @zhyncs I add a acc test and ensure it's ok. We can merge it? (https://github.com/sgl-project/sglang/pull/4515#pullrequestreview-2693295613)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-03-19T05:25:53Z` `issue` by `strgrb`; signals: benchmark, compile, cuda, deepgemm, gemm, perf, performance; excerpt: "I benchmark it on 8 H20, and compile sglang with cuda12.8 for best performance as DeepGEMM recommended. - before optimize - after optimize" (https://github.com/sgl-project/sglang/pull/4515#issuecomment-2735371999)
- `2025-03-17T13:45:18Z` `issue` by `strgrb`; signals: aligned, deepgemm, gemm, tma; excerpt: "Good job! Is the update to the deepgemm submodule necessary here? Yes, deep gemm.get col major tma aligned tensor will always copy tensor with ..." (https://github.com/sgl-project/sglang/pull/4515#issuecomment-2729568708)
- `2025-03-17T13:48:56Z` `issue` by `BBuf`; signals: aligned, deepgemm, gemm, tma; excerpt: "Good job! Is the update to the deepgemm submodule necessary here? Yes, deep gemm.get col major tma aligned tensor will always copy tensor with ..." (https://github.com/sgl-project/sglang/pull/4515#issuecomment-2729583209)
- `2025-03-17T13:41:49Z` `issue` by `BBuf`; signals: deepgemm, gemm; excerpt: "Good job! Is the update to the deepgemm submodule necessary here?" (https://github.com/sgl-project/sglang/pull/4515#issuecomment-2729557991)
