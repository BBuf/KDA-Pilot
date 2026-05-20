# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2098](https://github.com/tile-ai/tilelang/pull/2098)
- Source page: `sources/prs/tilelang/PR-2098.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2098`
- Generated at: `2026-05-20T15:32:57.954319+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-25T06:53:55Z`
- Merged: `2026-04-28T06:18:35Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: LeiWang1999, coderabbitai
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-25T07:00:37Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (2) examples/blockscaled gemm sm100/grouped gemm mxfp8 blockscaled 1d1d.py (1) 562-562: Unused ... (https://github.com/tile-ai/tilelang/pull/2098#pullrequestreview-4175263315)
- `2026-04-25T07:15:14Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (3) examples/blockscaled gemm sm100/mxfp8 illustrated.md (3) 8-8: Consider hyphenating "K-scale blocks" for clarity. The phrase ... (https://github.com/tile-ai/tilelang/pull/2098#pullrequestreview-4175278533)
- `2026-04-25T07:25:43Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (2) examples/blockscaled gemm sm100/grouped gemm mxfp8 blockscaled 1d1d.py (2) 549-549: Drop the unused m total ... (https://github.com/tile-ai/tilelang/pull/2098#pullrequestreview-4175287137)
- `2026-04-28T06:18:26Z` `APPROVED` by `LeiWang1999` (https://github.com/tile-ai/tilelang/pull/2098#pullrequestreview-4186304241)

## Inline Comment Hotspots

- `examples/blockscaled_gemm_sm100/grouped_gemm_mxfp8_blockscaled_1d1d.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-25T07:15:14Z` `review` `COMMENTED` by `coderabbitai`; signals: block, fp8, gemm, hang, kernel, layout, sm100, tmem; excerpt: "🧹 Nitpick comments (3) examples/blockscaled gemm sm100/mxfp8 illustrated.md (3) 8-8: Consider hyphenating "K-scale blocks" for clarity. The phrase "K scale blocks" should be hyphenated ..." (https://github.com/tile-ai/tilelang/pull/2098#pullrequestreview-4175278533)
- `2026-04-25T07:25:43Z` `review` `COMMENTED` by `coderabbitai`; signals: block, fp8, gemm, hang, kernel, sm100, tile, tmem; excerpt: "🧹 Nitpick comments (2) examples/blockscaled gemm sm100/grouped gemm mxfp8 blockscaled 1d1d.py (2) 549-549: Drop the unused m total binding. m total is unpacked but ..." (https://github.com/tile-ai/tilelang/pull/2098#pullrequestreview-4175287137)
- `2026-04-25T07:00:36Z` `inline` by `coderabbitai` `examples/blockscaled_gemm_sm100/grouped_gemm_mxfp8_blockscaled_1d1d.py`:56; signals: benchmark, block, cute, dtype, fp8, gemm, hang, sm100; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: tile-ai/tilelang Length of output: 4866 --- 🏁 Script executed: Repository: tile-ai/tilelang Length ..." (https://github.com/tile-ai/tilelang/pull/2098#discussion_r3141621115)
- `2026-04-25T07:00:36Z` `inline` by `coderabbitai` `examples/blockscaled_gemm_sm100/grouped_gemm_mxfp8_blockscaled_1d1d.py`:97; signals: block, epilogue, fp8, gemm, kernel, pipeline, sm100, tile; excerpt: "⚠️ Potential issue 🟡 Minor Empty / partial groups: TMA still issues loads at clamped tile m. For experts with m size == 0 ..." (https://github.com/tile-ai/tilelang/pull/2098#discussion_r3141621118)
- `2026-04-25T06:54:08Z` `issue` by `coderabbitai`; signals: benchmark, block, fp8, gemm, hang, kernel, layout, memory; excerpt: "📝 Walkthrough Walkthrough Adds optional transpose B handling to MXFP8 blockscaled GEMM kernels and reference, plus a new grouped SM100 MXFP8 blockscaled GEMM example ..." (https://github.com/tile-ai/tilelang/pull/2098#issuecomment-4318400447)
- `2026-04-25T07:00:37Z` `review` `COMMENTED` by `coderabbitai`; signals: block, fp8, gemm, hang, kernel, sm100; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (2) examples/blockscaled gemm sm100/grouped gemm mxfp8 blockscaled 1d1d.py (1) 562-562: Unused unpacked variable m total. m total ..." (https://github.com/tile-ai/tilelang/pull/2098#pullrequestreview-4175263315)
