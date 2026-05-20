# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2107](https://github.com/tile-ai/tilelang/pull/2107)
- Source page: `sources/prs/tilelang/PR-2107.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2107`
- Generated at: `2026-05-20T15:32:59.713482+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-27T14:44:22Z`
- Merged: `2026-04-28T04:35:17Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (commented=2)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LeiWang1999, coderabbitai
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-27T14:55:44Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (1) src/runtime/runtime.cc (1) 42-52: Centralize the fallback TensorMap enum values. These ... (https://github.com/tile-ai/tilelang/pull/2107#pullrequestreview-4181937853)
- `2026-04-27T15:29:09Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (2) src/op/utils.cc (1) 150-154: Share the CUDA compatibility enum values from one place. 13 is ... (https://github.com/tile-ai/tilelang/pull/2107#pullrequestreview-4182183449)

## Inline Comment Hotspots

- `testing/python/language/test_tilelang_language_tma_copy.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-27T14:55:42Z` `inline` by `coderabbitai` `testing/python/language/test_tilelang_language_tma_copy.py`:279; signals: blackwell, cuda, cute, fp4, hopper, memory, regression, sm100; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🌐 Web query: In which CUDA Toolkit / CUDA Driver API version was CU TENSOR MAP ..." (https://github.com/tile-ai/tilelang/pull/2107#discussion_r3148202625)
- `2026-04-27T14:44:31Z` `issue` by `coderabbitai`; signals: aligned, compile, correctness, cuda, dtype, fp4, hang, kernel; excerpt: "📝 Walkthrough Walkthrough Adds dtype-bit-aware TMA conversion helpers and updates TMA lowering to use them; introduces explicit FP4 (float4 e2m1fn) CUDA tensor-map data type ..." (https://github.com/tile-ai/tilelang/pull/2107#issuecomment-4327911119)
- `2026-04-27T15:29:09Z` `review` `COMMENTED` by `coderabbitai`; signals: cuda, fp4, hang, nan, tile, tma; excerpt: "🧹 Nitpick comments (2) src/op/utils.cc (1) 150-154: Share the CUDA compatibility enum values from one place. 13 is now hard-coded here and again in ..." (https://github.com/tile-ai/tilelang/pull/2107#pullrequestreview-4182183449)
- `2026-04-27T14:55:44Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, tile, tma; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (1) src/runtime/runtime.cc (1) 42-52: Centralize the fallback TensorMap enum values. These numeric constants now live in both ..." (https://github.com/tile-ai/tilelang/pull/2107#pullrequestreview-4181937853)
- `2026-04-27T17:35:50Z` `issue` by `LeiWang1999`; signals: perf, regression; excerpt: "@regression-perf" (https://github.com/tile-ai/tilelang/pull/2107#issuecomment-4329169794)
