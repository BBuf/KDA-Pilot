# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2008](https://github.com/tile-ai/tilelang/pull/2008)
- Source page: `sources/prs/tilelang/PR-2008.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2008`
- Generated at: `2026-05-20T15:32:47.281293+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T03:43:28Z`
- Merged: `2026-04-15T05:34:44Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 6 (commented=6)
- Inline review comments: 8
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=4, outdated=7
- Human participants with discussion text: LeiWang1999, coderabbitai, kurisu6912
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-02T03:52:50Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4048197769)
- `2026-04-02T03:58:36Z` `COMMENTED` by `coderabbitai` - ♻️ Duplicate comments (1) src/op/gemm py.cc (1) 322-335: ⚠️ Potential issue 🟠 Major Skip-on-existing still leaves strict shared ... (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4048210128)
- `2026-04-03T06:22:45Z` `COMMENTED` by `LeiWang1999` (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4054459559)
- `2026-04-07T07:05:11Z` `COMMENTED` by `kurisu6912` (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4066306932)
- `2026-04-14T07:27:38Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4104104617)
- `2026-04-14T14:16:57Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4106624115)

## Inline Comment Hotspots

- `src/op/gemm_py.cc`: 3 inline comment(s)
- `src/op/gemm.cc`: 2 inline comment(s)
- `src/op/gemm_sp_py.cc`: 2 inline comment(s)
- `src/transform/layout_inference.cc`: 1 inline comment(s)

## High-Signal Discussion

- `2026-04-14T07:27:37Z` `inline` by `coderabbitai` `src/op/gemm_sp_py.cc`:310; signals: block, cute, gemm, hopper, layout, tile, warp, wgmma; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: tile-ai/tilelang Length of output: 818 --- 🏁 Script executed: Repository: tile-ai/tilelang Length ..." (https://github.com/tile-ai/tilelang/pull/2008#discussion_r3077789931)
- `2026-04-02T03:43:48Z` `issue` by `coderabbitai`; signals: aligned, block, gemm, hang, layout, pipeline, tile, tma; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/tile-ai/tilelang/pull/2008#issuecomment-4174431733)
- `2026-04-02T03:52:49Z` `inline` by `coderabbitai` `src/op/gemm.cc`:695; signals: gemm, hopper, layout, sm100, wgmma; excerpt: "⚠️ Potential issue 🟠 Major Mixed MMA + strict-layout consumers can still fail depending on visit order. Line 688 participates in the surrounding SM100 ..." (https://github.com/tile-ai/tilelang/pull/2008#discussion_r3025741816)
- `2026-04-02T03:58:36Z` `review` `COMMENTED` by `coderabbitai`; signals: gemm, hang, layout, wgmma; excerpt: "♻️ Duplicate comments (1) src/op/gemm py.cc (1) 322-335: ⚠️ Potential issue 🟠 Major Skip-on-existing still leaves strict shared layouts visit-order dependent. If an MMA-backed ..." (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4048210128)
- `2026-04-14T14:16:55Z` `inline` by `coderabbitai` `src/op/gemm_sp_py.cc`:324; signals: benchmark, failing, gemm, layout; excerpt: "⚠️ Potential issue 🟠 Major Handle CDNA kMFMA as a strict-layout case here too. GetGemmInst() can return GemmInst::kMFMA on CDNA, but this branch falls ..." (https://github.com/tile-ai/tilelang/pull/2008#discussion_r3080101843)
- `2026-04-14T07:27:38Z` `review` `COMMENTED` by `coderabbitai`; signals: gemm, hang, layout; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4104104617)
- `2026-04-14T14:16:57Z` `review` `COMMENTED` by `coderabbitai`; signals: gemm, hang, layout; excerpt: "Actionable comments posted: 3 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4106624115)
- `2026-04-02T03:52:49Z` `inline` by `coderabbitai` `src/op/gemm_py.cc`:335; signals: gemm, layout, wgmma; excerpt: "⚠️ Potential issue 🟠 Major The Python infer path inherits the same visit-order gap. Line 333 only drops a shared-buffer layout after another op ..." (https://github.com/tile-ai/tilelang/pull/2008#discussion_r3025741814)
- `2026-04-14T14:16:55Z` `inline` by `coderabbitai` `src/op/gemm.cc`:509; signals: gemm, layout, wgmma; excerpt: "⚠️ Potential issue 🟠 Major kMFMA falls through to the non-strict path here. getGemmInst() returns GemmInst::kMFMA on CDNA, but the new switch only hardens ..." (https://github.com/tile-ai/tilelang/pull/2008#discussion_r3080101867)
- `2026-04-02T03:52:50Z` `review` `COMMENTED` by `coderabbitai`; signals: gemm, hang; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2008#pullrequestreview-4048197769)
- `2026-04-07T07:05:11Z` `inline` by `kurisu6912` `src/op/gemm_py.cc`:333; signals: gemm, layout; excerpt: "Maybe not. It seems that only mma support arbitrary shared buffer layout, and other atoms doesn't. If this is true, here is ok to ..." (https://github.com/tile-ai/tilelang/pull/2008#discussion_r3043374607)
- `2026-04-14T08:07:31Z` `issue` by `LeiWang1999`; signals: perf, regression; excerpt: "@regression-perf" (https://github.com/tile-ai/tilelang/pull/2008#issuecomment-4242241777)
