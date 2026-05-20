# PR Discussion Digest

- Source PR: [Dao-AILab/quack#96](https://github.com/Dao-AILab/quack/pull/96)
- Source page: `sources/prs/quack/PR-96.md`
- Evidence bundle: `evidence/pull-bundles/quack/gh-96`
- Generated at: `2026-05-20T15:17:26.314644+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-04T19:34:08Z`
- Merged: `2026-04-14T07:17:23Z`

## Discussion Counts

- Issue comments: 15
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: blake-snc, emre570, johnnynunez, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T07:17:09Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/quack/pull/96#pullrequestreview-4104029654)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-09T19:51:56Z` `issue` by `blake-snc`; signals: epilogue, gemm, kernel, nan, occupancy, perf, performance, pipeline; excerpt: "Had a solution but closed the PR — the non-gated paths are functionally correct (60 tests pass) but inherit a 4.5x performance gap from ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4217093251)
- `2026-04-10T07:22:03Z` `issue` by `emre570`; signals: epilogue, gemm, kernel, nan, occupancy, perf, performance, pipeline; excerpt: "Had a solution but closed the PR — the non-gated paths are functionally correct (60 tests pass) but inherit a 4.5x performance gap from ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4221904037)
- `2026-04-08T18:43:11Z` `issue` by `blake-snc`; signals: bf16, cuda, dtype, hang, kernel, tma; excerpt: "@emre570 Tested your rmsnorm changes on SM121a (DGX Spark) — all passing for N ≤ 8192 (bf16/fp16) and N ≤ 4096 (fp32). Beyond those ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4208690490)
- `2026-04-13T03:01:06Z` `issue` by `tridao`; signals: epilogue, gemm, hopper, kernel, layout, warp; excerpt: "Once we have the reduction kernels, gemm + epilogue should be next. Pure gemm and gemm + some epilogues are working already. Some aren't ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4233470860)
- `2026-04-13T10:41:00Z` `issue` by `emre570`; signals: bf16, kernel, sm120, tma; excerpt: "@emre570 is this PR ready? Hi sir, Yes, PR is ready. Rebased on latest main, all reduction kernel tests pass on SM120 (RTX 5080): ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4235751156)
- `2026-04-04T20:27:24Z` `issue` by `emre570`; signals: cute, kernel, tma; excerpt: "I corrected it based on your request, I'm also working through the softmax and cross entropy kernels next. This is my first time with ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4187699751)
- `2026-04-09T18:58:05Z` `issue` by `emre570`; signals: epilogue, gemm, sm120; excerpt: "Also I noticed gemm act, gemm dact, and gemm sq reduce still throw NotImplementedError on SM120. Would you be interested in a follow-up PR ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4216737080)
- `2026-04-05T00:30:31Z` `issue` by `tridao`; signals: bf16, sm120; excerpt: "I think generally 16k is the limit, but I haven't tested. The limit is smem: 16k elements in bf16 takes 32KB in smem, 16k ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4187991873)
- `2026-04-09T18:57:37Z` `issue` by `emre570`; signals: kernel, tma; excerpt: "All reduction kernels are covered now (rmsnorm, softmax, cross entropy, topk, rms final reduce). Test skips added for large N on SM12x due to ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4216733732)
- `2026-04-04T22:38:49Z` `issue` by `emre570`; signals: general review; excerpt: "You can skip the tests for larger dim if device capacity is 8.x or 12.x Is there a hard limit or something for decide ..." (https://github.com/Dao-AILab/quack/pull/96#issuecomment-4187862040)
