# PR Discussion Digest

- Source PR: [sgl-project/sglang#3035](https://github.com/sgl-project/sglang/pull/3035)
- Source page: `sources/prs/sglang/PR-3035.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3035`
- Generated at: `2026-05-20T15:29:55.957929+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-01-21T12:48:43Z`
- Merged: `2025-01-21T14:21:54Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: ispobock, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-01-21T12:51:11Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3035#pullrequestreview-2564530902)
- `2025-01-21T12:52:49Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/3035#pullrequestreview-2564536874)
- `2025-01-21T13:11:25Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/3035#pullrequestreview-2564588661)
- `2025-01-21T14:21:45Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3035#pullrequestreview-2564785887)

## Inline Comment Hotspots

- `sgl-kernel/src/sgl-kernel/csrc/int8_gemm_kernel.cu`: 2 inline comment(s)
- `sgl-kernel/tests/test_int8_gemm.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-01-21T12:52:49Z` `inline` by `ispobock` `sgl-kernel/tests/test_int8_gemm.py`:28; signals: bf16, dtype, gemm, kernel; excerpt: "The out dtype is fp16 or bf16. It's better to use random input for sufficient test." (https://github.com/sgl-project/sglang/pull/3035#discussion_r1923676358)
- `2025-01-21T12:50:48Z` `inline` by `zhyncs` `sgl-kernel/tests/test_int8_gemm.py`:28; signals: gemm, hang, kernel; excerpt: "Why change to randn here?" (https://github.com/sgl-project/sglang/pull/3035#discussion_r1923673433)
- `2025-01-21T12:50:20Z` `inline` by `zhyncs` `sgl-kernel/src/sgl-kernel/csrc/int8_gemm_kernel.cu`:8; signals: gemm, kernel; excerpt: "use include instead" (https://github.com/sgl-project/sglang/pull/3035#discussion_r1923672753)
- `2025-01-21T13:11:25Z` `inline` by `ispobock` `sgl-kernel/src/sgl-kernel/csrc/int8_gemm_kernel.cu`:8; signals: gemm, kernel; excerpt: "updated" (https://github.com/sgl-project/sglang/pull/3035#discussion_r1923705232)
- `2025-01-21T12:54:16Z` `issue` by `ispobock`; signals: flashinfer; excerpt: "The ut failed for flashinfer dependency. Could you help check? @zhyncs" (https://github.com/sgl-project/sglang/pull/3035#issuecomment-2604657798)
