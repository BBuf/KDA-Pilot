# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2002](https://github.com/tile-ai/tilelang/pull/2002)
- Source page: `sources/prs/tilelang/PR-2002.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2002`
- Generated at: `2026-05-20T15:32:45.341557+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-31T07:38:28Z`
- Merged: `2026-04-07T15:54:55Z`

## Discussion Counts

- Issue comments: 29
- Review submissions: 5 (commented=5)
- Inline review comments: 13
- Review threads observed: 13
- Resolved/outdated thread markers: resolved=9, outdated=8
- Human participants with discussion text: LeiWang1999, coderabbitai
- Automation comments/reviews omitted from high-signal summary: 11
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-31T07:56:39Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4035424968)
- `2026-03-31T15:10:17Z` `COMMENTED` by `coderabbitai` - ♻️ Duplicate comments (1) src/op/copy.cc (1) 639-647: ⚠️ Potential issue 🟠 Major Fallback legality still allows non-provable inner ... (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4038136502)
- `2026-03-31T18:06:14Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4039160143)
- `2026-04-01T11:13:47Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4043433046)
- `2026-04-01T11:58:19Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) examples/deepseek mhc/example mhc post.py (1) 148-148: Remove commented-out entrypoint code on Line 148. Commented ... (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4043674990)

## Inline Comment Hotspots

- `src/transform/producer_consumer_ws_tiled.cc`: 3 inline comment(s)
- `src/transform/pipeline_planning.cc`: 2 inline comment(s)
- `src/op/copy.cc`: 1 inline comment(s)
- `src/transform/instruction_annotation.cc`: 1 inline comment(s)
- `src/transform/layout_inference.cc`: 1 inline comment(s)
- `src/transform/lower_tile_op.cc`: 1 inline comment(s)
- `testing/python/issue/test_tilelang_issue_tma_no_ws.py`: 1 inline comment(s)
- `testing/python/transform/test_tilelang_transform_producer_consumer_ws_tiled.py`: 1 inline comment(s)
- `tilelang/engine/phase.py`: 1 inline comment(s)
- `src/op/copy.h`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-31T07:56:39Z` `review` `COMMENTED` by `coderabbitai`; signals: gemm, hang, layout, memory, pipeline, tile, tma, warp; excerpt: "Actionable comments posted: 10 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4035424968)
- `2026-04-01T11:13:47Z` `review` `COMMENTED` by `coderabbitai`; signals: block, epilogue, gemm, hang, layout, nan, perf, pipeline; excerpt: "Actionable comments posted: 2 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4043433046)
- `2026-03-31T07:38:43Z` `issue` by `coderabbitai`; signals: aligned, block, gemm, hang, layout, memory, nan, perf; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/tile-ai/tilelang/pull/2002#issuecomment-4160568857)
- `2026-03-31T07:56:38Z` `inline` by `coderabbitai` `tilelang/engine/phase.py`:185; signals: kernel, layout, nan, pipeline, tile, warp; excerpt: "⚠️ Potential issue 🟠 Major Run InstructionAnnotation() before tiled WS. The new tiled WS pass is documented to consume tl instruction kind, but LowerAndLegalize() ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3014169801)
- `2026-03-31T07:56:37Z` `inline` by `coderabbitai` `src/transform/lower_tile_op.cc`:1097; signals: epilogue, kernel, pipeline, tile, tma; excerpt: "⚠️ Potential issue 🔴 Critical Pipeline context needs stage/parity, not just the stage count. When software pipelining emits unit prologue/epilogue statements, there is no ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3014169765)
- `2026-03-31T07:56:37Z` `inline` by `coderabbitai` `testing/python/transform/test_tilelang_transform_producer_consumer_ws_tiled.py`:98; signals: benchmark, block, pipeline, regression, tile; excerpt: "⚠️ Potential issue 🟡 Minor This setup never produces a non-zero pipeline start. With N=128 and block N=64, bx is only 0 or 1, ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3014169792)
- `2026-03-31T07:56:37Z` `inline` by `coderabbitai` `src/transform/producer_consumer_ws_tiled.cc`:704; signals: benchmark, block, tile, tma; excerpt: "⚠️ Potential issue 🟠 Major Unwrap simple wrappers when classifying producer tile ops. This file already has GetEvaluateCallInSimpleWrapper() at Line 319, but ClassifyStmt() only ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3014169771)
- `2026-03-31T07:56:37Z` `inline` by `coderabbitai` `src/transform/layout_inference.cc`:811; signals: cute, layout, tile; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: tile-ai/tilelang Length of output: 50373 --- 🏁 Script executed: Repository: tile-ai/tilelang Length ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3014169748)
- `2026-03-31T07:56:37Z` `inline` by `coderabbitai` `src/transform/pipeline_planning.cc`:378; signals: benchmark, pipeline, tile; excerpt: "⚠️ Potential issue 🟠 Major Don’t recurse into tile-op args after recording regions. HandleTileOp() already adds the precise read/write regions. Descending into the same ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3014169769)
- `2026-03-31T07:56:37Z` `inline` by `coderabbitai` `src/transform/producer_consumer_ws_tiled.cc`:1213; signals: ptx, tile, tma; excerpt: "⚠️ Potential issue 🔴 Critical Choose the forward-arrival op per producer group, not from a global flag. group has cp async is derived from ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3014169786)
- `2026-04-01T11:13:46Z` `inline` by `coderabbitai` `src/transform/pipeline_planning.cc`:298; signals: alignment, pipeline, tma; excerpt: "⚠️ Potential issue 🟠 Major Use the full TMA legality check when setting tma copy. Passing check last dim=false skips CopyNode::CheckBulkLoad()'s last-dimension alignment gate, ..." (https://github.com/tile-ai/tilelang/pull/2002#discussion_r3021411000)
- `2026-04-01T11:58:19Z` `review` `COMMENTED` by `coderabbitai`; signals: hang, pipeline; excerpt: "🧹 Nitpick comments (1) examples/deepseek mhc/example mhc post.py (1) 148-148: Remove commented-out entrypoint code on Line 148. Commented executable code tends to drift. Prefer ..." (https://github.com/tile-ai/tilelang/pull/2002#pullrequestreview-4043674990)
