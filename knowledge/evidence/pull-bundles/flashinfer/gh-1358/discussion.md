# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1358](https://github.com/flashinfer-ai/flashinfer/pull/1358)
- Source page: `sources/prs/flashinfer/PR-1358.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1358`
- Generated at: `2026-05-20T15:22:25.723273+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-31T06:20:17Z`
- Merged: `2025-08-03T18:30:21Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: elfiegg, yzh119
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-31T06:20:34Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @elfiegg, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1358#pullrequestreview-3074111216)
- `2025-07-31T06:22:26Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request removes tensor transpositions for scale factors in the trtllm backend of gemm fp8 ... (https://github.com/flashinfer-ai/flashinfer/pull/1358#pullrequestreview-3074115087)
- `2025-08-01T06:02:19Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1358#pullrequestreview-3077802469)
- `2025-08-01T06:46:42Z` `COMMENTED` by `elfiegg` (https://github.com/flashinfer-ai/flashinfer/pull/1358#pullrequestreview-3077956825)
- `2025-08-01T06:47:11Z` `COMMENTED` by `elfiegg` (https://github.com/flashinfer-ai/flashinfer/pull/1358#pullrequestreview-3077958527)
- `2025-08-03T13:57:45Z` `APPROVED` by `yzh119` - Let's merge this one first and improve the interface and docstring in later PRs. Thanks @elfiegg ! (https://github.com/flashinfer-ai/flashinfer/pull/1358#pullrequestreview-3082188612)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 3 inline comment(s)
- `tests/test_groupwise_scaled_gemm_fp8.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-01T06:02:15Z` `inline` by `yzh119` `tests/test_groupwise_scaled_gemm_fp8.py`:116; signals: fp8, gemm, hang; excerpt: "The last .t() is not necessary, we only use the pointer of the tensor, and .t() only changes shape and stride order." (https://github.com/flashinfer-ai/flashinfer/pull/1358#discussion_r2247016642)
- `2025-08-01T06:46:41Z` `inline` by `elfiegg` `flashinfer/gemm.py`:1587; signals: flashinfer, gemm, kernel; excerpt: "Agree. The scale major mode is very confusing. For TRTLLM - it's not even used as the kernel only supports MN for a & ..." (https://github.com/flashinfer-ai/flashinfer/pull/1358#discussion_r2247121354)
- `2025-07-31T07:34:45Z` `issue` by `yzh119`; signals: fp8, gemm, hang; excerpt: "Some of the unittests (such as tests/test groupwise scaled gemm fp8.py::test fp8 groupwise gemm[trtllm-MN-8192-8192-8192] ⨯) failed with this change: @elfiegg @sergachev would you mind ..." (https://github.com/flashinfer-ai/flashinfer/pull/1358#issuecomment-3138868343)
- `2025-08-01T06:01:34Z` `inline` by `yzh119` `flashinfer/gemm.py`:1587; signals: flashinfer, gemm; excerpt: "It's weird to me to assume the b scale is contiguous on the first dimension while saying it's MN-major (it's actually K-major). I prefer ..." (https://github.com/flashinfer-ai/flashinfer/pull/1358#discussion_r2247014959)
- `2025-08-01T06:47:11Z` `inline` by `elfiegg` `tests/test_groupwise_scaled_gemm_fp8.py`:116; signals: fp8, gemm; excerpt: "Done." (https://github.com/flashinfer-ai/flashinfer/pull/1358#discussion_r2247122490)
