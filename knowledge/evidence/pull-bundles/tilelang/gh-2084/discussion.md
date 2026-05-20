# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2084](https://github.com/tile-ai/tilelang/pull/2084)
- Source page: `sources/prs/tilelang/PR-2084.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2084`
- Generated at: `2026-05-20T15:32:55.826032+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-22T13:28:38Z`
- Merged: `2026-05-20T06:53:49Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 6 (commented=4, dismissed=2)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: LeiWang1999, Rachmanino, Triang-jyed-driung, coderabbitai
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-22T13:33:51Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4155060371)
- `2026-04-22T14:26:54Z` `DISMISSED` by `LeiWang1999` (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4155456333)
- `2026-04-28T14:34:16Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4189744430)
- `2026-04-28T14:39:37Z` `COMMENTED` by `coderabbitai` - ♻️ Duplicate comments (1) testing/python/autotune/test tilelang autotune do not specialize.py (1) 113-123: ⚠️ Potential issue 🟠 Major Fix ... (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4189798362)
- `2026-05-13T09:09:47Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🧹 Nitpick comments (1) testing/python/transform/test tilelang transform producer consumer ws.py (1) 486-488: ⚡ Quick ... (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4280055317)
- `2026-05-20T06:49:21Z` `DISMISSED` by `LeiWang1999` (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4325849138)

## Inline Comment Hotspots

- `testing/python/autotune/test_tilelang_autotune_scalar_inputs.py`: 1 inline comment(s)
- `tilelang/autotuner/tuner.py`: 1 inline comment(s)
- `testing/python/autotune/test_tilelang_autotune_do_not_specialize.py`: 1 inline comment(s)
- `src/transform/producer_consumer_ws.cc`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-13T09:09:47Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, gemm, hang, kernel, regression, tile, tma; excerpt: "Actionable comments posted: 1 🧹 Nitpick comments (1) testing/python/transform/test tilelang transform producer consumer ws.py (1) 486-488: ⚡ Quick win Avoid hardcoding mbarrier array literal ..." (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4280055317)
- `2026-04-22T13:28:50Z` `issue` by `coderabbitai`; signals: autotune, block, cache, cuda, gemm, hang, kernel, pipeline; excerpt: "[!NOTE] Reviews paused It looks like this branch is under active development. To avoid overwhelming you with review comments due to an influx of ..." (https://github.com/tile-ai/tilelang/pull/2084#issuecomment-4296596633)
- `2026-04-28T14:39:37Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, cache, hang, kernel, tile; excerpt: "♻️ Duplicate comments (1) testing/python/autotune/test tilelang autotune do not specialize.py (1) 113-123: ⚠️ Potential issue 🟠 Major Fix tensor shape mismatch in positional-args test. ..." (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4189798362)
- `2026-04-22T13:33:49Z` `inline` by `coderabbitai` `testing/python/autotune/test_tilelang_autotune_scalar_inputs.py`:39; signals: autotune, benchmark, cuda, cute, tile; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: tile-ai/tilelang Length of output: 50373 --- 🏁 Script executed: Repository: tile-ai/tilelang Length ..." (https://github.com/tile-ai/tilelang/pull/2084#discussion_r3124314871)
- `2026-04-28T14:34:15Z` `inline` by `coderabbitai` `testing/python/autotune/test_tilelang_autotune_do_not_specialize.py`:136; signals: autotune, benchmark, kernel, tile; excerpt: "⚠️ Potential issue 🟠 Major Tensor shapes don't match the kernel parameters in the second call. The test reuses tensors a (512×256) and b ..." (https://github.com/tile-ai/tilelang/pull/2084#discussion_r3154937047)
- `2026-04-22T13:33:51Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, hang, tile; excerpt: "Actionable comments posted: 2 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4155060371)
- `2026-04-28T14:34:16Z` `review` `COMMENTED` by `coderabbitai`; signals: autotune, hang, tile; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/tile-ai/tilelang/pull/2084#pullrequestreview-4189744430)
- `2026-04-22T13:33:50Z` `inline` by `coderabbitai` `tilelang/autotuner/tuner.py`:426; signals: autotune, tile; excerpt: "⚠️ Potential issue 🟡 Minor Validate out idx before normalizing negative indices. Line 298 and Line 300 currently accept out-of-range values such as -len(params) ..." (https://github.com/tile-ai/tilelang/pull/2084#discussion_r3124314913)
- `2026-04-22T14:55:54Z` `issue` by `Triang-jyed-driung`; signals: hang, kernel; excerpt: "Like I said in I don't want a simple rejection for these kernels. I want a way to manually specify whether this kernel should ..." (https://github.com/tile-ai/tilelang/pull/2084#issuecomment-4297312546)
- `2026-04-22T15:09:21Z` `issue` by `Rachmanino`; signals: hang, kernel; excerpt: "Like I said in 2081, I don't want a simple rejection for these kernels. I want a way to manually specify whether this kernel ..." (https://github.com/tile-ai/tilelang/pull/2084#issuecomment-4297413681)
- `2026-04-23T03:23:22Z` `issue` by `LeiWang1999`; signals: autotune; excerpt: "@Triang-jyed-driung Thanks for your suggestion. For this issue, we should introduce a parameter like a do not specify argument in autotune, but this PR ..." (https://github.com/tile-ai/tilelang/pull/2084#issuecomment-4301528526)
- `2026-05-13T09:09:46Z` `inline` by `coderabbitai` `src/transform/producer_consumer_ws.cc`:1255; signals: general review; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Global iteration index is incorrect for irregular enclosing-loop extents Line 1239-Line 1242 computes a mixed-radix index ..." (https://github.com/tile-ai/tilelang/pull/2084#discussion_r3232906696)
