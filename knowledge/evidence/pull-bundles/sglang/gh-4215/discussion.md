# PR Discussion Digest

- Source PR: [sgl-project/sglang#4215](https://github.com/sgl-project/sglang/pull/4215)
- Source page: `sources/prs/sglang/PR-4215.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4215`
- Generated at: `2026-05-20T15:30:07.134696+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-08T23:02:48Z`
- Merged: `2025-03-12T07:08:03Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 7
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: BBuf, hebiao064, zcnrex
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-03-10T13:27:06Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2670952883)
- `2025-03-11T05:05:41Z` `COMMENTED` by `zcnrex` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2672825259)
- `2025-03-11T06:56:39Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2673067519)
- `2025-03-11T21:52:56Z` `COMMENTED` by `zcnrex` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2676197110)
- `2025-03-11T23:05:10Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2676328502)
- `2025-03-12T04:07:14Z` `COMMENTED` by `zcnrex` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2676835141)
- `2025-03-12T04:08:28Z` `COMMENTED` by `zcnrex` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2676837595)
- `2025-03-12T06:04:16Z` `COMMENTED` by `hebiao064` (https://github.com/sgl-project/sglang/pull/4215#pullrequestreview-2677068888)

## Inline Comment Hotspots

- `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`: 7 inline comment(s)

## High-Signal Discussion

- `2025-03-11T23:05:10Z` `inline` by `hebiao064` `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`:59; signals: cache, fp8, gemm, kernel, memory, register; excerpt: "token output is in global memory, we load it into output arr first in register/cache and then copy to global memory to make it ..." (https://github.com/sgl-project/sglang/pull/4215#discussion_r1990248872)
- `2025-03-11T06:56:39Z` `inline` by `hebiao064` `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`:47; signals: flashinfer, fp8, gemm, kernel, vector; excerpt: "we still need to handle remaining part when we use vectorization from flashinfer" (https://github.com/sgl-project/sglang/pull/4215#discussion_r1988522984)
- `2025-03-12T04:07:14Z` `inline` by `zcnrex` `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`:59; signals: flashinfer, fp8, gemm, kernel, vector; excerpt: "Can we try using flashinfer vector to store 8 ele at once using cast store()?" (https://github.com/sgl-project/sglang/pull/4215#discussion_r1990521056)
- `2025-03-12T06:04:16Z` `inline` by `hebiao064` `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`:59; signals: fp8, gemm, kernel, perf, performance; excerpt: "tried it, same performance, will not adopt that." (https://github.com/sgl-project/sglang/pull/4215#discussion_r1990668820)
- `2025-03-11T05:05:41Z` `inline` by `zcnrex` `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`:47; signals: fp8, gemm, kernel; excerpt: "Looks like this is equivalent to the original impl with additional input - vec - val? Should we revert?" (https://github.com/sgl-project/sglang/pull/4215#discussion_r1988399439)
- `2025-03-11T21:52:56Z` `inline` by `zcnrex` `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`:59; signals: fp8, gemm, kernel; excerpt: "Can we directly copy to token output?" (https://github.com/sgl-project/sglang/pull/4215#discussion_r1990175056)
- `2025-03-12T04:08:28Z` `inline` by `zcnrex` `sgl-kernel/csrc/gemm/per_token_quant_fp8.cu`:59; signals: fp8, gemm, kernel; excerpt: "it could be sth like output arr.cast store(token output + i vec size) after line 70" (https://github.com/sgl-project/sglang/pull/4215#discussion_r1990521955)
