# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1668](https://github.com/flashinfer-ai/flashinfer/pull/1668)
- Source page: `sources/prs/flashinfer/PR-1668.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1668`
- Generated at: `2026-05-20T15:23:12.609620+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-10T22:29:27Z`
- Merged: `2025-09-14T03:43:55Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 6 (approved=1, commented=5)
- Inline review comments: 10
- Review threads observed: 8
- Resolved/outdated thread markers: resolved=0, outdated=5
- Human participants with discussion text: Yang-YiFan, happierpig, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-09-10T22:29:48Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yangs75, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1668#pullrequestreview-3208021541)
- `2025-09-10T22:32:41Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new TGV GEMM backend for BF16, which is a significant performance ... (https://github.com/flashinfer-ai/flashinfer/pull/1668#pullrequestreview-3208025486)
- `2025-09-11T00:40:33Z` `COMMENTED` by `Yang-YiFan` (https://github.com/flashinfer-ai/flashinfer/pull/1668#pullrequestreview-3208174595)
- `2025-09-11T03:38:39Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1668#pullrequestreview-3208569993)
- `2025-09-11T03:43:29Z` `COMMENTED` by `yzh119` - Hi @yangs75 thanks for the contribution, would you mind spending some time resolving the [pre-commit errors]( (https://github.com/flashinfer-ai/flashinfer/pull/1668#pullrequestreview-3208575017)
- `2025-09-13T04:32:11Z` `APPROVED` by `yzh119` - Appended some commits to address the formats and more data types support comments. Ready to merge on my ... (https://github.com/flashinfer-ai/flashinfer/pull/1668#pullrequestreview-3219491948)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 4 inline comment(s)
- `csrc/tgv_gemm.cu`: 3 inline comment(s)
- `include/flashinfer/gemm/tgv_gemm.cuh`: 2 inline comment(s)
- `benchmarks/bench_tgv_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-09-11T04:24:19Z` `issue` by `Yang-YiFan`; signals: cutlass, gemm, hopper, kernel, latency, speedup, tmem, triton; excerpt: "The code can be adapted to use the hopper mma instructions. Though the mma synchronization intrinsics and tmem related logic needs to be updated. ..." (https://github.com/flashinfer-ai/flashinfer/pull/1668#issuecomment-3277414002)
- `2025-09-11T04:08:44Z` `issue` by `happierpig`; signals: cutlass, gemm, hopper, latency, speedup, tmem, triton; excerpt: "The code can be adapted to use the hopper mma instructions. Though the mma synchronization intrinsics and tmem related logic needs to be updated. ..." (https://github.com/flashinfer-ai/flashinfer/pull/1668#issuecomment-3277344289)
- `2025-09-11T03:35:49Z` `issue` by `yzh119`; signals: blackwell, hopper, kernel, sm100; excerpt: "Hey, wondering if this only works for SM100? Thanks! The kernel is written with blackwell features so currently I don't expect this could work ..." (https://github.com/flashinfer-ai/flashinfer/pull/1668#issuecomment-3277262236)
- `2025-09-10T23:42:40Z` `inline` by `Yang-YiFan` `csrc/tgv_gemm.cu`:159; signals: dtype, gemm, layout; excerpt: "seems like the dtype and input layout are both hard coded here and in [tgv gemm template.h]( Is this the correct way?" (https://github.com/flashinfer-ai/flashinfer/pull/1668#discussion_r2338170548)
- `2025-09-11T03:38:39Z` `inline` by `yzh119` `csrc/tgv_gemm.cu`:159; signals: cutlass, dtype, gemm; excerpt: "if we want to support fp16 as well, consider dispatching like this (cutlass dtype t will convert dtype to cutlass dtype:" (https://github.com/flashinfer-ai/flashinfer/pull/1668#discussion_r2338426002)
- `2025-09-11T03:40:57Z` `inline` by `yzh119` `flashinfer/gemm.py`:987; signals: dtype, flashinfer, gemm; excerpt: "can you add some docstring about input shape (e.g. b is column major) and dtype assumptions?" (https://github.com/flashinfer-ai/flashinfer/pull/1668#discussion_r2338428284)
- `2025-09-10T23:37:51Z` `inline` by `Yang-YiFan` `flashinfer/gemm.py`:908; signals: flashinfer, gemm; excerpt: "yeah looks like there is a config mismatch" (https://github.com/flashinfer-ai/flashinfer/pull/1668#discussion_r2338165641)
- `2025-09-13T04:32:08Z` `inline` by `yzh119` `benchmarks/bench_tgv_gemm.py`:101; signals: benchmark, gemm; excerpt: "Consider using" (https://github.com/flashinfer-ai/flashinfer/pull/1668#discussion_r2345888504)
- `2025-09-11T03:46:40Z` `issue` by `Yang-YiFan`; signals: hopper, tmem; excerpt: "The code can be adapted to use the hopper mma instructions. Though the mma synchronization intrinsics and tmem related logic needs to be updated." (https://github.com/flashinfer-ai/flashinfer/pull/1668#issuecomment-3277298336)
- `2025-09-10T23:35:27Z` `inline` by `Yang-YiFan` `csrc/tgv_gemm.cu`:95; signals: gemm; excerpt: "Could you make TGV GEMM CONFIG(64, 8, 8) (i.e. cta m=64, cta n=8, DMA stage=8) to be the default tactic. And fix the comment ..." (https://github.com/flashinfer-ai/flashinfer/pull/1668#discussion_r2338162494)
- `2025-09-11T03:43:29Z` `review` `COMMENTED` by `yzh119`; signals: general review; excerpt: "Hi @yangs75 thanks for the contribution, would you mind spending some time resolving the [pre-commit errors](" (https://github.com/flashinfer-ai/flashinfer/pull/1668#pullrequestreview-3208575017)
- `2025-09-11T02:49:21Z` `issue` by `happierpig`; signals: sm100; excerpt: "Hey, wondering if this only works for SM100? Thanks!" (https://github.com/flashinfer-ai/flashinfer/pull/1668#issuecomment-3277176384)
