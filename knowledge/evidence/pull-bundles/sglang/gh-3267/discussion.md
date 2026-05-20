# PR Discussion Digest

- Source PR: [sgl-project/sglang#3267](https://github.com/sgl-project/sglang/pull/3267)
- Source page: `sources/prs/sglang/PR-3267.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-3267`
- Generated at: `2026-05-20T15:29:58.216279+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-02-03T10:22:21Z`
- Merged: `2025-02-12T17:49:33Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 5 (approved=1, changes_requested=1, commented=3)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: yizhang2077, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-02-03T10:30:35Z` `CHANGES_REQUESTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3267#pullrequestreview-2589506150)
- `2025-02-03T10:45:37Z` `COMMENTED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3267#pullrequestreview-2589539589)
- `2025-02-09T15:18:39Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/3267#pullrequestreview-2604289564)
- `2025-02-11T08:11:05Z` `COMMENTED` by `yizhang2077` (https://github.com/sgl-project/sglang/pull/3267#pullrequestreview-2607969657)
- `2025-02-12T17:49:25Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/3267#pullrequestreview-2612763110)

## Inline Comment Hotspots

- `sgl-kernel/src/sgl-kernel/csrc/cutlass_extensions/gemm/collective/collective_builder.hpp`: 3 inline comment(s)
- `sgl-kernel/benchmark/bench_fp8_blockwise_gemm.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-02-03T10:30:31Z` `inline` by `zhyncs` `sgl-kernel/src/sgl-kernel/csrc/cutlass_extensions/gemm/collective/collective_builder.hpp`; signals: cutlass, gemm, hang, kernel, perf, performance; excerpt: "@yizhang2077 Delete all of these, we should use the version directly from 3rdparty CUTLASS instead. BTW @BBuf will integrate a higher-performance version than this ..." (https://github.com/sgl-project/sglang/pull/3267#discussion_r1939148410)
- `2025-02-03T10:45:37Z` `inline` by `zhyncs` `sgl-kernel/benchmark/bench_fp8_blockwise_gemm.py`:15; signals: benchmark, block, fp8, gemm, kernel; excerpt: "I think DeepSeek V3 is sufficient, other models use per-tensor FP8, so we don't need a benchmark in that form." (https://github.com/sgl-project/sglang/pull/3267#discussion_r1939168732)
- `2025-02-09T15:18:38Z` `inline` by `yizhang2077` `sgl-kernel/src/sgl-kernel/csrc/cutlass_extensions/gemm/collective/collective_builder.hpp`; signals: cutlass, gemm, kernel; excerpt: "Currently I try to use CUTLASS lastest version but it seems can not work correctly, I leave an issue for CUTLASS [here]( and wait ..." (https://github.com/sgl-project/sglang/pull/3267#discussion_r1948130931)
- `2025-02-11T08:11:04Z` `inline` by `yizhang2077` `sgl-kernel/src/sgl-kernel/csrc/cutlass_extensions/gemm/collective/collective_builder.hpp`; signals: cutlass, gemm, kernel; excerpt: "It seems like a bug, and there is a open PR to fix it if we want to remove these files, we need update ..." (https://github.com/sgl-project/sglang/pull/3267#discussion_r1950398853)
